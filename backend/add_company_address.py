#!/usr/bin/env python3
"""
Script to add company address to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_company_address_to_database():
    """Add company address to the database"""
    
    address_content = """Address:
3rd Floor, Diamond Jubeeli Hall,
IIT Kanpur,
Kanpur - 208016"""

    metadata = {
        "type": "company_address",
        "title": "LCB Fertilizers Address",
        "category": "address_info",
        "company_name": "LCB Fertilizers",
        "content_type": "address_information",
        "address_details": {
            "floor": "3rd Floor",
            "building": "Diamond Jubeeli Hall",
            "institution": "IIT Kanpur",
            "city": "Kanpur",
            "postal_code": "208016",
            "state": "Uttar Pradesh",
            "country": "India"
        },
        "tags": [
            "LCB Fertilizers",
            "address",
            "location",
            "IIT Kanpur",
            "Kanpur",
            "Diamond Jubeeli Hall",
            "office address",
            "company location"
        ]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(address_content, metadata, db_session)
        print(f"✅ Successfully added company address to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding company address to database...")
    result = add_company_address_to_database()
    
    if result:
        print("\n🎉 Company address has been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide the office address for LCB Fertilizers.")
    else:
        print("\n💥 Failed to add company address. Please check the error messages above.")