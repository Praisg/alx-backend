#!/usr/bin/env python3
"""Simple helper functions"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start index and  end index"""

    return (page * page_size - page_size, page * page_size)
