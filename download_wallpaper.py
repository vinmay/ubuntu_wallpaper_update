import requests, json, os
from datetime import date

API_URL = "https://api.nasa.gov/planetary/apod?api_key=iFMisDCaGUQG1kswmBB16b0rNLk3VErbWHtHnFAW"
FOLDER_NAME = "/home/xephyr/apod/"
data = requests.get(API_URL)
CHUNK_SIZE = 8192

def download_apod():
    if data.status_code == 200:
        json_data = json.loads(data.text)
        if not os.path.exists(FOLDER_NAME):
            os.makedirs(FOLDER_NAME)
        filename = os.path.join(FOLDER_NAME, str(date.today()) + ".jpg")
        print(filename)
        with requests.get(json_data["hdurl"], stream=True) as r:
            r.raise_for_status()
            total_length = int(r.headers.get("content-length"))
            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=CHUNK_SIZE):
                    f.write(chunk)
            print(f"-----Downloaded {total_length/CHUNK_SIZE} out of {total_length}")
        return filename
