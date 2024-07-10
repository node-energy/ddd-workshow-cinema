from __future__ import annotations

import datetime as dt
from dataclasses import dataclass
from enum import Enum
from src.domain.base.models import AggregateRoot, Entity, ValueObject


@dataclass
class WeeklySchedule(AggregateRoot):
    pass


class Status(str, Enum):
    open = "OPEN"
    reserved = "RESERVED"


@dataclass(kw_only=True)
class Seat(Entity):
    number: int
    status: Status


@dataclass(kw_only=True)
class SeatRow(Entity):
    number: int
    seats: list[Seat]


@dataclass(kw_only=True)
class HallPlan(AggregateRoot):
    rows: list[SeatRow]

    def mark_as_sold(self, row_number: int, seat_number: int):
        row = next(r for r in self.rows if r.number == row_number)
        seat = next(s for s in row.seats if s.number == seat_number)
        seat.status = Status.reserved


@dataclass(kw_only=True)
class Showing(ValueObject):
    start_datetime: dt.datetime
    title: str


@dataclass(kw_only=True)
class Movie(AggregateRoot):
    title: str
    duration: dt.timedelta
    min_age: int
