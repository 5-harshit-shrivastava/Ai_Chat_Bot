#!/usr/bin/env python3
"""
Script to add Navyakosh additional vegetables application guide to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_navyakosh_additional_vegetables_guide_to_database():
    """Add Navyakosh additional vegetables application guide information to the database"""
    
    additional_vegetables_guide_content = """How to Use Navyakosh: Application Guide for Vegetables

CUCUMBER

1st Application:
• Dosage: 50 grams of Navyakosh Organic Fertilizer per plant
• Timing & Method: Apply at the base of the plant during seedling transplantation

2nd Application:
• Dosage: 100 grams of Navyakosh Organic Fertilizer per plant
• Timing & Method: Apply at the base of the plant 45 days after seedling transplantation

Mechanism of Action:
Active microorganisms in the fertilizer (Mycorrhiza (VAM), Phosphate Solubilizing Bacteria, Azospirillum, Potassium Mobilizing Biofertilizer (KMB), Pseudomonas, etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle.

Note: For Cucumber, application is required two times throughout the crop cycle.

CARROT

Application:
• Dosage: 4-5 bags per acre
• Method: Apply using a broadcast pattern
• Timing: During seedbed preparation

Mechanism of Action:
Active microorganisms in the fertilizer (Mycorrhiza (VAM), Phosphate Solubilizing Bacteria, Azospirillum, Potassium Mobilizing Biofertilizer (KMB), Pseudomonas, etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle.

Note: For Carrot, this fertilizer is required only once throughout the crop cycle.

RADISH

Application:
• Dosage: 4-5 bags per acre
• Method: Apply using a broadcast pattern
• Timing: During seedbed preparation

Mechanism of Action:
Active microorganisms in the fertilizer (Mycorrhiza (VAM), Phosphate Solubilizing Bacteria, Azospirillum, Potassium Mobilizing Biofertilizer (KMB), Pseudomonas, etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle.

Note: For Radish, this fertilizer is required only once throughout the crop cycle.

CABBAGE

Application:
• Dosage: 50 grams of Navyakosh Organic Fertilizer per plant
• Timing & Method: Apply at the base of the plant during seedling transplantation

Mechanism of Action:
Active microorganisms in the fertilizer (Mycorrhiza (VAM), Phosphate Solubilizing Bacteria, Azospirillum, Potassium Mobilizing Biofertilizer (KMB), etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle.

CAPSICUM (BELL PEPPER)

1st Application:
• Dosage: 50 grams of Navyakosh Organic Fertilizer per plant
• Timing & Method: Apply at the base of the plant during seedling transplantation

2nd Application:
• Dosage: 100 grams of Navyakosh Organic Fertilizer per plant
• Timing & Method: Apply at the base of the plant 45 days after seedling transplantation

Mechanism of Action:
Active microorganisms in the fertilizer (Mycorrhiza (VAM), Phosphate Solubilizing Bacteria, Azotobacter, Potassium Mobilizing Biofertilizer (KMB), etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle.

BRINJAL (EGGPLANT)

1st Application:
• Dosage: 50 grams of Navyakosh Organic Fertilizer per plant
• Timing & Method: Apply at the base of the plant during seedling transplantation

2nd Application:
• Dosage: 100 grams of Navyakosh Organic Fertilizer per plant
• Timing & Method: Apply at the base of the plant 45 days after seedling transplantation

Mechanism of Action:
Active microorganisms in the fertilizer (Mycorrhiza (VAM), Phosphate Solubilizing Bacteria, Azotobacter, Potassium Mobilizing Biofertilizer (KMB), etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle."""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "application_guide",
        "company": "LCB Fertilizers",
        "content_type": "usage_instructions",
        "crop_category": "additional_vegetables",
        "crops_covered": [
            "cucumber",
            "carrot",
            "radish",
            "cabbage",
            "capsicum_bell_pepper",
            "brinjal_eggplant"
        ],
        "application_methods": {
            "individual_plants": "base_application_per_plant",
            "field_crops": "broadcast_pattern_per_acre",
            "timing_transplantation": "during_seedling_transplantation",
            "timing_field_prep": "during_seedbed_preparation"
        },
        "dosage_information": {
            "cucumber": {
                "first_application": "50 grams per plant",
                "second_application": "100 grams per plant (45 days later)"
            },
            "carrot": {
                "single_application": "4-5 bags per acre"
            },
            "radish": {
                "single_application": "4-5 bags per acre"
            },
            "cabbage": {
                "single_application": "50 grams per plant"
            },
            "capsicum": {
                "first_application": "50 grams per plant",
                "second_application": "100 grams per plant (45 days later)"
            },
            "brinjal": {
                "first_application": "50 grams per plant",
                "second_application": "100 grams per plant (45 days later)"
            }
        },
        "application_frequency": {
            "two_applications": ["cucumber", "capsicum", "brinjal"],
            "single_application": ["carrot", "radish", "cabbage"]
        },
        "microorganisms": {
            "common_all": ["Mycorrhiza (VAM)", "PSB", "Azospirillum", "KMB"],
            "cucumber": ["Mycorrhiza (VAM)", "PSB", "Azospirillum", "KMB", "Pseudomonas"],
            "carrot": ["Mycorrhiza (VAM)", "PSB", "Azospirillum", "KMB", "Pseudomonas"],
            "radish": ["Mycorrhiza (VAM)", "PSB", "Azospirillum", "KMB", "Pseudomonas"],
            "cabbage": ["Mycorrhiza (VAM)", "PSB", "Azospirillum", "KMB"],
            "capsicum": ["Mycorrhiza (VAM)", "PSB", "Azotobacter", "KMB"],
            "brinjal": ["Mycorrhiza (VAM)", "PSB", "Azotobacter", "KMB"]
        },
        "timing_patterns": {
            "transplantation_crops": ["cucumber", "cabbage", "capsicum", "brinjal"],
            "direct_seeding_crops": ["carrot", "radish"],
            "second_dose_timing": "45_days_after_transplantation"
        }
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(additional_vegetables_guide_content, metadata, db_session)
        print(f"✅ Successfully added Navyakosh Additional Vegetables Application Guide to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Navyakosh Additional Vegetables Application Guide to database...")
    result = add_navyakosh_additional_vegetables_guide_to_database()
    
    if result:
        print("\n🎉 Navyakosh Additional Vegetables Application Guide has been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide detailed application instructions for cucumber, carrot, radish, cabbage, capsicum, and brinjal.")
    else:
        print("\n💥 Failed to add Navyakosh Additional Vegetables Application Guide. Please check the error messages above.")