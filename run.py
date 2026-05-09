import subprocess
import sys

def run_scraper():
    print("\nStep 1: Creating catalog...")
    subprocess.run([sys.executable, "scraper.py"])

def run_vector():
    print("\nStep 2: Building vector store...")
    subprocess.run([sys.executable, "vector_store.py"])

def run_api():
    print("\nStep 3: Starting API...")
    subprocess.run([sys.executable, "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"])

if __name__ == "__main__":
    run_scraper()
    run_vector()
    run_api()
