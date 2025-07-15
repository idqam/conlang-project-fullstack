from fastapi import FastAPI

from app.constants.IPA import DEFAULT_CONSONANT_MAP
from app.services import phonology_generator

app = FastAPI()

@app.get("/")
def root():

    vowels = phonology_generator.phonology_generator()
    cc = list(DEFAULT_CONSONANT_MAP.keys())
    return {"msg": cc}
