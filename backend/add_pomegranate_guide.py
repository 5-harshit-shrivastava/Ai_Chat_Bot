#!/usr/bin/env python3
"""
Script to add pomegranate application guide to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_pomegranate_guide_to_database():
    """Add pomegranate application guide information to the database"""
    
    pomegranate_guide_content = """How to Use Navyakosh: Application Guide for Fruits & Vegetables

POMEGRANATE

Application (For Mature Trees):
• Method: Dig a ring around the stem, apply the fertilizer, and then cover it with soil
• Dosage: 1-2 kg of Navyakosh Organic Fertilizer per tree

Note (For Seedlings):
• Apply 500 grams of fertilizer per plant at the base during seedling transplantation

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
        "crops_covered": ["pomegranate"],
        "application_methods": {
            "mature_trees": "ring_around_stem_with_soil_cover",
            "seedlings": "base_application_during_transplantation"
        },
        "dosage_information": {
            "pomegranate": {
                "mature_trees": "1-2 kg per tree",
                "seedlings": "500 grams per plant"
            }
        },
        "application_frequency": "single_dose_system",
        "microorganisms": ["Mycorrhiza (VAM)", "Phosphate Solubilizing Bacteria (PSB)", "Azospirillum", "Potassium Mobilizing Biofertilizer (KMB)", "Pseudomonas"],
        "special_instructions": {
            "pomegranate": "dig_ring_around_stem_cover_with_soil",
            "mature_trees": "ring_method_application",
            "seedlings": "base_application_during_transplantation"
        },
        "crop_types": ["fruits", "tree_fruits"]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(pomegranate_guide_content, metadata, db_session)
        print(f"✅ Successfully added Pomegranate Application Guide to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Pomegranate Application Guide to database...")
    result = add_pomegranate_guide_to_database()
    
    if result:
        print("\n🎉 Pomegranate Application Guide has been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide detailed application instructions for pomegranate fertilization.")
    else:
        print("\n💥 Failed to add Pomegranate Application Guide. Please check the error messages above.")