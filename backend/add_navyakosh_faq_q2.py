#!/usr/bin/env python3
"""
Script to add Navyakosh FAQ Q2 to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_navyakosh_faq_q2_to_database():
    """Add Navyakosh FAQ Q2 information to the database"""
    
    navyakosh_faq_q2_content = """Frequently Asked Questions (FAQs) - Navyakosh Organic Fertilizer

Q2: How does Navyakosh improve soil health?

A: Navyakosh contains 60 types of beneficial microorganisms that restore the soil's natural balance. These microbes break down complex nutrients, making them easily available for crops. It also adds significant organic matter, which improves soil fertility and its capacity to hold water."""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "faq",
        "company": "LCB Fertilizers",
        "content_type": "frequently_asked_questions",
        "question_category": "soil_health_improvement",
        "topics_covered": [
            "soil_health",
            "beneficial_microorganisms",
            "nutrient_breakdown",
            "organic_matter",
            "soil_fertility",
            "water_retention"
        ],
        "microorganisms_count": "60_types",
        "benefits": [
            "restores_soil_natural_balance",
            "breaks_down_complex_nutrients",
            "makes_nutrients_available_for_crops",
            "adds_organic_matter",
            "improves_soil_fertility",
            "increases_water_holding_capacity"
        ],
        "mechanism": [
            "beneficial_microorganisms",
            "nutrient_breakdown",
            "organic_matter_addition"
        ]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(navyakosh_faq_q2_content, metadata, db_session)
        print(f"✅ Successfully added Navyakosh FAQ Q2 to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Navyakosh FAQ Q2 to database...")
    result = add_navyakosh_faq_q2_to_database()
    
    if result:
        print("\n🎉 Navyakosh FAQ Q2 has been successfully added to the RAG chatbot database!")
        print("The chatbot can now answer questions about how Navyakosh improves soil health.")
    else:
        print("\n💥 Failed to add Navyakosh FAQ Q2. Please check the error messages above.")