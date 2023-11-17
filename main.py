    
def gather_info():
        print("What is your name?")
        name = input()
        print("What is your gender?")
        sex = input()
        print("Next we will ask your height, please reply in feet and inches")
        print("How many feet tall?")
        feet = int(input())
        print("Inches?")
        inches = int(input())
        print("What is your weight in pounds?")
        pounds = int(input())
        print("How old are you?")
        age = int(input())
        #diet or workout
        print("Would you like a *diet* or a *workout* plan generated?")
        select_mode = input()

        return {
        "name": name,
        "sex": sex,
        "feet": feet,
        "inches": inches,
        "pounds": pounds,
        "age": age,
        "mode" : select_mode
    }

class User:
    def __init__(self, user_info):
        self.sex = user_info["sex"]
        self.feet = user_info["feet"]
        self.inches = user_info["inches"]
        self.pounds = user_info["pounds"]
        self.age = user_info["age"]
        self.mode = user_info["mode"]
    
    def user_stats(self):
         print(f"Generate a {self.mode} plan for a {self.age} year old {self.sex} with a height of {self.feet} feet and {self.inches} inches weighing {self.pounds} pounds.")
    

#Create methods for workout and diet to gather more refined info

def main():
   user_info = gather_info()
   new_user = User(user_info)
   new_user.user_stats()




if __name__ == "__main__":
    main()