from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class MonsterTrain2ArchipelagoOptions:
    pass


class MonsterTrain2Game(Game):

    name = "Monster Train 2"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = [
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = False

    options_cls = MonsterTrain2ArchipelagoOptions

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Defeat Seraph with your clans being: CLANS",
                data={
                    "CLANS": (self.clans, 2),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Defeat Seraph with CHAMP as your primary champion",
                data={
                    "CHAMP": (self.champions, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Defeat The Titans with your clans being: CLANS",
                data={
                    "CLANS": (self.clans, 2),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Defeat The Titans with CHAMP as your primary champion",
                data={
                    "CHAMP": (self.champions, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Complete the Dimensional Challenge: CHALLENGE",
                data={
                    "CHALLENGE": (self.challenges, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Add a CARD to your deck",
                data={
                    "CARD": (self.colourlessUnits, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Add a EQCARD to your deck",
                data={
                    "EQCARD": (self.equipment, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Add a RCARD to your deck",
                data={
                    "RCARD": (self.rooms, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Win a run with UPGRADE applied to a card",
                data={
                    "UPGRADE": (self.cardUpgrades, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Win a run with a Covenant Rank of RANK or higher",
                data={
                    "RANK": (self.easyRanks, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Win a run with a Covenant Rank of RANK or higher",
                data={
                    "RANK": (self.hardRanks, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a run with PYREHEART as your Pyre Heart",
                data={
                    "PYREHEART": (self.pyreHearts, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Win a run with any MUTNUM mutator(s)",
                data={
                    "MUTNUM": (self.mutatorNums, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Beat any CHALLENGENUM Dimensional Challenges",
                data={
                    "CHALLENGENUM": (self.challengeNums, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a run with STEWARDNUM stewards in your deck",
                data={
                    "STEWARDNUM": (self.stewardNums, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Complete TRIAL trials",
                data={
                    "TRIAL": (self.trialNums, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Complete TRIAL trials in a single run",
                data={
                    "TRIAL": (self.trialNums, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=4,
            ),
        ]

    @staticmethod
    def clans() -> List[str]:
        return [
            "Banished",
            "Pyreborne",
            "Luna Coven",
            "Underlegion",
            "Lazarus League",
            "Hellhorned",
            "Awoken",
            "Stygian Guard",
            "Umbra",
            "Melting Remnant",
        ]

    @staticmethod
    def champions() -> List[str]:
        return [
            "Fel",
            "Talos",
            "Lord Phoenix",
            "Lady Gilda",
            "Ekka",
            "Ardhun",
            "Bolete the Guillotine",
            "Madame Lionsmane",
            "Orechi",
            "Baron Grael",
            "Hornbreaker Prince",
            "Shardtail Queen",
            "The Sentient",
            "Wyldenten",
            "Tethys Titansbane",
            "Solgard the Martyr",
            "Penumbra",
            "Primordium",
            "Rector Flicker",
            "Little Fade",
        ]

    @staticmethod
    def colourlessUnits() -> List[str]:
        return [
            "Dante the Dependable",
            "Bone Dog",
            "Jack in the Box",
            "Follower",
        ]

    @staticmethod
    def cardUpgrades() -> List[str]:
        return [
            "Entropic Stone",
            "Entropic Growth",
            "Entropic Energy",
            "Dominating Power",
            "Dominating Authority",
            "Dominating Control",
            "Worthy Sacrifice",
            "Many Lives",
            "Fecundity",
            "Savage Skin",
            "Savage Heart",
            "Savage Spirit",
            "Wrath",
            "Benevolence",
            "Courage",
            "Frailty Absolution",
            "Ascetic Absolution",
            "Red Crown",
        ]

    @staticmethod
    def equipment() -> List[str]:
        return [
            "Bloodthirsty Blade",
            "Glass Cannon",
            "Meat Shield",
            "Stoic Platemail",
            "Swiftsteel Dagger",
            "Equalizing Rings",
            "Heph's Hammer",
            "Overgrowth Carapace",
            "Void Armament",
        ]

    @staticmethod
    def rooms() -> List[str]:
        return [
            "Steward's Quarters",
            "Boiler Room",
            "Enchanted Chamber",
            "Fight Club",
            "Hall of Mirrors",
            "Inferno Room",
            "Spell Sanctum",
            "Zone of Silence",
        ]

    @staticmethod
    def challenges() -> List[str]:
        return [
            "Weapons Make The Warrior",
            "Twofer",
            "I'm the Enemy Now!",
            "Stop Hitting Yourself",
            "Slow and Sloppy",
            "Calculation Station",
            "Revenge of the Collectors",
            "Time Bombs",
            "Bigger isn't Better",
            "Trigger Happy",
            "Organized Chaos",
            "Essential Magic",
            "Bigworm",
            "Vampiric Curse",
            "Herzal's Heroes",
            "Extra Roomy",
            "Anchored",
            "Entropic Agony",
            "Cheat and Repeat",
            "Body Blocking",
        ]

    @staticmethod
    def easyRanks() -> List[str]:
        return [
            "1",
            "2",
            "3",
            "4",
            "5",
        ]

    @staticmethod
    def hardRanks() -> List[str]:
        return [
            "6",
            "7",
            "8",
            "9",
            "10",
        ]

    @staticmethod
    def pyreHearts() -> List[str]:
        return [
            "Proto Heartcage",
            "Heart of the Pact",
            "Lifemother's Pyre",
            "Malicka's Shifting Pyre",
            "Wyngh's Spirit",
            "Fhyra's Greed",
            "Aquath's Reservation",
            "Bogwurm's Growth",
            "Echo of the Time Father",
            "Herzal's Horde",
            "Pyre of Savagery",
            "Pyre of Dominion",
            "Pyre of Entropy",
        ]

    @staticmethod
    def mutatorNums() -> List[str]:
        return [
            "1",
            "2",
            "3",
        ]

    @staticmethod
    def challengeNums() -> List[str]:
        return [
            "2",
            "3",
            "4",
        ]

    @staticmethod
    def stewardNums() -> List[str]:
        return [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
        ]

    @staticmethod
    def trialNums() -> List[str]:
        return [
            "1",
            "2",
            "3",
            "4",
        ]

    # Archipelago Options
    # ...