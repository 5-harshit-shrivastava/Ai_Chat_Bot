#!/usr/bin/env python3
"""Script to add 'Our Mission' content to the database."""

from db import get_db, init_db
from ingest import add_document

def main():
    # Initialize database if needed
    init_db()
    
    # Our Mission content
    mission_content = """Our Mission
At LCB Fertilizers, our mission is to revolutionize agriculture by providing farmers with sustainable and eco-friendly solutions that enhance crop yield, promote soil health, and contribute to a greener planet.

We are committed to pioneering innovative technologies and practices that not only meet the needs of today's farmers but also ensure the well being of future generations."""
    
    # Metadata for the mission
    mission_metadata = {
        "type": "company_mission",
        "title": "Our Mission",
        "category": "about",
        "tags": ["mission", "agriculture", "sustainable", "eco-friendly", "LCB Fertilizers", "innovation"]
    }
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(mission_content, mission_metadata, db_session)
        print(f"Successfully added 'Our Mission' to database with ID: {doc_id}")
    except Exception as e:
        print(f"Error adding document: {e}")
    finally:
        db_session.close()

if __name__ == "__main__":
    main()