#!/usr/bin/env python3
"""
Script to add basic company information to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_company_basic_info_to_database():
    """Add basic company information to the database"""
    
    company_info_content = """Company Information
Name: LCB Fertilizers"""

    metadata = {
        "type": "company_basic_info",
        "title": "LCB Fertilizers Basic Information",
        "category": "company_info",
        "company_name": "LCB Fertilizers",
        "content_type": "basic_company_details",
        "tags": [
            "LCB Fertilizers",
            "company",
            "name",
            "basic_info",
            "company_identification"
        ]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(company_info_content, metadata, db_session)
        print(f"✅ Successfully added basic company information to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding basic company information to database...")
    result = add_company_basic_info_to_database()
    
    if result:
        print("\n🎉 Basic company information has been successfully added to the RAG chatbot database!")
        print("The chatbot can now identify the company name: LCB Fertilizers.")
    else:
        print("\n💥 Failed to add basic company information. Please check the error messages above.")