from pyrostarter.contents import phrases
import os


def setup(
    repo_name: str,
    project_name: str,
    bot_name: str,
    api_id: str = "",
    api_hash: str = "",
    bot_token: str = "",
    virtualenv: str = "no",
    poetry: str = "no",
) -> None:

    os.makedirs(f"{repo_name}/{project_name}/plugins")
    os.makedirs(f"{repo_name}/{project_name}/utils")

    file_list: list = ["/__main__.py", "/BotConfig.py", "/plugins/say_hello.py"]
    file_phrases: list = ["main", "botconfig", "plugin"]

    if virtualenv == "yes":
        try:
            import venv

            venv.create(f"{repo_name}/.venv")
            with open(f"{repo_name}/requirements.txt", "w") as f:
                f.write(phrases["requirements"])

        except ModuleNotFoundError:
            print("venv module not found. install and create yourself manually\n")

    if poetry == "yes":
        with open(f"{repo_name}/pyproject.toml", "w") as f:
            f.write(phrases["poetry"].replace("MODULE_NAME", project_name))

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
            phrases["config"]
            .replace("api_id", api_id)
            .replace("api_hash", api_hash)
            .replace("bot_token", bot_token)
        )
