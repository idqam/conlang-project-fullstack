from typing import Optional, List
from pydantic import BaseModel

class GeneratedLanguage(BaseModel):
    name: str
    morphology: Optional[str] = None
    word_order: Optional[str] = None
    number_cases: Optional[int] = None
    grammatical_cases: Optional[List[str]] = None
    verb_conjugation: Optional[str] = None
    tense_aspect_mood: Optional[str] = None
