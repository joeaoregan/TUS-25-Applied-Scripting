# Question 16
# For a date object end_date which of the following is the correct code to return a date string in the format dd/mm/yyyy?
# Hint: To try this in the interactive interpreter, import the datetime module and create a date object as follows:
import datetime
end_date =  datetime.date(2026,12,31)
 
print(end_date.strftime("%d/%m/%Y")) # 31/12/2026

# print(end_date.strptime("%d/%m/%Y")) # AttributeError: 'datetime.date' object has no attribute 'strptime'. Did you mean: 'strftime'?

print(end_date.isoformat()) # 2026-12-31