#  Comparisons to singletons like None should always be done with is or is not, never the equality operators == or !=

result = None

# Correct
if result is None: 
    print("No result")
    
# Wrong
if result == None:
    print("No result")