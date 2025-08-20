#!/usr/bin/env python3
"""
Script to add Navyakosh application guide for fruits and vegetables to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_navyakosh_fruits_vegetables_guide_to_database():
    """Add Navyakosh fruits and vegetables application guide information to the database"""
    
    fruits_vegetables_guide_content = """How to Use Navyakosh: Application Guide for Fruits & Vegetables

MANGO

Application (For Mature Trees):
• Method: Dig a ring around the stem, apply the fertilizer, and then cover it with soil
• Dosage: 4-5 kg of Navyakosh Organic Fertilizer per tree

Note (For Seedlings):
• Apply 500 grams of fertilizer per plant at the base during seedling transplantation

Mechanism of Action:
Active microorganisms in the fertilizer get activated and help plants absorb and utilize all macro and micronutrients throughout the crop cycle.

Key Microorganisms: Mycorrhiza (VAM), Phosphate Solubilizing Bacteria (PSB), Azospirillum, Potassium Mobilizing Biofertilizer (KMB), Pseudomonas, etc.

BANANA

1st Application:
• Dosage: 500 grams of Navyakosh Organic Fertilizer per plant
• Timing & Method: Apply at the base of the plant during seedling transplantation

2nd Application:
• Dosage: 1 kg of Navyakosh Organic Fertilizer per plant
• Timing & Method: Apply at the base of the plant 6 months after seedling transplantation

Mechanism of Action:
Active microorganisms in the fertilizer get activated and help plants absorb and utilize all macro and micronutrients throughout the crop cycle.

Key Microorganisms: Mycorrhiza (VAM), Phosphate Solubilizing Bacteria (PSB), Azospirillum, Potassium Mobilizing Biofertilizer (KMB), etc.

WATERMELON

1st Application:
• Dosage: 50 grams of Navyakosh Organic Fertilizer per plant
• Timing & Method: Apply at the base of the plant during seedling transplantation

2nd Application:
• Dosage: 100 grams of Navyakosh Organic Fertilizer per plant
• Timing & Method: Apply at the base of the plant 45 days after seedling transplantation

Mechanism of Action:
Active microorganisms in the fertilizer get activated and help plants absorb and utilize all macro and micronutrients throughout the crop cycle.

Key Microorganisms: Mycorrhiza (VAM), Phosphate Solubilizing Bacteria (PSB), Azospirillum, Potassium Mobilizing Biofertilizer (KMB), Pseudomonas, etc.

POMEGRANATE

Application (For Mature Trees):
• Method: Dig a ring around the stem, apply the fertilizer, and then cover it with soil
• Dosage: 1-2 kg of Navyakosh Organic Fertilizer per tree

Note (For Seedlings):
• Apply 500 grams of fertilizer per plant at the base during seedling transplantation

Mechanism of Action:
Active microorganisms in the fertilizer get activated and help plants absorb and utilize all macro and micronutrients throughout the crop cycle.

Key Microorganisms: Mycorrhiza (VAM), Phosphate Solubilizing Bacteria (PSB), Azospirillum, Potassium Mobilizing Biofertilizer (KMB), Pseudomonas, etc.

MUSKMELON

1st Application:
• Dosage: 50 grams of Navyakosh Organic Fertilizer per plant
• Timing & Method: Apply at the base of the plant during seedling transplantation

2nd Application:
• Dosage: 100 grams of Navyakosh Organic Fertilizer per plant
• Timing & Method: Apply at the base of the plant 45 days after seedling transplantation

Mechanism of Action:
Active microorganisms in the fertilizer get activated and help plants absorb and utilize all macro and micronutrients throughout the crop cycle.

Key Microorganisms: Mycorrhiza (VAM), Phosphate Solubilizing Bacteria (PSB), Azospirillum, Potassium Mobilizing Biofertilizer (KMB), Pseudomonas, etc.

TOMATO

1st Application:
• Dosage: 50 grams of Navyakosh Organic Fertilizer per plant
• Timing & Method: Apply at the base of the plant during seedling transplantation

2nd Application:
• Dosage: 100 grams of Navyakosh Organic Fertilizer per plant
• Timing & Method: Apply at the base of the plant 45 days after seedling transplantation

Mechanism of Action:
Active microorganisms in the fertilizer get activated and help plants absorb and utilize all macro and micronutrients throughout the crop cycle.

Key Microorganisms: Mycorrhiza (VAM), Phosphate Solubilizing Bacteria (PSB), Azotobacter, Potassium Mobilizing Biofertilizer (KMB), etc."""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "application_guide",
        "company": "LCB Fertilizers",
        "content_type": "usage_instructions",
        "crop_category": "fruits_and_vegetables",
        "crops_covered": [
            "mango",
            "banana",
            "watermelon",
            "pomegranate",
            "muskmelon",
            "tomato"
        ],
        "application_methods": {
            "tree_crops": "ring_around_stem_with_soil_cover",
            "plant_crops": "base_application",
            "seedlings": "base_application_during_transplantation"
        },
        "dosage_information": {
            "mango": {
                "mature_trees": "4-5 kg per tree",
                "seedlings": "500 grams per plant"
            },
            "banana": {
                "first_application": "500 grams per plant",
                "second_application": "1 kg per plant (6 months later)"
            },
            "watermelon": {
                "first_application": "50 grams per plant",
                "second_application": "100 grams per plant (45 days later)"
            },
            "pomegranate": {
                "mature_trees": "1-2 kg per tree",
                "seedlings": "500 grams per plant"
            },
            "muskmelon": {
                "first_application": "50 grams per plant",
                "second_application": "100 grams per plant (45 days later)"
            },
            "tomato": {
                "first_application": "50 grams per plant",
                "second_application": "100 grams per plant (45 days later)"
            }
        },
        "microorganisms": {
            "common": ["Mycorrhiza (VAM)", "PSB", "Azospirillum", "KMB"],
            "mango": ["Mycorrhiza (VAM)", "PSB", "Azospirillum", "KMB", "Pseudomonas"],
            "banana": ["Mycorrhiza (VAM)", "PSB", "Azospirillum", "KMB"],
            "watermelon": ["Mycorrhiza (VAM)", "PSB", "Azospirillum", "KMB", "Pseudomonas"],
            "pomegranate": ["Mycorrhiza (VAM)", "PSB", "Azospirillum", "KMB", "Pseudomonas"],
            "muskmelon": ["Mycorrhiza (VAM)", "PSB", "Azospirillum", "KMB", "Pseudomonas"],
            "tomato": ["Mycorrhiza (VAM)", "PSB", "Azotobacter", "KMB"]
        },
        "timing_patterns": {
            "two_dose_system": ["banana", "watermelon", "muskmelon", "tomato"],
            "single_dose_mature": ["mango", "pomegranate"],
            "transplantation_timing": "during_seedling_transplantation",
            "second_dose_timing": "45_days_or_6_months_depending_on_crop"
        }
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(fruits_vegetables_guide_content, metadata, db_session)
        print(f"✅ Successfully added Navyakosh Fruits & Vegetables Application Guide to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Navyakosh Application Guide for Fruits & Vegetables to database...")
    result = add_navyakosh_fruits_vegetables_guide_to_database()
    
    if result:
        print("\n🎉 Navyakosh Fruits & Vegetables Application Guide has been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide detailed application instructions for mango, banana, watermelon, pomegranate, muskmelon, and tomato.")
    else:
        print("\n💥 Failed to add Navyakosh Fruits & Vegetables Application Guide. Please check the error messages above.")