import argparse
import functions

parser=argparse.ArgumentParser()
parser.add_argument("arguments", help="File to store as Gist", nargs="*")
args = parser.parse_args()
args = args.arguments
print(args)


if not args:
    functions.print_active_todo()
elif args[0] == "show":
    functions.print_active_todo()
elif args[0] == "showall":
    functions.print_all_todo()

# check -> Start Checker input
# check 2 -> check 2nd item

# add -> start adder input
# add tag desc time

# rm -> start Remover Input
# rm 2 -> remove 2