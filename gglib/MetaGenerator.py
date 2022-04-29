#! python
"""
  class that handles selecting which decks to choose
"""

from typing import List
from gglib.MetaSource import MetaSource
import gglib.Types as ggt
import enum


class GeneratorAlgorithm(enum.Enum):
  TopPlayRate = 0
  AggroComboControl = 1
  UpAndComing = 2
  Established = 3
  HighPerformig = 4
  All = -1


class MetaGenerator:
  """
    Class that handles selecting the decks
    Several different algorithms for deck selection are available
  """

  def __init__(self) -> None:
    self.__select_decks_selector = {
        GeneratorAlgorithm.TopPlayRate: self._select_decks_TopPlay,
        GeneratorAlgorithm.AggroComboControl: self._select_decks_ACC,
        GeneratorAlgorithm.UpAndComing: self._select_decks_UpAndComing,
        GeneratorAlgorithm.Established: self._select_decks_Established,
        GeneratorAlgorithm.HighPerformig: self._select_decks_HighPerform,
        GeneratorAlgorithm.All: self._select_decks_All,
    }

  def select_decks(self,
                   source: MetaSource,
                   format: ggt.Format,
                   total_decks: int = -1,  # -1 means as many as you like
                   algorithm: GeneratorAlgorithm = GeneratorAlgorithm.TopPlayRate
                   ) -> List[ggt.Decklist]:
    archs = source.get_archetype_breakdown(format)
    return self.__select_decks_selector[algorithm](archs, total_decks, source)

  def _select_decks_TopPlay(self, archs: List[ggt.Archetype],
                            source: MetaSource) -> List[ggt.Decklist]:
    # TODO(Rich): implement this one first
    pass

  def _select_decks_ACC(self, archs: List[ggt.Archetype], total_decks: int,
                        source: MetaSource) -> List[ggt.Decklist]:
    pass

  def _select_decks_UpAndComing(self, archs: List[ggt.Archetype], total_decks: int,
                                source: MetaSource) -> List[ggt.Decklist]:
    pass

  def _select_decks_Established(self, archs: List[ggt.Archetype], total_decks: int,
                                source: MetaSource) -> List[ggt.Decklist]:
    pass

  def _select_decks_HighPerform(self, archs: List[ggt.Archetype], total_decks: int,
                                source: MetaSource) -> List[ggt.Decklist]:
    pass

  # mostly for testing
  def _select_decks_All(self, archs: List[ggt.Archetype], total_decks: int,
                        source: MetaSource) -> List[ggt.Decklist]:
    n_decks_per_arch = total_decks // len(archs)
    if n_decks_per_arch < 1:
      n_decks_per_arch = 1
    # nested list comprehensions look weird, but this just runs get_decklists
    # for each archetype then puts all of the result into the return string
    return [deck for arch in archs for deck in source.get_decklists(arch, ndecks=n_decks_per_arch)]
