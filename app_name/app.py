# clear; python app_name/app.py
import argparse
import os

from dotenv import load_dotenv

from loguru import logger

load_dotenv()  # looks for a .env file in the current directory

from app_name.utils import say_hi


def cmd_run(args):
    logger.info(f"Running with param: {args.param}")

    print(os.getenv("MY_KEY"))

    say_hi()


def main():
    logger.info("App is running...")

    p = argparse.ArgumentParser(prog="app_name")
    sub = p.add_subparsers(dest="cmd", required=True)

    pb = sub.add_parser("run", help="Do something useful.")
    pb.add_argument("--param", required=True, help="Give me a param.")
    pb.set_defaults(func=cmd_run)

    args = p.parse_args()
    args.func(args)

    logger.info("App is running...")


if __name__ == "__main__":
    main()
