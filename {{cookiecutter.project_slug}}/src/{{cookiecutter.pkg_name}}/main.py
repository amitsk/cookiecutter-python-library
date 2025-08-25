from {{cookiecutter.pkg_name}}.app  import scrabble_score
from loguru import logger


def main() -> None:
    logger.info(scrabble_score("hello"))


if __name__ == "__main__":
    main()
