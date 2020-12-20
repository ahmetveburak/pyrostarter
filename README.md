# Pyrostarter

A CLI tool for creating [Pyrogram](https://docs.pyrogram.org/) project file structure.

## Installation

```
pip install git+https://github.com/ahmetveburak/pyrostarter.git
```

## Usage

- Arguments:
  - -h --help: prints help about tool
  - -p --projectname: project name for your file structure
  - -b --botname: your bot's name
  - -i --id: your Telegram API_ID (*optional)
  - -a --hash: your Telegram API_HASH (*optional)
  - -t --token: your Telegram BOT_TOKEN (*optional)
  - -c --clear: clear your .ini file [id, hash, token, all]
  - -u --userbot: if it's userbot [yes, no]

*optional: you can save your api keys locally

Running project:

```
pyrostarter -i api_id -a api_hash -t bot_token
pyrostarter -p projectName -b BotName
python -m projectName
```

- If api keys not provided
```
pyrostarter -p projectName -b BotName
```
Manually enter your api keys to `projectName/botname.ini` file and run:

```
python -m projectName
```
