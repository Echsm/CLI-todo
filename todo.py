import argparse
import functions
import json
parser=argparse.ArgumentParser()
parser.add_argument("arguments", help="File to store as Gist", nargs="*")
args = parser.parse_args()
args = args.arguments
print(args)

with open('config.json') as f:
    config = json.load(f)

print(config)


if not args:
    functions.print_active_todo(config["path"],config["renderASCII"])
elif args[0] == "show":
    functions.print_active_todo(config["path"],config["renderASCII"])
elif args[0] == "showall":
    functions.print_all_todo(config["path"],config["renderASCII"])

# check -> Start Checker input
# check 2 -> check 2nd item

# add -> start adder input
# add tag desc time

# rm -> start Remover Input
# rm 2 -> remove 2