

from fastapi.testclient import TestClient
from TestAndDebug import app

client = TestClient(app)
def test_read_item():
    response = client.get("/items/foo",headers={"x-token":"coneofsilence"})
    assert response.status_code==200
    assert response.json()=={
        "id":"foo",
        "title":"Foo",
        "description":"There Goes My Hero",
    }

def test_read_item_bad_token():
    response = client.get("/items/foo", headers={"x-token": "wrong"})
    assert response.status_code == 400
    assert response.json() == {"detail":"Invalid X-Token Header"}

def test_read_inexistent_item():
    response = client.get("/items/baz", headers={"x-token": "coneofsilence"})
    assert response.status_code == 404
    assert response.json() == {"detail":"item not found"}

def test_create_item():
    response = client.post(
        "/items/",
        json={
            "id": "foobar",
            "title": "Foo Bar",
            "description": "The Foo Bartender",
        },
        headers={"x-token":"coneofsilence"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Bartender",
    }

def test_create_item_bad_token():
    response = client.post(
        "/items/",
        headers={"x-token":"badheader"},
        json={"id":"bazz","title":"Bazz","description":"Drop the bazz"})
    assert response.status_code == 400
    assert response.json()=={"detail":"Invalid X-Token Header"}

def test_create_existing_item():
    response = client.post(
        "/items/",
        headers={"x-token":"coneofsilence"},
        json={"id":"foo","title":"Bazz","description":"Drop the bazz"}
    )
    assert response.status_code==400
    assert response.json()=={"detail":"item already exists"}



