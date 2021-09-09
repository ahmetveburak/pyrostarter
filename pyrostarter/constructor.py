import os

from pyrostarter.contents import phrases


def none_venv(none) -> None:
    pass


def virtualenv_type(none) -> None:
    try:
        from venv import EnvBuilder

        venv_manager = EnvBuilder(
            system_site_packages=False,
            clear=True,
            symlinks=False,
            with_pip=True,
        )
        venv_manager.create(".venv")

        with open(f"requirements.txt", "w") as f:
            f.write(phrases["requirements"])

    except ModuleNotFoundError:
        print("venv module not found. you can install and create yourself manually\n")


def poetry_type(project_name: str) -> None:
    f = open(f"pyproject.toml", "w")
    f.write(phrases["poetry"].replace("MODULE_NAME", project_name))


def builder(
    project_name: str,
    bot_name: str,
    api_id: str = "",
    api_hash: str = "",
    bot_token: str = "",
    venv_type: str = "none",
) -> None:

    os.makedirs(f"{project_name}/plugins")
    os.makedirs(f"{project_name}/utils")

    venv_dict = {
        "Standart": virtualenv_type,
        "Poetry": poetry_type,
    }

    venv_dict.get(venv_type, none_venv)(project_name)

    file_list: list = ["/__main__.py", "/BotConfig.py", "/plugins/say_hello.py"]
    file_phrases: list = ["main", "botconfig", "plugin"]

    with open(f"{project_name}/__init__.py", "w") as f:
        f.write('__version__ = "0.1.0"')

    for file, phrase in zip(file_list, file_phrases):
        open(f"{project_name}{file}", "w").write(
            phrases[phrase].replace("BOT_NAME", bot_name).replace("MODULE_NAME", project_name)
        )

    with open(f"{project_name}/utils/buttonator.py", "w") as f:
        f.write(phrases["util"])

    with open(f"{project_name}/{bot_name.lower()}.ini", "w") as f:
        f.write(
            phrases["config"].replace("api_id", api_id).replace("api_hash", api_hash).replace("bot_token", bot_token)
        )
