#!/usr/bin/python3
"""
Module representing the Review class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class representation"""

    place_id = ""
    user_id = ""
    text = ""
