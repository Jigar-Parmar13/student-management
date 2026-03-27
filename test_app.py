import pytest
from app import app, students

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    res = client.get("/")
    assert res.status_code == 200

def test_health_check(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert b"ok" in res.data

def test_add_student(client):
    res = client.post("/add", data={
        "name": "Test Student",
        "age": 21,
        "course": "DevOps",
        "grade": "A"
    }, follow_redirects=True)
    assert res.status_code == 200
    assert b"Test Student" in res.data

def test_delete_student(client):
    res = client.get("/delete/1", follow_redirects=True)
    assert res.status_code == 200
