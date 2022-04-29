"""
  Implementation of the Meta source class that scrapes data from mtgtop8.com
"""

from gglib.MetaSource import MetaSource
import gglib.Types as ggt
from gglib.Utils import get_page_source
from typing import List


class MtgTop8Source(MetaSource):
  pass
  # TODO(Stephen): design how this should be populated

  def __init__(self):
    self._format_dict = {
        ggt.Format.Modern: "MO",
        ggt.Format.Pioneer: "PI",
        ggt.Format.Legacy: "LE",
        ggt.Format.Standard: "ST"
    }

  def get_format_url(self, form: ggt.Format) -> str:
    return "https://www.mtgtop8.com/format?f=" + self._format_dict[form]

  def get_archetype_breakdown(self, format: ggt.Format) -> List[ggt.Archetype]:
    pgsrc = get_page_source(self.get_format_url(format))

    # TODO(Stephen): parse this
    pass

  def get_decklists(self, archetype: ggt.Archetype, ndecks: int = 1,
                    min_performance: int = -1) -> List[ggt.Decklist]:
    pgsrc = get_page_source(archetype.url)
    # TODO(Stephen): parse  this
