

import random
from app.constants.IPA import get_all_consonants, get_all_vowels, get_full_ipa_inventory


def phonology_generator(user_vowels = None, user_consonants = None):
    inventory_ipa_consonants = get_all_consonants()
    inventory_ipa_vowels = get_all_vowels()

    sampling_value_vowels = random.randint(4, 8)
    sampling_value_consonant = random.randint(7, 15)

    vowel_subset = user_vowels if user_vowels else random.sample(inventory_ipa_vowels, sampling_value_vowels)
    consonant_subset = user_consonants if user_consonants else random.sample(inventory_ipa_consonants, sampling_value_consonant)

    return (vowel_subset, consonant_subset)



