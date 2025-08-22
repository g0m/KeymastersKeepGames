from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class UFO50ArchipelagoOptions:
    UFO50_include_cherry: UFO50IncludeCherry


class UFO50Game(Game):

    name = "UFO 50"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = [
        KeymastersKeepGamePlatforms.SW,
    ]

    is_adult_only_or_unrated = True

    options_cls = UFO50ArchipelagoOptions

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Get the gift for GAME",
                data={
                    "GAME": (self.games, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=6,
            ),
            GameObjectiveTemplate(
                label="Get GIFTNUM gifts",
                data={
                    "GIFTNUM": (self.giftsobtained, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="WINCON QPGAME",
                data={
                    "WINCON": (self.winconditions, 1),
                    "QPGAME": (self.quickplaygames, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="WINCON GAMENUM games",
                data={
                    "WINCON": (self.winconditions, 1),
                    "GAMENUM": (self.gamescompleted, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Get a top 3 highscore in GAMENUM different high score boards",
                data={
                    "GAMENUM": (self.gamescompleted, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Win the tournament in Bushido Ball using BUSHCHAR",
                data={
                    "BUSHCHAR": (self.bushidoballcharacters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="After entering the terminal code ZATO-1CHI, win the tournament in Bushido Ball using BUSHCHAR",
                data={
                    "BUSHCHAR": (self.bushidoballcharacters, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Win the tournament in Hyper Contender using HYPECHAR",
                data={
                    "HYPECHAR": (self.hypercontendercharacters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="After entering the terminal code PAST-RULE, win the tournament in Hyper Contender using HYPECHAR",
                data={
                    "HYPECHAR": (self.hypercontendercharacters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Beat Fist Hell using FISTCHAR",
                data={
                    "FISTCHAR": (self.fisthellcharacters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="After entering the terminal code GOOD-GIRL, beat Fist Hell using FISTCHAR",
                data={
                    "FISTCHAR": (self.fisthellcharacters, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Get the MOONEGG in Mooncat",
                data={
                    "MOONEGG": (self.mooncateggs, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Get all 20 STARS in Rail Heist",
                data={
                    "STARS": (self.railheiststars, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="WINCON Star Waspir with the SHIP",
                data={
                    "WINCON": (self.winconditions, 1),
                    "SHIP": (self.starwaspirships, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Complete STREAK jobs in a row in Bug Hunter",
                data={
                    "STREAK": (self.streak, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Achieve a streak of STREAK in Party House",
                data={
                    "STREAK": (self.streak, 1),
                },
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Complete Overbold with a final score of at least SCORE",
                data={
                    "SCORE": (self.overboldscore, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Buy every upgrade in Overbold.",
                data={
                    "SCORE": (self.overboldscore, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Beat Scenario SCENARIO of Lords of Diskonia.",
                data={
                    "SCENARIO": (self.diskscenarios, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Beat TRIAL in Avianos.",
                data={
                    "TRIAL": (self.avianscenarios, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
        ]

    @staticmethod
    def games() -> List[str]:
        return [
            "Barbuta",
            "Bug Hunter",
            "Ninpek",
            "Paint Chase",
            "Magic Garden",
            "Mortol",
            "Velgress",
            "Planet Zoldath",
            "Attactics",
            "Devilition",
            "Kick Club",
            "Avianos",
            "Mooncat",
            "Bushido Ball",
            "Block Koala",
            "Camouflage",
            "Campanella",
            "Golfaria",
            "The Big Bell Race",
            "Warptank",
            "Waldorf's Journey",
            "Porgy",
            "Onion Delivery",
            "Caramel Caramel",
            "Party House",
            "Hot Foot",
            "Divers",
            "Rail Heist",
            "Vainger",
            "Rock On! Island",
            "Pingolf",
            "Mortol II",
            "Fist Hell",
            "Overbold",
            "Campanella 2",
            "Hyper Contender",
            "Valbrace",
            "Rakshasa",
            "Star Waspir",
            "Grimstone",
            "Lords of Diskonia",
            "Night Manor",
            "Elfazar's Hat",
            "Pilot Quest",
            "Mini & Max",
            "Combatants",
            "Quibble Race",
            "Seaside Drive",
            "Campanella 3",
            "Cyber Owls",
        ]

    def winconditions(self) -> List[str]:
        if self.include_cherry:
            return [
                "Win",
                "Cherry",
            ]
        else:
            return [
                "Win"
            ]

    @staticmethod
    def quickplaygames() -> List[str]:
        return [
            "Barbuta",
            "Bug Hunter",
            "Ninpek",
            "Paint Chase",
            "Magic Garden",
            "Velgress",
            "Planet Zoldath",
            "Attactics",
            "Devilition",
            "Kick Club",
            "Bushido Ball",
            "Campanella",
            "The Big Bell Race",
            "Waldorf's Journey",
            "Onion Delivery",
            "Caramel Caramel",
            "Hot Foot",
            "Pingolf",
            "Fist Hell",
            "Overbold",
            "Campanella 2",
            "Hyper Contender",
            "Rakshasa",
            "Star Waspir",
            "Elfazar's Hat",
            "Quibble Race",
            "Seaside Drive",
            "Campanella 3",
            "Cyber Owls",
        ]

    @staticmethod
    def gamescompleted() -> List[str]:
        return [
            "2",
            "3",
            "4",
        ]

    @staticmethod
    def giftsobtained() -> List[str]:
        return [
            "2",
            "3",
            "4",
            "5",
            "6",
        ]

    @staticmethod
    def bushidoballcharacters() -> List[str]:
        return [
            "Kotaro",
            "Ayumi",
            "Tomoe",
            "Raizo",
            "Chiyome",
            "Yamada",
        ]

    @staticmethod
    def fisthellcharacters() -> List[str]:
        return [
            "Jay",
            "Cat",
            "Victor",
            "Amy",
        ]

    @staticmethod
    def hypercontendercharacters() -> List[str]:
        return [
            "Elka",
            "Yogo",
            "Brazz",
            "Reck",
            "Sephy",
            "Gilroy",
            "Voltana",
            "Donkus",
        ]

    @staticmethod
    def mooncateggs() -> List[str]:
        return [
            "Green Egg",
            "Yellow Egg",
            "Red Egg",
        ]

    @staticmethod
    def railheiststars() -> List[str]:
        return [
            "Time Stars",
            "Angel Stars",
            "Devil Stars",
        ]

    @staticmethod
    def starwaspirships() -> List[str]:
        return [
            "Gray Ship",
            "Yellow Ship",
            "Red Ship",
        ]

    @staticmethod
    def streak() -> List[str]:
        return [
            "3",
            "4",
            "5",
            "6",
            "7",
        ]

    @staticmethod
    def overboldscore() -> List[str]:
        return [
            "3500",
            "3600",
            "3700",
            "3800",
            "3900",
            "4000",
            "4100",
            "4200",
            "4300",
        ]

    @staticmethod
    def diskscenarios() -> List[str]:
        return [
            "1. NARROW PASS",
            "2. EAST VALLEY",
            "3. THE ISLAND",
            "4. GOLD RUSH",
            "5. WAR SPIDERS",
            "6. PROMOTION",
            "7. TUNED UP",
            "8. MINER ISSUE",
            "9. LAND BRIDGES",
            "10. THE REGICIDE",
        ]

    @staticmethod
    def avianscenarios() -> List[str]:
        return [
            "ADULT",
            "TRIAL 1",
            "TRIAL 2",
            "TRIAL 3",
            "TRIAL 4",
            "TRIAL 5",
        ]

    @property
    def include_cherry(self) -> bool:
        return bool (self.archipelago_options.UFO50_include_cherry.value)

    # Archipelago Options
class UFO50IncludeCherry(Toggle):
    """
    Indicates whether to include the possibility that a goal will require getting the cherry for a given game
    """
    display_name = "UFO 50 Include Cherry"