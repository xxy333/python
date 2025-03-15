import requests

BASE_URL = "http://localhost:8080"  # Adjust if your API runs on a different port

def test_homepage():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200

def test_api_endpoint():
    response = requests.get(f"{BASE_URL}/your-endpoint")
    assert response.status_code == 200
    assert response.json() == {"key": "expected_value"}  # Adjust based on your API response
