from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_block():
    response = client.get("/block")

    assert response.status_code == 200

    data = response.json()
    assert "latest_block" in data
    assert isinstance(data["latest_block"], int)
    assert data["latest_block"] > 0


def test_invalid_wallet():
    response = client.get("/wallet/not-a-real-wallet")

    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid Ethereum address"}