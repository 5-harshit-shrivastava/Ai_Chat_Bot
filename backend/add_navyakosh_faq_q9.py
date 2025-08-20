#!/usr/bin/env python3
"""
Script to add Navyakosh FAQ Q9 about expected results to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_navyakosh_faq_q9_to_database():
    """Add Navyakosh FAQ Q9 information to the database"""
    
    navyakosh_faq_q9_content = """Frequently Asked Questions (FAQs) - Navyakosh Organic Fertilizer

Q9: What kind of results can I expect after using Navyakosh?

A: Farmers using Navyakosh consistently report higher yields, healthier crops, and better soil quality. Scientific studies have shown remarkable results, including a 29% increase in grain yield and a 24.8% improvement in seed weight compared to conventional chemical fertilizers."""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "faq",
        "company": "LCB Fertilizers",
        "content_type": "frequently_asked_questions",
        "question_category": "expected_results",
        "topics_covered": [
            "expected_results",
            "yield_improvement",
            "crop_health",
            "soil_quality",
            "scientific_studies",
            "performance_comparison"
        ],
        "farmer_reported_benefits": [
            "higher_yields",
            "healthier_crops",
            "better_soil_quality"
        ],
        "scientific_study_results": {
            "grain_yield_increase": "29_percent",
            "seed_weight_improvement": "24_8_percent",
            "comparison_baseline": "conventional_chemical_fertilizers"
        },
        "performance_metrics": [
            "29_percent_increase_in_grain_yield",
            "24_8_percent_improvement_in_seed_weight"
        ],
        "benefits": [
            "higher_yields",
            "healthier_crops",
            "better_soil_quality",
            "scientifically_proven_results"
        ],
        "evidence_type": [
            "farmer_reports",
            "scientific_studies"
        ]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(navyakosh_faq_q9_content, metadata, db_session)
        print(f"✅ Successfully added Navyakosh FAQ Q9 to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Navyakosh FAQ Q9 to database...")
    result = add_navyakosh_faq_q9_to_database()
    
    if result:
        print("\n🎉 Navyakosh FAQ Q9 has been successfully added to the RAG chatbot database!")
        print("The chatbot can now answer questions about expected results from using Navyakosh.")
    else:
        print("\n💥 Failed to add Navyakosh FAQ Q9. Please check the error messages above.")