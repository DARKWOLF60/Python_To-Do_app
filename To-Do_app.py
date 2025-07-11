#TO-DO app in terminal:
# Make it print "Welcome to your to-do app" *
#Let the user create a task 
#Save it to a list *
#Show the list *

#Add the time for the task *
#Add the day for the task *


tasks = []

print("Welcome to your to-do app \n ") 


while True:

    response = input("\nDo you want to 'add' (a), 'visualize' (v), or 'exit' (e)? ").lower()

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
         print("\nYour tasks:" )
         for i in tasks:
            print(i)

    elif response in ['e', 'exit']:
        print("Goodbye!")
        break

    else:
        print("Please answer with: 'a' to add, 'v' to view, or 'e' to exit.")
