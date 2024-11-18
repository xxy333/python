import pytest
from APIs import app  # Import your Flask app

@pytest.fixture
def client():
    # Set up a test client
    with app.test_client() as client:
        yield client  # This will be the test client

def test_send_data(client):
    # Test the /send_new_data endpoint
    response = client.post('/send_new_data', json={'key': 'value'})
    assert response.status_code == 201
    assert response.json['message'] == 'Data successfully sent!'
    assert 'id' in response.json  # Check if 'id' is returned

def test_return_data(client):
    # Test the /data_callback endpoint
    response = client.get('/data_callback')
    assert response.status_code == 200
    assert response.data.decode() == 'Ha, provolal jsi mě!'  # Check the response content
