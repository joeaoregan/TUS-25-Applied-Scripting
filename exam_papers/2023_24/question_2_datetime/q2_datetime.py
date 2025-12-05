# Q2(a)
import datetime
import shelve

with shelve.open("subscriptons") as subscriptions:
    while True:
        choice = input("\n[A]dd [R]emove [D]isplay [C]lear [Q]uit: ")

# Q2(b)
        if choice.lower()[0] == 'a':
            name = input("Enter the service's name: ")

            if name in subscriptions:
                print("The service already exists in the system")
                continue

            date_string = input("Enter the original subscription date in the form dd/mm/YYYY: ")
            date_obj = datetime.datetime.strptime(date_string, "%d/%m/%Y")

            subscriptions[name] = date_obj
            print(f"Added {name} with Date {date_string}")

# Q2(c)
        elif choice.lower()[0] == 'r':
            name = input("Enter the service's name: ")

            if name not in subscriptions:
                print("The name does not exist in the system")
                continue

            del subscriptions[name]
            print(f"Removed {name}")

# Q2(d)
        elif choice.lower()[0] == 'd':
            if subscriptions:
                today = datetime.date.today()
                this_year = today.year
                print("Name      Next Renewal      Days until renewal    Years subscribed")
                for name in sorted(subscriptions):
                    date_obj = subscriptions[name]
                    renewal = datetime.date(this_year, date_obj.month, date_obj.day)

                    if today > renewal:
                        renewal = datetime.date(this_year+1, date_obj.month, date_obj.day)

                    days_until = (renewal - today).days
                    years = renewal.year - date_obj.year

                    print(f"{name:10} {renewal.strftime('%d/%m/%Y')} {days_until:>15} {years:>20}")
            else:
                print("No subscriptions available")

# Q2(e)
        elif choice.lower()[0] == 'c':
            subscriptions.clear()
            print("Deleted all entries")

# Q2(f)
        elif choice.lower()[0] == 'q':
            print("Goodbye")
            break