# Smart Health Assistant - Combined Script

def get_name():
    return input("Enter your name: ")

def get_age():
    while True:
        try:
            age = int(input("Enter your age (years): "))
            if age > 0:
                return age
            print("Please enter a valid age.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_weight():
    while True:
        try:
            weight = float(input("Enter your weight (kg): "))
            if weight > 0:
                return weight
            print("Weight must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_height():
    while True:
        try:
            height = float(input("Enter your height (cm): "))
            if height > 0:
                return height
            print("Height must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_steps():
    while True:
        try:
            steps = int(input("Enter steps walked today: "))
            if steps >= 0:
                return steps
            print("Steps cannot be negative.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_water_intake():
    while True:
        try:
            water = float(input("Enter water intake today (litres): "))
            if water >= 0:
                return water
            print("Water intake cannot be negative.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_sleep_hours():
    while True:
        try:
            sleep = float(input("Enter sleep duration (hours): "))
            if sleep >= 0:
                return sleep
            print("Sleep duration cannot be negative.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return round(weight / (height_m ** 2), 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate_water_goal(weight):
    return round(weight * 35 / 1000, 2)

def feedback_steps(steps):
    if steps >= 10000:
        return "Great! You are very active."
    elif steps >= 7000:
        return "Good. Try to reach 10,000 steps."
    elif steps >= 4000:
        return "Okay, but you can walk more."
    else:
        return "Very low activity. Try to walk more."

def feedback_sleep(hours):
    if 7 <= hours <= 9:
        return "Good sleep duration."
    elif 5 <= hours < 7:
        return "Less sleep. Try to sleep a bit more."
    else:
        return "Very low sleep. This can affect your health."

def print_health_summary(name, age, weight, height, bmi, bmi_cat, water_intake, water_goal, steps, sleep_hours, steps_msg, sleep_msg):
    print("\n========== HEALTH SUMMARY ==========")
    print(f"Name           : {name}")
    print(f"Age            : {age} years")
    print(f"Weight         : {weight} kg")
    print(f"Height         : {height} cm")
    print(f"BMI            : {bmi} ({bmi_cat})")
    print(f"Water intake   : {water_intake} L | Suggested goal ≈ {water_goal} L")
    print(f"Steps walked   : {steps}")
    print(f"Sleep duration : {sleep_hours} hours")
    print("------------------------------------")
    print(f"Steps feedback : {steps_msg}")
    print(f"Sleep feedback : {sleep_msg}")
    print("====================================")
    print("Thank you for using Smart Health Assistant!")
    print("Stay healthy 🙂")

def main():
    print("=" * 35)
    print("        SMART HEALTH ASSISTANT     ")
    print("            Simple Version         ")
    print("=" * 35)

    name = get_name()
    age = get_age()
    weight = get_weight()
    height = get_height()
    steps = get_steps()
    water_intake = get_water_intake()
    sleep_hours = get_sleep_hours()

    bmi = calculate_bmi(weight, height)
    bmi_cat = get_bmi_category(bmi)
    water_goal = calculate_water_goal(weight)
    steps_msg = feedback_steps(steps)
    sleep_msg = feedback_sleep(sleep_hours)

    print_health_summary(
        name, age, weight, height,
        bmi, bmi_cat, water_intake, water_goal,
        steps, sleep_hours, steps_msg, sleep_msg
    )

if __name__ == "__main__":
    main()
    