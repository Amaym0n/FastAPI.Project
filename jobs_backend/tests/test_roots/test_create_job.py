import json


def test_create_job(client):
    data = {
        "owner_id": 5,
        "title": "test_vacancy",
        "company_name": "test_company",
        "company_url": "test_company.com",
        "location": "USA, NY",
        "description": "test description"
    }
    response = client.post('/jobs/create', json=data)
    assert response.status_code == 200, f'Тест не прошел'
