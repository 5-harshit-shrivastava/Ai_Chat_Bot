#!/usr/bin/env python3
"""
Script to add sugarcane application guide to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_sugarcane_guide_to_database():
    """Add sugarcane application guide information to the database"""
    
    sugarcane_guide_content = """How to Use Navyakosh: Application Guide for Other Crops

SUGARCANE

1st Application:
• Dosage: 4-5 bags per acre
• Method: Apply using a broadcast pattern
• Timing: During land preparation, just before sowing

Second Dose:
• Dosage: 3-4 bags per acre
• Timing & Method: Apply 120 days after sowing, near the base of the plants, just before the "full earthing-up" process

Note (For Transplantation Method):
• If sowing is done by transplantation, use 20-30 grams per seedling during the transplantation process

Mechanism of Action:
Active microorganisms in the fertilizer (Azospirillum, Acetobacter, Azotobacter, Phosphate Solubilizing Bacteria, etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle."""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "application_guide",
        "company": "LCB Fertilizers",
        "content_type": "usage_instructions",
        "crop_category": "sugarcane",
        "crops_covered": ["sugarcane"],
        "application_methods": {
            "broadcast_pattern": "first_application_land_preparation",
            "base_application": "second_dose_120_days_after_sowing",
            "transplantation": "per_seedling_application"
        },
        "dosage_information": {
            "sugarcane": {
                "first_application": "4-5 bags per acre",
                "second_application": "3-4 bags per acre (120 days later)",
                "transplantation": "20-30 grams per seedling"
            }
        },
        "application_frequency": "two_dose_system",
        "timing_patterns": {
            "first_dose": "land_preparation_before_sowing",
            "second_dose": "120_days_after_sowing_before_earthing_up"
        },
        "microorganisms": ["Azospirillum", "Acetobacter", "Azotobacter", "Phosphate Solubilizing Bacteria"],
        "special_instructions": {
            "sugarcane": "full_earthing_up_process_timing",
            "transplantation_method": "per_seedling_dosage_during_transplantation"
        },
        "crop_types": ["cash_crops"]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(sugarcane_guide_content, metadata, db_session)
        print(f"✅ Successfully added Sugarcane Application Guide to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Sugarcane Application Guide to database...")
    result = add_sugarcane_guide_to_database()
    
    if result:
        print("\n🎉 Sugarcane Application Guide has been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide detailed application instructions for sugarcane fertilization.")
    else:
        print("\n💥 Failed to add Sugarcane Application Guide. Please check the error messages above.")