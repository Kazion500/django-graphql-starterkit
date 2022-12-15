import strawberry
from strawberry.types import Info
from strawberry.channels.context import StrawberryChannelsContext
from typing import AsyncGenerator
from sub_django.types import ChatRoom, ChatRoomMessage
from typing import List


class _Info(Info):
    context: StrawberryChannelsContext


@strawberry.type
class Subscription:
    @strawberry.subscription
    async def join_chat_rooms(
        self,
        info: _Info,
        rooms: List[ChatRoom],
        user: str,
    ) -> AsyncGenerator[ChatRoomMessage, None]:
        """Join and subscribe to message sent to the given rooms."""
        ws = info.context.ws
        channel_layer = ws.channel_layer

        room_ids = [f"chat_{room.room_name}" for room in rooms]

        for room in room_ids:
            # Join room group
            await channel_layer.group_add(room, ws.channel_name)

        async for message in ws.channel_listen("chat.message"):
            yield ChatRoomMessage(
                room_name=message["room_id"],
                message=message["message"],
                current_user=user,
            )


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def send_chat_message(
        self,
        info: Info,
        room: ChatRoom,
        message: str,
    ) -> None:
        ws = info.context.ws
        channel_layer = ws.channel_layer

        await channel_layer.group_send(
            f"chat_{room.room_name}",
            {
                "type": "chat.message",
                "room_id": room.room_name,
                "message": message,
            },
        )
