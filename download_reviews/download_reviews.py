# Code based on https://github.com/zhenzuo2/IS_590_Final/tree/master/Gather_Data

from tqdm import tqdm
import requests
import json
import time

# IDs for Dota 2, PUBG, CS:GO, Warframe, Rainbow Six: Siege
app_id_list = [570, 578080, 730, 230410, 359550]

# Gets reviews for an app given the page we want to get it for. Documentation: https://partner.steamgames.com/doc/store/getreviews
def get_reviews(app_id: int, page: int, max_attempts: int = 10) -> dict:
    attempts = 0
    # Each page is 20 reviews, so we offset by 20 each time
    offset = page * 20
    while attempts < max_attempts:
        response = requests.get("http://store.steampowered.com/appreviews/"+str(app_id)+ "?json=1&filter=recent&start_offset=" + str(offset))
        if response.status_code == 200:
            return response.json()["reviews"]
        # If rate limited, wait and try again
        time.sleep((2 ** attempts) + random.random())
        attempts = attempts + 1
    print(f"Unable to retrieve reviews for app_id = {app_id}")
    return []

# Download reviews for every game in list
for app_id in app_id_list:
    app_reviews = []
    page = 0
    # Loop until we no longer get a result
    with tqdm(desc=f"Downloading reviews for {app_id} ") as bar:
        while True:
            current_reviews = get_reviews(app_id, page)
            if current_reviews == []:
                break
            app_reviews.extend(current_reviews)
            page += 1
            bar.update(1)
    # Dump results 
    with open(f'../../reviews/{app_id}.json', 'w') as fout:
        json.dump()
        