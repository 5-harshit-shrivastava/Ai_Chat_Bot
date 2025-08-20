#!/usr/bin/env python3
"""
Script to add Navyakosh key benefits to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_navyakosh_key_benefits_to_database():
    """Add Navyakosh key benefits information to the database"""
    
    navyakosh_key_benefits_content = """Key Benefits:
• Increases Crop Yield: Significantly boosts agricultural output
• Reduces Investment: Lowers overall farming expenses
• Improves Soil Health: Enhances the quality and fertility of the soil
• 100% Organic: A natural and sustainable solution for farming
• Increases Income: Higher yields and lower costs lead to greater profits
• Lab Approved: Certified for quality and effectiveness"""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "product_benefits",
        "company": "LCB Fertilizers",
        "content_type": "key_benefits_summary",
        "topics_covered": [
            "crop_yield_increase",
            "investment_reduction",
            "soil_health_improvement",
            "organic_certification",
            "income_increase",
            "lab_approval"
        ],
        "key_benefits": [
            "increases_crop_yield",
            "reduces_investment",
            "improves_soil_health",
            "100_percent_organic",
            "increases_income",
            "lab_approved"
        ],
        "benefit_details": {
            "crop_yield": "significantly_boosts_agricultural_output",
            "investment": "lowers_overall_farming_expenses",
            "soil_health": "enhances_quality_and_fertility_of_soil",
            "organic_nature": "natural_and_sustainable_solution_for_farming",
            "income": "higher_yields_and_lower_costs_lead_to_greater_profits",
            "certification": "certified_for_quality_and_effectiveness"
        },
        "economic_benefits": [
            "reduces_investment",
            "increases_income",
            "lowers_farming_expenses"
        ],
        "agricultural_benefits": [
            "increases_crop_yield",
            "improves_soil_health",
            "boosts_agricultural_output"
        ],
        "sustainability_benefits": [
            "100_percent_organic",
            "natural_solution",
            "sustainable_farming"
        ],
        "quality_assurance": [
            "lab_approved",
            "certified_for_quality",
            "certified_for_effectiveness"
        ]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(navyakosh_key_benefits_content, metadata, db_session)
        print(f"✅ Successfully added Navyakosh Key Benefits to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Navyakosh Key Benefits to database...")
    result = add_navyakosh_key_benefits_to_database()
    
    if result:
        print("\n🎉 Navyakosh Key Benefits have been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide comprehensive information about Navyakosh benefits.")
    else:
        print("\n💥 Failed to add Navyakosh Key Benefits. Please check the error messages above.")