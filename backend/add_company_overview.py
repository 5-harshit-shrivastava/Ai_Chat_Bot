#!/usr/bin/env python3
"""Script to add comprehensive company overview to the database."""

from db import get_db, init_db
from ingest import add_document

def main():
    # Initialize database if needed
    init_db()
    
    # Company Overview content
    overview_content = """Company Overview
Name: LCB Fertilizers

Business: A leader in organic fertilizers focused on sustainable and eco-friendly solutions for agriculture.

Founded: 2020

Mission: To revolutionize agriculture by providing solutions that enhance crop yield, promote soil health, and contribute to a greener planet through innovative technologies.

Core Belief: "Healthy soil is the foundation of a sustainable future."

Contact Information
Phone: +91 91988-03978
Email: contact@lcbfertilizers.com

Leadership
CEO: Akshay Srivastav
CEO's Vision: "I think agriculture is the ultimate solution for the growing world. That's why I believe in making organic fertilizers. It will eventually help us big time for sustainable economy."

Key Statistics & Highlights
Manufacturing Plants: 05 units across the country.
Reach: Serves farmers in 12+ states.
Partnerships: Collaborates with over 20 growth partners.
Team Size: 50+ skilled team members.
Customer Base: 35,000+ satisfied customers.

Products Mentioned
For Farms (General)
Soil Activator
Flower Booster
Cacti and Succulents

Areas of Impact
Growing Farming: Supports farmers with resources to increase crop yields.
Accelerating Startups: Encourages startup culture in Uttar Pradesh and India.
Helping Education: Collaborates with researchers and students to expand agricultural fields.

Certifications & Recognitions
Govt. of India (DPIIT): Recognized as a Startup.
Govt. of Uttar Pradesh: Registered and recognized as a Startup.
AGROWTH: Winner of the AGROWTH AGtech Startup Pitchfest 2020.
IWIL: Winner of the "Disrupting the Entrepreneurial DNA: StartUp Marathon" in 2021.

Growth Partners
Bill & Melinda Gates Foundation
Pradan Foundation
Bhungroo | Narita Services
Ernst & Young
Paani Foundation
Bhoomi Farms

Other Initiatives
Navyakosh: A specific initiative or section mentioned on their website."""
    
    # Metadata for the company overview
    overview_metadata = {
        "type": "company_overview",
        "title": "LCB Fertilizers Company Overview",
        "category": "company_info",
        "tags": ["LCB Fertilizers", "company", "overview", "contact", "leadership", "CEO", "Akshay Srivastav", "statistics", "products", "certifications", "partners", "agriculture", "organic fertilizers"]
    }
    
    # Add to database
    db_session = next(get_db())
    try:
        doc_id = add_document(overview_content, overview_metadata, db_session)
        print(f"Successfully added 'Company Overview' to database with ID: {doc_id}")
    except Exception as e:
        print(f"Error adding document: {e}")
    finally:
        db_session.close()

if __name__ == "__main__":
    main()