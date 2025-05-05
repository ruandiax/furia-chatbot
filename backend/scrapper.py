import os
from scrappers.draft5 import Draft5Scrapper

DRAFT5_FURIA_ID = os.getenv("DRAFT5_FURIA_ID")
DRAFT5_FURIA_NAME = os.getenv("DRAFT5_FURIA_NAME")
SCRAPPER_FILE_OUTPUT_PATH = os.getenv("SCRAPPER_FILE_OUTPUT_PATH")

draft5 = Draft5Scrapper(team_id=DRAFT5_FURIA_ID, team_name=DRAFT5_FURIA_NAME)
team_data = draft5.run()

# Store
with open(f"{SCRAPPER_FILE_OUTPUT_PATH}/{DRAFT5_FURIA_NAME}.json", "w+") as f:
    f.write(team_data.model_dump_json())
