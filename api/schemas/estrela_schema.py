from pydantic import BaseModel
from typing import Optional, List
from model.estrela import Estrela
import json
import numpy as np


class EstrelaSchema(BaseModel):
    """ Define como um novo paciente a ser inserido deve ser representado
    """
    temperature: float = 0
    luminosity: float = 0
    radius: float = 0
    absolute_magnitude: float = 0


class EstrelaViewSchema(BaseModel):
    """Define como um paciente será retornado
    """
    temperature: float = 0
    luminosity: float = 0
    radius: float = 0
    absolute_magnitude: float = 0
    type: int = 0
