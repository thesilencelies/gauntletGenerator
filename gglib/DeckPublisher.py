"""
  Classes that define the way we can use the decklist data
"""

import abc
import gglib.Types as ggt
import os


class DeckPublisher(abc.ABC):
  """
    Abstract class that defines the interface for the deck publishing interactions
  """
  @abc.abstractmethod
  def publish(self, deck: ggt.Decklist) -> None:
    """
      publishes the deck
    """
    pass


class TxtPublisher(DeckPublisher):
  """
    simply writes the deck to a txt file in MTGO format
  """

  def __init__(self, save_folder: str) -> None:
    super().__init__()
    self._save_folder = save_folder

  def publish(self, deck: ggt.Decklist) -> None:
    with open(os.path.join(self._save_folder, deck.name + ".txt"), "w") as f:
      pass
      # TODO(Rich): write the decklist to the txt file


class ImagesPublishe(DeckPublisher):
  """
    saves a pdf of all the card images ready to be printed out for proxy play
  """

  def __init__(self, save_folder: str) -> None:
    super().__init__()
    self._save_folder = save_folder

  def publish(self, deck: ggt.Decklist) -> None:
    # TODO(Stephen): work out what libraries etc to use to do this
    pass

# for easy testing


class PrintPublisher(DeckPublisher):
  """
    prints the decklist to stdout
  """

  def publish(self, deck: ggt.Decklist) -> None:
    print(f"deck {deck.name}:")
    print("  mainboard:")
    for c in deck.mainboard:
      print(f"    {c.quantity:02} {c.name} [{c.edition}]")
    print("  sideboard:")
    for c in deck.sideboard:
      print(f"    {c.quantity:02} {c.name} [{c.edition}]")
