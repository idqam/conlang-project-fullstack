from fastapi import FastAPI

from app.services import morphology_generator, phonology_generator


app = FastAPI()

@app.get("/")
def root():

    phonology = phonology_generator.PhonologyGenerator(
        include_allophony=True,
        include_sound_change=True,
        apply_diacritics=["nasalized", "aspirated"]
    )

    morphology = morphology_generator.MorphologyGenerator(phonology=phonology.export())
    morphemes = morphology.generate_morpheme_set(5)

    return {
        "phonology": phonology.export(),
        "morphology": morphemes,
        "morphological_type": morphology.morphology_type
    }
