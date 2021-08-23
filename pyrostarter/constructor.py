import os

from pyrostarter.contents import phrases


def virtualenv_type(repo_name: str):
    try:
        from venv import EnvBuilder

        venv_manager = EnvBuilder(
            system_site_packages=False,
            clear=True,
            symlinks=False,
            with_pip=True,
        )
        venv_manager.create(f"{repo_name}/.venv")

        with open(f"{repo_name}/requirements.txt", "w") as f:
            f.write(phrases["requirements"])

    except ModuleNotFoundError:
        print("venv module not found. install and create yourself manually\n")


def poetry_type(repo_name: str, project_name: str):
    f = open(f"{repo_name}/pyproject.toml", "w")
    f.write(phrases["poetry"].replace("MODULE_NAME", project_name))


def setup(
    repo_name: str,
    project_name: str,
    bot_name: str,
    api_id: str = "",
    api_hash: str = "",
    bot_token: str = "",
    venv_type: str = "none",
) -> None:

    os.makedirs(f"{repo_name}/{project_name}/plugins")
    os.makedirs(f"{repo_name}/{project_name}/utils")

    venv_dict = {
        "virtualenv": virtualenv_type(repo_name=repo_name),
        "poetry": poetry_type(repo_name=repo_name, project_name=project_name),
    }

    venv_dict.get(venv_type)

    file_list: list = ["/__main__.py", "/BotConfig.py", "/plugins/say_hello.py"]
    file_phrases: list = ["main", "botconfig", "plugin"]

    with open(f"{repo_name}/{project_name}/__init__.py", "w") as f:
        f.write('__version__ = "0.1.0"')

    for file, phrase in zip(file_list, file_phrases):
        open(f"{repo_name}/{project_name}{file}", "w").write(
            phrases[phrase].replace("BOT_NAME", bot_name).replace("MODULE_NAME", project_name)
        )

    with open(f"{repo_name}/{project_name}/utils/buttonator.py", "w") as f:
        f.write(phrases["util"])

    with open(f"{repo_name}/{project_name}/{bot_name.lower()}.ini", "w") as f:
        f.write(
            phrases["config"].replace("api_id", api_id).replace("api_hash", api_hash).replace("bot_token", bot_token)
        )
