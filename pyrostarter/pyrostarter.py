from cleo import Application

from pyrostarter.commands.config import ConfigCommand
from pyrostarter.commands.init import InitCommand


def main() -> None:
    application = Application()
    application.add(InitCommand())
    application.add(ConfigCommand())

    application.run()


if __name__ == "__main__":
    main()
