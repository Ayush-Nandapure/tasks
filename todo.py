import argparse
import datetime
import json


def add(t):
    tasks = {}
    try:
        with open("task.json", "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        pass

    maximum = 0
    for t2 in tasks.values():
        maximum = max(maximum, t2["id"])
        
    t1 = {
        "id" : maximum + 1,
        "status" : "created",
        "task" : t,
        "created_at": str(datetime.datetime.now()),
        "updated_at" : None
    }
    tasks[str(t1["id"])] = t1
    with open("task.json", "w") as f1:
        json.dump(tasks, f1, indent=4)
        


def update(task_id, t):
    try:
        tasks = {}
        with open("task.json", "r") as f:
            tasks = json.load(f)
        str_id =str(task_id)
        if str_id in tasks:
            tasks[str_id]["task"] = t
            tasks[str_id]["updated_at"] = str(datetime.datetime.now())
            with open("task.json", "w") as f1:
                json.dump(tasks, f1, indent = 4)
    except Exception as e:
        print(f"An error occurred: {e}")



def delete(task_id):
    try:
        tasks = {}
        with open("task.json", "r") as f:
            tasks = json.load(f)
        str_id =str(task_id)
        if str_id in tasks:
            tasks.pop(str_id) 
            with open("task.json", "w") as f1:
                json.dump(tasks, f1, indent = 4)
    except Exception as e:
        print(f"An error occurred: {e}")    


def mark(task_id, i):
    try:
        tasks = {}
        with open("task.json", "r") as f:
            tasks = json.load(f)
        str_id =str(task_id)
        if str_id in tasks:
            if(i == 1):
                tasks[str_id]["status"] = "done"
            elif(i == 2):
                tasks[str_id]["status"] = "in progress"
            tasks[str_id]["updated_at"] = str(datetime.datetime.now())

            with open("task.json", "w") as f1:
                json.dump(tasks, f1, indent = 4)
    except Exception as e:
        print(f"An error occurred: {e}")


def list_tasks(i):
    try:
        tasks = {}
        with open("task.json", "r") as f:
            tasks = json.load(f)
        if(len(tasks) == 0):
            print("NO tasks")
            return
            
        if(i == 1):
            for t in tasks.values():
                print(f'''
taskid      : {t["id"]}
status      : {t["status"]}
task        : {t["task"]}
created     : {t['created_at']}''')
                if(t["updated_at"] != None):
                    print(f"last updated: {t["updated_at"]}")
                print("")
        elif(i == 2):
            for t in tasks.values():
                if(t["status"] == "done"):
                    print(f'''
taskid      : {t["id"]}
task        : {t["task"]}
created     : {t['created_at']}''')
                    if(t["updated_at"] != None):
                        print(f"last updated: {t["updated_at"]}")
                print("")
        else:
            for t in tasks.values():
                if(t["status"] == "in progress"):
                    print(f'''
taskid      : {t["id"]}
task        : {t["task"]}
created     : {t['created_at']}''')
                    if(t["updated_at"] != None):
                        print(f"last updated: {t["updated_at"]}")
                print("") 
    except Exception as e:
        print(f"An error occurred: {e}")

parser = argparse.ArgumentParser(description= "for todo")

subparser = parser.add_subparsers(dest = "command")

add_t = subparser.add_parser("add")
add_t.add_argument("task")

update_t = subparser.add_parser("update")
update_t.add_argument("id")
update_t.add_argument("task")

delete_t = subparser.add_parser("delete")
delete_t.add_argument("id")

mark_t = subparser.add_parser("mark")
mark_t.add_argument("id")
mark_t.add_argument("status")

list_t = subparser.add_parser("list")
list_t.add_argument("filter",nargs = '?')

args = parser.parse_args()

if(args.command == "add"):
    add(args.task)
elif(args.command == "update"):
    update(args.id, args.task)
elif(args.command == "delete"):
    delete(args.id)
elif(args.command == "mark"):
    i = 1 if (args.status == "done") else 2
    mark(args.id, i)
elif(args.command == "list"):
    i = 1 if(args.filter is None) else (2 if args.filter == "done" else 3)
    list_tasks(i)
else:
    print("INVALID COMMAND!!")


