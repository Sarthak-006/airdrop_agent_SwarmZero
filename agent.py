
import requests

# Define the base URL for the AI agent's API
url = "http://localhost:8000/api/v1/chat"

# Define the prompt for the AI agent
prompt = """
"content": (
    "I need comprehensive details about the most recent blockchain airdrops available for August 2024. "
    "Please identify the top airdrops currently active or upcoming within this month. For each airdrop, "
    "provide the following information: the project name, the blockchain network it is associated with, "
    "the exact URL where users can claim the airdrop, and any necessary steps or requirements for claiming "
    "the airdrop. If the airdrop is restricted to certain users or regions, include that information as well. "
    "Additionally, mention any deadlines or important dates related to the airdrop, such as when the claim period "
    "ends or when tokens will be distributed. Ensure that the details are accurate and up-to-date to avoid "
    "any issues for users attempting to claim these airdrops. Lastly, if there are any potential risks or "
    "scams associated with these airdrops, briefly mention them and provide guidance on how to proceed safely."
)
"""

# Define the payload with user information and the prompt
data = {
    "user_id": "user123",
    "session_id": "session123",
    "chat_data": {
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
}

# Send the request to the AI agent API
response = requests.post(url, json=data)

# Print the JSON response from the API
print(response.json())
