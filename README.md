<a href="https://github.com/python/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

# Pyrostarter

A CLI tool for creating [Pyrogram](https://docs.pyrogram.org/) ready to start project structure. (*All my lazy options included.* 😄)

## Installation

```
pip install git+https://github.com/ahmetveburak/pyrostarter.git
```

## Overview

```
└── repo_name
    └── .venv (optional)
    └── requirement.txt (comes with built-in venv)
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

## Basic Usage

Create a folder for the bot to initialize project.

`$ mkdir PyrostarterBot`

Run command
`$ pyrostarter init`

That's it, follow the edit the `project_name/bot_name.ini` file and if you have already installed the dependencies run your bot.
`$ python -m project_name`

## Config

Save your bot information in your local and automically create full `.ini` folder.
`$ pyrostarter config`


## Credits
<p align="center">
    <a href="https://github.com/pyrogram/pyrogram">
        <img src="https://i.imgur.com/BOgY9ai.png" alt="Pyrogram" width="300">
    </a>
</p>

[Pyrogram | Telegram MTProto API Framework for Python](https://github.com/pyrogram/pyrogram)
[Dan | Creator of Pyrogram](https://github.com/delivrance)