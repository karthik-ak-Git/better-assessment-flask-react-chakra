from tests.factories import CommentFactory


def test_create_comment(client):
    res = client.post(
        "/api/comments", json={"task_id": 1, "content": "pytest test"})
    assert res.status_code == 201


def test_get_comments(client):
    CommentFactory.create_batch(3, task_id=5)
    res = client.get("/api/comments/5?page=1&limit=2")
    assert res.status_code == 200
    assert len(res.get_json()) == 2


def test_update_comment(client):
    comment = CommentFactory(task_id=7, content="Old")
    client.put(f"/api/comments/{comment.id}", json={"content": "New content"})
    updated = client.get(f"/api/comments/{comment.task_id}")
    assert "New content" in str(updated.get_json())


def test_delete_comment(client):
    comment = CommentFactory()
    res = client.delete(f"/api/comments/{comment.id}")
    assert res.status_code == 200
