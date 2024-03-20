import requests
r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36')

# Check if the request was successful
if r.status_code == 200:
    print("The request has succeeded")
    # Check if the response is not empty
    if r.text.strip():
        r_json = r.json()
        print(r_json)
    else:
        print("The response is empty.")
else:
    print(f"Request failed with status code {r.status_code}. Response: {r.text}")