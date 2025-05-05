from typing import Optional
from enum import Enum
from datetime import date
from pydantic import BaseModel


class PlayerStatuses(Enum):
    BENCHED = "BENCHED"
    MAIN = "MAIN"
    COACH = "COACH"


class Draft5StatusesMapping(Enum):
    Reserva = PlayerStatuses.BENCHED
    Titular = PlayerStatuses.MAIN
    Coach = PlayerStatuses.COACH


class Player(BaseModel):
    name: str
    nickname: str
    country: str
    status: PlayerStatuses
    start_date: date


class Match(BaseModel):
    against: str
    date: date


class Matches(BaseModel):
    upcoming: list[Match]
    recent: list[Match]


class Team(BaseModel):
    name: str
    players: Optional[list[Player]] = None
    matches: Optional[Matches] = None
