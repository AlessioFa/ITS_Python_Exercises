""" User: stores first_name, last_name, username, and email; includes describe_user() and greet_user() methods.
    Privileges: holds a list of privileges and a method show_privileges() to display them.
    Admin: stores a User instance and a Privileges instance as attributes.
"""

class User:
    def __init__(self, first_name: str, last_name: str, username: str, email: str):
        """Initialize the user's personal infotmation"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
    
    def describe_user(self) -> None:
        """Display the user's detail"""
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"E-mail: {self.email}")


class Privileges:
    def __init__(self, privileges: list[str]):
        """Display the user's privileges"""
        self.privileges = privileges
    
    def show_privileges(self) -> list[str]:
        if self.privileges:
            print("This user has the following privileges:\n")
            for privilege in self.privileges:
                print(f"-{privilege}")
        else:
            print("This user has no privileges.")


class Admin:
    def __init__(self,user: User, privileges: Privileges):
        """Initialize the admin with user information and proivileges"""
        self.user = user
        self.privileges = privileges

    def describe_user    

    
            
            




