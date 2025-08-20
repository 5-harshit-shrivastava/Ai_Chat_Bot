#!/usr/bin/env python3
"""
Script to add Navyakosh FAQ Q8 about purchasing channels to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_navyakosh_faq_q8_to_database():
    """Add Navyakosh FAQ Q8 information to the database"""
    
    navyakosh_faq_q8_content = """Frequently Asked Questions (FAQs) - Navyakosh Organic Fertilizer

Q8: Where can I buy Navyakosh Organic Fertilizer?

A: You can purchase Navyakosh through several channels:
• Online: Visit our store on Amazon at https://amzn.in/d/hBRlaGo
• Retail: Through authorized dealers and agricultural stores
• Bulk Orders: For bulk purchases, please contact us directly at +91 91988 03978"""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "faq",
        "company": "LCB Fertilizers",
        "content_type": "frequently_asked_questions",
        "question_category": "purchasing_information",
        "topics_covered": [
            "purchasing_channels",
            "online_store",
            "retail_availability",
            "bulk_orders",
            "contact_information"
        ],
        "purchasing_channels": [
            "online",
            "retail",
            "bulk_orders"
        ],
        "online_availability": {
            "platform": "Amazon",
            "url": "https://amzn.in/d/hBRlaGo"
        },
        "retail_availability": [
            "authorized_dealers",
            "agricultural_stores"
        ],
        "bulk_order_contact": {
            "phone": "+91 91988 03978",
            "method": "direct_contact"
        },
        "contact_information": [
            "+91 91988 03978"
        ]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(navyakosh_faq_q8_content, metadata, db_session)
        print(f"✅ Successfully added Navyakosh FAQ Q8 to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Navyakosh FAQ Q8 to database...")
    result = add_navyakosh_faq_q8_to_database()
    
    if result:
        print("\n🎉 Navyakosh FAQ Q8 has been successfully added to the RAG chatbot database!")
        print("The chatbot can now answer questions about where to buy Navyakosh Organic Fertilizer.")
    else:
        print("\n💥 Failed to add Navyakosh FAQ Q8. Please check the error messages above.")