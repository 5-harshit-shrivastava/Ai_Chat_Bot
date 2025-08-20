#!/usr/bin/env python3
"""
Script to add Navyakosh product overview and description to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_navyakosh_product_overview_to_database():
    """Add Navyakosh product overview and description information to the database"""
    
    navyakosh_product_overview_content = """Navyakosh: The Most Trusted Organic Fertilizer Range

A pioneering, crop-specific organic fertilizer developed using biotechnology, nanotechnology, and chemical engineering. It's designed to boost crop yields, improve soil health, and reduce water usage in one sustainable solution.

Why Choose Navyakosh?
Navyakosh allows farmers to embrace the benefits of organic farming while simultaneously boosting productivity and sustainability."""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "product_overview",
        "company": "LCB Fertilizers",
        "content_type": "product_description_and_positioning",
        "topics_covered": [
            "product_positioning",
            "technology_used",
            "primary_benefits",
            "value_proposition",
            "organic_farming_benefits"
        ],
        "product_positioning": "most_trusted_organic_fertilizer_range",
        "development_technologies": [
            "biotechnology",
            "nanotechnology",
            "chemical_engineering"
        ],
        "product_characteristics": [
            "pioneering",
            "crop_specific",
            "organic_fertilizer"
        ],
        "primary_benefits": [
            "boost_crop_yields",
            "improve_soil_health",
            "reduce_water_usage"
        ],
        "solution_type": "sustainable_solution",
        "value_proposition": [
            "embrace_organic_farming_benefits",
            "boost_productivity",
            "enhance_sustainability"
        ],
        "target_audience": "farmers",
        "key_advantages": [
            "organic_farming_benefits",
            "increased_productivity",
            "sustainability",
            "all_in_one_solution"
        ],
        "product_description": "pioneering_crop_specific_organic_fertilizer_with_advanced_technology"
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(navyakosh_product_overview_content, metadata, db_session)
        print(f"✅ Successfully added Navyakosh Product Overview to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Navyakosh Product Overview to database...")
    result = add_navyakosh_product_overview_to_database()
    
    if result:
        print("\n🎉 Navyakosh Product Overview has been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide comprehensive product positioning and overview information for Navyakosh.")
    else:
        print("\n💥 Failed to add Navyakosh Product Overview. Please check the error messages above.")