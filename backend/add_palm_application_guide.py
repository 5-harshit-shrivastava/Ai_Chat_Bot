#!/usr/bin/env python3
"""
Script to add separate palm application guide to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_palm_application_guide_to_database():
    """Add palm application guide to the database"""
    
    palm_guide_content = """How to Use Navyakosh: Application Guide for Other Crops

PALM

Application (For Mature Trees):
• Method: Dig a ring around the stem, apply the fertilizer, and then cover it with soil
• Dosage: 2-5 kg of Navyakosh Organic Fertilizer per tree

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
        "crop_category": "palm_specific",
        "crops_covered": ["palm"],
        "application_method": "ring_around_stem",
        "dosage_information": {
            "mature_trees": "2-5 kg per tree",
            "seedlings": "500 grams per plant",
            "application_timing": "during seedling transplantation"
        },
        "application_details": {
            "method_mature": "dig ring around stem and cover with soil",
            "method_seedlings": "base application during transplantation",
            "tree_stage": ["mature_trees", "seedlings"]
        },
        "microorganisms": [
            "Mycorrhiza (VAM)",
            "Phosphate Solubilizing Bacteria",
            "Azospirillum",
            "Potassium Mobilizing Biofertilizer (KMB)",
            "Pseudomonas"
        ],
        "crop_type": "plantation_crop",
        "application_frequency": "single_dose_system",
        "special_instructions": [
            "ring_method_for_mature_trees",
            "base_application_for_seedlings",
            "cover_with_soil_after_application"
        ],
        "tags": [
            "palm",
            "plantation_crop",
            "ring_application",
            "mature_trees",
            "seedlings",
            "transplantation",
            "tree_crop",
            "tropical_crop"
        ]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(palm_guide_content, metadata, db_session)
        print(f"✅ Successfully added Palm Application Guide to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Palm Application Guide to database...")
    result = add_palm_application_guide_to_database()
    
    if result:
        print("\n🎉 Palm Application Guide has been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide detailed palm-specific application instructions.")
    else:
        print("\n💥 Failed to add Palm Application Guide. Please check the error messages above.")