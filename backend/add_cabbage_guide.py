#!/usr/bin/env python3
"""
Script to add cabbage application guide to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_cabbage_guide_to_database():
    """Add cabbage application guide information to the database"""
    
    cabbage_guide_content = """How to Use Navyakosh: Application Guide for Vegetables

CABBAGE

Application:
• Dosage: 50 grams of Navyakosh Organic Fertilizer per plant
• Timing & Method: Apply at the base of the plant during seedling transplantation

Mechanism of Action:
Active microorganisms in the fertilizer (Mycorrhiza (VAM), Phosphate Solubilizing Bacteria, Azospirillum, Potassium Mobilizing Biofertilizer (KMB), etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle."""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "application_guide",
        "company": "LCB Fertilizers",
        "content_type": "usage_instructions",
        "crop_category": "vegetables",
        "crops_covered": ["cabbage"],
        "application_methods": {
            "transplantation": "base_application_during_seedling_transplantation"
        },
        "dosage_information": {
            "cabbage": {
                "application": "50 grams per plant"
            }
        },
        "application_frequency": "single_dose_system",
        "timing_patterns": {
            "single_dose": "during_seedling_transplantation"
        },
        "microorganisms": ["Mycorrhiza (VAM)", "Phosphate Solubilizing Bacteria", "Azospirillum", "Potassium Mobilizing Biofertilizer (KMB)"],
        "special_instructions": {
            "cabbage": "apply_at_base_during_transplantation",
            "application_method": "per_plant_base_application"
        },
        "crop_types": ["vegetables", "leafy_vegetables", "brassicas"]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(cabbage_guide_content, metadata, db_session)
        print(f"✅ Successfully added Cabbage Application Guide to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Cabbage Application Guide to database...")
    result = add_cabbage_guide_to_database()
    
    if result:
        print("\n🎉 Cabbage Application Guide has been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide detailed application instructions for cabbage fertilization.")
    else:
        print("\n💥 Failed to add Cabbage Application Guide. Please check the error messages above.")