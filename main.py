import mmh3
import requests
import codecs

# Read the list of URLs from url.txt file
with open('url.txt', 'r') as file:
    urls = file.readlines()

# Iterate through the URLs and calculate the hash for each favicon
for url in urls:
    url = url.strip()  # Remove leading/trailing whitespace
    response = requests.get(url)
    if response.status_code == 200:
        favicon = codecs.encode(response.content, "base64")
        hash = mmh3.hash(favicon)
        print(f'URL: {url}, Favicon Hash: {hash}')

