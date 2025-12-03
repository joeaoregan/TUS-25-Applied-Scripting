for i in range(5):
    print(f"{i=}")
# variable i still exists in the module scope
# but doesn't "move onto 5" (unlike java for loop)
print(f"After: {i=}")
