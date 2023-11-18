    
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
        self.prompt = (f"Generate a {self.mode} plan for a {self.age} year old {self.sex} with a height of {self.feet} feet and {self.inches} inches weighing {self.pounds} pounds.")

        
    def generate_workout_plan(self):
         print("What are your fitness goals? - (weightloss, strength, hypertropy)")
         fitness_goals  = input()
         print("On a scale of 1-5, What's your current fitness level?")
         fitness_level = int(input())
         print("What is your current exercise program?")
         current_program = input()
         print("How many days would you like to workout?")
         weekly_sessions = int(input())
         print("Will you be going to a gym or working out at home? \n If at home, please tell us what type of equipment you have access to.")
         eqpmnt_situation = input()


    def report_user_stats(self):
         print(self.prompt)

   
    

#Create methods for workout and diet to gather more refined info

def main():
   user_info = gather_info()
   new_user = User(user_info)
   new_user.report_user_stats()

   if new_user.mode.lower() == "workout":
        new_user.generate_workout_plan()
   elif new_user.mode.lower() == "diet":
        new_user.generate_diet_plan()





if __name__ == "__main__":
    main()