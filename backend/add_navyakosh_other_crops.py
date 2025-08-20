#!/usr/bin/env python3
"""
Script to add Navyakosh other crops application guide to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_navyakosh_other_crops_guide_to_database():
    """Add Navyakosh other crops application guide information to the database"""
    
    other_crops_guide_content = """How to Use Navyakosh: Application Guide for Other Crops

COTTON

1st Application:
• Dosage: 4-5 bags per acre
• Method: Apply using a broadcast pattern on the ridges
• Timing: During land preparation, just before sowing

Second Dose (For Irrigated Crops):
• Dosage: 2-3 bags per acre
• Timing & Method: Apply 45 days after sowing near the base of the plants, immediately after weeding

Mechanism of Action:
Active microorganisms in the fertilizer (Silicate Solubilizing Bacteria, Phosphate Solubilizing Bacteria, Azospirillum, etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle.

WALNUT

Application (For Mature Trees):
• Method: Dig a ring around the stem, apply the fertilizer, and then cover it with soil
• Dosage: 2-5 kg of Navyakosh Organic Fertilizer per tree

Note (For Seedlings):
• Apply 500 grams of fertilizer per plant at the base during seedling transplantation

Mechanism of Action:
Active microorganisms in the fertilizer (Mycorrhiza (VAM), Phosphate Solubilizing Bacteria, Azospirillum, Potassium Mobilizing Biofertilizer (KMB), Pseudomonas, etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle.

PALM

Application (For Mature Trees):
• Method: Dig a ring around the stem, apply the fertilizer, and then cover it with soil
• Dosage: 2-5 kg of Navyakosh Organic Fertilizer per tree

Note (For Seedlings):
• Apply 500 grams of fertilizer per plant at the base during seedling transplantation

Mechanism of Action:
Active microorganisms in the fertilizer (Mycorrhiza (VAM), Phosphate Solubilizing Bacteria, Azospirillum, Potassium Mobilizing Biofertilizer (KMB), Pseudomonas, etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle.

COFFEE

Application by Plant Age:
• Seedlings: 500 grams per plant
• Less than 1 year old: 1 kg per plant
• 2-4 years old: 3 kg per plant
• Above 4 years old: 5 kg per plant

Application Timing:
• First Application: Apply the fertilizer in a 30 cm deep ring around the crop before the monsoon season (pre-monsoon)
• Second Application: Apply after the monsoon season (post-monsoon). For this application, ensure weeds and vegetative debris are completely turned under and buried in the soil, and any stumps are removed

COCONUT

Application (For Mature Trees):
• Method: Dig a ring around the stem, apply the fertilizer, and then cover it with soil
• Dosage: 4-5 kg of Navyakosh Organic Fertilizer per tree

Note (For Seedlings):
• Apply 500 grams of fertilizer per plant at the base during seedling transplantation

Mechanism of Action:
Active microorganisms in the fertilizer (Mycorrhiza (VAM), Phosphate Solubilizing Bacteria, Azospirillum, Potassium Mobilizing Biofertilizer (KMB), Pseudomonas, etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle.

COCONUT (Additional Guide)

Application (For Mature Trees):
• Method: Dig a ring around the stem, apply the fertilizer, and then cover it with soil
• Dosage: 4-5 kg of Navyakosh Organic Fertilizer per tree

Note (For Seedlings):
• Apply 500 grams of fertilizer per plant at the base during seedling transplantation

Mechanism of Action:
Active microorganisms in the fertilizer (Mycorrhiza (VAM), Phosphate Solubilizing Bacteria, Azospirillum, Potassium Mobilizing Biofertilizer (KMB), Pseudomonas, etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle.

SUGARCANE

1st Application:
• Dosage: 4-5 bags per acre
• Method: Apply using a broadcast pattern
• Timing: During land preparation, just before sowing

Second Dose:
• Dosage: 3-4 bags per acre
• Timing & Method: Apply 120 days after sowing, near the base of the plants, just before the "full earthing-up" process

Note (For Transplantation Method):
• If sowing is done by transplantation, use 20-30 grams per seedling during the transplantation process

Mechanism of Action:
Active microorganisms in the fertilizer (Azospirillum, Acetobacter, Azotobacter, Phosphate Solubilizing Bacteria, etc.) get activated and help plants to get and utilize all macro and micronutrients throughout the crop cycle."""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "application_guide",
        "company": "LCB Fertilizers",
        "content_type": "usage_instructions",
        "crop_category": "other_crops",
        "crops_covered": [
            "cotton",
            "walnut",
            "palm",
            "coffee",
            "coconut",
            "sugarcane"
        ],
        "application_methods": {
            "cash_crops": "broadcast_pattern_per_acre",
            "tree_crops": "ring_around_stem_with_soil_cover",
            "sugarcane_transplant": "per_seedling_application"
        },
        "dosage_information": {
            "cotton": {
                "first_application": "4-5 bags per acre",
                "second_application": "2-3 bags per acre (45 days later)"
            },
            "walnut": {
                "mature_trees": "2-5 kg per tree",
                "seedlings": "500 grams per plant"
            },
            "palm": {
                "mature_trees": "2-5 kg per tree",
                "seedlings": "500 grams per plant"
            },
            "coffee": {
                "seedlings": "500 grams per plant",
                "less_than_1_year": "1 kg per plant",
                "2_to_4_years": "3 kg per plant",
                "above_4_years": "5 kg per plant"
            },
            "coconut": {
                "mature_trees": "4-5 kg per tree",
                "seedlings": "500 grams per plant"
            },
            "sugarcane": {
                "first_application": "4-5 bags per acre",
                "second_application": "3-4 bags per acre (120 days later)",
                "transplantation": "20-30 grams per seedling"
            }
        },
        "application_frequency": {
            "two_dose_system": ["cotton", "coffee", "sugarcane"],
            "single_dose_system": ["walnut", "palm", "coconut"]
        },
        "timing_patterns": {
            "cotton": "land_preparation_then_45_days_after_sowing",
            "coffee": "pre_monsoon_and_post_monsoon",
            "sugarcane": "land_preparation_then_120_days_later",
            "tree_crops": "ring_method_around_stem"
        },
        "microorganisms": {
            "cotton": ["Silicate Solubilizing Bacteria", "PSB", "Azospirillum"],
            "tree_crops_general": ["Mycorrhiza (VAM)", "PSB", "Azospirillum", "KMB", "Pseudomonas"],
            "sugarcane": ["Azospirillum", "Acetobacter", "Azotobacter", "PSB"]
        },
        "special_instructions": {
            "cotton": "apply_on_ridges_broadcast_pattern",
            "coffee": "30_cm_deep_ring_seasonal_application",
            "sugarcane": "full_earthing_up_process_timing",
            "coffee_post_monsoon": "remove_weeds_and_debris_before_application"
        },
        "crop_types": {
            "cash_crops": ["cotton", "sugarcane"],
            "tree_nuts": ["walnut", "coconut"],
            "plantation_crops": ["coffee", "palm"]
        }
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(other_crops_guide_content, metadata, db_session)
        print(f"✅ Successfully added Navyakosh Other Crops Application Guide to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Navyakosh Other Crops Application Guide to database...")
    result = add_navyakosh_other_crops_guide_to_database()
    
    if result:
        print("\n🎉 Navyakosh Other Crops Application Guide has been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide detailed application instructions for cotton, walnut, palm, coffee, coconut, and sugarcane.")
    else:
        print("\n💥 Failed to add Navyakosh Other Crops Application Guide. Please check the error messages above.")