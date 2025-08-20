#!/usr/bin/env python3
"""
Script to add Navyakosh FAQ to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_navyakosh_faq_to_database():
    """Add Navyakosh FAQ information to the database"""
    
    navyakosh_faq_content = """Frequently Asked Questions (FAQs) - Navyakosh Organic Fertilizer

Q1: What is Navyakosh Organic Fertilizer, and how is it different from chemical fertilizers?

A: Navyakosh is a 100% organic fertilizer made from natural ingredients like cow dung, agricultural waste, and fermented organic manure. Unlike chemical fertilizers that can leave harmful residues, Navyakosh enriches the soil's natural health and supports sustainable farming by increasing yields while protecting the environment."""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "faq",
        "company": "LCB Fertilizers",
        "content_type": "frequently_asked_questions",
        "question_category": "product_description",
        "topics_covered": [
            "product_definition",
            "organic_vs_chemical_fertilizers",
            "natural_ingredients",
            "sustainable_farming",
            "environmental_protection"
        ],
        "key_ingredients": [
            "cow_dung",
            "agricultural_waste",
            "fermented_organic_manure"
        ],
        "benefits": [
            "enriches_soil_health",
            "sustainable_farming",
            "increases_yields",
            "protects_environment",
            "no_harmful_residues"
        ],
        "fertilizer_type": "100_percent_organic"
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(navyakosh_faq_content, metadata, db_session)
        print(f"✅ Successfully added Navyakosh FAQ to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Navyakosh FAQ to database...")
    result = add_navyakosh_faq_to_database()
    
    if result:
        print("\n🎉 Navyakosh FAQ has been successfully added to the RAG chatbot database!")
        print("The chatbot can now answer questions about what Navyakosh is and how it differs from chemical fertilizers.")
    else:
        print("\n💥 Failed to add Navyakosh FAQ. Please check the error messages above.")