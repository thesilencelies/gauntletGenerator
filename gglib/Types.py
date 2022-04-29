"""
  Simple structs and enums used throughout the project
"""
from dataclasses import dataclass
from enum import Enum
from typing import List

# Enums


class Format(Enum):
  """
    Enum noting which mtg format we are considering
  """
  Standard = 0
  Modern = 1
  Pioneer = 2
  Legacy = 3


class ArchetypeCategory(Enum):
  """
    Enum denoting what category a deck is assigned.
    Not all MetaSources will use all these categories
  """
  Aggro = 0
  Midrange = 1
  Control = 2
  Combo = 3

# structs


@dataclass
class Card:
  """
    data object denoting a card
    we use this rather than just a string because different output formats
    want different specifiers about set etc
  """
  name: str
  edition: str
  quantity: int


@dataclass
class Decklist:
  """
    data object denoting a decklist
    the performance score indicates how well it performed, probably as a function
    of record and the challenge at the tournament.
    Exact meaning will depend on the meta source
  """
  mainboard: List[Card]
  sideboard: List[Card]
  name: str
  performance: int


@dataclass
class Archetype:
  """
    placeholder for an archetype
  """
  name: str
  category: ArchetypeCategory
  meta_share: float
  share_change: float
  # used internally by sources
  url: str
