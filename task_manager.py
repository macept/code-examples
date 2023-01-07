#imports datetime for checking if things are overdue or not
from datetime import datetime

#note to hypdev code reviewer: I had a session with another hypdev code reviewer but we couldn't find any issues with the
#date time formatting, and the line numbers quoted with issues appeared different to us to the ones in which date time
#appears in the code. The only related issue I found was that when splitting the data up for checking the due date and assigned
#date had a logical error that led to them being displayed incorrectly in view mine, everything
#seems to be working now but please let me know if there's anything that needs changing and will be happy to resubmit again.

def reg_user():
    """Register new users.

    Runs while loop to check for errors. Only allows admin to add new users.
    Checks for existence of username in user list before accepting, returns error if there already.
    Adds password by double confirming and requires it to be 8 characters or longer.
    """
    # username registry variables
    new_password = ""
    confirm_new_passw = ""
    error = False
    while error == False:
        if username_input == "admin":
            new_username = input("Enter the new account name: ")
            with open("user.txt", "r") as f:
                for line_r in f:
                    split_users_pws = line_r.split(", ")
                    if new_username in split_users_pws[0::2]:
                        print("\nError, username already taken, please try again.")
                        error = True
                        break

            while error == False:
                new_password = input("Enter a password for the new account, minimum 8 characters: ")
                if len(new_password) >= 8:
                    confirm_new_passw = input("Enter your new password again to confirm: ")
                    break
                if new_password == confirm_new_passw:
                    break
                else:
                    print("Entry error, please try again.")
            while error == False:
                with open("user.txt", "a") as f:
                    f.write("\n" + new_username)
                    f.write(", " + new_password)
                    print("\nRegistration successful.")
                    error = True
                    break
        else:
            print("\nAdministrator account required to register new users.")
            break


def add_task():
    """function adds task

    Get all the information from user.  Use datetime to store the information correctly.  Then open the tasks file and
    appends it with the new task
    """
    while True:
        task_username = input("Who is the task assigned to? ")
        task_title = input("What is the title of the task? ")
        task_description = input("Please describe the task: ")
        task_due_date_string = str(input("When should the task be complete? (yyyy-mm-dd hh:mm) "))
        task_due_date = datetime.strptime(task_due_date_string, "%Y-%m-%d %H:%M")
        current_date_string = str(input("What is the current date? (yyyy-mm-dd hh:mm) "))
        current_date = datetime.strptime(current_date_string, "%Y-%m-%d %H:%M")
        with open("tasks.txt", "a") as u:
            u.write(f"\n{task_username}, {task_title}, {task_description}, {task_due_date}, {current_date}, {task_completion}")
        print("\nTask input successful.")
        break

def view_all():
    """function prints all task information

    for loop goes through each stored task and uses data list variable to print it
    """
    with open("tasks.txt", "r") as g:
        for line in g:
            data_list = line.split(", ")
            print("Task Title:         " + data_list[1])
            print("Task Description:   " + data_list[2])
            print("Task Assigned to:   " + data_list[0])
            print("Task Date Assigned: " + data_list[3])
            print("Task Due Date:      " + data_list[4])
            print("Task Complete?:     " + data_list[5])


def view_mine():
    """views user tasks and gives option to edit

    Reads task information from file and prints it on screen using data list variable.
    While loop to get choice from user to edit task or go back to main menu.
    If numbered choice is made, task is reprinted to allow user to view and gives options for modification.
    If 1 is chosen, the task is marked as complete and everything is rewritten into the tasks.txt file
    If 2 is chosen, checks if task is already complete. If so, gives error message and breaks loop, refusing to edit.
    Otherwise, it will then ask for a new date using datetime and replace what's in the original task information before then
    writing all the data back to file.
    If 3 is chosen, checks if task already complete, if so gives error message and breaks loop, refusing to edit. If not,
    it asks for new user information, compiles it with current task information and saves it back in the file.
    """
    view_mine_task_count = 0
    with open("tasks.txt", "r") as g:
        all_data = g.readlines()
        for line in all_data:
            data_list = line.split(",")
            if data_list[0] == username_input:
                view_mine_task_count += 1
                print("\nTask number:         " + str(view_mine_task_count))
                print("Task Title:         " + data_list[1])
                print("Task Description:   " + data_list[2])
                print("Task Assigned to:    " + data_list[0])
                print("Task Date Assigned: " + data_list[4])
                print("Task Due Date:      " + data_list[3])
                print("Task Complete?:     " + data_list[5])

    while True:
        edit_decision = int(input("\nSelect a task number to edit a task or -1 to return to main menu: "))
        if edit_decision == -1:
            break
        else:
            view_mine_task_count = 0
            index_count: int = -1
            with open("tasks.txt", "r") as g:
                all_data = g.readlines()
                for line in all_data:
                    index_count += 1
                    data_list = line.split(", ")
                    if data_list[0] == username_input:
                        view_mine_task_count += 1
                        if edit_decision == view_mine_task_count:
                            print("\nTask number:        " + str(view_mine_task_count))
                            print("Task Title:         " + data_list[1])
                            print("Task Description:   " + data_list[2])
                            print("Task Assigned to:   " + data_list[0])
                            print("Task Date Assigned: " + data_list[3])
                            print("Task Due Date:      " + data_list[4])
                            print("Task Complete?:     " + data_list[5])
                            edit_or_complete = int(input("\nWould you like to 1) mark task as complete, 2) edit due date, or 3) edit task assignment? Enter a number: "))
                            if edit_or_complete == 1 and edit_decision == view_mine_task_count:
                                with open("tasks.txt", "w") as g:
                                    all_data[index_count] = line.replace("No", "Yes")
                                    all_data_string = "".join(all_data)
                                    g.write(str(all_data_string))

                            elif edit_or_complete == 2 and edit_decision == view_mine_task_count:
                                while True:
                                    if data_list[5] == "Yes":
                                        print("Task already complete, unable to edit.")
                                        break
                                    else:
                                        with open("tasks.txt", "w") as g:
                                            date_replace_string = str(input("Enter the new date you would like to record (yyyy-mm-dd hh:mm): "))
                                            date_replace = datetime.strptime(date_replace_string, "%Y-%m-%d %H:%M")
                                            date_replace_string_two = str(date_replace)
                                            data_list[3] = date_replace_string_two
                                            data_list_string = ", ".join(data_list)
                                            all_data[index_count] = data_list_string
                                            all_data_string = "".join(all_data)
                                            g.write(all_data_string)
                                            break

                            elif edit_or_complete == 3 and edit_decision == view_mine_task_count:
                                while True:
                                    with open("tasks.txt", "w") as g:
                                        if data_list[5] == "Yes":
                                            print("Task already complete, unable to edit.")
                                            break
                                        else:
                                            user_replace = input("Enter the user you want to reassign the task to: ")
                                            data_list[0] = user_replace
                                            data_list_string = ", ".join(data_list)
                                            all_data[index_count] = data_list_string
                                            all_data_string = "".join(all_data)
                                            g.write(all_data_string)
                                            edit_decision = -1
                                            break
                        else:
                            continue

def tasks_to_user(username):
    """Gets total number of tasks assigned to user for use by program.

    Adds up tasks per user and returns the name and amount for use in other functions
    """
    task_count_for_user = 0
    with open("tasks.txt", "r") as t:
        for line in t:
            task_data_list = line.split(", ")
            if username == task_data_list[0]:
                task_count_for_user += 1
    return username, task_count_for_user

def print_tasks_to_user(username):
    """Gets total number of tasks assigned to user and returns string for user to view.

    Adds up tasks per user and returns the name and amount for use in printing to file for user
    """
    task_count_for_user = 0
    with open("tasks.txt", "r") as t:
        for line in t:
            task_data_list = line.split(", ")
            if username == task_data_list[0]:
                task_count_for_user += 1
    return f"{username} has a total number of {task_count_for_user} tasks."

def user_and_task_data():
    """Counts all users and tasks

    Opens both storage files and counts the number of things in there to return info to program
    """
    all_tasks = 0
    all_users = 0
    with open("user.txt", "r") as b:
        for the_lines in b:
            all_users += 1
    with open("tasks.txt", "r") as o:
        for a_line in o:
            all_tasks += 1
    print(all_tasks)
    print(all_users)
    return f"The total number of tasks is {all_tasks} and total users is {all_users}.\n"

def completion_analysis(username):
    """Calculates percentages of complete and incomplete tasks

    Goes through tasks file and checks if tasks are complete or not for username, adds up how many of each and then
    performs calculation to get number. To avoid division by 0 an elif statement is used to give the percentage
    value of zero if the user has no tasks. Returns print statement with information.
    """
    incomplete_tasks = 0
    completed_tasks = 0
    user_percent_complete_tasks = 0
    user_percent_incomplete_tasks = 0
    with open("tasks.txt", "r") as g:
        for line in g:
            data_list = line.split(", ")
            if username == data_list[0]:
                if "Yes" in data_list[5]:
                    completed_tasks += 1
                elif "No" in data_list[5]:
                    incomplete_tasks += 1
            total_num_tasks = completed_tasks + incomplete_tasks
            if incomplete_tasks != 0:
                user_percent_incomplete_tasks: float = incomplete_tasks / total_num_tasks * 100
                user_percent_complete_tasks = completed_tasks / total_num_tasks * 100
            elif incomplete_tasks == 0:
                user_percent_incomplete_tasks = 0.00
                user_percent_complete_tasks = 100
    return f"{username} has {round(user_percent_complete_tasks, 2)}% task completion, {round(user_percent_incomplete_tasks, 2)}% incomplete tasks."

def count_individual_user_tasks(username):
    """Calculates number of tasks one user has

    Checks how many tasks an individual has by splitting up the data in list and counting them up
    """
    with open("tasks.txt", "r") as g:
        with open("user.txt", "r") as h:
            for user_info in h:
                tasks_of_individual_user = 0
                user_data_list = user_info.split(", ")
                if username == user_data_list[0]:
                    for task_info in g:
                        task_data_list = task_info.split(", ")
                        if task_data_list[0] == username:
                            tasks_of_individual_user += 1
                return tasks_of_individual_user


def overdue_analysis(username):
    """Gets percentage of a users tasks that are overdue or not

    Gets data from tasks and checks the times of them against current time. They are then counted into variables
    above the for statement and finally calculated based on these variables at the bottom of the function. An elif
    statement is used in case it ends up being 0 to avoid division by 0. Then returns statement to be written
    to text file for user viewing
    """
    overdue_tasks = 0
    non_overdue_tasks = 0
    incomplete_overdue = 0
    with open("tasks.txt", "r") as g:
        for line in g:
            data_list = line.split(", ")
            current_time: datetime = datetime.now()
            due_date_string_check = str(data_list[3])
            due_date: datetime = datetime.strptime(due_date_string_check, "%Y-%m-%d %H:%M:%S")
            if username == data_list[0]:
                if current_time > due_date:
                    overdue_tasks += 1
                    if "No" in data_list[5]:
                        incomplete_overdue += 1
                elif due_date > current_time:
                    non_overdue_tasks += 1
        total_num_tasks = tasks_to_user(username)
        user_percent_overdue_tasks = 0
        if overdue_tasks != 0:
            user_percent_overdue_tasks = incomplete_overdue / total_num_tasks[1] * 100
        elif overdue_tasks == 0:
            user_percent_overdue_tasks = 0
    return f"{username} has {round(user_percent_overdue_tasks, 2)}% tasks overdue."


def percentages_tasks_all(username):
    """Works out what percentage of total tasks have been assigned to one user

    checks username against asks in file and records those that are assigned to username sent to function and those
    that are not. Then performs calculation and returns a sentence for writing to text file.
    """
    with open("tasks.txt", "r") as y:
        total_tasks = 0
        user_tasks = 0
        for line in y:
            total_tasks += 1
            data_for_percent = line.split(", ")
            if data_for_percent[0] == username:
                user_tasks += 1
        percentage_user_tasks = user_tasks / total_tasks * 100
        return f"{username} has been assigned {round(percentage_user_tasks, 2)}% of all tasks."

def generate_reports():
    """Generates reports for all information in program

    First collects data of all complete and incomplete tasks from tasks.txt and performs percentage calculation.
    Then collects data for all overdue, non-overdue, and incomplete-overdue tasks from tasks.txt and performs
    percentage calculations, with elif statement to avoid division by zero.
    Then opens and writes all gathered information to task_overview.txt using f statements.
    Finally calls other functions from program and collects the information there into variables, converts them to writable
    strings (variable names are shortened to acronyms with string) and then writes them to file.
    """
    incomplete_tasks = 0
    completed_tasks = 0
    if username_input == "admin":
        with open("tasks.txt", "r") as g:
            for line in g:
                data_list = line.split(", ")
                if "Yes" in data_list[5]:
                    completed_tasks += 1
                elif "No" in data_list[5]:
                    incomplete_tasks += 1
            total_num_tasks = completed_tasks + incomplete_tasks
            if incomplete_tasks != 0:
                percent_incomplete_tasks = incomplete_tasks / total_num_tasks * 100
        with open("tasks.txt", "r") as g:
            overdue_tasks = 0
            non_overdue_tasks = 0
            incomplete_overdue = 0
            for line in g:
                data_list = line.split(", ")
                current_time: datetime = datetime.now()
                due_date_string_check = str(data_list[4])
                due_date: datetime = datetime.strptime(due_date_string_check, "%Y-%m-%d %H:%M:%S")
                if current_time > due_date:
                    overdue_tasks += 1
                    if "No" in data_list[5]:
                        incomplete_overdue += 1
                elif due_date > current_time:
                    non_overdue_tasks += 1
            if overdue_tasks != 0:
                percent_overdue_tasks = overdue_tasks / total_num_tasks * 100
            elif overdue_tasks == 0:
                percent_overdue_tasks = 0
            with open("task_overview.txt", "w") as f:
                f.write(f"The total number of tasks generated and tracked is {total_num_tasks}."
                        f"\nThe total number of completed tasks is {completed_tasks}."
                        f"\nThe total number of uncompleted tasks is {incomplete_tasks}."
                        f"\nThe total number of uncompleted overdue tasks is {incomplete_overdue}."
                        f"\nThe percentage of incomplete tasks is {round(percent_incomplete_tasks, 2)} percent."
                        f"\nThe percentage of overdue tasks is {round(percent_overdue_tasks, 2)} percent.")
        with open("user.txt", "r") as u:
            with open("user_overview.txt", "w") as w:
                user_count = 0
                uat_string = user_and_task_data()
                w.write(uat_string + "\n")
                for line in u:
                    user_count += 1
                    user_data_list = line.split(", ")
                    username = user_data_list[0]
                    ptty_string = print_tasks_to_user(username) + "\n"
                    pta_string = (percentages_tasks_all(username)) + "\n"
                    ca_string = completion_analysis(username) + "\n"
                    oa_string = overdue_analysis(username) + "\n\n"
                    w.write(ptty_string)
                    w.write(pta_string)
                    w.write(ca_string)
                    w.write(oa_string)

def display_statistics():
    """
    Displays reports on screen for user.

    Calls generate reports function to update text files with latest information, then prints them line by line to screen
    for user to view.
    """
    generate_reports()
    with open("user_overview.txt", "r") as uo:
        for line in uo:
            print(line)
    with open("task_overview.txt", "r") as uo:
        for line in uo:
            print(line)

#====Login Section====
user_entry_data = []
login_success = False

#log in variables
username_input = ""
password_input = ""

#task assignment variables
task_username = ""
task_title = ""
task_description = ""
task_due_date = ""
current_date = ""
task_completion = "No"

#statistics variables
user_count = 0
task_count = 0
tasks_created = 0
completed_tasks = 0
incomplete_tasks = 0

#log in section for user, checks username and password in same line in text file
while login_success == False:
    username_input = (input("Please enter your username: "))
    password_input = (input("Please enter your password: "))
    with open("user.txt", "r") as user_entry_data:
        for line in user_entry_data:
            if username_input in line and password_input in line:
                login_success = True
                print("\nLogin success!")
                break
        else:
            print("Incorrect username or password, please try again.")

#presenting the menu to the user and making sure that the user input is converted to lower case.
while True:
    menu = input('''\nSelect one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
ds - display program statistics
gr - generate reports
e - Exit
: ''').lower()

    #if statement to control menu
    if menu == 'r':
        #registering new users protected by username check for admin, writes to text file after password check
        reg_user()

    #gets info about tasks and saves in text file
    elif menu == 'a':
        add_task()
        tasks_created += 1

    #calls view all function
    elif menu == 'va':
        view_all()

    #views user tasks based on checking name against names of tasks in text file
    elif menu == 'vm':
        view_mine()

    #Calls generate reports function
    elif menu == 'gr':
        generate_reports()

    #checks if user is admin, if so generates and displays report info, else prints admin required
    elif menu == 'ds':
        if username_input == "admin":
            display_statistics()
        else:
            print("\nAdministrator account required to view statistics.\n")

    #ends program if e is entered
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    #sends error message if one of menu options is not chosen
    else:
        print("You have made a wrong choice, please try again")