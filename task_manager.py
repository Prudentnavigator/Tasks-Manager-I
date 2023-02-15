# Lesson SE-T21
# Task CapstoneProject II - Files


# task_manager.py--a program for a small business that manages tasks
#                  assigned to each member of the team.


#=====importing libraries===========

import datetime


#====Login Section====

print()

while True:
    user_name = input("\t\t\tPlease enter your username: ")
    user_passwd = input("\t\t\tPlease enter your password: ")

    # Open user.txt file and until username and password entered match one of the
    #   username  and corresponding password in the file, keep requesting to login.
    # Once there is match, quit loop.

    with open('user.txt', 'r') as user_data:
        u_name = ""
        passwd = ""
        for line in user_data:
            user_credentials = line.split(",")
            for name in user_credentials[ :1]:
                if user_name == name:
                    u_name = name 
                    for passw in user_credentials[1: ]:
                        passwd = passw.strip()
    
    if user_name == u_name and user_passwd == passwd:
        break


#====Menu Section====

# Presenting the menu to the user and  making sure that
#   the user input is converted to lower case.

while True:
        
    if user_name == "admin":
        menu = input('''
                            Admin-menu

                        Select one of the following Options below:
                
                        r - Registering a user
                        a - Adding a task
                        va - View all tasks
                        vm - view my task
                        s - Display user and task statistics
                        e - Exit
                        :  ''').lower()

    else:
        menu = input('''
                        Select one of the following Options below:
                
                        r - Registering a user
                        a - Adding a task
                        va - View all tasks
                        vm - view my task
                        e - Exit
                        :  ''').lower()


#====Compute Selected====

    # Add a new user to the user.txt file

    if menu == 'r':

        # Check if user has permission to add a new user and request new user data.

        if user_name == "admin" :
            new_user = input("\n\t\t\tPlease enter a username for the new user: ")
            while True:
                new_passwd = input("\n\t\t\tPlease enter a password: ")
                repeat_passwd = input("\n\t\t\tConfirm password: ")
            
                # Check if the provided password matches the confirmed password

                if new_passwd == repeat_passwd:
                    passwd = new_passwd

                    # If passwords match, append data of the added user to the user.txt file.

                    with open("user.txt", "a") as user_data: 
                        user_data.write( new_user + ", " + passwd + "\n")
                        break

                # If passwords do not match, print an error message and request 
                #   the user to enter the passwords again.

                else:
                    print("\n\t\t\t***Passwords do not match!***\n")

        else:
            print("\n\t\t\t***Must be an administrative user in order to add new users!***\n")


    # Add a new task to tasks.txt file

    elif menu == 'a':
        
        # Get todays date from the datetime module and convert to 
        #   desired date format.

        date_today = datetime.date.today()
        current_date = date_today.strftime("%d %b %Y")

        # Request the user to enter data of the new task.

        assign_user = input("\n\t\t\tPlease enter the user you wish to assign the task to: ")
        task = input("\t\t\tPlease enter the title of the task: ")
        description = input("\t\t\tEnter a description of the task: ")
        due_date = input("\t\t\tWhen is the task due (i.e. 20 Mar 2024): ")
        assign_date = current_date
        completion = "No"

        # Append data to tasks.txt file.

        with open("tasks.txt", "a") as user_tasks:
            first_part = (f"{assign_user}, {task}, {description},") 
            second_part= (f" {assign_date}, {due_date}, {completion}" ) 
            user_tasks.write( first_part + second_part + "\n")


    # Read the tasks from tasks.txt file and print *all tasks* to the console in the 
    #   format of Output 2 in the task PDF(i.e. include spacing and labelling).

    elif menu == 'va':
        
        with open('tasks.txt', 'r') as user_tasks:
            for line in user_tasks:
                line = line.split(",")
                for value in line[1:2]:
                    task = value 
                for name in line[:1]:
                    user = name 
                for date in line[3:4]:
                    assign_date = date 
                for due in line[4:5]:
                    due_date = due 
                for status in line[5:6]:
                    completion = status
                for value in line[2:3]:
                    description = value

                print(f"""

                _______________________________________________________________


                        Task:                           {task}
                        Assigned to:                     {user}
                        Assign date:                    {assign_date}
                        Due date:                       {due_date}
                        Task Complete?                  {completion}
                        Task description:   
                         {description[0:50]}
                          {description[50:100]}
                           {description[100:150]}
                _______________________________________________________________

                """)


    # Read the tasks from tasks.txt file and print the *users tasks* to the console in the 
    #   format of Output 2 in the task PDF(i.e. include spacing and labelling)

    elif menu == 'vm':
                 
        with open("tasks.txt", "r") as user_tasks:
            for line in user_tasks:
                line = line.split(",")
                for name in line[:1]:
                    if user_name == name: 
                        user = user_name 
                        for value in line[1:2]:
                            task = value 
                        for date in line[3:4]:
                            assign_date = date 
                        for due in line[4:5]:
                            due_date = due 
                        for status in line[5:6]:
                            completion = status
                        for value in line[2:3]:
                            description = value

                        print(f"""

                _______________________________________________________________


                        Task:                           {task}
                        Assigned to:                     {user}
                        Assign date:                    {assign_date}
                        Due date:                       {due_date}
                        Task Complete?                  {completion}
                        Task description:   
                         {description[0:50]}
                          {description[50:100]}
                           {description[100:150]}
                _______________________________________________________________

                """)


    # Compute and display user and tasks statistics.
    # This option is only available for admin users.

    elif menu == "s":

        if user_name == "admin":

            with open("user.txt", "r") as users:
                user_count = 0
                for user in users:
                    user_count +=1    

            with open("tasks.txt", "r") as tasks:
                task_count = 0
                for task in tasks:
                    task_count += 1 

                print(f"""


                _______________________________________________________________


                            *** User and tasks statistics ***


                        Total Tasks:                        {task_count}             
                        Total Users:                        {user_count} 

                _______________________________________________________________

            """)


    # Option to exit the program

    elif menu == 'e':
        print('\n\t\t\tGoodbye!!!\n')
        exit()

    # When selected is not in the menu, display an error message.

    else:
        print("\n\t\t\t***You have made a wrong choice, Please Try again***\n")


