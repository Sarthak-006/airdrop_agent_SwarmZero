import requests
from typing import Optional, Dict
from hive_agent import HiveAgent
from dotenv import load_dotenv

load_dotenv()

def fetch_airdrop_details() -> Optional[str]:
    """
    Fetches comprehensive details about the most recent blockchain airdrops available for August 2024.
    
    :return: A summary of the top airdrops, or None if an error occurs or no airdrops are found.
    """
    url = "http://localhost:8000/api/v1/chat"
    
    prompt = """
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
    
    data = {
        "user_id": "user123",
        "session_id": "session123",
        "chat_data": {
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    }

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    my_agent = HiveAgent(
       name="airdrop_agent",
       functions=[fetch_airdrop_details],
       config_path="./hive_config.toml",
       instruction="Use appropriate sources to answer the questions about blockchain airdrops.",
    )
    
    my_agent.run()
