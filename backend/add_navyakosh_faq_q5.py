#!/usr/bin/env python3
"""
Script to add Navyakosh FAQ Q5 about safety to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_navyakosh_faq_q5_to_database():
    """Add Navyakosh FAQ Q5 information to the database"""
    
    navyakosh_faq_q5_content = """Frequently Asked Questions (FAQs) - Navyakosh Organic Fertilizer

Q5: Is Navyakosh safe for my crops, family, and the environment?

A: Absolutely. Navyakosh is 100% organic and free from harmful chemicals. It does not pollute the soil, water, or air. Crops grown using Navyakosh are safe and healthy for consumption."""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "faq",
        "company": "LCB Fertilizers",
        "content_type": "frequently_asked_questions",
        "question_category": "safety_and_environment",
        "topics_covered": [
            "product_safety",
            "environmental_safety",
            "family_safety",
            "crop_safety",
            "pollution_free",
            "organic_certification"
        ],
        "safety_features": [
            "100_percent_organic",
            "free_from_harmful_chemicals",
            "does_not_pollute_soil",
            "does_not_pollute_water",
            "does_not_pollute_air",
            "safe_for_consumption"
        ],
        "environmental_benefits": [
            "no_soil_pollution",
            "no_water_pollution",
            "no_air_pollution",
            "environmentally_friendly"
        ],
        "health_benefits": [
            "safe_for_family",
            "safe_for_crops",
            "healthy_crops_for_consumption"
        ],
        "certifications": "100_percent_organic"
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(navyakosh_faq_q5_content, metadata, db_session)
        print(f"✅ Successfully added Navyakosh FAQ Q5 to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Navyakosh FAQ Q5 to database...")
    result = add_navyakosh_faq_q5_to_database()
    
    if result:
        print("\n🎉 Navyakosh FAQ Q5 has been successfully added to the RAG chatbot database!")
        print("The chatbot can now answer questions about Navyakosh safety for crops, family, and environment.")
    else:
        print("\n💥 Failed to add Navyakosh FAQ Q5. Please check the error messages above.")