#TO-DO app in terminal:
#Possibility to delete/complete the task 

import json
import os   


#function to save tasks 
def save_task():
    with open ("tasks.json", "w") as file: #opens the file in write mode
        json.dump(tasks, file) #saves the file with the dump function 


print("Welcome to your to-do app \n ") 

# Check if the file exists and is not empty, then load it
if os.path.exists("tasks.json") and os.path.getsize("tasks.json") > 0:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
else: 
    tasks = []


#main code
while True:

    response = input("\nDo you want to 'add' (a), 'visualize' (v), 'complete' (c), 'delete' (d) or 'exit' (e)? ").lower() #lower function to make the string (letter) lowercase

    if response in ['a', 'add']:

        task = input("Insert the task: ")
        time = input("Insert the time: ")
        date = input("insert the date: ")

        task_info = {
            "task": task,
            "time": time,
            "date": date,
            "completed" : False 
        }
        tasks.append(task_info) #append = list method to add an item at the end of the list 
        save_task()

    elif response in ['v', 'visualize']: 
        if tasks:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                 status = "Completed" if task.get("completed") else "Not Completed" #shows the status of the task
                 print(f"{i}. {task['task']} at {task['time']} on {task['date']} - {status}")
        else:
             print("No tasks yet.")

    elif response in ['c', 'complete']:
        
        if tasks:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task['task']} at {task['time']} on {task['date']}")
            d_task = int(input('which task do you want to mark as complete? (number) or mark all (0)\n'))

            if (d_task == 0 ):
                print("All the tasks are marked as completed! \n")
                for task in tasks :
                    task["completed"] = True
                    save_task() 
                    
            else:
                del tasks[d_task - 1] 
                save_task()
                
        else:
             print("No tasks yet.")


    elif response in ['e', 'exit']:
        print("Goodbye!")
        break

    else:
        print("Please answer with: 'a' to add, 'v' to view, or 'e' to exit.")
