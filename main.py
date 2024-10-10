import requests
import json
from bs4 import BeautifulSoup


def fetch_user(username):
    response = requests.get(f"https://www.tiktok.com/@{username}")                        # Get content from target's tiktok page
    soup = BeautifulSoup(response.content, "html.parser")                                 # Parse html content (make it readable for the beginners)
    script_tag = soup.find("script", id="__UNIVERSAL_DATA_FOR_REHYDRATION__")             # Find data script tag
    json_str = script_tag.string                                                          # Get the json string table of data from the script tag
    data = json.loads(json_str)                                                           # Use json to turn it from a string to a table
    target = data["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"].get("user")      # Isolate the user data
    return target                                                                         # Return it to end the function


data = fetch_user("theonly5a3k")
