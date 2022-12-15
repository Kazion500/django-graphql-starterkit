import strawberry
from strawberry import auto
from typing import List
from . import models


@strawberry.django.type(models.Fruit)
class Fruit:
    id: auto
    name: auto
    color: "Color"


@strawberry.django.type(models.Color)
class Color:
    id: auto
    name: auto
    fruits: List[Fruit]


@strawberry.input
class ChatRoom:
    room_name: str


@strawberry.type
class ChatRoomMessage:
    room_name: str
    current_user: str
    message: str
