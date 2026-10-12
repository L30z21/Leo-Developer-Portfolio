# weekly step tracker

steps = [8000,9500,10000,7500,11000,9000,8500]
daily_goal = 10000

def calculate_total(steps):
    total = 0

    for day_steps in steps:
        total += day_steps

    return total

def calculate_average(steps):
    total = calculate_total(steps)
    average =total / len (steps)
    return average

def count_goals_days(steps, goal):
    count = 0

    for day_steps in steps:
        if day_steps >= goal:
            count = count + 1

    return count


weekly_total = calculate_total(steps)
print("Total steps this week:", weekly_total)
weekly_average = calculate_average(steps)
print("Average daily steps:", round(weekly_average, 2))
goal_days = count_goals_days(steps, daily_goal)
print("Days goals reached:", goal_days)
