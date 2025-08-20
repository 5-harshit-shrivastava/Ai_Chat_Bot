#!/usr/bin/env python3
"""
Script to add carrot application guide to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_carrot_guide_to_database():
    """Add carrot application guide information to the database"""
    
    carrot_guide_content = """How to Use Navyakosh: Application Guide for Vegetables

CARROT

Application:
• Dosage: 4-5 bags per acre
• Method: Apply using a broadcast pattern
• Timing: During seedbed preparation

Mechanism of Action:
Active microorganisms in the fertilizer (Mycorrhiza (VAM), Phosphate Solubilizing Bacteria, Azospirillum, Potassium Mobilizing Biofertilizer (KMB), Pseudomonas, etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle.

Note: For Carrot, this fertilizer is required only once throughout the crop cycle."""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "application_guide",
        "company": "LCB Fertilizers",
        "content_type": "usage_instructions",
        "crop_category": "vegetables",
        "crops_covered": ["carrot"],
        "application_methods": {
            "broadcast_pattern": "seedbed_preparation"
        },
        "dosage_information": {
            "carrot": {
                "application": "4-5 bags per acre"
            }
        },
        "application_frequency": "single_dose_system",
        "timing_patterns": {
            "single_dose": "during_seedbed_preparation"
        },
        "microorganisms": ["Mycorrhiza (VAM)", "Phosphate Solubilizing Bacteria", "Azospirillum", "Potassium Mobilizing Biofertilizer (KMB)", "Pseudomonas"],
        "special_instructions": {
            "carrot": "fertilizer_required_only_once_throughout_crop_cycle",
            "application_method": "broadcast_pattern_during_seedbed_preparation"
        },
        "crop_types": ["vegetables", "root_vegetables"]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(carrot_guide_content, metadata, db_session)
        print(f"✅ Successfully added Carrot Application Guide to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Carrot Application Guide to database...")
    result = add_carrot_guide_to_database()
    
    if result:
        print("\n🎉 Carrot Application Guide has been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide detailed application instructions for carrot fertilization.")
    else:
        print("\n💥 Failed to add Carrot Application Guide. Please check the error messages above.")