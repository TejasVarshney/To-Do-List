def reset() :
    global current_task
    global total_task

    file = open("Task.txt", "r")

    current_task = ["Nothing", "Nothing", "Nothing", "Nothing", "Nothing"]
    total_task = 5
    tsk = file.readlines()
    print(tsk)

    for i in range (0, total_task) :
        current_task[i] = tsk[i][0:len(tsk[i])-1]

    file.close()

def setTask(index, task) :
    current_task[index] = task


def getTask(index) :
    if(index < 5) :
        return str(current_task[index])
    else :
        return "None"

def totalTask() :
    c = 0
    for i in range(0, 5) :
        if current_task[i] != "Nothing" and current_task[i] != "DONE" :
            c+=1
    return c

def Done(index) :
    if(current_task[index] != "Nothing") :
        current_task[index] = "DONE"
        return False

    else :
        return True

def Saving() :
    file = open("Task.txt", "w")
    for i in range(0, 5) :
        if(current_task[i] == "DONE") :
            current_task[i] = "Nothing"
        file.writelines(current_task[i] + "\n")

    file.close()
