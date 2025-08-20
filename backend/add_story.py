#!/usr/bin/env python3
"""Script to add 'Our Story' content to the database."""

from db import get_db, init_db
from ingest import add_document

def main():
    # Initialize database if needed
    init_db()
    
    # Our Story content
    story_content = """Our Story
Our journey began in 2020, driven by a passion for sustainable farming practices. Despite facing challenges along the way, we persevered and achieved significant milestones.

From humble beginnings to becoming a leader in organic fertilizers, our story is a testament to our dedication and resilience."""
    
    # Metadata for the story
    story_metadata = {
        "type": "company_story",
        "title": "Our Story",
        "category": "about",
        "tags": ["company", "history", "sustainable farming", "organic fertilizers"]
    }
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(story_content, story_metadata, db_session)
        print(f"Successfully added 'Our Story' to database with ID: {doc_id}")
    except Exception as e:
        print(f"Error adding document: {e}")
    finally:
        db_session.close()

if __name__ == "__main__":
    main()