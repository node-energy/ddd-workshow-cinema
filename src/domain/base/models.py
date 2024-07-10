from __future__ import annotations

from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class ValueObject:
    pass


@dataclass
class Entity:
    id: UUID = field(hash=True, default_factory=uuid4)

    def __eq__(self, other: Entity):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)


@dataclass
class AggregateRoot(Entity):
    pass