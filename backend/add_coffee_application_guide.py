#!/usr/bin/env python3
"""
Script to add separate coffee application guide to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_coffee_application_guide_to_database():
    """Add coffee application guide to the database"""
    
    coffee_guide_content = """How to Use Navyakosh: Application Guide for Other Crops

COFFEE

Application by Plant Age:
• Seedlings: 500 grams per plant
• Less than 1 year old: 1 kg per plant
• 2-4 years old: 3 kg per plant
• Above 4 years old: 5 kg per plant

Application Timing:
• First Application: Apply the fertilizer in a 30 cm deep ring around the crop before the monsoon season (pre-monsoon)
• Second Application: Apply after the monsoon season (post-monsoon). For this application, ensure weeds and vegetative debris are completely turned under and buried in the soil, and any stumps are removed"""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "application_guide",
        "company": "LCB Fertilizers",
        "content_type": "usage_instructions",
        "crop_category": "coffee_specific",
        "crops_covered": ["coffee"],
        "application_method": "ring_around_plant_age_based",
        "dosage_information": {
            "seedlings": "500 grams per plant",
            "less_than_1_year": "1 kg per plant",
            "2_to_4_years": "3 kg per plant",
            "above_4_years": "5 kg per plant"
        },
        "application_timing": {
            "first_application": "pre_monsoon_season",
            "second_application": "post_monsoon_season",
            "ring_depth": "30 cm deep ring around crop"
        },
        "special_instructions": {
            "pre_monsoon": "30 cm deep ring application before monsoon",
            "post_monsoon": "remove weeds and vegetative debris, bury in soil, remove stumps"
        },
        "age_based_dosing": {
            "seedling_stage": "500g",
            "young_plant": "1kg",
            "developing_plant": "3kg",
            "mature_plant": "5kg"
        },
        "crop_type": "plantation_crop",
        "application_frequency": "two_dose_seasonal_system",
        "seasonal_timing": [
            "pre_monsoon",
            "post_monsoon"
        ],
        "tags": [
            "coffee",
            "plantation_crop",
            "age_based_dosing",
            "seasonal_application",
            "monsoon_timing",
            "ring_application",
            "deep_ring_method",
            "weed_management"
        ]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(coffee_guide_content, metadata, db_session)
        print(f"✅ Successfully added Coffee Application Guide to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Coffee Application Guide to database...")
    result = add_coffee_application_guide_to_database()
    
    if result:
        print("\n🎉 Coffee Application Guide has been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide detailed coffee-specific application instructions based on plant age and seasonal timing.")
    else:
        print("\n💥 Failed to add Coffee Application Guide. Please check the error messages above.")