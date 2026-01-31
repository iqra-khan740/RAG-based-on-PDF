import requests
from bs4 import BeautifulSoup
import os

# Create folder to save text (optional)
os.makedirs("scraped_docs", exist_ok=True)

# The single VS Code docs page
url = "https://code.visualstudio.com/docs/getstarted/getting-started"

# Add headers to avoid 403 or blocked request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/144.0.0.0 Safari/537.36"
}

# Fetch page
response = requests.get(url, headers=headers)
if response.status_code != 200:
    raise Exception(f"Failed to fetch {url}, status code {response.status_code}")

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract main content (VS Code docs uses <main>)
main_content = soup.find("main")
if not main_content:
    raise Exception("Could not find the main content on the page.")

# Get clean text
text = main_content.get_text(separator="\n", strip=True)

# Save as a text file (UTF-8)
filename = "scraped_docs/getting_started.txt"
with open(filename, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Scraping done! Saved to {filename}")
