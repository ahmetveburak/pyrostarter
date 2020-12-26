from pyrostarter.contents import phrases
import os


def setup(
    project_name: str,
    bot_name: str,
    api_id: str = "",
    api_hash: str = "",
    bot_token: str = "",
) -> None:

    os.mkdir(project_name)
    os.mkdir(f"{project_name}/plugins")
    os.mkdir(f"{project_name}/utils")
    file_list: list = ["/__main__.py", "/BotConfig.py", "/plugins/say_hello.py"]
    file_phrases: list = ["main", "botconfig", "plugin"]

    with open(f"{project_name}/__init__.py", "w") as f:
        f.write('__version__ = "0.1.0"')

    for file, phrase in zip(file_list, file_phrases):
        open(f"{project_name}{file}", "w").write(
            phrases[phrase]
            .replace("BOT_NAME", bot_name)
            .replace("MODULE_NAME", project_name)
        )

    with open(f"{project_name}/utils/buttonator.py", "w") as f:
        f.write(phrases["util"])

    if not api_id.strip():
        with open(f"{project_name}/{bot_name.lower()}.ini", "w") as f:
            f.write(
                phrases["config"]
                .replace("api_id", api_id)
                .replace("api_hash", api_hash)
                .replace("bot_token", bot_token)
            )
    else:
        with open(f"{project_name}/{bot_name.lower()}.ini", "w") as f:
            f.write(phrases["config"])