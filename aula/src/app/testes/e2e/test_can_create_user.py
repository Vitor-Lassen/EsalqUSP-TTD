from fastapi.testclient import TestClient
from uuid import UUID
from infra.api.main import app

client = TestClient(app)

#testar se é possivel criar um usuario atraves da api 

def test_can_create_user():
    response = client.post("/users", json={"name": "Willian"})

    data = response.json()

    assert response.status_code == 201
    assert isinstance(UUID(data['id']), UUID)
    assert data['name'] == "Willian"
