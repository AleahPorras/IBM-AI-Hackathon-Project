import requests
import streamlit as st

ENDPOINT_TEMPLATE = f"{st.secrets.WX0_INSTANCE_URL}/v1/orchestrate/{st.secrets.AGENT_ID}/chat/completions"


@st.cache_data(ttl=3000, show_spinner=False) # Caches the token for 50 minutes
def get_saas_token():
    """Authenticates with IBM SaaS IAM and retrieves a bearer token."""
    token_url = "https://iam.platform.saas.ibm.com/siusermgr/api/1.0/apikeys/token"
    
    try:
        response = requests.post(
            token_url,
            headers={"Content-Type": "application/json", "Accept": "application/json"},
            json={"apikey": st.secrets.WX0_API_KEY}
        )
        if response.status_code in (200, 201):
            data = response.json()
            return data.get("token") or data.get("access_token")
        else:
            print(f"Auth Error: {response.text}")
            return None
    except Exception as e:
        print(f"Auth Exception: {str(e)}")
        return None


def ask_agent(agent_id, message):
    """Sends a prompt to the specified Orchestrate Agent and returns the text response."""
    jwt_token = get_saas_token()
    
    if not jwt_token:
        return "System Error: The application could not authenticate with IBM Watsonx."
        
    api_endpoint = ENDPOINT_TEMPLATE.format(agent_id=agent_id)

    try:
        response = requests.post(
            api_endpoint,
            headers={
                "Authorization": f"Bearer {jwt_token}",
                "Content-Type": "application/json"
            },
            json={
                "messages": [{"role": "user", "content": message}],
                "stream": False
            }
        )
        
        data = response.json()
        
        # Safely extract the response, avoiding KeyError if 'choices' is missing
        if response.status_code == 200 and "choices" in data:
            return data["choices"][0]["message"]["content"]
        else:
            print("API Error Payload:", data)  # Logs to your VS Code terminal
            error_msg = data.get("message") or data.get("error", "Unknown API error occurred.")
            return f"Agent Error: {error_msg}"
            
    except Exception as e:
        print("Request Exception:", str(e))
        return f"System Error: Could not connect to the agent. Details: {str(e)}"