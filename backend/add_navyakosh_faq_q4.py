#!/usr/bin/env python3
"""
Script to add Navyakosh FAQ Q4 about crop compatibility to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_navyakosh_faq_q4_to_database():
    """Add Navyakosh FAQ Q4 information to the database"""
    
    navyakosh_faq_q4_content = """Frequently Asked Questions (FAQs) - Navyakosh Organic Fertilizer

Q4: On which crops can I use Navyakosh?

A: Navyakosh is a versatile, one-time-use fertilizer suitable for a wide range of crops, including:
• Wheat, Rice, Maize, Bajra, Jowar
• Cotton and Sugarcane
• Pulses
• Vegetables, Fruits, and Spices

It is designed to be crop-specific, adapting to the unique needs of each plant"""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "faq",
        "company": "LCB Fertilizers",
        "content_type": "frequently_asked_questions",
        "question_category": "crop_compatibility",
        "topics_covered": [
            "crop_compatibility",
            "versatile_fertilizer",
            "crop_specific_adaptation",
            "wide_range_of_crops"
        ],
        "compatible_crops": [
            "wheat",
            "rice",
            "maize",
            "bajra",
            "jowar",
            "cotton",
            "sugarcane",
            "pulses",
            "vegetables",
            "fruits",
            "spices"
        ],
        "crop_categories": [
            "grains_and_cereals",
            "cash_crops",
            "pulses",
            "vegetables",
            "fruits",
            "spices"
        ],
        "fertilizer_properties": [
            "versatile",
            "one_time_use",
            "crop_specific",
            "adapts_to_unique_plant_needs"
        ],
        "benefits": [
            "suitable_for_wide_range_of_crops",
            "crop_specific_adaptation",
            "versatile_application"
        ]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(navyakosh_faq_q4_content, metadata, db_session)
        print(f"✅ Successfully added Navyakosh FAQ Q4 to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Navyakosh FAQ Q4 to database...")
    result = add_navyakosh_faq_q4_to_database()
    
    if result:
        print("\n🎉 Navyakosh FAQ Q4 has been successfully added to the RAG chatbot database!")
        print("The chatbot can now answer questions about crop compatibility with Navyakosh.")
    else:
        print("\n💥 Failed to add Navyakosh FAQ Q4. Please check the error messages above.")