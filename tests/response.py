""" Response seeker
"""
import requests

payload = {
  "Unnamed: 0": 234,
  "checkin_acc": "A14",
  "duration": 4,
  "credit_history": "A34",
  "amount": 1544,
  "savings_acc": "A61",
  "present_emp_since": "A74",
  "inst_rate": 2,
  "personal_status": "A93",
  "residing_since": 1,
  "age": 42,
  "inst_plans": "A143",
  "num_credits": 3,
  "job": "A172",
  
}

url = "http://localhost:6000/predict"
response = requests.post(url, json=payload)
result = response.json()
print(result)