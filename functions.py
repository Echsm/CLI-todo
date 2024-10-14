import datetime
import re

def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

def convertDate(input_str:str) -> str:
    date_full = re.compile('^[0-3]?[0-9]\.[0-3]?[0-9]\.20[0-9]{1,2}')
    date_half_year = re.compile('^[0-3]?[0-9]\.[0-3]?[0-9]\.[0-9]{1,2}')
    date_no_year = re.compile('^[0-3]?[0-9]\.[01]?[0-9]')
    weekday_no_number = re.compile('^(mo|di|mi|do|fr|sa|so)')
    weekday_number = re.compile('^[0-9]+(mo|di|mi|do|fr|sa|so)')
    number = re.compile('^-?[0-9]+')
    if date_full.fullmatch(input_str):
        date = datetime.strptime(input_str, '%d.%m.%Y').date()

    elif date_half_year.fullmatch(input_str):
        date = datetime.strptime(input_str, '%d.%m.%y').date()

    elif date_no_year.fullmatch(input_str):
        date = (datetime.strptime(input_str, '%d.%m'))
        current_year = int(datetime.today().strftime("%Y"))
        date = date.replace(year = current_year).date()

    elif weekday_no_number.fullmatch(input_str):
        translation = {
            "mo":0,
            "di":1,
            "mi":2,
            "do":3,
            "fr":4,
            "sa":5,
            "so":6}
        today = datetime.datetime.today().date()
        date = next_weekday(today, translation[input_str])

    elif weekday_number.fullmatch(input_str):
        translation = {
            "mo":0,
            "di":1,
            "mi":2,
            "do":3,
            "fr":4,
            "sa":5,
            "so":6}
        today = datetime.datetime.today().date()
        date = next_weekday(today, translation[input_str[-2:]])
        date = date + datetime.timedelta(days=(int(input_str[:-2])-1)*7)
    
    elif number.fullmatch(input_str):
        date = datetime.datetime.today().date() + datetime.timedelta(days=int(input_str))
    else:
        date = None
    return date.strftime("%d.%m.%y")

def formatdate(input_str: str) -> str:
    parts = input_str.split(".")
    return  f"{parts[0] if len(parts[0]) == 2 else ' '+parts[0]}.{parts[1] if len(parts[1]) == 2 else ' '+parts[1]}.{parts[2]}"
    
def save_todo(all_todos:list, path:str):
    result = ""
    for line in all_todos:
        result += (line[0]+"|"+line[1]+"|"+line[2]+"|"+line[3]+"\n")

    with open(path,"w") as todo:
        todo.write(result)

def load_todo(path: str):
    todo = []
    today = datetime.datetime.today()
    with open(path,"r") as todo:
        all_todos = [[element.strip() for element in line.strip("\n").split("|")] for line in todo]
    all_todos.sort(key=lambda element:( 0 if element[0] == "" else 1,
                                (datetime.datetime.strptime(element[3], '%d.%m.%y')-datetime.datetime.today()).total_seconds() if element[0] == "" else -(datetime.datetime.strptime(element[3], '%d.%m.%y')-datetime.datetime.today()).total_seconds()))
    return all_todos

def print_active_todo(path:str,simpleMode:bool):
    all_todos = load_todo(path)
    active_todos = [todo for todo in all_todos if todo[0] == ""]
    try:
        maxlenght_tags = max([len(todo[1]) for todo in active_todos])
        maxlenght_content = max([len(todo[2]) for todo in active_todos])
    except:
        maxlenght_content = 20
        maxlenght_tags = 10

    if simpleMode:
        print("+--+"+maxlenght_tags*"-"+"+"+maxlenght_content*"-"+"+--------+")
        for line in active_todos:
            print(f"|{'{0:02}'.format(active_todos.index(line))}|{line[1]+' '*(maxlenght_tags-len(line[1]))}|{line[2]+' '*(maxlenght_content-len(line[2]))}|{formatdate(line[3])}|")
        print("+--+"+maxlenght_tags*"-"+"+"+maxlenght_content*"-"+"+--------+")
        save_todo(all_todos, path)
    else:
        print("┌──┬"+maxlenght_tags*"─"+"┬"+maxlenght_content*"─"+"┬────────┐")
        for line in active_todos:
            print(f"│{'{0:02}'.format(active_todos.index(line))}│{line[1]+' '*(maxlenght_tags-len(line[1]))}│{line[2]+' '*(maxlenght_content-len(line[2]))}│{formatdate(line[3])}│")
        print("└──┴"+maxlenght_tags*"─"+"┴"+maxlenght_content*"─"+"┴────────┘")
        save_todo(all_todos, path)

def print_all_todo(path:str,simpleMode:bool):
    all_todos = load_todo(path)
    print("wassa")
    active_todos = [todo for todo in all_todos if todo[0] == ""]
    unactive_todos = [todo for todo in all_todos if todo[0] == "x"]

    try:
        maxlenght_tags = max([len(todo[1]) for todo in all_todos])
        maxlenght_content = max([len(todo[2]) for todo in all_todos])
    except:
        maxlenght_content = 20
        maxlenght_tags = 10
    if simpleMode:
        print("+--+"+maxlenght_tags*"-"+"+"+maxlenght_content*"-"+"+--------+")
        for line in active_todos:
            print(f"│{'{0:02}'.format(active_todos.index(line))}│{line[1]+' '*(maxlenght_tags-len(line[1]))}│{line[2]+' '*(maxlenght_content-len(line[2]))}│{formatdate(line[3])}│")
        print("+--+"+maxlenght_tags*"-"+"+"+maxlenght_content*"-"+"+--------+")
        for line in unactive_todos:
            print(f"| v|{line[1]+' '*(maxlenght_tags-len(line[1]))}|{line[2]+' '*(maxlenght_content-len(line[2]))}|{formatdate(line[3])}|")
        print("+--+"+maxlenght_tags*"-"+"+"+maxlenght_content*"-"+"+--------+")
    else:
        print("┌──┬"+maxlenght_tags*"─"+"┬"+maxlenght_content*"─"+"┬────────┐")
        for line in active_todos:
            print(f"│{'{0:02}'.format(active_todos.index(line))}│{line[1]+' '*(maxlenght_tags-len(line[1]))}│{line[2]+' '*(maxlenght_content-len(line[2]))}│{formatdate(line[3])}│")
        print("├──┼"+maxlenght_tags*"─"+"┼"+maxlenght_content*"─"+"┼────────┤")
        for line in unactive_todos:
            print(f"│ ✓│{line[1]+' '*(maxlenght_tags-len(line[1]))}│{line[2]+' '*(maxlenght_content-len(line[2]))}│{formatdate(line[3])}│")
        print("└──┴"+maxlenght_tags*"─"+"┴"+maxlenght_content*"─"+"┴────────┘")
    save_todo(all_todos,path)

def check_todo(index: int, path:str):
    all_todos = load_todo(path)
    all_todos[index][0] = "x"
    #all_todos.pop(index)
    save_todo(all_todos, path)

def add_todo(tag:str,description:str,date:str,path:str):
    today = datetime.datetime.today()
    all_todos = load_todo(path)
    
    all_todos.append(["",tag,description,convertDate(date)])
    
    all_todos.sort(key=lambda element:( 0 if element[0] == "" else 1,
                                (datetime.datetime.strptime(element[3], '%d.%m.%y')-datetime.datetime.today()).total_seconds() if element[0] == "" else -(datetime.datetime.strptime(element[3], '%d.%m.%y')-datetime.datetime.today()).total_seconds(),
                                ))
    
    
    save_todo(all_todos, path)
    return all_todos


print(convertDate("-7"))