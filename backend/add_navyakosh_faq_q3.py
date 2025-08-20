#!/usr/bin/env python3
"""
Script to add Navyakosh FAQ Q3 to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_navyakosh_faq_q3_to_database():
    """Add Navyakosh FAQ Q3 information to the database"""
    
    navyakosh_faq_q3_content = """Frequently Asked Questions (FAQs) - Navyakosh Organic Fertilizer

Q3: Can Navyakosh reduce the need for irrigation?

A: Yes. Navyakosh uses advanced super absorbent polymer technology. These polymers can absorb up to 268 times their weight in water and release it slowly back to the plant roots. This process keeps the soil moist for longer and can reduce irrigation needs by up to 33%."""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "faq",
        "company": "LCB Fertilizers",
        "content_type": "frequently_asked_questions",
        "question_category": "irrigation_reduction",
        "topics_covered": [
            "irrigation_reduction",
            "water_conservation",
            "super_absorbent_polymer_technology",
            "water_absorption",
            "slow_release_mechanism",
            "soil_moisture_retention"
        ],
        "technology": "super_absorbent_polymer",
        "water_absorption_capacity": "268_times_their_weight",
        "irrigation_reduction": "up_to_33_percent",
        "benefits": [
            "reduces_irrigation_needs",
            "absorbs_water_efficiently",
            "slow_release_to_plant_roots",
            "keeps_soil_moist_longer",
            "water_conservation"
        ],
        "mechanism": [
            "super_absorbent_polymers",
            "water_absorption",
            "slow_water_release",
            "soil_moisture_retention"
        ]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(navyakosh_faq_q3_content, metadata, db_session)
        print(f"✅ Successfully added Navyakosh FAQ Q3 to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Navyakosh FAQ Q3 to database...")
    result = add_navyakosh_faq_q3_to_database()
    
    if result:
        print("\n🎉 Navyakosh FAQ Q3 has been successfully added to the RAG chatbot database!")
        print("The chatbot can now answer questions about how Navyakosh reduces irrigation needs.")
    else:
        print("\n💥 Failed to add Navyakosh FAQ Q3. Please check the error messages above.")