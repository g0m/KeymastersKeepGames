from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class KindWordsArchipelagoOptions:
    pass


class KindWordsGame(Game):

    name = "Kind Words 2"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = [
    ]

    is_adult_only_or_unrated = False

    options_cls = KindWordsArchipelagoOptions

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Respond to a request for help at LOCATION",
                data={
                    "LOCATION": (self.helpLocations, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="POEM at the Cafe",
                data={
                    "POEM": (self.poemTypes, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Reply to CHAIN chains in the Chain Forest",
                data={
                    "CHAIN": (self.chainNums, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),

        ]

    @staticmethod
    def helpLocations() -> List[str]:
        return [
            "Home",
            "Vintage Stuff",
        ]

    @staticmethod
    def poemTypes() -> List[str]:
        return [
            "Share a poem",
            "Reply to a poetry challenge",
        ]

    @staticmethod
    def chainNums() -> List[str]:
        return [
            "2",
            "3",
            "4",
        ]

    # Archipelago Options
    # ...