#!/usr/bin/env python3
"""
Script to add separate cotton application guide to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_cotton_application_guide_to_database():
    """Add cotton application guide to the database"""
    
    cotton_guide_content = """How to Use Navyakosh: Application Guide for Other Crops

COTTON

1st Application:
• Dosage: 4-5 bags per acre
• Method: Apply using a broadcast pattern on the ridges
• Timing: During land preparation, just before sowing

Second Dose (For Irrigated Crops):
• Dosage: 2-3 bags per acre
• Timing & Method: Apply 45 days after sowing near the base of the plants, immediately after weeding

Mechanism of Action:
Active microorganisms in the fertilizer (Silicate Solubilizing Bacteria, Phosphate Solubilizing Bacteria, Azospirillum, etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle."""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "application_guide",
        "company": "LCB Fertilizers",
        "content_type": "usage_instructions",
        "crop_category": "cotton_specific",
        "crops_covered": ["cotton"],
        "application_method": "broadcast_on_ridges",
        "dosage_information": {
            "first_application": "4-5 bags per acre",
            "second_application": "2-3 bags per acre",
            "timing_first": "during land preparation, before sowing",
            "timing_second": "45 days after sowing, after weeding"
        },
        "application_details": {
            "method_first": "broadcast pattern on ridges",
            "method_second": "near base of plants",
            "irrigation_requirement": "for irrigated crops"
        },
        "microorganisms": [
            "Silicate Solubilizing Bacteria",
            "Phosphate Solubilizing Bacteria", 
            "Azospirillum"
        ],
        "timing_pattern": "two_dose_system",
        "special_instructions": [
            "apply_on_ridges_broadcast_pattern",
            "immediate_after_weeding_for_second_dose"
        ],
        "tags": [
            "cotton",
            "cash_crop",
            "broadcast_application",
            "ridge_application",
            "two_dose_system",
            "irrigated_crops"
        ]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(cotton_guide_content, metadata, db_session)
        print(f"✅ Successfully added Cotton Application Guide to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Cotton Application Guide to database...")
    result = add_cotton_application_guide_to_database()
    
    if result:
        print("\n🎉 Cotton Application Guide has been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide detailed cotton-specific application instructions.")
    else:
        print("\n💥 Failed to add Cotton Application Guide. Please check the error messages above.")