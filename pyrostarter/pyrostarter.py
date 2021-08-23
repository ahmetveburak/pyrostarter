#!/usr/bin/env python3
import argparse
import os
import sys
from argparse import RawTextHelpFormatter
from configparser import ConfigParser

from pyrostarter.constructor import setup

mod_path = os.getenv("HOME")


def get_args():

    structure = """.
└── repo_name
    └── .venv (optional)
    └── pyproject.toml (optional)
    └── project_name
        ├── plugins
        │   └── say_hello.py
        ├── utils
        │   └── buttonator.py
        ├── __init__.py
        ├── __main__.py
        ├── BotConfig.py
        └── botname.ini
"""

    parser = argparse.ArgumentParser(
        description=f"A Pyrogram project template starter\n{structure}",
        formatter_class=RawTextHelpFormatter,
    )

    parser.add_argument(
        "-p",
        "--projectname",
        required=False,
        help="name of your project",
    )

    parser.add_argument(
        "-r",
        "--reponame",
        required=False,
        help="name of your repo. default <project name>",
    )

    parser.add_argument(
        "-b",
        "--botname",
        required=False,
        help="name of your bot",
    )

    parser.add_argument(
        "-i",
        "--id",
        help="your Telegram API_ID",
    )

    parser.add_argument(
        "-a",
        "--hash",
        help="your Telegram API_HASH",
    )
    parser.add_argument(
        "-t",
        "--token",
        help="your Telegram BOT_TOKEN",
    )
    parser.add_argument(
        "-u",
        "--userbot",
        choices=["yes", "no"],
        default="no",
        help="is userbot? default 'no'",
    )

    parser.add_argument(
        "-c",
        "--clear",
        choices=["id", "hash", "token", "all"],
        required=False,
        help="name of your bot",
    )

    parser.add_argument(
        "--venv",
        choices=["virtualenv", "poetry"],
        default="none",
        required=False,
        help="select your virtual enviroment in type",
    )

    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        quit()
    return args


def main() -> None:
    args = get_args()

    if any(" " in i for i in [args.projectname, args.botname, args.reponame] if i != None):
        print("Whitespace not allowed in names. Aborted..")
        quit()

    project_name = args.projectname
    bot_name = args.botname
    repo_name = args.reponame if args.reponame else project_name
    virtualenv = args.venv

    config = ConfigParser()
    config.read(f"{mod_path}/.pyrouser.ini")

    if config.sections() == []:
        print(
            "It's first time runing Pyrostarter. There are no user defined config file. Check help for further information."
        )
        config["pyrouser"] = {}
        config["pyrouser"]["API_ID"] = ""
        config["pyrouser"]["API_HASH"] = ""
        config["pyrouser"]["BOT_TOKEN"] = ""
        config["pyrouser"]["USER_CONF"] = ""
        with open(f"{mod_path}/.pyrouser.ini", "w") as f:
            config.write(f)

    if args.clear == "all":
        config["pyrouser"]["API_ID"] = ""
        config["pyrouser"]["API_HASH"] = ""
        config["pyrouser"]["BOT_TOKEN"] = ""
        config["pyrouser"]["USER_CONF"] = ""
        print("All configuration data is deleted..")

    elif args.clear:
        clear = {"id": "api_id", "hash": "api_hash", "token": "bot_token"}
        config["pyrouser"][clear[args.clear]] = ""
        config["pyrouser"]["USER_CONF"] = ""
        print(f"{clear[args.clear]} is deleted..")

    if args.id:
        config["pyrouser"]["API_ID"] = args.id
        print("Your API_ID saved succesfully..")
    if args.hash:
        config["pyrouser"]["API_HASH"] = args.hash
        print("Your API_HASH saved succesfully..")
    if args.token:
        config["pyrouser"]["BOT_TOKEN"] = args.token
        print("Your BOT_TOKEN  saved succesfully..")

    if config["pyrouser"]["API_ID"] and config["pyrouser"]["API_HASH"]:
        config["pyrouser"]["USER_CONF"] = "YES"

    if args.id or args.hash or args.token or args.clear:
        with open(f"{mod_path}/.pyrouser.ini", "w") as f:
            config.write(f)

    if config["pyrouser"]["USER_CONF"] and project_name and bot_name:
        api_id = config["pyrouser"]["API_ID"]
        api_hash = config["pyrouser"]["API_HASH"]
        bot_token = config["pyrouser"]["BOT_TOKEN"] if args.userbot == "no" else ""

        print(
            f"Repository Name: {repo_name}\n"
            f"Project Name:    {project_name}\n"
            f"Bot Name:        {bot_name}\n"
            f"Userbot:         {args.userbot.capitalize()}\n"
            f"Venv Type:       {virtualenv.capitalize()}\n"
            f"API_ID:       Provided\n"
            f"API_HASH:     Provided\n"
            f"BOT_TOKEN:    Provided\n"
        )

        sure = input(
            f"Your project will be created as above. Do you want to continue?\n"
            "press enter to continue or 'no' to quit: "
        ).lower()

        if sure not in ["n", "no"]:
            setup(
                repo_name=repo_name,
                project_name=project_name,
                bot_name=bot_name,
                api_id=api_id,
                api_hash=api_hash,
                bot_token=bot_token,
                venv_type=virtualenv,
            )

        else:
            print("Aborted..")
            quit()

    elif project_name and bot_name:
        print(
            f"Repository Name: {repo_name}\n"
            f"Project Name:    {project_name}\n"
            f"Bot Name:        {bot_name}\n"
            f"Userbot:         {args.userbot.capitalize()}\n"
            f"Venv Type:       {virtualenv.capitalize()}\n"
            f"API_ID, API_HASH or BOT_TOKEN are not provided. You should manually enter to {bot_name}.ini file\n"
        )

        sure = input(
            f"Your project will be created as above. Do you want to continue?\n"
            "press enter to continue or 'n/no' to quit: "
        ).lower()
        if sure not in ["n", "no"]:
            setup(
                repo_name=repo_name,
                project_name=project_name,
                bot_name=bot_name,
                venv_type=virtualenv,
            )

        else:
            print("Aborted..")
            quit()

    else:
        print("Project name or bot name not defined..")


if __name__ == "__main__":
    main()
