#!/usr/bin/env python3
"""
Script to add Navyakosh certifications and recommendations to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_navyakosh_certifications_to_database():
    """Add Navyakosh certifications and recommendations information to the database"""
    
    navyakosh_certifications_content = """Certifications & Recommendations:
• Government Approved (Authorization Letter Exemption): LCB Fertilizers is exempted from needing an authority letter to manufacture Navyakosh organic fertilizers
• NABL Lab Tested: Certified by a reputed, NABL-accredited Government of India laboratory
• Recommended by ICAR and IIPR: Has received official recommendations from the Indian Council of Agricultural Research (ICAR) and the Indian Institute of Pulses Research (IIPR)
• Proven Performer: A comparative analysis by DAV PG College, Gorakhpur, concluded that Navyakosh is superior for crop production"""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "certifications_and_recommendations",
        "company": "LCB Fertilizers",
        "content_type": "official_approvals_and_certifications",
        "topics_covered": [
            "government_approval",
            "lab_testing_certification",
            "institutional_recommendations",
            "comparative_analysis_results"
        ],
        "government_approvals": [
            "authorization_letter_exemption",
            "government_approved_manufacturing"
        ],
        "lab_certifications": [
            "NABL_lab_tested",
            "government_of_india_laboratory_certified"
        ],
        "institutional_recommendations": [
            "ICAR_recommended",
            "IIPR_recommended"
        ],
        "research_validations": [
            "DAV_PG_College_comparative_analysis",
            "proven_superior_for_crop_production"
        ],
        "certification_details": {
            "government_approval": "LCB_Fertilizers_exempted_from_authority_letter_requirement",
            "lab_testing": "NABL_accredited_Government_of_India_laboratory",
            "ICAR": "Indian_Council_of_Agricultural_Research",
            "IIPR": "Indian_Institute_of_Pulses_Research",
            "research_institution": "DAV_PG_College_Gorakhpur"
        },
        "credibility_indicators": [
            "government_approved",
            "NABL_lab_tested",
            "ICAR_recommended",
            "IIPR_recommended",
            "research_validated"
        ],
        "quality_assurance": [
            "NABL_accredited_testing",
            "government_laboratory_certification",
            "institutional_recommendations",
            "comparative_analysis_superiority"
        ]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(navyakosh_certifications_content, metadata, db_session)
        print(f"✅ Successfully added Navyakosh Certifications & Recommendations to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Navyakosh Certifications & Recommendations to database...")
    result = add_navyakosh_certifications_to_database()
    
    if result:
        print("\n🎉 Navyakosh Certifications & Recommendations have been successfully added to the RAG chatbot database!")
        print("The chatbot can now provide detailed information about Navyakosh's official approvals, certifications, and institutional recommendations.")
    else:
        print("\n💥 Failed to add Navyakosh Certifications & Recommendations. Please check the error messages above.")