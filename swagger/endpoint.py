import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = 'http://ca5d5a5d-f714-4875-806e-1baacba2d9b1.westus.azurecontainer.io/score'
# If the service is authenticated, set the key or token
key = 'BBG58RuUDCyYamm7sNGzq3ZnPO6hoqvc'

# Two sets of data to score, so we get two results back
data = {
  "data": [1.1,2.2,2.5,1.2],
  "method": "predict_proba"
}
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())


