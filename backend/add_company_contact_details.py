#!/usr/bin/env python3
"""
Script to add company contact details to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_company_contact_details_to_database():
    """Add company contact details to the database"""
    
    contact_details_content = """Contact Details

Address:
3rd Floor, Diamond Jubeeli Hall,
IIT Kanpur,
Kanpur - 208016

Phone:
+91 91988-03978

Email:
General Inquiries: contact@lcbfertilizers.com
B2B and Dealership: ceo@lcbfertilizers.com"""

    metadata = {
        "type": "contact_details",
        "title": "LCB Fertilizers Contact Information",
        "category": "contact_info",
        "company_name": "LCB Fertilizers",
        "content_type": "contact_information",
        "contact_info": {
            "address": {
                "floor": "3rd Floor",
                "building": "Diamond Jubeeli Hall",
                "location": "IIT Kanpur",
                "city": "Kanpur",
                "postal_code": "208016"
            },
            "phone": "+91 91988-03978",
            "emails": {
                "general_inquiries": "contact@lcbfertilizers.com",
                "b2b_dealership": "ceo@lcbfertilizers.com"
            }
        },
        "tags": [
            "LCB Fertilizers",
            "contact",
            "address",
            "phone",
            "email",
            "IIT Kanpur",
            "Kanpur",
            "B2B",
            "dealership",
            "general inquiries"
        ]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(contact_details_content, metadata, db_session)
        print(f"✅ Successfully added company contact details to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding company contact details to database...")
    result = add_company_contact_details_to_database()
    
    if result:
        print("\n🎉 Company contact details have been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide address, phone, and email information for LCB Fertilizers.")
    else:
        print("\n💥 Failed to add company contact details. Please check the error messages above.")