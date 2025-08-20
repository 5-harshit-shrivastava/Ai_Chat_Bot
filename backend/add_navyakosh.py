#!/usr/bin/env python3
"""
Script to add Navyakosh product information to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_navyakosh_to_database():
    """Add Navyakosh product information to the database"""
    
    navyakosh_content = """Navyakosh: The Most Trusted Organic Fertilizer Range

A pioneering, crop-specific organic fertilizer developed using biotechnology, nanotechnology, and chemical engineering. It's designed to boost crop yields, improve soil health, and reduce water usage in one sustainable solution.

Key Benefits:
• Increases Crop Yield: Significantly boosts agricultural output
• Reduces Investment: Lowers overall farming expenses
• Improves Soil Health: Enhances the quality and fertility of the soil
• 100% Organic: A natural and sustainable solution for farming
• Increases Income: Higher yields and lower costs lead to greater profits
• Lab Approved: Certified for quality and effectiveness

Performance Metrics:
Navyakosh delivers measurable results:
• Up to 21% Reduction in Farming Expenses
• A 33% Decrease in Crop Irrigation Demand
• As high as a 35% Increase in Crop Yield
• Up to a 42% Increase in Organic Soil Matter

Why Choose Navyakosh?
Navyakosh allows farmers to embrace the benefits of organic farming while simultaneously boosting productivity and sustainability.

Certifications & Recommendations:
• Government Approved (Authorization Letter Exemption): LCB Fertilizers is exempted from needing an authority letter to manufacture Navyakosh organic fertilizers
• NABL Lab Tested: Certified by a reputed, NABL-accredited Government of India laboratory
• Recommended by ICAR and IIPR: Has received official recommendations from the Indian Council of Agricultural Research (ICAR) and the Indian Institute of Pulses Research (IIPR)
• Proven Performer: A comparative analysis by DAV PG College, Gorakhpur, concluded that Navyakosh is superior for crop production"""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "company": "LCB Fertilizers",
        "type": "product_information",
        "benefits": [
            "increases_crop_yield",
            "reduces_investment",
            "improves_soil_health",
            "100_percent_organic",
            "increases_income",
            "lab_approved"
        ],
        "performance_metrics": {
            "farming_expense_reduction": "21%",
            "irrigation_demand_decrease": "33%",
            "crop_yield_increase": "35%",
            "organic_soil_matter_increase": "42%"
        },
        "certifications": [
            "government_approved",
            "nabl_lab_tested",
            "icar_recommended",
            "iipr_recommended"
        ]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(navyakosh_content, metadata, db_session)
        print(f"✅ Successfully added Navyakosh to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Navyakosh product information to database...")
    result = add_navyakosh_to_database()
    
    if result:
        print("\n🎉 Navyakosh product information has been successfully added to the RAG chatbot database!")
        print("The chatbot can now answer questions about Navyakosh organic fertilizers.")
    else:
        print("\n💥 Failed to add Navyakosh information. Please check the error messages above.")