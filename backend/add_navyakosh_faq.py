#!/usr/bin/env python3
"""
Script to add Navyakosh FAQ information to the RAG chatbot database.
"""

from db import get_db, init_db
from ingest import add_document

def add_navyakosh_faq_to_database():
    """Add Navyakosh FAQ information to the database"""
    
    faq_content = """Frequently Asked Questions (FAQs) - Navyakosh Organic Fertilizer

Q1: What is Navyakosh Organic Fertilizer, and how is it different from chemical fertilizers?

A: Navyakosh is a 100% organic fertilizer made from natural ingredients like cow dung, agricultural waste, and fermented organic manure. Unlike chemical fertilizers that can leave harmful residues, Navyakosh enriches the soil's natural health and supports sustainable farming by increasing yields while protecting the environment.

Q2: How does Navyakosh improve soil health?

A: Navyakosh contains 60 types of beneficial microorganisms that restore the soil's natural balance. These microbes break down complex nutrients, making them easily available for crops. It also adds significant organic matter, which improves soil fertility and its capacity to hold water.

Q3: Can Navyakosh reduce the need for irrigation?

A: Yes. Navyakosh uses advanced super absorbent polymer technology. These polymers can absorb up to 268 times their weight in water and release it slowly back to the plant roots. This process keeps the soil moist for longer and can reduce irrigation needs by up to 33%.

Q4: On which crops can I use Navyakosh?

A: Navyakosh is a versatile, one-time-use fertilizer suitable for a wide range of crops, including:
• Wheat, Rice, Maize, Bajra, Jowar
• Cotton and Sugarcane
• Pulses
• Vegetables, Fruits, and Spices

It is designed to be crop-specific, adapting to the unique needs of each plant.

Q5: Is Navyakosh safe for my crops, family, and the environment?

A: Absolutely. Navyakosh is 100% organic and free from harmful chemicals. It does not pollute the soil, water, or air. Crops grown using Navyakosh are safe and healthy for consumption.

Q6: Can I use Navyakosh with other fertilizers or pesticides?

A: Navyakosh is a comprehensive solution designed to meet most of your crop's nutrient needs, which significantly reduces the requirement for additional chemical fertilizers.

Q7: How do I apply Navyakosh to my crops?

A: Apply Navyakosh according to the recommended dosage for your specific crop (e.g., wheat, paddy). After application, it is important to irrigate the field to activate the nutrients and the super absorbent polymers.

Q8: Where can I buy Navyakosh Organic Fertilizer?

A: You can purchase Navyakosh through several channels:
• Online: Visit our store on Amazon at https://amzn.in/d/hBRlaGo
• Retail: Through authorized dealers and agricultural stores
• Bulk Orders: For bulk purchases, please contact us directly at +91 91988 03978

Q9: What kind of results can I expect after using Navyakosh?

A: Farmers using Navyakosh consistently report higher yields, healthier crops, and better soil quality. Scientific studies have shown remarkable results, including a 29% increase in grain yield and a 24.8% improvement in seed weight compared to conventional chemical fertilizers."""

    metadata = {
        "product_name": "Navyakosh",
        "category": "organic_fertilizer",
        "type": "faq",
        "company": "LCB Fertilizers",
        "content_type": "frequently_asked_questions",
        "topics": [
            "product_definition",
            "soil_health_improvement",
            "irrigation_reduction",
            "crop_compatibility",
            "safety",
            "compatibility_with_other_products",
            "application_instructions",
            "purchasing_information",
            "expected_results"
        ],
        "key_features": [
            "100_percent_organic",
            "60_types_microorganisms",
            "super_absorbent_polymer_technology",
            "268_times_water_absorption",
            "33_percent_irrigation_reduction",
            "29_percent_yield_increase",
            "24.8_percent_seed_weight_improvement"
        ],
        "contact_info": {
            "phone": "+91 91988 03978",
            "amazon_store": "https://amzn.in/d/hBRlaGo"
        },
        "compatible_crops": [
            "wheat",
            "rice", 
            "maize",
            "bajra",
            "jowar",
            "cotton",
            "sugarcane",
            "pulses",
            "vegetables",
            "fruits",
            "spices"
        ]
    }

    # Initialize database if needed
    init_db()
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(faq_content, metadata, db_session)
        print(f"✅ Successfully added Navyakosh FAQ to database!")
        print(f"Document ID: {doc_id}")
        return doc_id
    except Exception as e:
        print(f"❌ Error adding document: {e}")
        return None
    finally:
        db_session.close()

if __name__ == "__main__":
    print("Adding Navyakosh FAQ information to database...")
    result = add_navyakosh_faq_to_database()
    
    if result:
        print("\n🎉 Navyakosh FAQ information has been successfully added to the RAG chatbot database!")
        print("The chatbot can now answer specific questions about Navyakosh usage, application, and benefits.")
    else:
        print("\n💥 Failed to add Navyakosh FAQ information. Please check the error messages above.")