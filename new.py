tasks = []

while True:
    print("\n1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

    elif choice == "2":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

            num = int(input("Task number to delete: "))
            tasks.pop(num - 1)
            print("Task deleted!")
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Enter a number from 1 to 4.")

