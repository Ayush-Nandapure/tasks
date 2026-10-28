import argparse
import datetime
import json




taskscount = 0

def add(t):
    global taskscount
    taskscount+=1
    t1 = {
    "id" : taskscount,
    "status" : "created",
    "task" : t,
    "created_at": str(datetime.datetime.now()),
    "updated_at" : None
    }
    with open("task.json", "r") as f:
        tasks = json.load(f)
        tasks[t1["id"]] = t1
        with open("task.json") as f1:
            json.dump(tasks, f1, indent = 4)


def update(id, t):
    try:
        with open("task.json", "r") as f:
            tasks = json.load(f)
        if str(id) in tasks:
            tasks[id]["task"] = t
            tasks[id]["updated_at"] = str(datetime.datetime.now())
            with open("task.json", "w") as f1:
                json.dump(tasks, f1, indent = 4)
    except FileNotFoundError:
        print("No tasks")


def delete(id):
    try:
        with open("task.json", "r") as f:
            tasks = json.load(f)
        if str(id) in tasks:
            tasks.pop(id) 
            with open("task.json", "w") as f1:
                json.dump(tasks, f1, indent = 4)
    except FileNotFoundError:
        print("No tasks")

def mark(id, i):
    try:
        with open("task.json", "r") as f:
            tasks = json.load(f)
        if str(id) in tasks:
            if(i == 1):
                tasks[id]["status"] = "done"
            elif(i == 2):
                tasks[id]["status"] = "in progress"
            tasks[id]["updated_at"] = str(datetime.datetime.now())

            with open("task.json", "w") as f1:
                json.dump(tasks, f1, indent = 4)
    except FileNotFoundError:
        print("No tasks")


def list_tasks(i):
    try:
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
    created     : {t['created_at']}
    ''')
                if(t["updated_at"] != None):
                    print(f"last updated: {t["updated_at"]}")
                print("")
        elif(i == 2):
            for t in tasks.values():
                if(t["status"] == "done"):
                    print(f'''
    taskid      : {t["id"]}
    task        : {t["task"]}
    created     : {t['created_at']}
    ''')
                    if(t["updated_at"] != None):
                        print(f"last updated: {t["updated_at"]}")
                print("")
        else:
            for t in tasks.values():
                if(t["status"] == "in progress"):
                    print(f'''
    taskid      : {t["id"]}
    task        : {t["task"]}
    created     : {t['created_at']}
    ''')
                if(t["updated_at"] != None):
                    print(f"last updated: {t["updated_at"]}")
                print("") 
    except FileNotFoundError:
        print("No tasks")


if __name__ == "__main__" :
    add("complete assignment")
    list_tasks(1)
    update(1, "complete pns")
    list_tasks(1)
    mark(1, 2)
    list_tasks(1)
    mark(1,1)
    list_tasks(1)
    delete(1)
    list_tasks(1)
