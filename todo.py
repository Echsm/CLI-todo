import argparse
import functions
import json
parser=argparse.ArgumentParser()
parser.add_argument("arguments", help="File to store as Gist", nargs="*")
args = parser.parse_args()
args = args.arguments

with open('config.json') as f:
    config = json.load(f)


if not args:
    functions.print_active_todo(config["path"],config["renderASCII"])
elif args[0] == "show":
    functions.print_active_todo(config["path"],config["renderASCII"])
elif args[0] == "showall":
    functions.print_all_todo(config["path"],config["renderASCII"])
elif args[0] == "check":
    if len(args) == 2:
        functions.check_todo(int(args[1]),config["path"])
    else:
        functions.check_todo(int(input("index:")),config["path"])
elif args[0] == "add":
    if len(args) == 4:
        functions.add_todo(args[1],args[2],args[3],config["path"])
    else:
        functions.add_todo(input("tag:"),input("description:"),input("date:"),config["path"])