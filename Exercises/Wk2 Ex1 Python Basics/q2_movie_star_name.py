# A00258304

# Write a Python program which generates and displays your Movie Star name, 
# by adding the name of your favourite season or holiday and the name your favourite flower

# Example:

# Input     | Result
# ----------|---------------------------------------------------------------
# daisy     | Enter the name of your favourite flower: daisy
# summer    | Enter the name of your favourite season or holiday: summer
#           | Your Movie Star Name is: Daisy Summer
# ----------|---------------------------------------------------------------
# rose      | Enter the name of your favourite flower: rose
# winter    | Enter the name of your favourite season or holiday: winter
#           | Your Movie Star Name is: Rose Winter
# ----------|---------------------------------------------------------------
# Lily      | Enter the name of your favourite flower: Lily
# spring    | Enter the name of your favourite season or holiday: spring
#           | Your Movie Star Name is: Lily Spring
# ----------|---------------------------------------------------------------
# holly     | Enter the name of your favourite flower: holly
# Christmas | Enter the name of your favourite season or holiday: Christmas
#           | Your Movie Star Name is: Holly Christmas
# ----------|---------------------------------------------------------------
# buttercup | Enter the name of your favourite flower: buttercup
# Easter    | Enter the name of your favourite season or holiday: Easter
#           | Your Movie Star Name is: Buttercup Easter

favourite_flower = input("Enter the name of your favourite flower: ")
favourite_season_or_holiday = input("Enter the name of your favourite season or holiday: ")

movie_star_name = (favourite_flower + " " + favourite_season_or_holiday).title()

print(f"Your Movie Star Name is: {movie_star_name}")
