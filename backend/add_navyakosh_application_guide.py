#!/usr/bin/env python3
"""
Script to add Navyakosh application guide for grains and millets to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_navyakosh_application_guide_to_database():
    """Add Navyakosh application guide information to the database"""
    
    application_guide_content = """How to Use Navyakosh: Application Guide for Grains & Millets

WHEAT

1st Application:
• Dosage: 4-5 bags per acre
• Method: Apply using a broadcast pattern
• Timing: During land preparation, just before sowing the seeds

Second Dose (For Irrigated Crops):
• Dosage: 2-3 bags per acre
• Timing: Apply 45-60 days after sowing, immediately after weeding

Mechanism of Action:
Active microorganisms in the fertilizer get activated and help plants absorb and utilize all macro and micronutrients throughout the crop cycle.

Key Microorganisms: Azospirillium, Azotobacter, Phosphate Solubilizing Bacteria (PSB), and Sulphur Solubilizing Bacteria (SSB).

PADDY (RICE)

1st Application:
• Dosage: 4-5 bags per acre
• Method: Apply using a broadcast pattern
• Timing: During land preparation, just before sowing the seeds

Second Dose (For Irrigated Crops):
• Dosage: 2-3 bags per acre
• Timing: Apply 45-60 days after sowing, immediately after weeding

Mechanism of Action:
Active microorganisms in the fertilizer get activated and help plants absorb and utilize all macro and micronutrients throughout the crop cycle.

Key Microorganisms: Blue-green algae (Anabaena), Azolla algae, Azospirillum, and Phosphate Solubilizing Bacteria (PSB).

MAIZE (CORN)

1st Application:
• Dosage: 4-5 bags per acre
• Method: Apply using a broadcast pattern
• Timing: During land preparation, just before sowing the seeds

Second Dose (For Irrigated Crops):
• Dosage: 2-3 bags per acre
• Timing: Apply 45-60 days after sowing, immediately after weeding

Mechanism of Action:
Active microorganisms in the fertilizer get activated and help plants absorb and utilize all macro and micronutrients throughout the crop cycle.

Key Microorganisms: Azospirillum, Phosphate Solubilizing Bacteria (PSB), and Vesicular Arbuscular Mycorrhiza (VAM).

Note: The nutrient requirement for maize is higher compared to other cereal crops.

MUSTARD

1st Application:
• Dosage: 4-5 bags per acre
• Method: Apply using a broadcast pattern
• Timing: During land preparation, just before sowing the seeds

Second Dose (For Irrigated Crops):
• Dosage: 2-3 bags per acre
• Timing: Apply 45-60 days after sowing, immediately after weeding

Mechanism of Action:
Active microorganisms in the fertilizer get activated and help plants absorb and utilize all macro and micronutrients throughout the crop cycle.

Key Microorganisms: Azotobacter, Phosphate Solubilizing Bacteria (PSB), and Sulphur Solubilizing Bacteria (SSB).

BAJRA (PEARL MILLET)

1st Application:
• Dosage: 4-5 bags per acre
• Method: Apply using a broadcast pattern
• Timing: During land preparation, just before sowing the seeds

Second Dose (For Irrigated Crops):
• Dosage: 2-3 bags per acre
• Timing: Apply 45-60 days after sowing, immediately after weeding

Mechanism of Action:
Active microorganisms in the fertilizer get activated and help plants absorb and utilize all macro and micronutrients throughout the crop cycle.

Key Microorganisms: Phosphate Solubilizing Bacteria (PSB), Azospirillum, and Vesicular Arbuscular Mycorrhiza (VAM).

JOWAR (GREAT MILLET / SORGHUM)

1st Application:
• Dosage: 4-5 bags per acre
• Method: Apply using a broadcast pattern
• Timing: During land preparation, just before sowing the seeds

Second Dose (For Irrigated Crops):
• Dosage: 2-3 bags per acre
• Timing: Apply 45-60 days after sowing, immediately after weeding

Mechanism of Action:
Active microorganisms in the fertilizer get activated and help plants absorb and utilize all macro and micronutrients throughout the crop cycle.

Key Microorganisms: Phosphate Solubilizing Bacteria (PSB), Azospirillum, and Vesicular Arbuscular Mycorrhiza (VAM)."""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "application_guide",
        "company": "LCB Fertilizers",
        "content_type": "usage_instructions",
        "crop_category": "grains_and_millets",
        "application_method": "broadcast_pattern",
        "crops_covered": [
            "wheat",
            "paddy_rice",
            "maize_corn",
            "mustard",
            "bajra_pearl_millet",
            "jowar_sorghum"
        ],
        "dosage_information": {
            "first_application": "4-5 bags per acre",
            "second_application": "2-3 bags per acre",
            "timing_first": "during land preparation, before sowing",
            "timing_second": "45-60 days after sowing, after weeding"
        },
        "microorganisms": {
            "wheat": ["Azospirillium", "Azotobacter", "PSB", "SSB"],
            "paddy": ["Blue-green algae (Anabaena)", "Azolla algae", "Azospirillum", "PSB"],
            "maize": ["Azospirillum", "PSB", "VAM"],
            "mustard": ["Azotobacter", "PSB", "SSB"],
            "bajra": ["PSB", "Azospirillum", "VAM"],
            "jowar": ["PSB", "Azospirillum", "VAM"]
        },
        "key_features": [
            "broadcast_application",
            "two_dose_system",
            "microorganism_activation",
            "macro_micronutrient_absorption",
            "crop_specific_formulation"
        ]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(application_guide_content, metadata, db_session)
        print(f"✅ Successfully added Navyakosh Application Guide to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Navyakosh Application Guide for Grains & Millets to database...")
    result = add_navyakosh_application_guide_to_database()
    
    if result:
        print("\n🎉 Navyakosh Application Guide has been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide detailed application instructions for wheat, rice, maize, mustard, bajra, and jowar.")
    else:
        print("\n💥 Failed to add Navyakosh Application Guide. Please check the error messages above.")