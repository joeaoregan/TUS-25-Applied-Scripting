# A00258304

# Write a program which inputs the final score of a match:

#   home team name and score
#   away team name and score

# and determines and displays the match result 
# (the name of the winning team, or “draw”).

# Example: 
# Test      | Input     | Result
#-----------|-----------|---------------------------
# Home win  | Lithuania | Home team name? Lithuania
#           | 4         | Home team score? 4
#           | Moldova   | Away team name? Moldova
#           | 0         | Away team score? 0
#           |           | Winner is Lithuania
#-----------|-----------|---------------------------
# Draw      | Sweden    | Home team name? Sweden
#           | 1         | Home team score? 1
#           | Ireland   | Away team name? Ireland
#           | 1         | Away team score? 1
#           |           | Draw
#-----------|-----------|---------------------------
# Away win  | Scotland  | Home team name? Scotland
#           | 0         | Home team score? 0
#           | Spain     | Away team name? Spain
#           | 2         | Away team score? 2
#           |           | Winner is Spain


# home_team = input("Home team name? ")
# home_score = int(input("Home team score? "))
# away_team = input("Away team name? ")
# away_score = int(input("Away team score? "))

home_team = "Lithuania"
home_score = 4
away_team = "Moldova"
away_score = 0

if home_score > away_score:
    print(f"Winner is {home_team}")
elif away_score > home_score:
    print(f"Winner is {away_team}")
else:
    print("Draw")