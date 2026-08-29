user_chores = ["fold clothes", "mop floors", "mow the lawn"]

counter = 1
while counter != 100:
    user_input = input("What would you like to do?\na:Show current task\nb:Add task\nc:Remove task\n")
    if user_input == "show current task":
        print(user_chores)      
    elif user_input == "Remove task":
        print(user_chores)
        remove_task = input("What task would you like to remove?\n")
        user_chores.remove(remove_task)
        print(user_chores)
    elif user_input == "Add task":
        add_task = input("What task would you like to add?\n")
        user_chores.append(add_task)
        print(user_chores)
    else:
        print("INPUT IS INVALID!")


