#!/usr/bin/env python3
"""
Script to add phone and email contact details to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_phone_email_contact_to_database():
    """Add phone and email contact details to the database"""
    
    contact_details_content = """Contact Details

Phone:
+91 91988-03978

Email:
General Inquiries: contact@lcbfertilizers.com
B2B and Dealership: ceo@lcbfertilizers.com"""

    metadata = {
        "type": "phone_email_contact",
        "title": "LCB Fertilizers Phone and Email Contact",
        "category": "contact_info",
        "company_name": "LCB Fertilizers",
        "content_type": "contact_information",
        "contact_details": {
            "phone_number": "+91 91988-03978",
            "emails": {
                "general_inquiries": "contact@lcbfertilizers.com",
                "b2b_dealership": "ceo@lcbfertilizers.com"
            }
        },
        "communication_channels": [
            "phone",
            "email"
        ],
        "tags": [
            "LCB Fertilizers",
            "contact",
            "phone",
            "email",
            "communication",
            "general inquiries",
            "B2B",
            "dealership",
            "customer service"
        ]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(contact_details_content, metadata, db_session)
        print(f"✅ Successfully added phone and email contact details to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding phone and email contact details to database...")
    result = add_phone_email_contact_to_database()
    
    if result:
        print("\n🎉 Phone and email contact details have been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide phone and email information for LCB Fertilizers.")
    else:
        print("\n💥 Failed to add phone and email contact details. Please check the error messages above.")