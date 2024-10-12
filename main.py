import requests
import json
from bs4 import BeautifulSoup


def fetch_user(username):
    response = requests.get(f"https://www.tiktok.com/@{username}")                        # Get content from target's tiktok page
    soup = BeautifulSoup(response.content, "html.parser")                                 # Parse html content (make it readable by code)
    script_tag = soup.find("script", id="__UNIVERSAL_DATA_FOR_REHYDRATION__")             # Find script tag with data
    json_str = script_tag.string                                                          # Get the string of content in the script tag
    data = json.loads(json_str)                                                           # Use json to turn it from a string to a dictionary
    target = data["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"].get("user")      # Isolate the user data
    return target                                                                         # Return it to end the function


data = fetch_user("theonly5a3k")
print(data)
