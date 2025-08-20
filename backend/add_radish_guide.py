#!/usr/bin/env python3
"""
Script to add radish application guide to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_radish_guide_to_database():
    """Add radish application guide information to the database"""
    
    radish_guide_content = """How to Use Navyakosh: Application Guide for Vegetables

RADISH

Application:
• Dosage: 4-5 bags per acre
• Method: Apply using a broadcast pattern
• Timing: During seedbed preparation

Mechanism of Action:
Active microorganisms in the fertilizer (Mycorrhiza (VAM), Phosphate Solubilizing Bacteria, Azospirillum, Potassium Mobilizing Biofertilizer (KMB), Pseudomonas, etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle.

Note: For Radish, this fertilizer is required only once throughout the crop cycle."""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "application_guide",
        "company": "LCB Fertilizers",
        "content_type": "usage_instructions",
        "crop_category": "vegetables",
        "crops_covered": ["radish"],
        "application_methods": {
            "broadcast_pattern": "seedbed_preparation"
        },
        "dosage_information": {
            "radish": {
                "application": "4-5 bags per acre"
            }
        },
        "application_frequency": "single_dose_system",
        "timing_patterns": {
            "single_dose": "during_seedbed_preparation"
        },
        "microorganisms": ["Mycorrhiza (VAM)", "Phosphate Solubilizing Bacteria", "Azospirillum", "Potassium Mobilizing Biofertilizer (KMB)", "Pseudomonas"],
        "special_instructions": {
            "radish": "fertilizer_required_only_once_throughout_crop_cycle",
            "application_method": "broadcast_pattern_during_seedbed_preparation"
        },
        "crop_types": ["vegetables", "root_vegetables"]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(radish_guide_content, metadata, db_session)
        print(f"✅ Successfully added Radish Application Guide to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Radish Application Guide to database...")
    result = add_radish_guide_to_database()
    
    if result:
        print("\n🎉 Radish Application Guide has been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide detailed application instructions for radish fertilization.")
    else:
        print("\n💥 Failed to add Radish Application Guide. Please check the error messages above.")