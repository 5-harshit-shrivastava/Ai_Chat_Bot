#!/usr/bin/env python3
"""
Script to add jowar (great millet/sorghum) application guide to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_jowar_sorghum_guide_to_database():
    """Add jowar sorghum application guide information to the database"""
    
    jowar_sorghum_guide_content = """How to Use Navyakosh: Application Guide for Grains & Millets

JOWAR (GREAT MILLET / SORGHUM)

1st Application:
• Dosage: 4-5 bags per acre
• Method: Apply using a broadcast pattern
• Timing: During land preparation, just before sowing the seeds

Second Dose (For Irrigated Crops):
• Dosage: 2-3 bags per acre
• Timing: Apply 45-60 days after sowing, immediately after weeding

Mechanism of Action:
Active microorganisms in the fertilizer get activated and help plants absorb and utilize all macro and micronutrients throughout the crop cycle.

Key Microorganisms: Phosphate Solubilizing Bacteria (PSB), Azospirillum, and Vesicular Arbuscular Mycorrhiza (VAM)."""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "application_guide",
        "company": "LCB Fertilizers",
        "content_type": "usage_instructions",
        "crop_category": "grains_and_millets",
        "crops_covered": ["jowar", "great_millet", "sorghum"],
        "application_methods": {
            "broadcast_pattern": "first_application_land_preparation",
            "post_weeding_application": "second_dose_45_60_days_after_sowing"
        },
        "dosage_information": {
            "jowar": {
                "first_application": "4-5 bags per acre",
                "second_application": "2-3 bags per acre (45-60 days later)"
            }
        },
        "application_frequency": "two_dose_system",
        "timing_patterns": {
            "first_dose": "land_preparation_before_sowing",
            "second_dose": "45_60_days_after_sowing_post_weeding"
        },
        "microorganisms": ["Phosphate Solubilizing Bacteria (PSB)", "Azospirillum", "Vesicular Arbuscular Mycorrhiza (VAM)"],
        "special_instructions": {
            "jowar": "broadcast_pattern_land_preparation_then_post_weeding",
            "irrigated_crops": "second_dose_after_weeding_for_irrigated_crops"
        },
        "crop_types": ["millets", "drought_resistant_crops"]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(jowar_sorghum_guide_content, metadata, db_session)
        print(f"✅ Successfully added Jowar (Great Millet/Sorghum) Application Guide to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Jowar (Great Millet/Sorghum) Application Guide to database...")
    result = add_jowar_sorghum_guide_to_database()
    
    if result:
        print("\n🎉 Jowar (Great Millet/Sorghum) Application Guide has been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide detailed application instructions for jowar/great millet/sorghum fertilization.")
    else:
        print("\n💥 Failed to add Jowar (Great Millet/Sorghum) Application Guide. Please check the error messages above.")