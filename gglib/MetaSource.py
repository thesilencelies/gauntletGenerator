#! python
"""
  Abstract class for unifyng tht interaction with different APIs
"""
# allows us to use abstract base classes, which is what this is
import abc
from typing import List
import gglib.Types as ggt


class MetaSource(abc.ABC):
  """
    Abstract class that represents the interface for a decklist soure
    (typically  a website, e.g. mtgTop8 or an API)
    defines functionality to do with gathering data from that site
  """
  @abc.abstractmethod
  def get_archetype_breakdown(self, format: ggt.Format) -> List[ggt.Archetype]:
    """
      returns all the archetypes from the metagame according to the meta source
    """
    return [ggt.Archetype()]

  @abc.abstractmethod
  def get_decklists(self, archetype: ggt.Archetype, ndecks: int = 1,
                    min_performance: int = -1) -> List[ggt.Decklist]:
    return [ggt.Decklist()]


class TestSource(MetaSource):
  """
    a simple test source that allows us to test the rest of the code without
    having to use an actual source
  """

  def get_archetype_breakdown(self, format: ggt.Format) -> List[ggt.Archetype]:
    rval = []
    for i in range(6):
      rval.append(ggt.Archetype(
          f"aggro{i}", ggt.ArchetypeCategory.Aggro, i*0.02, 0.03-i*0.01))
    for i in range(5):
      rval.append(ggt.Archetype(
          f"midrange{i}", ggt.ArchetypeCategory.Midrange, i*0.03, 0.03-i*0.01))
    for i in range(7):
      rval.append(ggt.Archetype(
          f"control{i}", ggt.ArchetypeCategory.Control, i*0.01, 0.03-i*0.01))
    for i in range(2):
      rval.append(ggt.Archetype(
          f"combo{i}", ggt.ArchetypeCategory.Combo, i*0.05, 0.03-i*0.01))

    return rval

  def get_decklists(self, archetype: ggt.Archetype, ndecks: int = 1,
                    min_performance: int = -1) -> List[ggt.Decklist]:
    mainboard = [ggt.Card("Island", edition="KHD", quantity=30)]
    mainboard += [ggt.Card("Persistent Petitioners",
                           edition="RNA", quantity=30)]
    sideboard = [ggt.Card("Pithing Needle", edition="RTR", quantity=4)]
    sideboard += [ggt.Card("Colossal Dreadmaw ", edition="C21", quantity=11)]
    return [ggt.Decklist(mainboard, sideboard, f"{archetype.name}_{i}", min_performance+1)
            for i in range(ndecks)]
