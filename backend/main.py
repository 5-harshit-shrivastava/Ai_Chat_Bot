from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any
import os

# Import your modules with error handling
try:
    from db import get_db, init_db
    from sqlalchemy.orm import Session
    
    # Try to import the functions
    try:
        from chat import get_rag_response
        chat_available = True
    except ImportError as e:
        print(f"Chat import error: {e}")
        chat_available = False
        
    try:
        from ingest import add_document
        ingest_available = True
    except ImportError as e:
        print(f"Ingest import error: {e}")
        ingest_available = False
        
except ImportError as e:
    print(f"Database import error: {e}")
    # Fallback functions for deployment
    def get_rag_response(query: str, db: Session = None) -> str:
        return "Backend service is initializing. Please try again in a moment."
    def add_document(content: str, metadata: dict = {}, db: Session = None):
        return "temp_id"
    def get_db():
        return None
    def init_db():
        pass
    chat_available = False
    ingest_available = False

app = FastAPI(
    title="RAG Chatbot API",
    description="AI-powered RAG chatbot backend",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    try:
        init_db()
        print("Database initialized successfully")
    except Exception as e:
        print(f"Database initialization failed: {e}")

class ChatRequest(BaseModel):
    message: str

class DocumentRequest(BaseModel):
    content: str
    metadata: Dict[str, Any] = {}

@app.get("/")
async def root():
    return {
        "message": "RAG Chatbot API is running!",
        "status": "healthy",
        "version": "1.0.0",
        "features": {
            "chat": chat_available,
            "ingest": ingest_available
        }
    }

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "rag-chatbot-backend"}

@app.post("/chat")
async def chat_endpoint(request: ChatRequest, db: Session = Depends(get_db)):
    try:
        if not chat_available:
            return {"response": "Chat service is currently unavailable. Please try again later."}
        
        response = get_rag_response(request.message, db)
        return {"response": response}
    except Exception as e:
        print(f"Chat error: {e}")
        return {"response": "I apologize, but I'm experiencing technical difficulties. Please try again later."}

@app.post("/documents")
async def add_document_endpoint(request: DocumentRequest, db: Session = Depends(get_db)):
    try:
        if not ingest_available:
            return {"document_id": "temp_id", "status": "Ingest service unavailable"}
        
        doc_id = add_document(request.content, request.metadata, db)
        return {"document_id": doc_id, "status": "success"}
    except Exception as e:
        print(f"Document error: {e}")
        return {"document_id": "temp_id", "status": "error", "message": str(e)}

# For Vercel compatibility
handler = app