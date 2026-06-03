from fastapi.testclient import TestClient
from main import app, connection

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "Hello, Taybah!" in response.text

def test_database_connection():
    print(connection)
    assert connection is not None
    
    
def test_for_coin():
    response = client.get('/coins')
    assert response.status_code == 200
    coins = response.json()
    
    assert type(coins) == list
    assert len(coins) > 0

def test_assemble_coin():
    response = client.get('/coins')
    coins = response.json()
    assert [1, 'Automate'] in coins
    
def test_for_biscuit():
    response = client.post("/coins")
    assert response.status_code == 201
    coins = response.json()
    print(coins)

    assert [14, "Biscuit"] in coins