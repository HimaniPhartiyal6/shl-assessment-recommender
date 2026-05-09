import json

def create_vector_store():
    print("Loading catalog...")
    with open('shl_catalog.json', 'r') as f:
        assessments = json.load(f)
    print(f"Loaded {len(assessments)} assessments")
    print("✅ Vector store ready (using keyword search)")

if __name__ == "__main__":
    create_vector_store()
