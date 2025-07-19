import random
from typing import List, Dict

from app.services.phonology_generator import PhonologyGenerator
from app.services.phonology_generator import generate_random_phonology


class MorphologyGenerator:
    def __init__(self, phonology: Dict = None):
        self.phonology = phonology or generate_random_phonology()
        self.inventory = self.phonology["inventory"]
        self.syllable_templates = self.phonology["syllable_templates"]
        self.sound_changes = self.phonology.get("sound_change_rules", [])
        self.typology = self._provide_morphology()
        self.affix_inventory = self._generate_affix_inventory()

    def _generate_affix_inventory(self, num: int = 10) -> List[str]:
        return [self._generate_random_syllable() for _ in range(num)]

    def _generate_random_syllable(self) -> str:
        template = random.choice(self.syllable_templates)
        syllable = ""
        for symbol in template:
            if symbol == "C":
                syllable += random.choice(self.inventory["consonants"])["symbol"]
            elif symbol == "V":
                syllable += random.choice(self.inventory["vowels"])["symbol"]
        return syllable

    def generate_root(self) -> str:
        return self._generate_random_syllable()

    def inflect(self, root: str, affix: str = None, apply_changes: bool = True) -> str:
        affix = affix or random.choice(self.affix_inventory)
        word = root + affix
        if apply_changes and self.sound_changes:
            word = PhonologyGenerator.apply_sound_changes(word, self.sound_changes)
        return word

    def generate_morpheme_set(self, count: int = 10) -> List[Dict[str, str]]:
        morphemes = []
        for _ in range(count):
            root = self.generate_root()
            affix = random.choice(self.affix_inventory)
            inflected = self.inflect(root, affix)
            morphemes.append({
                "root": root,
                "affix": affix,
                "inflected": inflected
            })
        return morphemes

    def _provide_morphology(self) -> Dict:
        morphology_weights = {
            "Analytic": 0.15,
            "Isolating": 0.10,
            "Synthetic": 0.20,
            "Agglutinative": 0.20,
            "Fusional": 0.15,
            "Polysynthetic": 0.05,
            "Nonconcatenative": 0.05,
            "Introflexive": 0.05,
            "Incorporating": 0.05
        }

        morphology_explanations = {
            "Analytic": "Uses mostly single-morpheme words. Grammatical relationships are shown by word order and helper words.",
            "Synthetic": "Words are formed by combining multiple morphemes. Grammar is often encoded directly into words.",
            "Agglutinative": "Builds words from chains of clearly separable morphemes, each expressing a single function. Example: Turkish.",
            "Fusional": "Combines morphemes that often express multiple grammatical functions in one fused form. Example: Spanish verb endings.",
            "Polysynthetic": "Extremely morpheme-dense; entire sentences can be expressed in a single word. Example: Inuktitut.",
            "Isolating": "A subtype of analytic morphology; words usually consist of a single morpheme. No affixes or inflections.",
            "Incorporating": "Combines the object noun into the verb to form a single word. Found in some Native American languages.",
            "Nonconcatenative": "Morphological changes happen internally to the root rather than by adding affixes. Example: Arabic root-pattern system.",
            "Introflexive": "A form of nonconcatenative morphology where vowels and consonants are interwoven to express grammar."
        }

        word_order_explanations = {
            "SVO": "Subject comes first, followed by verb, then object. Common in English, Chinese.",
            "SOV": "Subject first, object second, verb last. Found in Japanese, Turkish, Hindi.",
            "VSO": "Verb comes first, followed by subject and object. Seen in Classical Arabic, Welsh.",
            "VOS": "Verb first, then object, then subject. Found in some Austronesian languages.",
            "OVS": "Object first, then verb, then subject. Rare but seen in some Amazonian languages.",
            "OSV": "Object first, followed by subject and verb. Extremely rare and often marked.",
            "Free": "No dominant word order; constituent order changes based on focus, topic, or emphasis."
        }

        grammatical_cases = [
            "Nominative", "Accusative", "Genitive", "Dative", "Ablative", "Locative", "Instrumental",
            "Vocative", "Ergative", "Absolutive", "Allative", "Elative", "Illative", "Perlative",
            "Comitative", "Possessive", "Partitive", "Superessive", "Sublative", "Delative",
            "Terminative", "Essive", "Translative", "Prolative", "Causal", "Temporal",
            "Benefactive", "Malefactive", "Comparative", "Equative"
        ]

        grammatical_cases_explanations = {
            case: explanation for case, explanation in zip(
                grammatical_cases,
                [
                    "Marks the subject of a sentence or clause.",
                    "Marks the direct object of a verb.",
                    "Indicates possession or relationship between nouns.",
                    "Marks the indirect object, typically the recipient or beneficiary.",
                    "Denotes motion away from or origin.",
                    "Indicates location or place where something occurs.",
                    "Marks the means or tool used to perform an action.",
                    "Used to address or call upon someone or something directly.",
                    "Marks the subject of a transitive verb in ergative-absolutive languages.",
                    "Marks the subject of an intransitive verb or object of a transitive verb.",
                    "Denotes motion toward a place or goal.",
                    "Indicates motion out of or from within something.",
                    "Indicates motion into or toward the interior of something.",
                    "Denotes motion through, along, or across something.",
                    "Indicates accompaniment or association, often meaning 'with'.",
                    "Marks ownership or association, often overlaps with genitive.",
                    "Indicates partial quantity or an incomplete object.",
                    "Denotes position on the surface of something.",
                    "Marks movement onto a surface or higher position.",
                    "Indicates motion off or down from a surface.",
                    "Denotes the endpoint or limit of an action or time.",
                    "Marks a temporary state, role, or identity.",
                    "Indicates a change of state, becoming something else.",
                    "Marks movement along a path or by means of something.",
                    "Indicates cause, reason, or motive.",
                    "Denotes time when an event occurs.",
                    "Marks the entity for whose benefit an action is done.",
                    "Marks the entity that suffers harm or loss from an action.",
                    "Used for comparison, often meaning 'like' or 'as'.",
                    "Denotes equality or sameness in comparison."
                ]
            )
        }

        conjugation_patterns = [
            "Subject Agreement", "Tense-Only", "Aspect-Based", "Mood-Based", "Polypersonal Agreement",
            "Voice-Based", "Evidentiality", "Switch-Reference", "Object Agreement", "Person-Based", "Honorific-Based"
        ]

        conjugation_explanations = {
            "Subject Agreement": "Verb changes to reflect the grammatical subject (e.g., person, number). Common in Indo-European languages.",
            "Tense-Only": "Verb inflection focuses on time (past, present, future) without person agreement.",
            "Aspect-Based": "Verb changes to show type or flow of action (completed, ongoing, habitual).",
            "Mood-Based": "Conjugation reflects speaker attitude (indicative, subjunctive, imperative, etc.).",
            "Polypersonal Agreement": "Verb agrees with both subject and object (and sometimes indirect object). Common in Basque.",
            "Voice-Based": "Conjugation reflects grammatical voice (active, passive, causative, etc.).",
            "Evidentiality": "Verb shows source or certainty of information (e.g., seen, heard, inferred). Found in Turkish, Quechua.",
            "Switch-Reference": "Verb indicates whether the subject of the next clause is the same or different. Found in many Papuan languages.",
            "Object Agreement": "Verb changes based on object features (e.g., person, number).",
            "Person-Based": "Inflection varies mainly by grammatical person (1st, 2nd, 3rd).",
            "Honorific-Based": "Verb forms change based on respect or social status of participants. Common in Korean, Japanese."
        }

        morphology_to_syntax = {
            "Analytic": ["SVO", "SOV"],
            "Isolating": ["SVO", "SOV"],
            "Agglutinative": ["SOV", "OSV", "Free"],
            "Fusional": ["SVO", "SOV", "VSO"],
            "Polysynthetic": ["Free", "SOV", "OVS"],
            "Synthetic": ["SOV", "SVO", "VSO"],
            "Nonconcatenative": ["VSO", "SVO"],
            "Introflexive": ["VSO", "SVO"],
            "Incorporating": ["Free", "SOV"]
        }

        alignment_systems = {
            "Analytic": ["Nominative-Accusative"],
            "Isolating": ["Nominative-Accusative"],
            "Agglutinative": ["Nominative-Accusative", "Ergative-Absolutive", "Split-Ergative"],
            "Fusional": ["Nominative-Accusative"],
            "Polysynthetic": ["Ergative-Absolutive", "Direct-Inverse", "Hierarchical"],
            "Synthetic": ["Nominative-Accusative", "Ergative-Absolutive"],
            "Nonconcatenative": ["Nominative-Accusative"],
            "Introflexive": ["Nominative-Accusative"],
            "Incorporating": ["Ergative-Absolutive", "Direct-Inverse"]
        }

        alignment_explanations = {
            "Nominative-Accusative": "Subjects of both transitive and intransitive verbs are treated the same (nominative), and different from direct objects (accusative).",
            "Ergative-Absolutive": "Subjects of intransitive verbs are treated like objects of transitive verbs (absolutive), and different from transitive subjects (ergative).",
            "Split-Ergative": "Mix of ergative and nominative alignment depending on factors like tense or person.",
            "Direct-Inverse": "Verb morphology changes based on the hierarchy of subject and object (e.g., 1st > 2nd > 3rd).",
            "Hierarchical": "Argument marking depends on animacy, definiteness, or person hierarchy rather than grammatical function."
        }

        morph_type = random.choices(list(morphology_weights.keys()), weights=list(morphology_weights.values()), k=1)[0]
        selected_orders = random.sample(morphology_to_syntax.get(morph_type, []), k=random.randint(1, 3))
        selected_cases = random.sample(grammatical_cases, k=random.randint(1, len(grammatical_cases)))
        selected_conjugations = random.sample(conjugation_patterns, k=random.randint(1, 3))
        selected_alignment = random.choice(alignment_systems.get(morph_type, ["Nominative-Accusative"]))

        return {
            "Morphological Type": {
                "Type": morph_type,
                "Explanation": morphology_explanations[morph_type]
            },
            "Word Order": {
                "Orders": selected_orders,
                "Explanations": {o: word_order_explanations[o] for o in selected_orders}
            },
            "Grammatical Cases": {
                "Cases": selected_cases,
                "Explanations": {c: grammatical_cases_explanations[c] for c in selected_cases}
            },
            "Conjugation Patterns": {
                "Patterns": selected_conjugations,
                "Explanations": {p: conjugation_explanations[p] for p in selected_conjugations}
            },
            "Alignment System": {
                "System": selected_alignment,
                "Explanation": alignment_explanations[selected_alignment]
            }
        }

    @property
    def morphology_type(self) -> str:
        return self.typology["Morphological Type"]["Type"]
