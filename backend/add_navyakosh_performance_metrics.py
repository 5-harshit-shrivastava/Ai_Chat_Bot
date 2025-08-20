#!/usr/bin/env python3
"""
Script to add Navyakosh performance metrics to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_navyakosh_performance_metrics_to_database():
    """Add Navyakosh performance metrics information to the database"""
    
    navyakosh_performance_metrics_content = """Performance Metrics:
Navyakosh delivers measurable results:
• Up to 21% Reduction in Farming Expenses
• A 33% Decrease in Crop Irrigation Demand
• As high as a 35% Increase in Crop Yield
• Up to a 42% Increase in Organic Soil Matter"""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "performance_metrics",
        "company": "LCB Fertilizers",
        "content_type": "measurable_results",
        "topics_covered": [
            "farming_expense_reduction",
            "irrigation_demand_decrease",
            "crop_yield_increase",
            "organic_soil_matter_increase"
        ],
        "performance_metrics": {
            "farming_expenses_reduction": "up_to_21_percent",
            "irrigation_demand_decrease": "33_percent",
            "crop_yield_increase": "up_to_35_percent",
            "organic_soil_matter_increase": "up_to_42_percent"
        },
        "economic_metrics": [
            "21_percent_reduction_in_farming_expenses"
        ],
        "water_conservation_metrics": [
            "33_percent_decrease_in_irrigation_demand"
        ],
        "productivity_metrics": [
            "35_percent_increase_in_crop_yield"
        ],
        "soil_health_metrics": [
            "42_percent_increase_in_organic_soil_matter"
        ],
        "measurable_benefits": [
            "reduces_farming_expenses_by_21_percent",
            "decreases_irrigation_demand_by_33_percent",
            "increases_crop_yield_by_35_percent",
            "increases_organic_soil_matter_by_42_percent"
        ],
        "result_categories": [
            "cost_reduction",
            "water_conservation",
            "yield_improvement",
            "soil_enhancement"
        ]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(navyakosh_performance_metrics_content, metadata, db_session)
        print(f"✅ Successfully added Navyakosh Performance Metrics to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Navyakosh Performance Metrics to database...")
    result = add_navyakosh_performance_metrics_to_database()
    
    if result:
        print("\n🎉 Navyakosh Performance Metrics have been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide specific performance data and measurable results for Navyakosh.")
    else:
        print("\n💥 Failed to add Navyakosh Performance Metrics. Please check the error messages above.")