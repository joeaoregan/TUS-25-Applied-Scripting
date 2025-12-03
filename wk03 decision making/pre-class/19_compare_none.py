#  Comparisons to singletons like None should always be done with is or is not, never the equality operators == or !=

result = None

# Correct
# The is opetator checks identity: whether two variables point to the exact same object.
if result is None: 
    print("No result")
    
# Wrong
# The == operator checks equality: whether two objects have the same value.
if result == None:
    print("No result")


# Good
if result is not None:
    print("Result")

# Bad
if not result is None:
    print("Result")