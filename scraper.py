import json

def scrape_shl_catalog():
    print("Starting SHL catalog...")
    assessments = [
        {"name": "Java Programming Test", "url": "https://www.shl.com/en/assessments/java-programming-test/", "test_type": "K", "duration": 30, "remote_testing": "Yes", "adaptive_support": "No", "description": "Measures Java programming", "skills": "Java, OOP"},
        {"name": "OPQ Questionnaire", "url": "https://www.shl.com/en/assessments/opq/", "test_type": "P", "duration": 25, "remote_testing": "Yes", "adaptive_support": "Yes", "description": "Measures personality", "skills": "Leadership, Teamwork"},
        {"name": "Verbal Reasoning", "url": "https://www.shl.com/en/assessments/verbal-reasoning/", "test_type": "A", "duration": 18, "remote_testing": "Yes", "adaptive_support": "Yes", "description": "Verbal analysis", "skills": "Reading, Logic"},
        {"name": "Numerical Reasoning", "url": "https://www.shl.com/en/assessments/numerical-reasoning/", "test_type": "A", "duration": 18, "remote_testing": "Yes", "adaptive_support": "Yes", "description": "Numerical data", "skills": "Math, Analysis"}
    ]
    return assessments

def save_catalog(assessments):
    with open('shl_catalog.json', 'w') as f:
        json.dump(assessments, f, indent=2)
    print(f"Saved {len(assessments)} assessments")

if __name__ == "__main__":
    catalog = scrape_shl_catalog()
    save_catalog(catalog)
    print("Done!")
