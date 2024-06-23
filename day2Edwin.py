import requests
import os

# Discogs API credentials
USER_AGENT = 'SEO Example/1.0'
PERSONAL_ACCESS_TOKEN = 'tjwAAygVBowKmGgLaNDqVocpYvyQHHKmEJDtYeSI'

BASE_URL = 'https://api.discogs.com'

headers = {
    'User-Agent': USER_AGENT,
    'Authorization': f'Discogs token={PERSONAL_ACCESS_TOKEN}'
}

release_id = input('Enter release ID: ')
response = requests.get(f'{BASE_URL}/releases/{release_id}', headers=headers)

print(response.json())