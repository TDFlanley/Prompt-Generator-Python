    
def gather_info():
        name = input("What is your name?\n")
        sex = input("What is your gender?\n")
        print("Height collection is next, please reply in feet and inches")
        feet = int(input("How many feet tall?\n"))
        inches = int(input("Inches?\n"))
        pounds = int(input("What is your weight in pounds?\n"))
        age = int(input("How old are you?\n"))
        #diet or workout
        select_mode = input("Would you like a *diet* or a *workout* plan generated?\n")

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
        self.prompt = (f"Generate a weekly {self.mode} plan for a {self.age} year old {self.sex} with a height of {self.feet} feet and {self.inches} inches weighing {self.pounds} pounds. ")

        
    def generate_workout_plan(self):
         fitness_goals  = input("What are your fitness goals? - (weightloss, strength, hypertropy)\n")
         fitness_level = int(input("On a scale of 1-5, What's your current fitness level?\n"))
         current_program = input("What is your current exercise program?\n")
         weekly_sessions = int(input("How many days would you like to workout?\n"))
         eqpmnt_situation = input("Will you be going to a gym or working out at home? \nIf at home, please tell us what type of equipment you have access to.\n")

         self.prompt += f"Current fitness goal is {fitness_goals}, current fitness level (on a scale of 1-5) is {fitness_level}, current exercise regimen is {current_program}.\n"
         self.prompt += f"Workouts should take place {weekly_sessions} days a week. Equipment that will be used: {eqpmnt_situation}."

    def generate_diet_plan(self):
         diet_restrictions = input("Do you have any dietary restrictions?\n")
         diet_goals = input("Dietary Goals (increase protein, lower sugar, go keto, encourage weight loss)\n")
         ensure_inclusion = input("Are there any foods you want to ensure are included in your diet?\n")
         ensure_exclusion = input("Are there any foods you want to ensure are excluded from your diet?\n")
         self.prompt += f"Dietary restrictions include: {diet_restrictions}. The aim of the diet is to {diet_goals}. Please make sure to include {ensure_inclusion} and exclude {ensure_exclusion}."

    def report_user_stats(self):
         print(self.prompt)


def main():
   user_info = gather_info()
   new_user = User(user_info)
   new_user.report_user_stats()

   if new_user.mode.lower() == "workout":
        new_user.generate_workout_plan()
   elif new_user.mode.lower() == "diet":
        new_user.generate_diet_plan()
    
   new_user.report_user_stats()


if __name__ == "__main__":
    main()