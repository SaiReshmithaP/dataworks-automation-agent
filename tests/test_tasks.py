import requests

BASE_URL = "http://localhost:8000"

def test_run_task():
    response = requests.post(f"{BASE_URL}/run", params={"task": "Count the number of Wednesdays in /data/dates.txt"})
    assert response.status_code == 200

def test_read_file():
    response = requests.get(f"{BASE_URL}/read", params={"path": "/data/dates-wednesdays.txt"})
    assert response.status_code == 200
