#TO-DO app in terminal 
# Make it print "Welcome to your to-do app" *
#Let the user create a task 
#Save it to a list 
#Show the list 

#Add the time for the task
#Add the day for the task 


tasks = []

print('Welcome to your to-do app \n') 

task = input("Insert the task: ")
time = input("Insert the time: ")
date = input("insert the date: ")

task_info = {
    "task": task,
    "time": time,
    "date": date
}
tasks.append(task_info)

print("\nYour tasks:" )
for i in tasks:
    print(i)
