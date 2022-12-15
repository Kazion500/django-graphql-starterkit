import strawberry
from sub_django.schema import Query
from sub_django.subscription import Subscription, Mutation

schema = strawberry.Schema(query=Query, subscription=Subscription, mutation=Mutation)
