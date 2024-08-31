from pydantic import BaseModel
from typing import Optional, List
from model.estrela import Estrela
import json
import numpy as np


class EstrelaSchema(BaseModel):
    """ Define como uma estrela deve ser representada
    """
    temperature: float
    luminosity: float
    radius: float
    absolute_magnitude: float


class EstrelaViewSchema(BaseModel):
    """Define como uma estrela será retornada
    """
    type: int
