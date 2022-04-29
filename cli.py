#! python

""" point of entry for the gauntlet generator code.
    presents a command line interface for the tool
"""

import argparse
import gglib.Types as ggt
import gglib.MetaSource as ggms
import gglib.DeckPublisher as ggdp
import gglib.MetaGenerator as ggmg


def generate_gauntlet(args, gen: ggmg.MetaGenerator,
                      src: ggms.MetaSource, pub: ggdp.DeckPublisher):

  form = ggt.Format[args.format.capitalize()]
  alg = ggmg.GeneratorAlgorithm[args.algorithm.capitalize()]
  decks = gen.select_decks(source=src, format=form,
                           total_decks=args.ndecks, algorithm=alg)
  for d in decks:
    pub.publish(d)


def get_arguments():
  parser = argparse.ArgumentParser()
  parser.add_argument("--ndecks", type=int, default=10,
                      help="how many decks to generate. -1 is as many as possible")
  parser.add_argument("--format", "-f", default="Modern",
                      help="which format to scrape")
  parser.add_argument("--output-dir", default="~/decks",
                      help="which folder to save the decks to")
  parser.add_argument("--algorithm", default="TopPlayRate",
                      help="which algorithm to use")

  # TODO(Stephen): add arguments and handling to specify which meta source
  # TODO(Stephen): add arguments and handling to specify which output format

  args = parser.parse_args()
  return args


if __name__ == "__main__":
  args = get_arguments()

  gen = ggmg.MetaGenerator()

  # debug
  args.algorithm = "All"

  src = ggms.TestSource()
  pub = ggdp.PrintPublisher()

  generate_gauntlet(args, gen, src, pub)
