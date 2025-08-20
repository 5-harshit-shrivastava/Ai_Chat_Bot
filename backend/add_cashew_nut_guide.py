#!/usr/bin/env python3
"""
Script to add cashew nut application guide to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_cashew_nut_guide_to_database():
    """Add cashew nut application guide information to the database"""
    
    cashew_nut_guide_content = """How to Use Navyakosh: Application Guide for Nuts & Pulses

CASHEW NUT

Application (For Mature Trees):
• Method: Dig a ring around the stem, apply the fertilizer, and then cover it with soil
• Dosage: 3-4 kg of Navyakosh Organic Fertilizer per tree

Note (For Seedlings):
• Apply 500 grams of fertilizer per plant at the base during seedling transplantation

Mechanism of Action:
Active microorganisms in the fertilizer (Mycorrhiza (VAM), Phosphate Solubilizing Bacteria, Azospirillum, Potassium Mobilizing Biofertilizer (KMB), Pseudomonas, etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle."""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "application_guide",
        "company": "LCB Fertilizers",
        "content_type": "usage_instructions",
        "crop_category": "nuts_and_pulses",
        "crops_covered": ["cashew_nut"],
        "application_methods": {
            "mature_trees": "ring_around_stem_with_soil_cover",
            "seedlings": "base_application_during_transplantation"
        },
        "dosage_information": {
            "cashew_nut": {
                "mature_trees": "3-4 kg per tree",
                "seedlings": "500 grams per plant"
            }
        },
        "application_frequency": "single_dose_system",
        "microorganisms": ["Mycorrhiza (VAM)", "Phosphate Solubilizing Bacteria", "Azospirillum", "Potassium Mobilizing Biofertilizer (KMB)", "Pseudomonas"],
        "special_instructions": {
            "cashew_nut": "dig_ring_around_stem_cover_with_soil"
        },
        "crop_types": ["tree_nuts"]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(cashew_nut_guide_content, metadata, db_session)
        print(f"✅ Successfully added Cashew Nut Application Guide to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Cashew Nut Application Guide to database...")
    result = add_cashew_nut_guide_to_database()
    
    if result:
        print("\n🎉 Cashew Nut Application Guide has been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide detailed application instructions for cashew nut fertilization.")
    else:
        print("\n💥 Failed to add Cashew Nut Application Guide. Please check the error messages above.")