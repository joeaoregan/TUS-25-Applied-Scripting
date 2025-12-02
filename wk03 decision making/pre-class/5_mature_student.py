
print(f"{"Age":^5}{"Status":^11}{"School":^13}{"Version 1":^13}{"Version 2":^13}")

age = 25
status = "part-time"
school = "Engineering"

print(f"{age:^5}{status:^11}{school:^13}{str(age > 23 or status == "part-time" and school == "Engineering"):^13}{str(school == "Engineering" and age > 23 or status == "part-time"):^13}")

age = 25
status = "full-time"
school = "Engineering"

print(f"{age:^5}{status:^11}{school:^13}{str(age > 23 or status == "part-time" and school == "Engineering"):^13}{str(school == "Engineering" and age > 23 or status == "part-time"):^13}")

age = 18
status = "part-time"
school = "Engineering"

print(f"{age:^5}{status:^11}{school:^13}{str(age > 23 or status == "part-time" and school == "Engineering"):^13}{str(school == "Engineering" and age > 23 or status == "part-time"):^13}")

age = 18
status = "full-time"
school = "Engineering"

print(f"{age:^5}{status:^11}{school:^13}{str(age > 23 or status == "part-time" and school == "Engineering"):^13}{str(school == "Engineering" and age > 23 or status == "part-time"):^13}")

age = 18
status = "part-time"
school = "Science"

print(f"{age:^5}{status:^11}{school:^13}{str(age > 23 or status == "part-time" and school == "Engineering"):^13}{str(school == "Engineering" and age > 23 or status == "part-time"):^13}")

age = 25
status = "full-time"
school = "Science"

print(f"{age:^5}{status:^11}{school:^13}{str(age > 23 or status == "part-time" and school == "Engineering"):^13}{str(school == "Engineering" and age > 23 or status == "part-time"):^13}")

# Check

print((age > 23 or status == "part-time") and school == "Engineering")

print(school == "Engineering" and (age > 23 or status == "part-time"))