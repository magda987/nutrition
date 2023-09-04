from uuid import UUID, uuid4
from enum import StrEnum, auto

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Solubility(StrEnum):
    WATER = auto()
    FAT = auto()
    

class Food(Base):
    __tablename__="foodEntity"

    id: Mapped[UUID]=mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column()
    vitamin_id: Mapped[UUID]=mapped_column(ForeignKey("vitaminEntity.id"))
    mineral_id: Mapped[UUID]=mapped_column(ForeignKey("mineralEntity.id"))

    vitamins: Mapped["Vitamin"]=relationship(back_populates="food")
    minerals: Mapped["Mineral"]=relationship(back_populates="food")

class Vitamin(Base):
    __tablename__="vitaminEntity"

    id: Mapped[UUID]=mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column()
    solubility: Mapped(Solubility)=mapped_column()

    food: Mapped["Food"]=relationship(back_populates="vitamins")

class Mineral(Base):
    __tablename__="mineralEntity"

    id: Mapped[UUID]=mapped_column(primary_key=True, default=uuid4)
    name: Mapped[str] = mapped_column()

    food: Mapped["Food"]=relationship(back_populates="minerals")









