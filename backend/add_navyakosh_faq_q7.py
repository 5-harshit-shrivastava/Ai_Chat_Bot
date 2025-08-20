#!/usr/bin/env python3
"""
Script to add Navyakosh FAQ Q7 about application method to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_navyakosh_faq_q7_to_database():
    """Add Navyakosh FAQ Q7 information to the database"""
    
    navyakosh_faq_q7_content = """Frequently Asked Questions (FAQs) - Navyakosh Organic Fertilizer

Q7: How do I apply Navyakosh to my crops?

A: Apply Navyakosh according to the recommended dosage for your specific crop (e.g., wheat, paddy). After application, it is important to irrigate the field to activate the nutrients and the super absorbent polymers."""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "faq",
        "company": "LCB Fertilizers",
        "content_type": "frequently_asked_questions",
        "question_category": "application_method",
        "topics_covered": [
            "application_method",
            "dosage_recommendation",
            "crop_specific_application",
            "irrigation_requirement",
            "nutrient_activation",
            "super_absorbent_polymer_activation"
        ],
        "application_steps": [
            "apply_according_to_recommended_dosage",
            "follow_crop_specific_guidelines",
            "irrigate_field_after_application"
        ],
        "crop_examples": [
            "wheat",
            "paddy"
        ],
        "activation_requirements": [
            "irrigation_needed_after_application",
            "activates_nutrients",
            "activates_super_absorbent_polymers"
        ],
        "important_notes": [
            "crop_specific_dosage",
            "irrigation_essential_for_activation"
        ]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(navyakosh_faq_q7_content, metadata, db_session)
        print(f"✅ Successfully added Navyakosh FAQ Q7 to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Navyakosh FAQ Q7 to database...")
    result = add_navyakosh_faq_q7_to_database()
    
    if result:
        print("\n🎉 Navyakosh FAQ Q7 has been successfully added to the RAG chatbot database!")
        print("The chatbot can now answer questions about how to apply Navyakosh to crops.")
    else:
        print("\n💥 Failed to add Navyakosh FAQ Q7. Please check the error messages above.")