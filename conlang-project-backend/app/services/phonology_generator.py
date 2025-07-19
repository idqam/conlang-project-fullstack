import random
import re
from typing import List, Dict, Optional, Tuple

from app.constants.IPA import (
    DEFAULT_CONSONANT_MAP,
    DEFAULT_VOWEL_MAP,
    DIACRITICS,
    SUPRASEGMENTAL_OPTIONS,
    SOUND_CHANGE_TEMPLATES,
    ALLOPHONY_RULES
)


def apply_diacritic(symbol: str, diacritic_name: str) -> str:
    diacritic = DIACRITICS.get(diacritic_name, "")
    return f"{symbol}{diacritic}"


class PhonologyGenerator:
    def __init__(
        self,
        user_vowels: Optional[List[str]] = None,
        user_consonants: Optional[List[str]] = None,
        vowel_count_range: Tuple[int, int] = (5, 8),
        consonant_count_range: Tuple[int, int] = (12, 20),
        allowed_complexities: List[str] = ["basic", "advanced"],
        allowed_groups: Optional[List[str]] = None,
        apply_diacritics: Optional[List[str]] = None,
        syllable_template_count: int = 5,
        include_allophony: bool = False,
        include_sound_change: bool = False
    ):
        self.user_vowels = user_vowels
        self.user_consonants = user_consonants
        self.vowel_count_range = vowel_count_range
        self.consonant_count_range = consonant_count_range
        self.allowed_complexities = allowed_complexities
        self.allowed_groups = allowed_groups
        self.apply_diacritics = apply_diacritics
        self.syllable_template_count = syllable_template_count
        self.include_allophony = include_allophony
        self.include_sound_change = include_sound_change

        self.vowels, self.consonants = self._generate_phoneme_inventory()
        self.vowels = self._apply_diacritics(self.vowels)
        self.consonants = self._apply_diacritics(self.consonants)

        self.syllable_templates = self._generate_syllable_templates()
        self.phonotactics = self._generate_phonotactic_rules()
        self.suprasegmentals = self._generate_suprasegmentals()
        self.allophony_rules = self._generate_allophony_rules()
        self.sound_change_rules = self._generate_sound_change_rules()

    def _generate_phoneme_inventory(self) -> Tuple[List[Dict], List[Dict]]:
        full_vowels = [
            v for v in DEFAULT_VOWEL_MAP.values()
            if v["complexity"] in self.allowed_complexities
        ]
        full_consonants = [
            c for c in DEFAULT_CONSONANT_MAP.values()
            if c["complexity"] in self.allowed_complexities
            and (self.allowed_groups is None or c["manner"] in self.allowed_groups)
        ]

        vowels = (
            [DEFAULT_VOWEL_MAP[v] for v in self.user_vowels if v in DEFAULT_VOWEL_MAP]
            if self.user_vowels else random.sample(full_vowels, random.randint(*self.vowel_count_range))
        )
        consonants = (
            [DEFAULT_CONSONANT_MAP[c] for c in self.user_consonants if c in DEFAULT_CONSONANT_MAP]
            if self.user_consonants else random.sample(full_consonants, random.randint(*self.consonant_count_range))
        )

        return vowels, consonants

    def _apply_diacritics(self, phonemes: List[Dict]) -> List[Dict]:
        if not self.apply_diacritics:
            return phonemes

        modified = []
        for phoneme in phonemes:
            modified_phoneme = phoneme.copy()
            if random.random() < 0.3:
                chosen = random.choice(self.apply_diacritics)
                modified_phoneme["symbol"] = apply_diacritic(phoneme["symbol"], chosen)
                modified_phoneme["diacritic"] = chosen
            modified.append(modified_phoneme)

        return modified

    def _generate_syllable_templates(self) -> List[str]:
        templates = []
        onsets = ["C"] + [f"{'C'*i}" for i in range(2, 3)]
        nuclei = ["V", "VV"]
        codas = ["", "C", "CC"]

        possible_structures = []
        for onset in onsets:
            for nucleus in nuclei:
                for coda in codas:
                    structure = f"{onset}{nucleus}{coda}"
                    possible_structures.append(structure)

        max_allowed = min(len(possible_structures), self.syllable_template_count)
        return random.sample(possible_structures, max_allowed)

    def _generate_phonotactic_rules(self) -> Dict:
        return {
            "max_onset_length": max(template.count("C") for template in self.syllable_templates),
            "max_coda_length": max(len(template) - template.find("V") - 1 for template in self.syllable_templates),
            "legal_onsets": [template.split("V")[0] for template in self.syllable_templates],
            "legal_codas": [template.split("V")[-1] for template in self.syllable_templates if len(template.split("V")) > 1]
        }

    def _generate_suprasegmentals(self) -> Dict:
        return {
            "stress": random.choice(SUPRASEGMENTAL_OPTIONS["stress"]),
            "tone": random.choice(SUPRASEGMENTAL_OPTIONS["tone"]),
            "intonation": random.choice(SUPRASEGMENTAL_OPTIONS["intonation"])
        }

    def _generate_allophony_rules(self) -> List[str]:
        if not self.include_allophony:
            return []
        return random.sample(ALLOPHONY_RULES, k=random.randint(1, 3))

    def _generate_sound_change_rules(self) -> List[str]:
        if not self.include_sound_change:
            return []
        return random.sample(SOUND_CHANGE_TEMPLATES, k=random.randint(1, 4))
    @staticmethod
    
    def apply_sound_changes(word: str, rules: List[str]) -> str:
        transformed = word
        for rule in rules:
            match = re.match(r"(\S+)\s*>\s*(\S+)(?:\s*/\s*(.+))?", rule)
            if not match:
                continue

            source, target, environment = match.groups()

            if not environment:
                
                transformed = transformed.replace(source, target)
            else:
                
                if environment.startswith("_"):
                    context = environment[1:]
                    pattern = rf"{re.escape(source)}(?={context})"
                elif environment.endswith("_"):
                    context = environment[:-1]
                    pattern = rf"(?<={context}){re.escape(source)}"
                elif "_" in environment:
                    left, right = environment.split("_")
                    pattern = rf"(?<={left}){re.escape(source)}(?={right})"
                else:
                    pattern = re.escape(source)

                transformed = re.sub(pattern, target, transformed)

        return transformed
    


    def export(self) -> Dict:
        return {
        "inventory": {
            "vowels": self.vowels,
            "consonants": self.consonants
        },
        "syllable_templates": self.syllable_templates,
        "phonotactics": self.phonotactics,
        "suprasegmentals": self.suprasegmentals,
        "allophony_rules": self.allophony_rules,
        "sound_change_rules": self.sound_change_rules,
        "apply_sound_changes": self.apply_sound_changes  
    }
def generate_random_phonology(
    include_allophony=True,
    include_sound_change=True,
    apply_diacritics=None
) -> dict:
        generator = PhonologyGenerator(
        include_allophony=include_allophony,
        include_sound_change=include_sound_change,
        apply_diacritics=apply_diacritics or []
    )
        return generator.export()
