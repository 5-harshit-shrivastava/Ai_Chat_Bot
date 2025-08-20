#!/usr/bin/env python3
"""Script to add company contact information to the database."""

from db import get_db, init_db
from ingest import add_document

def main():
    # Initialize database if needed
    init_db()
    
    # Company contact information
    contact_content = """Company Information
Name: LCB Fertilizers

Contact Details
Address:
3rd Floor, Diamond Jubeeli Hall,
IIT Kanpur,
Kanpur - 208016

Phone:
+91 91988-03978

Email:
General Inquiries: contact@lcbfertilizers.com
B2B and Dealership: ceo@lcbfertilizers.com

Social Media Profiles
Facebook: https://www.facebook.com/Lcbfertilizers/
Instagram: https://www.instagram.com/lcbfertilizers/
LinkedIn: https://www.linkedin.com/company/lcbfertilizers/
YouTube: https://www.youtube.com/@lcbfertilizers"""
    
    # Metadata for contact information
    contact_metadata = {
        "type": "contact_information",
        "title": "LCB Fertilizers Contact Details",
        "category": "contact",
        "tags": [
            "LCB Fertilizers", "contact", "address", "phone", "email", 
            "IIT Kanpur", "social media", "Facebook", "Instagram", 
            "LinkedIn", "YouTube", "B2B", "dealership"
        ]
    }
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(contact_content, contact_metadata, db_session)
        print(f"Successfully added 'Contact Information' to database with ID: {doc_id}")
    except Exception as e:
        print(f"Error adding document: {e}")
    finally:
        db_session.close()

if __name__ == "__main__":
    main()