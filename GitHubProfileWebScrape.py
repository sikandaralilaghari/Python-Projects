import requests
from bs4 import BeautifulSoup as bs

# GitHub profile URL
github_profile = "https://github.com/razaquegoraya007"
req = requests.get(github_profile)

# Parse the HTML content
scraper = bs(req.content, "html.parser")

# Try to find the image with the class "avatar-user"
profile_picture_element = scraper.find("img", {"class": "avatar-user"})
if profile_picture_element:
    profile_picture = profile_picture_element['src']
    print("Profile picture URL:", profile_picture)
else:
    print("Profile picture not found. The structure of the page may have changed.")
