def test_health_endpoint_returns_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_then_fetch_task(client):
    created = client.post("/tasks", json={"title": "Submit Week 10"})
    assert created.status_code == 201
    task_id = created.json()["id"]
    fetched = client.get(f"/tasks/{task_id}")
    assert fetched.status_code == 200
    assert fetched.json()["title"] == "Submit Week 10"

def test_blank_title_is_rejected(client):
    assert client.post("/tasks", json={"title": "   "}).status_code == 422

def test_unknown_task_returns_404(client):
    assert client.get("/tasks/9999").status_code == 404

def test_complete_endpoint_updates_task(client):
    created = client.post("/tasks", json={"title": "Check CI"})
    task_id = created.json()["id"]
    response = client.patch(f"/tasks/{task_id}/complete")
    assert response.status_code == 200
    assert response.json()["completed"] is True
