<p align="center">
    <a href="https://github.com/pyrogram/pyrogram">
        <img src="https://i.imgur.com/BOgY9ai.png" alt="Pyrogram" width="300">
    </a>
</p>

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

## Usage

Create a directory for your project. In your project directory run the command and follow the instructions:
```shell
pyrostarter init
```

## Credits
[Pyrogram | Telegram MTProto API Framework for Python](https://github.com/pyrogram/pyrogram)
[Dan | Creator of Pyrogram](https://github.com/delivrance)