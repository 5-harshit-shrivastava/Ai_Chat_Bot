#!/usr/bin/env python3
"""
Script to add only the coconut application guide to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_coconut_guide_to_database():
    """Add only coconut application guide information to the database"""
    
    coconut_guide_content = """How to Use Navyakosh: Application Guide for Other Crops

COCONUT

Application (For Mature Trees):
• Method: Dig a ring around the stem, apply the fertilizer, and then cover it with soil
• Dosage: 4-5 kg of Navyakosh Organic Fertilizer per tree

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
        "crop_category": "coconut",
        "crops_covered": ["coconut"],
        "application_methods": {
            "mature_trees": "ring_around_stem_with_soil_cover",
            "seedlings": "base_application_during_transplantation"
        },
        "dosage_information": {
            "coconut": {
                "mature_trees": "4-5 kg per tree",
                "seedlings": "500 grams per plant"
            }
        },
        "microorganisms": ["Mycorrhiza (VAM)", "Phosphate Solubilizing Bacteria", "Azospirillum", "Potassium Mobilizing Biofertilizer (KMB)", "Pseudomonas"],
        "special_instructions": {
            "coconut": "dig_ring_around_stem_cover_with_soil"
        }
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(coconut_guide_content, metadata, db_session)
        print(f"✅ Successfully added Coconut Application Guide to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Coconut Application Guide to database...")
    result = add_coconut_guide_to_database()
    
    if result:
        print("\n🎉 Coconut Application Guide has been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide detailed application instructions for coconut fertilization.")
    else:
        print("\n💥 Failed to add Coconut Application Guide. Please check the error messages above.")