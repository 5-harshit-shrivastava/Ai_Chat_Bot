#!/usr/bin/env python3
"""
Script to add watermelon application guide to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_watermelon_guide_to_database():
    """Add watermelon application guide information to the database"""
    
    watermelon_guide_content = """How to Use Navyakosh: Application Guide for Fruits & Vegetables

WATERMELON

1st Application:
• Dosage: 50 grams of Navyakosh Organic Fertilizer per plant
• Timing & Method: Apply at the base of the plant during seedling transplantation

2nd Application:
• Dosage: 100 grams of Navyakosh Organic Fertilizer per plant
• Timing & Method: Apply at the base of the plant 45 days after seedling transplantation

Mechanism of Action:
Active microorganisms in the fertilizer get activated and help plants absorb and utilize all macro and micronutrients throughout the crop cycle.

Key Microorganisms: Mycorrhiza (VAM), Phosphate Solubilizing Bacteria (PSB), Azospirillum, Potassium Mobilizing Biofertilizer (KMB), Pseudomonas, etc."""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "application_guide",
        "company": "LCB Fertilizers",
        "content_type": "usage_instructions",
        "crop_category": "fruits_and_vegetables",
        "crops_covered": ["watermelon"],
        "application_methods": {
            "transplantation": "base_application_during_seedling_transplantation",
            "follow_up": "base_application_45_days_after_transplantation"
        },
        "dosage_information": {
            "watermelon": {
                "first_application": "50 grams per plant",
                "second_application": "100 grams per plant (45 days later)"
            }
        },
        "application_frequency": "two_dose_system",
        "timing_patterns": {
            "first_dose": "during_seedling_transplantation",
            "second_dose": "45_days_after_transplantation"
        },
        "microorganisms": ["Mycorrhiza (VAM)", "Phosphate Solubilizing Bacteria (PSB)", "Azospirillum", "Potassium Mobilizing Biofertilizer (KMB)", "Pseudomonas"],
        "special_instructions": {
            "watermelon": "two_applications_required_throughout_crop_cycle",
            "application_method": "base_application_per_plant"
        },
        "crop_types": ["fruits", "cucurbits"]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(watermelon_guide_content, metadata, db_session)
        print(f"✅ Successfully added Watermelon Application Guide to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Watermelon Application Guide to database...")
    result = add_watermelon_guide_to_database()
    
    if result:
        print("\n🎉 Watermelon Application Guide has been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide detailed application instructions for watermelon fertilization.")
    else:
        print("\n💥 Failed to add Watermelon Application Guide. Please check the error messages above.")