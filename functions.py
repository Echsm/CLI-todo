from datetime import datetime
import random


def formatdate(input_str: str) -> str:
    parts = input_str.split(".")
    return  f"{parts[0] if len(parts[0]) == 2 else ' '+parts[0]}.{parts[1] if len(parts[1]) == 2 else ' '+parts[1]}.{parts[2]}"

def save_todo(all_todos:list):
    PATH = "todo.txt"
    #LOAD PATH FROM CONFIG
    result = ""
    for line in all_todos:
        result += (line[0]+"|"+line[1]+"|"+line[2]+"|"+line[3]+"\n")

    with open(PATH,"w") as todo:
        todo.write(result)

def load_todo():
    PATH = "todo.txt"
    #LOAD PATH FORM CONFIG
    todo = []
    today = datetime.today()
    with open(PATH,"r") as todo:
        all_todos = [[element.strip() for element in line.strip("\n").split("|")] for line in todo]
    all_todos.sort(key=lambda element:( 0 if element[0] == "" else 1,
                                (datetime.strptime(element[3], '%d.%m.%y')-datetime.today()).total_seconds() if element[0] == "" else -(datetime.strptime(element[3], '%d.%m.%y')-datetime.today()).total_seconds()))
    return all_todos

def print_active_todo():
    all_todos = load_todo()
    active_todos = [todo for todo in all_todos if todo[0] == ""]
    try:
        maxlenght_tags = max([len(todo[1]) for todo in active_todos])
        maxlenght_content = max([len(todo[2]) for todo in active_todos])
    except:
        maxlenght_content = 20
        maxlenght_tags = 10
    print("┌──┬"+maxlenght_tags*"─"+"┬"+maxlenght_content*"─"+"┬────────┐")
    for line in active_todos:
        print(f"│{'{0:02}'.format(active_todos.index(line))}│{line[1]+' '*(maxlenght_tags-len(line[1]))}│{line[2]+' '*(maxlenght_content-len(line[2]))}│{formatdate(line[3])}│")
    print("└──┴"+maxlenght_tags*"─"+"┴"+maxlenght_content*"─"+"┴────────┘")

def print_all_todo():
    all_todos = load_todo()
    print("wassa")
    active_todos = [todo for todo in all_todos if todo[0] == ""]
    unactive_todos = [todo for todo in all_todos if todo[0] == "x"]
    maxlenght_tags = max([len(todo[1]) for todo in all_todos])
    maxlenght_content = max([len(todo[2]) for todo in all_todos])

    print("┌──┬"+maxlenght_tags*"─"+"┬"+maxlenght_content*"─"+"┬────────┐")
    for line in active_todos:
        print(f"│{'{0:02}'.format(active_todos.index(line))}│{line[1]+' '*(maxlenght_tags-len(line[1]))}│{line[2]+' '*(maxlenght_content-len(line[2]))}│{formatdate(line[3])}│")
    print("├──┼"+maxlenght_tags*"─"+"┼"+maxlenght_content*"─"+"┼────────┤")
    for line in unactive_todos:
        print(f"│ ✓│{line[1]+' '*(maxlenght_tags-len(line[1]))}│{line[2]+' '*(maxlenght_content-len(line[2]))}│{formatdate(line[3])}│")
    print("└──┴"+maxlenght_tags*"─"+"┴"+maxlenght_content*"─"+"┴────────┘")

    save_todo(all_todos)

def check_todo(index: int):
    all_todos = load_todo()
    all_todos[index][0] = "x"
    #all_todos.pop(index)
    save_todo(all_todos=all_todos)

def add_todo(tag:str,description:str,date:str,):


    todo = []
    today = datetime.today()
    with open(PATH,"r") as todo:
        all_todos = [[element.strip() for element in line.strip("\n").split("|")] for line in todo]
        all_todos.append(["",tag,description,date])
    
    all_todos.sort(key=lambda element:( 0 if element[0] == "" else 1,
                                (datetime.strptime(element[3], '%d.%m.%y')-datetime.today()).total_seconds() if element[0] == "" else -(datetime.strptime(element[3], '%d.%m.%y')-datetime.today()).total_seconds(),
                                ))
    
    
    save_todo(all_todos=all_todos)
    return all_todos
