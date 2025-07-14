tasks=[]
while True:
    print("\n===== TO-DO LIST =====")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Quit")
    choice=int(input("Select an option:(1-5)"))

    if choice==1:
        if tasks==[]:
            print("No tasks yet!!")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not done"
                print(f"{i + 1}. {task['task']} [{status}]")
    elif choice == 2:
        new_task = input("Enter the task: ")
        tasks.append({"task": new_task, "done": False})
        print("Task added!")

    elif choice == 3:
        if not tasks:
            print("No tasks to mark done!")
        else:
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task['task']}")
            num = int(input("Enter the task number to mark done: "))
            if 1 <= num <= len(tasks):
                tasks[num - 1]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid number.")

    elif choice == 4:
        if not tasks:
            print("No tasks to delete!")
        else:
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task['task']}")
            num = int(input("Enter the task number to delete: "))
            if 1 <= num <= len(tasks):
                deleted = tasks.pop(num - 1)
                print(f"Deleted task: {deleted['task']}")
            else:
                print("Invalid number.")

    elif choice == 5:
        print("Goodbye!")
        break

    else:
        print("Please choose a valid option (1-5).")