varmap = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}

def add_to_varmap():
    print("Create your own variable and add to Var Map")
    key = input("Enter the name of varible varmap (key): ")
    value = input("Enter the value (val): ")
    # Convert value to integer if it's supposed to be an integer
    try:
        value = int(value)
    except ValueError:
        print("Value entered is not an integer. Storing it as a string.")
    varmap[key] = value
    print("Updated varmap:", varmap)

def find_in_varmap(v):
    if v in varmap:
        return varmap[v]
    else:
        raise ValueError("Variable not found")

add_to_varmap()  # Adds a new key-value pair to varmap

# To find a value by key
try:
    print("Enter key to return value in var map:")
    wantedValue = input()
    print(find_in_varmap(wantedValue))  # This will print the value associated with 'a'
except ValueError as e:
    print(e)
