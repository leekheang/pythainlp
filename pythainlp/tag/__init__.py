# -*- coding: utf-8 -*-
"""
Linguistic and other taggers.

Tagging each token in a sentence with supplementary information,
such as its part-of-speech (POS) tag, and named entity (NE) tag.
"""

__all__ = ["pos_tag", "pos_tag_sents", "tag_provinces"]

from pythainlp.tag.locations import tag_provinces
from pythainlp.tag.pos_tag import pos_tag
from pythainlp.tag.pos_tag import pos_tag_sents
