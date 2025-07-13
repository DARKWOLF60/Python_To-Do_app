#TO-DO app in terminal:

#Possibility to delete/complete the task 

tasks = []
print("Welcome to your to-do app \n ") 

while True:

    response = input("\nDo you want to 'add' (a), 'visualize' (v), 'complete' (c) or 'exit' (e)? ").lower()

    if response in ['a', 'add']:

        task = input("Insert the task: ")
        time = input("Insert the time: ")
        date = input("insert the date: ")

        task_info = {
          "task": task,
            "time": time,
        "date": date
        }
        tasks.append(task_info)

    elif response in ['v', 'visualize']: 
        if tasks:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task['task']} at {task['time']} on {task['date']}")
        else:
             print("No tasks yet.")

    elif response in ['c', 'complete']:
        
        if tasks:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task['task']} at {task['time']} on {task['date']}")
            d_task = int(input('which task do you want to mark as complete? (number) \n'))
            del tasks[d_task - 1] 
                
        else:
             print("No tasks yet.")


    elif response in ['e', 'exit']:
        print("Goodbye!")
        break

    else:
        print("Please answer with: 'a' to add, 'v' to view, or 'e' to exit.")
