#!/usr/bin/env python3
"""
Script to add Navyakosh nuts and pulses application guide to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_navyakosh_nuts_pulses_guide_to_database():
    """Add Navyakosh nuts and pulses application guide information to the database"""
    
    nuts_pulses_guide_content = """How to Use Navyakosh: Application Guide for Nuts & Pulses

ARECA NUT

Application (For Mature Trees):
• Method: Dig a ring around the stem, apply the fertilizer, and then cover it with soil
• Dosage: 2-3 kg of Navyakosh Organic Fertilizer per tree

Note (For Seedlings):
• Apply 500 grams of fertilizer per plant at the base during seedling transplantation

Mechanism of Action:
Active microorganisms in the fertilizer (Mycorrhiza (VAM), Phosphate Solubilizing Bacteria, Azospirillum, Potassium Mobilizing Biofertilizer (KMB), Pseudomonas, etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle.

CASHEW NUT

Application (For Mature Trees):
• Method: Dig a ring around the stem, apply the fertilizer, and then cover it with soil
• Dosage: 3-4 kg of Navyakosh Organic Fertilizer per tree

Note (For Seedlings):
• Apply 500 grams of fertilizer per plant at the base during seedling transplantation

Mechanism of Action:
Active microorganisms in the fertilizer (Mycorrhiza (VAM), Phosphate Solubilizing Bacteria, Azospirillum, Potassium Mobilizing Biofertilizer (KMB), Pseudomonas, etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle.

GROUND NUT (PEANUT)

1st Application:
• Dosage: 4-5 bags per acre
• Method: Apply using a broadcast pattern
• Timing: During land preparation, just before sowing the seeds

Second Dose (For Irrigated Crops):
• Dosage: 2-3 bags per acre
• Timing: Apply 45-60 days after sowing, immediately after weeding

Mechanism of Action:
Active microorganisms in the fertilizer (Phosphate Solubilizing Bacteria, Rhizobium, Azospirillum, etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle.

CHICKPEA DAL (CHANA)

1st Application:
• Dosage: 4-5 bags per acre
• Method: Apply using a broadcast pattern
• Timing: During land preparation, just before sowing the seeds

Second Dose (For Irrigated Crops):
• Dosage: 2-3 bags per acre
• Timing: Apply 45-60 days after sowing, immediately after weeding

Mechanism of Action:
Active microorganisms in the fertilizer (Rhizobium, Phosphate Solubilizing Bacteria, Vesicular Arbuscular Mycorrhiza (VAM), etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle.

SOYA BEANS

1st Application:
• Dosage: 4-5 bags per acre
• Method: Apply using a broadcast pattern
• Timing: During land preparation, just before sowing the seeds

Second Dose (For Irrigated Crops):
• Dosage: 2-3 bags per acre
• Timing: Apply 45-60 days after sowing, immediately after weeding

Mechanism of Action:
Active microorganisms in the fertilizer (Rhizobium, Phosphate Solubilizing Bacteria, Vesicular Arbuscular Mycorrhiza (VAM), etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle.

TUR DAL (ARHAR / PIGEON PEA)

1st Application:
• Dosage: 4-5 bags per acre
• Method: Apply using a broadcast pattern
• Timing: During land preparation, just before sowing the seeds

Second Dose (For Irrigated Crops):
• Dosage: 2-3 bags per acre
• Timing: Apply 45-60 days after sowing, immediately after weeding

Mechanism of Action:
Active microorganisms in the fertilizer (Rhizobium, Phosphate Solubilizing Bacteria, Vesicular Arbuscular Mycorrhiza (VAM), etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle."""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "application_guide",
        "company": "LCB Fertilizers",
        "content_type": "usage_instructions",
        "crop_category": "nuts_and_pulses",
        "crops_covered": [
            "areca_nut",
            "cashew_nut",
            "ground_nut_peanut",
            "chickpea_dal_chana",
            "soya_beans",
            "tur_dal_arhar_pigeon_pea"
        ],
        "application_methods": {
            "nut_trees": "ring_around_stem_with_soil_cover",
            "pulse_crops": "broadcast_pattern_per_acre",
            "seedlings": "base_application_during_transplantation"
        },
        "dosage_information": {
            "areca_nut": {
                "mature_trees": "2-3 kg per tree",
                "seedlings": "500 grams per plant"
            },
            "cashew_nut": {
                "mature_trees": "3-4 kg per tree",
                "seedlings": "500 grams per plant"
            },
            "ground_nut": {
                "first_application": "4-5 bags per acre",
                "second_application": "2-3 bags per acre (45-60 days later)"
            },
            "chickpea_dal": {
                "first_application": "4-5 bags per acre",
                "second_application": "2-3 bags per acre (45-60 days later)"
            },
            "soya_beans": {
                "first_application": "4-5 bags per acre",
                "second_application": "2-3 bags per acre (45-60 days later)"
            },
            "tur_dal": {
                "first_application": "4-5 bags per acre",
                "second_application": "2-3 bags per acre (45-60 days later)"
            }
        },
        "application_frequency": {
            "tree_crops_single": ["areca_nut", "cashew_nut"],
            "pulse_crops_two_doses": ["ground_nut", "chickpea_dal", "soya_beans", "tur_dal"]
        },
        "microorganisms": {
            "nut_trees": ["Mycorrhiza (VAM)", "PSB", "Azospirillum", "KMB", "Pseudomonas"],
            "ground_nut": ["PSB", "Rhizobium", "Azospirillum"],
            "legume_pulses": ["Rhizobium", "PSB", "VAM"]
        },
        "timing_patterns": {
            "tree_application": "ring_method_around_stem",
            "pulse_first_dose": "during_land_preparation_before_sowing",
            "pulse_second_dose": "45_60_days_after_sowing_after_weeding",
            "seedling_timing": "during_transplantation"
        },
        "crop_types": {
            "nuts": ["areca_nut", "cashew_nut", "ground_nut"],
            "pulses_legumes": ["chickpea_dal", "soya_beans", "tur_dal"]
        }
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(nuts_pulses_guide_content, metadata, db_session)
        print(f"✅ Successfully added Navyakosh Nuts & Pulses Application Guide to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Navyakosh Nuts & Pulses Application Guide to database...")
    result = add_navyakosh_nuts_pulses_guide_to_database()
    
    if result:
        print("\n🎉 Navyakosh Nuts & Pulses Application Guide has been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide detailed application instructions for areca nut, cashew nut, ground nut, chickpea dal, soya beans, and tur dal.")
    else:
        print("\n💥 Failed to add Navyakosh Nuts & Pulses Application Guide. Please check the error messages above.")