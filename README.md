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

- Arguments:
  - `-h --help`: prints help about tool
  - `-p --projectname:` project name for your file structure
  - `--reponame`: main project folder as repository name 
  - `-b --botname`: your bot's name
  - `-c --clear`: clear your .ini file [id, hash, token, all]
  - `-u --userbot`: [yes, no]
  - `--venv`: creates virtual enviroment named .venv in project [yes, no]
  - `--poetry`: creates pyproject.toml file [yes, no]

- One time configurated parameters for initialize project faster. Configuration will be file saved to $HOME/.pyrouser.ini
  - `-i --id`: your Telegram API_ID
  - `-a --hash`: your Telegram API_HASH
  - `-t --token`: your Telegram BOT_TOKEN
  

Running project:

```
$ pyrostarter -r repo_name -p project_name -b BotName
$ python -m project_name
```
If api keys not provided, manually enter your api keys to `projectName/botname.ini` file before running the bot.

Save your api keys locally or update them with same command. Delete your keys `-c` or `--clear` command with parameters `id, hash, token, all`.
```
pyrostarter -i api_id -a api_hash -t bot_token
```

More initialize settings
```
pyrostarter -r repoName -p projectName -b BotName --venv yes
pyrostarter -r repoName -p projectName -b BotName --poetry yes
```

## Credits
[Pyrogram | Telegram MTProto API Framework for Python](https://github.com/pyrogram/pyrogram)
[Dan | Creator of Pyrogram](https://github.com/delivrance)