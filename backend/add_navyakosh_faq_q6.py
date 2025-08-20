#!/usr/bin/env python3
"""
Script to add Navyakosh FAQ Q6 about compatibility with other fertilizers to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_navyakosh_faq_q6_to_database():
    """Add Navyakosh FAQ Q6 information to the database"""
    
    navyakosh_faq_q6_content = """Frequently Asked Questions (FAQs) - Navyakosh Organic Fertilizer

Q6: Can I use Navyakosh with other fertilizers or pesticides?

A: Navyakosh is a comprehensive solution designed to meet most of your crop's nutrient needs, which significantly reduces the requirement for additional chemical fertilizers."""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "faq",
        "company": "LCB Fertilizers",
        "content_type": "frequently_asked_questions",
        "question_category": "compatibility_with_other_products",
        "topics_covered": [
            "fertilizer_compatibility",
            "pesticide_compatibility",
            "comprehensive_solution",
            "nutrient_completeness",
            "chemical_fertilizer_reduction"
        ],
        "product_features": [
            "comprehensive_solution",
            "meets_most_nutrient_needs",
            "reduces_chemical_fertilizer_requirement"
        ],
        "benefits": [
            "significantly_reduces_additional_chemical_fertilizer_requirement",
            "comprehensive_nutrient_solution",
            "meets_most_crop_nutrient_needs"
        ],
        "compatibility": [
            "designed_as_comprehensive_solution",
            "reduces_need_for_additional_fertilizers"
        ]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(navyakosh_faq_q6_content, metadata, db_session)
        print(f"✅ Successfully added Navyakosh FAQ Q6 to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Navyakosh FAQ Q6 to database...")
    result = add_navyakosh_faq_q6_to_database()
    
    if result:
        print("\n🎉 Navyakosh FAQ Q6 has been successfully added to the RAG chatbot database!")
        print("The chatbot can now answer questions about using Navyakosh with other fertilizers or pesticides.")
    else:
        print("\n💥 Failed to add Navyakosh FAQ Q6. Please check the error messages above.")