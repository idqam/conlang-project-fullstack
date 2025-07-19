from fastapi import FastAPI

from app.constants.IPA import DEFAULT_CONSONANT_MAP
from app.services import grammar_generator_engine, phonology_generator

app = FastAPI()

@app.get("/")
def root():

    vowels = phonology_generator.phonology_generator()
    grammar_spec = grammar_generator_engine.provide_morphology()
    cc = list(DEFAULT_CONSONANT_MAP.keys())
    return {"msg": grammar_spec}
