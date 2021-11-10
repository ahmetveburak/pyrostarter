<p align="center">
    <a href="https://github.com/pyrogram/pyrogram">
        <img src="https://i.imgur.com/BOgY9ai.png" alt="Pyrogram" width="300">
    </a>
</p>

# Pyrostarter

A CLI tool for creating [Pyrogram](https://docs.pyrogram.org/) ready to start project structure. (*All my lazy options included.* 😄)

## Overview

```
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
```
## Installation

```
pip install git+https://github.com/ahmetveburak/pyrostarter.git
```

## Usage

Create a directory for your project. In your project directory run the command and follow the instructions:
```shell
$ mkdir YourProject
$ pyrostarter init
```

```shell
This command will guide you through creating your Telegram Bot template.

Project name: <project_name>
Bot name: <BotName> (PascalCase recommended)

API ID, API Hash and Bot Token are optional.
You can enter manually to .ini file after setup.

Your API ID: <api_id>
Your API Hash: <api_hash>
Your Bot Token: <bot_token>
Is user bot?: (yes/no) [no] 

Virtual enviroment type? Default: No virtual environment.

Standart, Poetry (s/p):
```

Run your project

## Credits
[Pyrogram | Telegram MTProto API Framework for Python](https://github.com/pyrogram/pyrogram)
[Dan | Creator of Pyrogram](https://github.com/delivrance)