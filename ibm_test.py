import requests


WXO_INSTANCE_URL = "https://api.dl.watson-orchestrate.ibm.com/instances/20260316-1517-3709-6082-3788811342d3"
WXO_API_KEY = "azE6dXNyXzAyZGY2YWJlLWRlZWEtMzI3YS05ZDM5LTNlMGNhMGY3OTRmZTo1d2w2YTlnWTB2TytNZlY4YWNPVHhkUElBQUJmOWRtNVFZcHVmdkw5b3hFPTpXNXh5"
AGENT_ID = "531cae83-c236-40bd-b428-7d548f656e73"  # Your Medication Manager ID


# ==========================================================
# STEP 1: Exchange API Key for a SaaS JWT Token
# ==========================================================
print("Step 1: Requesting SaaS JWT Token...")
token_url = "https://iam.platform.saas.ibm.com/siusermgr/api/1.0/apikeys/token"


token_response = requests.post(
    token_url,
    headers={"Content-Type": "application/json", "Accept": "application/json"},
    json={"apikey": WXO_API_KEY}
)


if token_response.status_code in (200, 201):
    jwt_token = token_response.json().get("token") or token_response.json().get("access_token")
    print("Success! SaaS JWT token retrieved.\n")
else:
    print(f"Auth Failed. Status: {token_response.status_code}")
    exit()


# ==========================================================
# STEP 2: Endpoint Enumeration
# ==========================================================
print("Step 2: Hunting for the correct SaaS endpoint...")


# Testing the 4 standard routing patterns for IBM SaaS environments
possible_endpoints = [
    f"{WXO_INSTANCE_URL}/v1/orchestrate/{AGENT_ID}/chat/completions",
    f"{WXO_INSTANCE_URL}/v1/agents/{AGENT_ID}/chat/completions",
    f"{WXO_INSTANCE_URL}/api/v1/orchestrate/{AGENT_ID}/chat/completions",
    f"{WXO_INSTANCE_URL}/api/v1/agents/{AGENT_ID}/chat/completions"
]


for endpoint in possible_endpoints:
    print(f"\nTrying: {endpoint}")
    response = requests.post(
        endpoint,
        headers={
            "Authorization": f"Bearer {jwt_token}",
            "Content-Type": "application/json"
        },
        json={
            "messages": [{"role": "user", "content": "Hello"}],
            "stream": False
        }
    )
   
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        print("✅ SUCCESS! We found the correct route.")
        print("Response payload:")
        print(response.json())
        break
    else:
        print(f"Error details: {response.text}")
       



