#!/usr/bin/env python3
"""
Script to add social media profiles to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_social_media_profiles_to_database():
    """Add social media profiles to the database"""
    
    social_media_content = """Social Media Profiles
Facebook: https://www.facebook.com/Lcbfertilizers/
Instagram: https://www.instagram.com/lcbfertilizers/
LinkedIn: https://www.linkedin.com/company/lcbfertilizers/
YouTube: https://www.youtube.com/@lcbfertilizers/"""

    metadata = {
        "type": "social_media_profiles",
        "title": "LCB Fertilizers Social Media Profiles",
        "category": "social_media",
        "company_name": "LCB Fertilizers",
        "content_type": "social_media_links",
        "social_platforms": {
            "facebook": "https://www.facebook.com/Lcbfertilizers/",
            "instagram": "https://www.instagram.com/lcbfertilizers/",
            "linkedin": "https://www.linkedin.com/company/lcbfertilizers/",
            "youtube": "https://www.youtube.com/@lcbfertilizers/"
        },
        "platform_handles": {
            "facebook": "Lcbfertilizers",
            "instagram": "lcbfertilizers",
            "linkedin": "lcbfertilizers",
            "youtube": "lcbfertilizers"
        },
        "tags": [
            "LCB Fertilizers",
            "social media",
            "Facebook",
            "Instagram",
            "LinkedIn",
            "YouTube",
            "online presence",
            "social profiles",
            "digital marketing"
        ]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(social_media_content, metadata, db_session)
        print(f"✅ Successfully added social media profiles to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding social media profiles to database...")
    result = add_social_media_profiles_to_database()
    
    if result:
        print("\n🎉 Social media profiles have been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide Facebook, Instagram, LinkedIn, and YouTube links for LCB Fertilizers.")
    else:
        print("\n💥 Failed to add social media profiles. Please check the error messages above.")