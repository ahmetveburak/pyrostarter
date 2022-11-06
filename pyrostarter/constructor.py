import os

from pyrostarter.contents import phrases


def builtin_venv() -> None:
    try:
        from venv import EnvBuilder

        venv_manager = EnvBuilder(
            system_site_packages=False,
            clear=True,
            symlinks=False,
            with_pip=True,
        )
        venv_manager.create(".venv")

        with open("requirements.txt", "w", encoding="utf-8") as f:
            f.write(phrases["requirements"])

    except ModuleNotFoundError:
        print("venv module not found. you can install and create yourself manually\n")


def poetry_venv(project_name: str) -> None:
    with open("pyproject.toml", "w", encoding="utf-8") as f:
        f.write(phrases["poetry"].replace("MODULE_NAME", project_name))


def builder(
    project_name: str,
    bot_name: str,
    api_id: str = "",
    api_hash: str = "",
    bot_token: str = "",
    venv_type: str = "",
) -> None:

    os.makedirs(f"{project_name}/plugins")
    os.makedirs(f"{project_name}/utils")

    if venv_type == "Poetry":
        poetry_venv(project_name)
    else:
        builtin_venv()

    file_list: list = ["/__main__.py", "/BotConfig.py", "/plugins/say_hello.py"]
    file_phrases: list = ["main", "botconfig", "plugin"]

    with open(f"{project_name}/__init__.py", "w", encoding="utf-8") as f:
        f.write('__version__ = "0.1.0"')

    for file, phrase in zip(file_list, file_phrases):
        with open(f"{project_name}{file}", "w", encoding="utf-8") as f:
            f.write(
                phrases[phrase]
                .replace("BOT_NAME", bot_name)
                .replace("MODULE_NAME", project_name)
            )

    with open(f"{project_name}/utils/buttonator.py", "w", encoding="utf-8") as f:
        f.write(phrases["util"])

    with open(f"{bot_name.lower()}.ini", "w", encoding="utf-8") as f:
        f.write(
            phrases["config"]
            .replace("api_id", api_id)
            .replace("api_hash", api_hash)
            .replace("bot_token", bot_token)
        )
