from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class WorldOfHorrorArchipelagoOptions:
    pass


class WorldOfHorrorGame(Game):

    name = "WORLD OF HORROR"
    platform = KeymastersKeepGamePlatforms.PC
    platforms_other = [
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.SW,
    ]

    is_adult_only_or_unrated = False

    options_cls = WorldOfHorrorArchipelagoOptions

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="As CHARACTER with the BACKSTORY backstory, stop the summoning of OLDGOD",
                data={
                    "CHARACTER": (self.characters, 1),
                    "BACKSTORY": (self.backstories, 1),
                    "OLDGOD": (self.gods, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),

            GameObjectiveTemplate(
                label="Complete the challenge CHALLENGE",
                data={
                    "CHALLENGE": (self.challenges, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),

            GameObjectiveTemplate(
                label="Solve the Mystery MYSTERY",
                data={
                    "MYSTERY": (self.mysteries, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),

            GameObjectiveTemplate(
                label="Have at least FOLLOWER followers following you at once",
                data={
                    "FOLLOWER": (self.followers, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),

            GameObjectiveTemplate(
                label="Pay the Monument with COST",
                data={
                    "COST": (self.monumentCost, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),

            GameObjectiveTemplate(
                label="Know at least SPELL spells at the same time",
                data={
                    "SPELL": (self.spells, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),

            GameObjectiveTemplate(
                label="Win a run after only starting to climb the lighthouse when your doom reaches DOOM",
                data={
                    "DOOM": (self.doom, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),

            GameObjectiveTemplate(
                label="Get ENDING Ending As in the same run",
                data={
                    "ENDING": (self.endings, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),

            GameObjectiveTemplate(
                label="Banish GHOST ghost enemies with a ritual",
                data={
                    "GHOST": (self.ghosts, 1),
                },
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),

            GameObjectiveTemplate(
                label="Obtain a SHOPITEM",
                data={
                    "SHOPITEM": (self.shopItems, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),

        ]

    @staticmethod
    def characters() -> List[str]:
        return [
            "Kirie Minami",
            "Aiko Takahashi",
            "Haru",
            "Mizuki Hamasaki",
            "Kouji Tagawa",
            "Mimi",
            "Miku",
            "Moriko Ishii",
            "Yashiro Kawaj",
            "Ayaka Kuroi",
            "Toshiaki Wakamatsu",
            "Juri Okusawa",
            "Yumiko Ichimura",
        ]

    @staticmethod
    def backstories() -> List[str]:
        return [
            "World of Horror",
            "Medical History",
            "Hunted by the Cult",
            "The Seventh Curse",
            "Ill-Fated",
            "Knight-Errant",
            "Scars",
            "Curious Birthmark",
            "Fatalist",
            "Exquisite Taste",
            "Eldritch Parasite",
        ]

    @staticmethod
    def gods() -> List[str]:
        return [
            "Herald of the Shattered Court",
            "Ygothaeg, the Irresistible Gaze",
            "Cthac-Atorasu, the Spider God",
            "Ithotu, the Devouring Fire",
            "Ath-Yolazsth, the Towering Eye",
            "Goizo, the Thing Forsaken by God",
            "Zhectast, the Horror from the Stars",
            "Ktu-Rufu, the Dreaming",
            "Eh-Zhal, the Inconceivable Sadness",
        ]

    @staticmethod
    def mysteries() -> List[str]:
        return [
            "Alarming Account of Abnormal Arms",
            "Bizarre Bruit of the Blood-curdling Botanist",
            "Bloody Brief of a Beckoning Bulletin",
            "Chilling Chronicle of a Crimson Cape",
            "Curious Case of a Contagious Coma",
            "Eerie Episode of Evolving Eels",
            "Far-out Fable of a Fear Festival",
            "Freakish Fable of a Frightening Flood",
            "Freaky Feature of Found Footage",
            "Horrible History of Household Hell",
            "Macabre Memoir of Morbid Mermaids",
            "Mysterious Myth of Medusa Metamorphosis",
            "Nightmare News of the Noisy Nails",
            "Perilous Parable of the Peculiar Painting",
            "Restless Rumors of a Residential Recluse",
            "Rotten Report of a Rancid Ramen",
            "Sorrowful Saga of the Moonlight Sailors",
            "Spine-Chilling Story of School Scissors",
            "Tragic Tale of the Thaumaturgy Teacher",
            "Vicious Verses of A Violent Vigil",
            "Worrying Write-Up Of A Wordless Ward",
        ]

    @staticmethod
    def followers() -> List[str]:
        return range(2, 4)

    @staticmethod
    def spells() -> List[str]:
        return range(3, 6)

    @staticmethod
    def doom() -> List[str]:
        return range(75, 90, 5)

    @staticmethod
    def endings() -> List[str]:
        return range(2, 4)

    @staticmethod
    def ghosts() -> List[str]:
        return range(2, 4)

    @staticmethod
    def monumentCost() -> List[str]:
        return [
            "Reason",
            "Stamina",
            "Funds",
        ]

    @staticmethod
    def shopItems() -> List[str]:
        return [
            "Backpack",
            "Camera",
            "Cigarettes",
            "Compass",
            "Dog Treats",
            "Energy Drink",
            "Flashlight",
            "Foreign Cigarettes",
            "Map",
            "Salt",
            "Sewing Kit",
            "Steak Knife",
            "Cursed Cartridge",
            "Cursed Doll",
            "Funny Mask",
            "Glass Eye",
            "Gruesome Token",
            "Holy Candle",
            "Lump of Flesh",
            "Mummified Heart",
            "Ritual Mask",
            "Ritual Dagger",
            "Ritual Robes",
            "Small Candle",
            "Tainted Violin",
            "Can of Acid",
            "Carpenter Hammer",
            "Crowbar",
            "Flare Gun",
            "Fuel",
            "Heavy Duty Flashlight",
            "Monkey Wrench",
            "Pocket Knife",
            "Shovel",
        ]

    @staticmethod
    def challenges() -> List[str]:
        return [
            "Parole Violation",
            "Going Cold Turkey",
            "But Dad!!!",
            "Ghastly Presence",
            "Ghost Town",
            "Wrong Book!",
            "Mimi's Little Project",
        ]

    # Archipelago Options
    # ...