from fastapi import Form
from pydantic import BaseModel, Field, EmailStr, SecretStr
from typing import List, Union
import inspect

from enum import Enum

class OilSchema(str, Enum):
    HPDSb7 = "Hi Premium Diesel S B7"
    HiDieselSb = "Diesel S B7"
    HiDieselS = "HI DIESEL S"
    B20 = "HI DIESEL B20 S"
    E85 = "Gasohol E85 S EVO"
    E20 = "Gasohol E20 S EVO"
    G91 = "Gasohol 91 S EVO"
    G95 = "Gasohol 95 S EVO"