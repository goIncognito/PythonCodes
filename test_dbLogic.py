def test_user_exists(db_client):
    result = db_client.execute_query(
        "SELECT * FROM users WHERE username='admin'"
    )
    assert len(result) == 1
