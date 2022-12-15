from typing import List
from sub_django.types import Fruit
from .subscription import Subscription
import strawberry


@strawberry.type
class Query:
    fruits: List[Fruit] = strawberry.django.field()


@strawberry.type
class Subscription(Subscription):
    pass
