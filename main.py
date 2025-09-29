# Activity 5: NFL Week 4 Fantasy Tracker! 🏈

print("🏈 Welcome to NFL Week 4 Fantasy Manager!")
print("Build and manage your fantasy team using lists!")
print()

# TODO 1: Draft your starting lineup 
print("🏈 TODO 1: Draft Your Starting Lineup")
# Create a list with your 5 starting players (QB, RB, WR, TE, K)
starting_lineup = []  # Replace [] with ["QB_name", "RB_name", "WR_name", "TE_name", "K_name"]
print(f"Your starting lineup: {starting_lineup}")
print(f"Lineup size: {len(starting_lineup)} players")
print()

# TODO 2: Choose your team to follow this week
print("📺 TODO 2: Pick Your Team to Follow This Week")
# All NFL teams that played on September 28, 2025 (Week 4)
week4_teams = ["Steelers", "Vikings", "Falcons", "Commanders", "Bills", "Saints", 
               "Lions", "Browns", "Texans", "Titans", "Patriots", "Panthers", 
               "Giants", "Chargers", "Eagles", "Buccaneers", "Rams", "Colts"]
print("Teams playing this week:")
for index in range(len(week4_teams)):
    print(f"{index + 1}. {week4_teams[index]}")

# Get user input to select their team to follow
print(f"\nWhich team has players you want to watch? (Enter 1-{len(week4_teams)}): ", end="")
team_choice = int(input()) - 1  # Convert to list index
# TODO: Use team_choice to access the selected team from the list
team_to_watch = None  # Replace with week4_teams[team_choice]
print(f"📺 You are watching the {team_to_watch} this week!")
print()

# TODO 3: Track your season performance
print("📊 TODO 3: Season Performance Tracker")
# Your fantasy points from each week so far
weekly_scores = [89, 76, 102, 64, 95]
print(f"Your weekly fantasy scores: {weekly_scores}")
print(f"Weeks played: {len(weekly_scores)}")

# Find your best week using a for loop
best_score = weekly_scores[0]  # Start with first week
# TODO: Use a for loop to find the highest score in the list
# Hint: for score in weekly_scores:
#          if score > best_score:
#              best_score = score

print(f"🏆 Your best week: {best_score} points")

# Calculate your season average
total_points = 0
# TODO: Use a for loop to calculate the total of all weekly scores
# Hint: for score in weekly_scores:
#          total_points = total_points + score

# TODO: Calculate average by dividing total by number of weeks
average_score = 0  # Replace 0 with total_points / len(weekly_scores)

print(f"📊 Season average: {average_score:.1f} points per week")
if best_score > average_score + 10:
    print("🔥 You had some explosive weeks!")
else:
    print("📈 You are consistently solid!")

print(f"\n🏈 Great job managing your fantasy team!")