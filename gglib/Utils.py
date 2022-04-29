"""
  various utility functions that various things need
"""

import requests


def get_page_source(url: str) -> str:
  return str(requests.get(url).content)
