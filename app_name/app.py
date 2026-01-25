import argparse
import os

from dotenv import load_dotenv

from loguru import logger

from app_name.utils import say_hi

load_dotenv()  # looks for a .env file in the current directory

MY_KEY = os.getenv("MY_KEY", "")


def cmd_say(args):
    print(args.msg)


def cmd_shout(args):
    print(args.msg.upper())


def cmd_repeat(args):
    for _ in range(args.times):
        print(args.msg)


def main():
    logger.info("App is running...")

    p = argparse.ArgumentParser(prog="say_hi")
    sub = p.add_subparsers(dest="cmd", required=True)

    # say
    pb = sub.add_parser("say", help="Say something.")
    pb.add_argument("--msg", required=True, help="What to say?")
    pb.set_defaults(func=cmd_say)

    # shout
    pb = sub.add_parser("shout", help="Shout something")
    pb.add_argument("--msg", required=True)
    pb.set_defaults(func=cmd_shout)

    # repeat
    pb = sub.add_parser("repeat", help="Repeat something")
    pb.add_argument("--msg", required=True)
    pb.add_argument("--times", type=int, default=1)
    pb.set_defaults(func=cmd_repeat)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
