
from typing import List

from typing import List

IPA_CONSONANTS_FLAGGED_FULL = [
    {"symbol": 'p', "group": 'plosives', "voicing": 'voiceless', "complexity": 'basic'},
    {"symbol": 't', "group": 'plosives', "voicing": 'voiceless', "complexity": 'basic'},
    {"symbol": 'ʈ', "group": 'plosives', "voicing": 'voiceless', "complexity": 'basic'},
    {"symbol": 'c', "group": 'plosives', "voicing": 'voiceless', "complexity": 'basic'},
    {"symbol": 'k', "group": 'plosives', "voicing": 'voiceless', "complexity": 'basic'},
    {"symbol": 'q', "group": 'plosives', "voicing": 'voiceless', "complexity": 'basic'},
    {"symbol": 'ʔ', "group": 'plosives', "voicing": 'voiceless', "complexity": 'basic'},
    {"symbol": 'b', "group": 'plosives', "voicing": 'voiced', "complexity": 'basic'},
    {"symbol": 'd', "group": 'plosives', "voicing": 'voiced', "complexity": 'basic'},
    {"symbol": 'ɖ', "group": 'plosives', "voicing": 'voiced', "complexity": 'basic'},
    {"symbol": 'ɟ', "group": 'plosives', "voicing": 'voiced', "complexity": 'basic'},
    {"symbol": 'g', "group": 'plosives', "voicing": 'voiced', "complexity": 'basic'},
    {"symbol": 'ɢ', "group": 'plosives', "voicing": 'voiced', "complexity": 'basic'},
    {"symbol": 'm', "group": 'nasals', "voicing": 'voiced', "complexity": 'basic'},
    {"symbol": 'ɱ', "group": 'nasals', "voicing": 'voiced', "complexity": 'advanced'},
    {"symbol": 'n', "group": 'nasals', "voicing": 'voiced', "complexity": 'basic'},
    {"symbol": 'ɳ', "group": 'nasals', "voicing": 'voiced', "complexity": 'advanced'},
    {"symbol": 'ɲ', "group": 'nasals', "voicing": 'voiced', "complexity": 'advanced'},
    {"symbol": 'ŋ', "group": 'nasals', "voicing": 'voiced', "complexity": 'basic'},
    {"symbol": 'ɴ', "group": 'nasals', "voicing": 'voiced', "complexity": 'advanced'},
    {"symbol": 'ʙ', "group": 'trills', "voicing": 'voiced', "complexity": 'experimental'},
    {"symbol": 'r', "group": 'trills', "voicing": 'voiced', "complexity": 'basic'},
    {"symbol": 'ʀ', "group": 'trills', "voicing": 'voiced', "complexity": 'experimental'},
    {"symbol": 'ⱱ', "group": 'taps_flaps', "voicing": 'voiced', "complexity": 'experimental'},
    {"symbol": 'ɾ', "group": 'taps_flaps', "voicing": 'voiced', "complexity": 'advanced'},
    {"symbol": 'ɽ', "group": 'taps_flaps', "voicing": 'voiced', "complexity": 'experimental'},
    {"symbol": 'ɸ', "group": 'fricatives', "voicing": 'voiceless', "complexity": 'advanced'},
    {"symbol": 'f', "group": 'fricatives', "voicing": 'voiceless', "complexity": 'basic'},
    {"symbol": 'θ', "group": 'fricatives', "voicing": 'voiceless', "complexity": 'basic'},
    {"symbol": 's', "group": 'fricatives', "voicing": 'voiceless', "complexity": 'basic'},
    {"symbol": 'ʃ', "group": 'fricatives', "voicing": 'voiceless', "complexity": 'basic'},
    {"symbol": 'ʂ', "group": 'fricatives', "voicing": 'voiceless', "complexity": 'advanced'},
    {"symbol": 'ç', "group": 'fricatives', "voicing": 'voiceless', "complexity": 'advanced'},
    {"symbol": 'x', "group": 'fricatives', "voicing": 'voiceless', "complexity": 'basic'},
    {"symbol": 'χ', "group": 'fricatives', "voicing": 'voiceless', "complexity": 'advanced'},
    {"symbol": 'ħ', "group": 'fricatives', "voicing": 'voiceless', "complexity": 'experimental'},
    {"symbol": 'h', "group": 'fricatives', "voicing": 'voiceless', "complexity": 'basic'},
    {"symbol": 'β', "group": 'fricatives', "voicing": 'voiced', "complexity": 'advanced'},
    {"symbol": 'v', "group": 'fricatives', "voicing": 'voiced', "complexity": 'basic'},
    {"symbol": 'ð', "group": 'fricatives', "voicing": 'voiced', "complexity": 'basic'},
    {"symbol": 'z', "group": 'fricatives', "voicing": 'voiced', "complexity": 'basic'},
    {"symbol": 'ʒ', "group": 'fricatives', "voicing": 'voiced', "complexity": 'basic'},
    {"symbol": 'ʐ', "group": 'fricatives', "voicing": 'voiced', "complexity": 'advanced'},
    {"symbol": 'ʝ', "group": 'fricatives', "voicing": 'voiced', "complexity": 'advanced'},
    {"symbol": 'ɣ', "group": 'fricatives', "voicing": 'voiced', "complexity": 'advanced'},
    {"symbol": 'ʁ', "group": 'fricatives', "voicing": 'voiced', "complexity": 'advanced'},
    {"symbol": 'ʕ', "group": 'fricatives', "voicing": 'voiced', "complexity": 'experimental'},
    {"symbol": 'ɦ', "group": 'fricatives', "voicing": 'voiced', "complexity": 'experimental'},
    {"symbol": 'ɬ', "group": 'lateral_fricatives', "voicing": 'voiceless', "complexity": 'advanced'},
    {"symbol": 'ɮ', "group": 'lateral_fricatives', "voicing": 'voiced', "complexity": 'advanced'},
    {"symbol": 'ʋ', "group": 'approximants', "voicing": 'voiced', "complexity": 'advanced'},
    {"symbol": 'ɹ', "group": 'approximants', "voicing": 'voiced', "complexity": 'basic'},
    {"symbol": 'ɻ', "group": 'approximants', "voicing": 'voiced', "complexity": 'advanced'},
    {"symbol": 'j', "group": 'approximants', "voicing": 'voiced', "complexity": 'basic'},
    {"symbol": 'ɰ', "group": 'approximants', "voicing": 'voiced', "complexity": 'advanced'},
    {"symbol": 'l', "group": 'lateral_approximants', "voicing": 'voiced', "complexity": 'basic'},
    {"symbol": 'ɭ', "group": 'lateral_approximants', "voicing": 'voiced', "complexity": 'advanced'},
    {"symbol": 'ʎ', "group": 'lateral_approximants', "voicing": 'voiced', "complexity": 'advanced'},
    {"symbol": 'ʟ', "group": 'lateral_approximants', "voicing": 'voiced', "complexity": 'advanced'},
    {"symbol": 't͡s', "group": 'affricates', "voicing": 'voiceless', "complexity": 'advanced'},
    {"symbol": 't͡ʃ', "group": 'affricates', "voicing": 'voiceless', "complexity": 'basic'},
    {"symbol": 'ʈ͡ʂ', "group": 'affricates', "voicing": 'voiceless', "complexity": 'advanced'},
    {"symbol": 'c͡ç', "group": 'affricates', "voicing": 'voiceless', "complexity": 'experimental'},
    {"symbol": 'k͡x', "group": 'affricates', "voicing": 'voiceless', "complexity": 'experimental'},
    {"symbol": 'q͡χ', "group": 'affricates', "voicing": 'voiceless', "complexity": 'experimental'},
    {"symbol": 'd͡z', "group": 'affricates', "voicing": 'voiced', "complexity": 'advanced'},
    {"symbol": 'd͡ʒ', "group": 'affricates', "voicing": 'voiced', "complexity": 'basic'},
    {"symbol": 'ɖ͡ʐ', "group": 'affricates', "voicing": 'voiced', "complexity": 'experimental'},
    {"symbol": 'ɟ͡ʝ', "group": 'affricates', "voicing": 'voiced', "complexity": 'experimental'},
    {"symbol": 'g͡ɣ', "group": 'affricates', "voicing": 'voiced', "complexity": 'experimental'},
    {"symbol": 'ɢ͡ʁ', "group": 'affricates', "voicing": 'voiced', "complexity": 'experimental'},
    {"symbol": 'pʼ', "group": 'ejectives', "voicing": 'voiceless', "complexity": 'experimental'},
    {"symbol": 'tʼ', "group": 'ejectives', "voicing": 'voiceless', "complexity": 'experimental'},
    {"symbol": 'kʼ', "group": 'ejectives', "voicing": 'voiceless', "complexity": 'experimental'},
    {"symbol": 'sʼ', "group": 'ejectives', "voicing": 'voiceless', "complexity": 'experimental'},
    {"symbol": 't͡ʃʼ', "group": 'ejectives', "voicing": 'voiceless', "complexity": 'experimental'},
    {"symbol": 'ɓ', "group": 'implosives', "voicing": 'voiced', "complexity": 'experimental'},
    {"symbol": 'ɗ', "group": 'implosives', "voicing": 'voiced', "complexity": 'experimental'},
    {"symbol": 'ʄ', "group": 'implosives', "voicing": 'voiced', "complexity": 'experimental'},
    {"symbol": 'ɠ', "group": 'implosives', "voicing": 'voiced', "complexity": 'experimental'},
    {"symbol": 'ʛ', "group": 'implosives', "voicing": 'voiced', "complexity": 'experimental'},
    {"symbol": 'ʘ', "group": 'clicks', "voicing": 'voiceless', "complexity": 'experimental'},
    {"symbol": 'ǀ', "group": 'clicks', "voicing": 'voiceless', "complexity": 'experimental'},
    {"symbol": 'ǃ', "group": 'clicks', "voicing": 'voiceless', "complexity": 'experimental'},
    {"symbol": 'ǂ', "group": 'clicks', "voicing": 'voiceless', "complexity": 'experimental'},
    {"symbol": 'ǁ', "group": 'clicks', "voicing": 'voiceless', "complexity": 'experimental'}
]



IPA_VOWELS_FLAGGED_FULL = [
    {"symbol": "i", "height": "close", "backness": "front", "roundedness": "unrounded", "complexity": "basic"},
    {"symbol": "y", "height": "close", "backness": "front", "roundedness": "rounded", "complexity": "basic"},
    {"symbol": "ɨ", "height": "close", "backness": "central", "roundedness": "unrounded", "complexity": "basic"},
    {"symbol": "ʉ", "height": "close", "backness": "central", "roundedness": "rounded", "complexity": "basic"},
    {"symbol": "ɯ", "height": "close", "backness": "back", "roundedness": "unrounded", "complexity": "basic"},
    {"symbol": "u", "height": "close", "backness": "back", "roundedness": "rounded", "complexity": "basic"},
    {"symbol": "ɪ", "height": "near-close", "backness": "front", "roundedness": "unrounded", "complexity": "basic"},
    {"symbol": "ʏ", "height": "near-close", "backness": "front", "roundedness": "rounded", "complexity": "basic"},
    {"symbol": "ʊ", "height": "near-close", "backness": "back", "roundedness": "rounded", "complexity": "basic"},
    {"symbol": "e", "height": "close-mid", "backness": "front", "roundedness": "unrounded", "complexity": "basic"},
    {"symbol": "ø", "height": "close-mid", "backness": "front", "roundedness": "rounded", "complexity": "basic"},
    {"symbol": "ɘ", "height": "close-mid", "backness": "central", "roundedness": "unrounded", "complexity": "basic"},
    {"symbol": "ɵ", "height": "close-mid", "backness": "central", "roundedness": "rounded", "complexity": "basic"},
    {"symbol": "ɤ", "height": "close-mid", "backness": "back", "roundedness": "unrounded", "complexity": "basic"},
    {"symbol": "o", "height": "close-mid", "backness": "back", "roundedness": "rounded", "complexity": "basic"},
    {"symbol": "ə", "height": "mid", "backness": "central", "roundedness": "unrounded", "complexity": "basic"},
    {"symbol": "ɛ", "height": "open-mid", "backness": "front", "roundedness": "unrounded", "complexity": "basic"},
    {"symbol": "œ", "height": "open-mid", "backness": "front", "roundedness": "rounded", "complexity": "basic"},
    {"symbol": "ɜ", "height": "open-mid", "backness": "central", "roundedness": "unrounded", "complexity": "basic"},
    {"symbol": "ɞ", "height": "open-mid", "backness": "central", "roundedness": "rounded", "complexity": "basic"},
    {"symbol": "ʌ", "height": "open-mid", "backness": "back", "roundedness": "unrounded", "complexity": "basic"},
    {"symbol": "ɔ", "height": "open-mid", "backness": "back", "roundedness": "rounded", "complexity": "basic"},
    {"symbol": "æ", "height": "near-open", "backness": "front", "roundedness": "unrounded", "complexity": "basic"},
    {"symbol": "ɐ", "height": "near-open", "backness": "central", "roundedness": "unrounded", "complexity": "basic"},
    {"symbol": "a", "height": "open", "backness": "front", "roundedness": "unrounded", "complexity": "basic"},
    {"symbol": "ɶ", "height": "open", "backness": "front", "roundedness": "rounded", "complexity": "basic"},
    {"symbol": "ä", "height": "open", "backness": "central", "roundedness": "unrounded", "complexity": "basic"},
    {"symbol": "ɑ", "height": "open", "backness": "back", "roundedness": "unrounded", "complexity": "basic"},
    {"symbol": "ɒ", "height": "open", "backness": "back", "roundedness": "rounded", "complexity": "basic"}
]

DEFAULT_CONSONANT_MAP = {
    item["symbol"]: {
        "symbol": item["symbol"],
        "type": "consonant",
        "manner": item["group"],
        "voicing": item["voicing"],
        "complexity": item["complexity"]
    } for item in IPA_CONSONANTS_FLAGGED_FULL
}

DEFAULT_VOWEL_MAP = {
    item["symbol"]: {
        "symbol": item["symbol"],
        "type": "vowel",
        "height": item["height"],
        "backness": item["backness"],
        "roundedness": item["roundedness"],
        "complexity": item["complexity"]
    } for item in IPA_VOWELS_FLAGGED_FULL
}



DIACRITICS = {
    "aspirated": "ʰ",
    "nasalized": "̃",
    "voiceless": "̥",
    "voiced": "̬",
    "long": "ː",
    "short": "ˑ",
    "creaky": "̰",
    "breathy": "̤",
    "high_tone": "˥",
    "low_tone": "˩"
}


def apply_diacritic(phoneme: str, diacritic_type: str) -> str:
    mark = DIACRITICS.get(diacritic_type)
    if not mark:
        raise ValueError(f"Unsupported diacritic: {diacritic_type}")

    suffix_diacritics = {"ʰ", "ː", "ˑ", "˥", "˩"}
    return f"{phoneme}{mark}" if mark in suffix_diacritics else f"{phoneme}{mark}"


def get_all_consonants() -> List[str]:
    return [entry["symbol"] for entry in IPA_CONSONANTS_FLAGGED_FULL]


def get_all_vowels() -> List[str]:
    return [entry["symbol"] for entry in IPA_VOWELS_FLAGGED_FULL]


def get_full_ipa_inventory() -> List[str]:
    return get_all_consonants() + get_all_vowels()