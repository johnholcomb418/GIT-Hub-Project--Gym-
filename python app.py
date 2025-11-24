#Gym Workout Tracker Program

#Welcome message
print("Welcome to the Gym Workout Tracker!")

# We ask how many minutes they worked out today.
minutes = input("How many minutes did you work out today? ")

#Basic error handling (must come before calculation)
try:
    minutes = float(minutes)
except ValueError:
    print("Please enter a valid number for minutes.")
    exit()
  
#Convert daily workout minutes to weekly total
weekly_minutes = minutes * 7
hours_weekly = weekly_minutes / 60

#Display results
print("\n🏋️ Gym Progress Report 🏋️")
print(f"You worked out for {minutes} minutes today.")
print(f"At this pace, you'll get about {weekly_minutes:.0f} minutes of exercise this week.")
print(f"That's roughly {hours_weekly:.1f} hours per week — great job staying active!")

# Program ends cleanly with no unused variables.
