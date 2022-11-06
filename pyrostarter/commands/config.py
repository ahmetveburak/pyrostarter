import os
from configparser import ConfigParser
from typing import Optional

from cleo import Command
from cleo.helpers import option

from pyrostarter.contents import phrases


class ConfigCommand(Command):
    name = "config"
    description = "Creates a .pyrouser.ini config file at your home directory"

    options = [
        option("api-id", "i", description="Telegram API ID.", flag=False),
        option("api-hash", "a", description="Telegram API Hash.", flag=False),
        option("bot-token", "t", description="Bot Token.", flag=False),
        option("userbot", "u", description="Is userbot?.", flag=False),
        option(
            "clear", "c", description="Clear your id/hash/token fields.", flag=False
        ),
    ]

    def __init__(self):
        super(ConfigCommand, self).__init__()
        home_dir = os.getenv("HOME")
        self.config_file_path = f"{home_dir}/.pyrouser.ini"

        if not self.config_exists():
            self.create_config()

    def config_exists(self) -> bool:
        return os.path.isfile(self.config_file_path)

    def get_config(self):
        config = ConfigParser()
        config.read(self.config_file_path)
        return config

    def create_config(self) -> None:
        """
        Creates an empty config file at home directory with predefined settings
        """
        with open(self.config_file_path, "w", encoding="utf-8") as f:
            f.write(phrases["user_config"].lower())

    def handle(self) -> Optional[int]:

        clear = self.option("clear")
        if clear == "yes":
            self.create_config()
            return

        if self.io.is_interactive():
            self.line("")
            self.line(
                "Create your <info>.pyrouser.ini</> config.\n"
                "Pass for unchanged infos."
            )
            self.line("")

        api_id = self.option("api-id")
        if not api_id:
            question = self.create_question("Your API ID:")
            api_id = self.ask(question)

        api_hash = self.option("api-hash")
        if not api_hash:
            question = self.create_question("Your API Hash:")
            api_hash = self.ask(question)

        bot_token = self.option("bot-token")
        if not bot_token:
            question = self.create_question("Your Bot Token:")
            bot_token = self.ask(question)

        userbot = self.option("userbot")
        if not userbot:
            question = self.create_question(
                f"Is userbot?:", default=False, type="confirmation"
            )
            userbot = f"{self.ask(question)}"

        config = self.get_config()
        user_config = config["pyrouser"]
        user_config["API_ID"] = api_id if api_id else user_config["API_ID"]
        user_config["API_HASH"] = api_hash if api_hash else user_config["API_HASH"]
        user_config["BOT_TOKEN"] = bot_token if bot_token else user_config["BOT_TOKEN"]
        user_config["USER_CONF"] = f"{userbot}"

        with open(self.config_file_path, "w", encoding="utf-8") as f:
            config.write(f)
