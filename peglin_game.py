from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class PeglinArchipelagoOptions:
    pass


class PeglinGame(Game):

    name = "Peglin"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = [
        KeymastersKeepGamePlatforms.SW,
        KeymastersKeepGamePlatforms.IOS,
        KeymastersKeepGamePlatforms.AND,
    ]

    is_adult_only_or_unrated = False

    options_cls = PeglinArchipelagoOptions

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Win a run as CLASS",
                data={
                    "CLASS": (self.peglinClasses, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Win a run on cruciball level CRUCIBALL or higher",
                data={
                    "CRUCIBALL": (self.easyCruciball, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Win a run on cruciball level CRUCIBALL or higher",
                data={
                    "CRUCIBALL": (self.hardCruciball, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Win a run as CLASS on cruciball level CRUCIBALL or higher",
                data={
                    "CLASS": (self.peglinClasses, 1),
                    "CRUCIBALL": (self.easyCruciball, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Win a run as CLASS on cruciball level CRUCIBALL or higher",
                data={
                    "CLASS": (self.peglinClasses, 1),
                    "CRUCIBALL": (self.hardCruciball, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Defeat a rainbow slime on cruciball level CRUCIBALL or higher",
                data={
                    "CRUCIBALL": (self.easyCruciball, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Defeat a rainbow slime on cruciball level CRUCIBALL or higher",
                data={
                    "CRUCIBALL": (self.hardCruciball, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Assemble the Assemball on cruciball level CRUCIBALL or higher",
                data={
                    "CRUCIBALL": (self.easyCruciball, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Defeat an Act ACTNUM boss in one turn",
                data={
                    "ACTNUM": (self.acts, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Inflict POISON spinfection on a single enemy",
                data={
                    "POISON": (self.spinfection, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win a battle with at least BLOCK ballwark remaining",
                data={
                    "BLOCK": (self.ballwark, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Obtain a ITEM",
                data={
                    "ITEM": (self.eventItem, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Obtain a ITEM",
                data={
                    "ITEM": (self.rareOrb, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Win a run with a ITEM",
                data={
                    "ITEM": (self.bossRelic, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win a run with an intact ITEM",
                data={
                    "ITEM": (self.fragileItem, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),

        ]

    @staticmethod
    def peglinClasses() -> List[str]:
        return [
            "Peglin",
            "Balladin",
            "Roundrel",
            "Spinventor",
        ]

    @staticmethod
    def easyCruciball() -> List[str]:
        return [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
        ]

    @staticmethod
    def hardCruciball() -> List[str]:
        return [
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
        ]

    @staticmethod
    def acts() -> List[str]:
        return [
            "1",
            "2",
            "3",
        ]

    @staticmethod
    def spinfection() -> List[str]:
        return [
            "25",
            "30",
            "35",
            "40",
            "45",
        ]

    @staticmethod
    def ballwark() -> List[str]:
        return [
            "75",
            "80",
            "85",
            "90",
            "100",
            "110",
        ]

    @staticmethod
    def eventItem() -> List[str]:
        return [
            "Infernal Ingot",
            "IOU",
            "Perfect Forger",
            "Modest Mallet",
            "Weighted Chip",
            "Egg",
            "Orboros",
            "Mirrorb",
            "Ballectrum",
        ]

    @staticmethod
    def rareOrb() -> List[str]:
        return [
            "Orbelisk",
            "Matryorbshka",
            "Poltorbgeist",
            "Critiball",
            "Bob-Orb",
            "Doctorb",
            "Nosforbatu",
            "Shock Orbsorber",
            "Best Orbfence",
            "Ballanx",
            "Signal Boostorb",
            "Douball Douball",
            "Go For The Icircle",
            "Spinterest Payment",
            "Ballm",
            "Summoning Circle",
            "Replenishorb",
            "Lazorb",
            "Collatorball Damage",
            "Potion Ballt",
            "Countorb Attack",
            "Double-Edged Sworb",
            "Duplicatorb",
            "Instigatorb",
            "Irresponsiball",
            "Lazorb",
            "OffeRing",
            "Opposite Rearction",
        ]

    @staticmethod
    def bossRelic() -> List[str]:
        return [
            "Consuming Chalice",
            "Cursed Mask",
            "Gift That Keeps Giving",
            "Glorious SuffeRing",
            "Haglin's Satchel",
            "Kinetic Meteorite",
            "Electropegnet",
            "Matryoshka Shell",
            "Sapper Sack",
            "Sealed Conviction",
            "Wand of Skulltimate Wrath",
            "Unpretentious Pendant",
            "Constricting Chains",
            "Molten Mantle",
            "Wand of Skulltimate Greed",
            "Defresh Potion",
            "Spheridae's Fate",
            "Leaf The Rest For Later",
            "Heavy Hand",
            "Safety Pegulations",
            "Gopher Gold",
            "Viridian Trinket",
            "Status Symbol",
        ]

    @staticmethod
    def fragileItem() -> List[str]:
        return [
            "Egg",
            "Spheridae's Fate",
            "IOU",
        ]

    # Archipelago Options
    # ...