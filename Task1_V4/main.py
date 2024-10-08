from Task1_V4 import UsersManager, User
from enum import Enum
import time

class UserState(Enum):
    LOGGED_OUT = 0
    LOGGED_IN = 1

class UserSession:
    __users_manager = UsersManager()

    def __init__(self):
        self.user = User()
        self.state = UserState.LOGGED_OUT

    def __prompt_menu(self):
        if self.state == UserState.LOGGED_OUT:
            print("1. Register")
            print("2. Login")
            print("3. Exit")
        elif self.state == UserState.LOGGED_IN:
            print("1. Add task")
            print("2. View all tasks")
            print("3. View completed tasks")
            print("4. View uncompleted tasks")
            print("5. Remove task")
            print("6. Complete task")
            print("7. Uncomplete task")
            print("8. Dump user to file")
            print("9. Logout")
            print("10. Exit")
        option = input("Enter option: ")
        print()
        return option

    def __register(self):
        name = input("Enter name: ")
        UserSession.__users_manager.add_user(name)
        self.user = UserSession.__users_manager.get_user(name)
        self.state = UserState.LOGGED_IN

    def __login(self):
        name = input("Enter name: ")
        self.user = UserSession.__users_manager.get_user(name)
        self.state = UserState.LOGGED_IN

    def __add_task(self, date=time.strftime("%Y-%m-%d")):
        data = {
            "title": input("Enter title: "),
            "description": input("Enter description: ")
        }
        date = time.strftime("%Y-%m-%d")
        self.user.add_task(data, date)
    
    def __remove_task(self):
        task_id = int(input("Enter task id: "))
        self.user.remove_task(task_id)

    def __complete_task(self):
        task_id = int(input("Enter task id: "))
        self.user.complete_task(task_id)

    def __uncomplete_task(self):
        task_id = int(input("Enter task id: "))
        self.user.uncomplete_task(task_id)

    def __dump(self):
        file_path = input("Enter file path: ")
        self.user.dump(f"{file_path}")

    def __logout(self):
        self.user = User()
        self.state = UserState.LOGGED_OUT
    
    def run(self):
        while True:
            try:
                if self.state == UserState.LOGGED_OUT:
                    option = self.__prompt_menu()
                    if option == "1":
                        self.__register()
                    elif option == "2":
                        self.__login()
                    elif option == "3":
                        break
                    else:
                        print("Invalid option")

                elif self.state == UserState.LOGGED_IN:
                    option = self.__prompt_menu()
                    if option == "1":
                        self.__add_task()
                    elif option == "2":
                        print("\n".join([str(i) for i in self.user.all_tasks()]) 
                              if len(self.user.all_tasks()) != 0 else "No tasks")
                    elif option == "3":
                        print("\n".join([str(i) for i in self.user.completed_tasks()])
                              if len(self.user.completed_tasks()) != 0 else "No tasks")
                    elif option == "4":
                        print("\n".join([str(i) for i in self.user.uncompleted_tasks()])
                              if len(self.user.uncompleted_tasks()) != 0 else "No tasks")
                    elif option == "5":
                        self.__remove_task()
                    elif option == "6":
                        self.__complete_task()
                    elif option == "7":
                        self.__uncomplete_task()
                    elif option == "8":
                        self.__dump()
                    elif option == "9":
                        self.__logout()
                        continue
                    elif option == "10":
                        break
                    else:
                        print("Invalid option")
            except ValueError as e:
                print("Error occurred:", e)

            print()


if __name__ == "__main__":
    app = UserSession()
    app.run()
