from typing import Optional

from cleo import Command
from cleo.helpers import option
from pyrostarter.constructor import builder


class InitCommand(Command):
    name = "init"
    description = "Creates Telegram Bot template structure."

    options = [
        option("project-name", description="Name of the bot project.", flag=False),
        option("bot-name", description="Name of the bot.", flag=False),
        option("api-id", description="Telegram API ID.", flag=False),
        option("api-hash", description="Telegram API Hash.", flag=False),
        option("bot-token", description="Bot Token.", flag=False),
        option("userbot", description="Is userbot?", flag=False),
        option(
            "venv-type",
            description="Standart/Poetry?, default: no virtual environment",
            flag=False,
        ),
    ]

    help = "The init command starts the interactive bot setup."

    def __init__(self):

        super(InitCommand, self).__init__()

    def handle(self) -> None:
        self.add_style("opt", fg="red", options=["bold"])
        if self.io.is_interactive():
            self.line("")
            self.line("This command will guide you through creating your <info>Telegram Bot</> template.")
            self.line("")

        project_name = self.option("project-name")
        if not project_name:
            question = self.create_question("Project name:")
            project_name = self.ask(question)
            while not self.check_answer(project_name):
                project_name = self.ask(question)

        bot_name = self.option("bot-name")
        if not bot_name:
            question = self.create_question("Bot name:")
            bot_name = self.ask(question)
            while not self.check_answer(bot_name):
                bot_name = self.ask(question)

        self.line(
            "\n<comment>API ID, API Hash and Bot Token are optional.\n"
            "You can enter manually to</comment> <info>.ini</info> <comment>file after setup.</comment>\n"
        )

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
            bot_token = bot_token if bot_token else ""

        userbot = self.option("userbot")
        if not userbot:
            userbot = False
            question = self.create_question(f"Is user bot?:", default=userbot, type="confirmation")
            userbot = self.ask(question)

        venv_type = self.option("venv-type")
        if not venv_type:
            venv_type = "no"
            self.line("<comment>\nVirtual enviroment type? Default: No virtual environment.</>\n")
            question = self.create_question("Standart, Poetry (s/p):", default=venv_type)
            venv_type = self.ask(question).lower()

        venvs = {"s": "Standart", "p": "Poetry"}

        self.line(
            f"<info>Project Name  :</> <comment>{project_name}\n</>"
            f"<info>Bot Name      :</> <comment>{bot_name}\n</>"
            f"<info>Userbot       :</> <comment>{userbot}\n</>"
            f"<info>Venv Type     :</> <comment>{venvs.get(venv_type, 'No venv.')}\n</>"
            f"<info>API_ID        :</> <comment>{'Provided.' if api_id else 'Not provided.'}\n</>"
            f"<info>API_HASH      :</> <comment>{'Provided.' if api_hash else 'Not provided.'}\n</>"
            f"<info>BOT_TOKEN     :</> <comment>{'Provided.' if bot_token else 'Not provided.'}\n</>"
        )

        question = self.create_question("Do you confirm generation?:", default=True, type="confirmation")
        confirm = self.ask(question)

        if not confirm:
            self.line("<error>Aborted..</>")
            return

        builder(
            project_name=project_name,
            bot_name=bot_name,
            api_id=api_id if api_id else "",
            api_hash=api_hash if api_hash else "",
            bot_token=bot_token if userbot else "",
            venv_type=venvs.get(venv_type),
        )

    def check_answer(self, answer: str) -> bool:
        if not answer:
            self.line("<error>This field is required.</error>\n")
            return False
        elif " " in answer:
            self.line("<error>No whitespace allowed in this field.</error>\n")
            return False
        elif answer[0].isdigit():
            self.line("<error>The field name cannot start with digits.</error>\n")
            return False
        else:
            return True
