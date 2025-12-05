# Q2(a)
import datetime
import shelve

with shelve.open("birthdays") as birthdays:
    while True:
        choice = input("\n[A]dd [R]emove [D]isplay [C]lear [Q]uit: ")

# Q2(b)
        if choice.lower()[0] == 'a':
            name = input("Enter the person's name: ")

            if name in birthdays:
                print("The name already exists in the system")
                continue

            dob_string = input("Enter the date of birth in the form dd/mm/YYYY: ")
            dob_obj = datetime.datetime.strptime(dob_string, "%d/%m/%Y")

            birthdays[name] = dob_obj
            print(f"Added {name} with Date of Birth {dob_string}")

# Q2(c)
        elif choice.lower()[0] == 'r':
            name = input("Enter the person's name: ")

            if name not in birthdays:
                print("The name does not exist in the system")
                continue

            del birthdays[name]
            print(f"Removed {name}")

# Q2(d)
        elif choice.lower()[0] == 'd':
            if birthdays:
                today = datetime.date.today()
                this_year = today.year

                print("Name      Next birthday      Days until birthday    Age next birthday")
                for name in sorted(birthdays):
                    dob_obj = birthdays[name]
                    birthday = datetime.date(this_year, dob_obj.month, dob_obj.day)

                    if today > birthday:
                        birthday = datetime.date(this_year+1, dob_obj.month, dob_obj.day)

                    days_until = (birthday - today).days
                    age = birthday.year - dob_obj.year

                    print(f"{name:10} {birthday.strftime('%d/%m/%Y')} {days_until:>15} {age:>20}")
            else:
                print("No birthdays available")

# Q2(e)
        elif choice.lower()[0] == 'c':
            birthdays.clear()
            print("Deleted all entries")

# Q2(f)
        elif choice.lower()[0] == 'q':
            print("Goodbye")
            break