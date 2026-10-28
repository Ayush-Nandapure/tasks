import argparse
import datetime



tasks = {}
taskscount = 0

def add(t):
    global taskscount
    taskscount+=1
    t1 = {
        "id" : taskscount,
        "status" : "created",
        "task" : t,
        "created_at": datetime.datetime.now(),
        "updated_at" : None
    }
    tasks[t1["id"]] = t1

def update(id, t):
    if id in tasks:
        tasks[id]["task"] = t
        tasks[id]["updated_at"] = datetime.datetime.now()


def delete(id):
    if id in tasks:
        tasks.pop(id) 

def mark(id, i):
    if id in tasks:
        if(i == 1):
            tasks[id]["status"] = "done"
        elif(i == 2):
            tasks[id]["status"] = "in progress"
        tasks[id]["updated_at"] = datetime.datetime.now()


def list_tasks(i):
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
        for t in tasks:
            if(t["status"] == "done"):
                print(f'''
    taskid      : {t["id"]}
    task        : {t["task"]}
    created     : {t['created_at']}
    ''')
                if(t["updated"] != None):
                    print(f"last updated: {t["updated_at"]}")
                print("")
    else:
        for t in tasks:
            if(t["status"] == "in progress"):
                print(f'''
    taskid      : {t["id"]}
    task        : {t["task"]}
    created     : {t['created_at']}
    ''')
                if(t["updated"] != None):
                    print(f"last updated: {t["updated_at"]}")
                print("") 


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
