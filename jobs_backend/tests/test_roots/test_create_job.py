def test_create_job(client):
    data = {"owner_id": 0, "title": "string", "company_name": "string", "company_url": "string", "location": "string",
            "description": "string", "date_posted": "2022-12-22"}
    response = client.post('/jobs/create', json=data)
    assert response.status_code == 200, f'Тест не прошел'
    assert response.json()['email'] == data['email']
    assert response.json()['username'] == data['username']
    assert response.json()['is_active']
