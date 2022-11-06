phrases = {
    "main": """\
from MODULE_NAME.BotConfig import BOT_NAME

if __name__ == "__main__":
    BOT_NAME().run()
""",
    "config": """\
[pyrogram]
API_ID = api_id
API_HASH = api_hash
BOT_TOKEN = bot_token
""",
    "user_config": """\
[pyrouser]
API_ID = 
API_HASH = 
BOT_TOKEN = 
USER_CONF = 
""",
    "botconfig": """\
from configparser import ConfigParser
from functools import partial

from pyrogram import Client, filters

command = partial(filters.command, prefixes=["!", "/", "."])


class BOT_NAME(Client):
    def __init__(self):
        module_name = "MODULE_NAME"
        self.name = self.__class__.__name__.lower()
        config = self.load_config()
        super().__init__(
            name=self.name,
            api_id=config["api_id"],
            api_hash=config["api_hash"],
            bot_token=config["bot_token"],
            workers=8,
            plugins=dict(root=f"{module_name}/plugins"),
        )

    async def start(self):
        await super().start()

    async def stop(self, *args):
        await super().stop()

    def load_config(self):
        config = ConfigParser()
        config.read(f"{self.name}.ini")
        return config["pyrogram"]
""",
    "plugin": """\
import asyncio
import time

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, Message

from starter.BotConfig import command, BOT_NAME
from starter.utils import buttonator


@BOT_NAME.on_message(command("start"))
async def say_hello(_: Client, message: Message) -> None:
    msg = await message.reply_text(text="`Hello..`", quote=True)
    await asyncio.sleep(1)
    await msg.edit_text(text="`Hello I'm Ready to Use`")


@BOT_NAME.on_message(command("ping"))
async def ping(_, message: Message):
    start = time.time()
    reply = await message.reply_text("...")
    delta_ping = time.time() - start
    await reply.edit_text(f"**Pong!** `{delta_ping * 1000:.3f} ms`")


my_buttons = {
    "Button1": "Button1",
    "Button2": "Button2",
    "Button3": "Button3",
    "Button4": "Button4",
    "Button5": "Button5",
}
button_filter = filters.create(lambda _, __, query: query.data in my_buttons.keys())


@BOT_NAME.on_message(command("buttons"))
async def buttons(client: Client, message: Message):
    me = await client.get_me()

    if me.is_bot:
        await message.reply_text(
            text="These are test buttons with callback",
            reply_markup=buttonator.button_maker(buttons=my_buttons, size=2),
        )
    else:
        await message.reply_text(
            text="Users can not send `keyboard markup`. **I'm sorry..**",
        )


@BOT_NAME.on_callback_query(button_filter)
async def reply_callback(_: Client, callback=CallbackQuery):
    await callback.message.reply_text(text=callback.data)""",
    "util": """\
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def slicer(button_list: list, size: int) -> list:
    return [button_list[i : i + size] for i in range(0, len(button_list), size)]


def button_maker(buttons: dict, size: int) -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(text=v, callback_data=k) for k, v in buttons.items()
    ]
    buttons = slicer(buttons, size)

    return InlineKeyboardMarkup(buttons)
""",
    "poetry": """\
[tool.poetry]
name = "MODULE_NAME"
version = "0.1.0"
description = "YOUR DESCRIPTION"
authors = ["YOU <ABOUT@YOU.COM>"]
license = "YOUR LICENSE"

[tool.poetry.dependencies]
python = "^3.9"
Pyrogram = "^2.0.0"
TgCrypto = "^1.2.2"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
""",
    "requirements": """\
pyrogram>=2.0.0;
tgcrypto>=1.2.2;
""",
}
