import requests
import os
import sqlalchemy as db
import pandas as pd
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

release_data = response.json()

df = pd.DataFrame(release_data)

engine = db.create_engine('sqlite:///discogs_releases.db')

df.to_sql('releases', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
    query_result = connection.execute(db.text("SELECT * FROM releases;")).fetchall()
    print(pd.DataFrame(query_result))
