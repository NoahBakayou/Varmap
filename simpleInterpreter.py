# implement a simple interpreter that understands the following
# two statement types:

# For now, just accept the program as a
# String called testProgram

## 1. Assignments
# ASSIGN {var}={val}
# Example: ASSIGN X=4
## These types of statements define a variable

## 2. Prints
# PRINT {var}
# Example PRINT X
## These types of statements will print the current variable
## at that state

# def varmap(targetVar, s):
#     for mapping in s:
#         var, val = mapping[0], mapping[1]
#         if targetVar == var:
#             return val
#     raise ValueError("Variable not found")

def varmap(targetVar, state):
    if targetVar in state:
        return state[targetVar]
    else:
        raise ValueError("Error: Var not found")

def executeProgram(program):
    state = dict()

    for line in program.splitlines():
        instruction, expression = line.split()

        if instruction == "ASSIGN":
                var, val = expression.split('=')
                state[var] = val
        elif instruction == "PRINT":
                try:
                    val = varmap(expression, state)
                    print(val)
                except:
                     print("Error: Val not found")
        else:
             print("Error! Instruction not found")

sampleProgram = """ASSIGN X=4
ASSIGN Y=5
PRINT X
PRINT Y
PRINT X
PRINT Z
ASSIGN Z=10
ASSIGN _=2
Woo hoo!
PRINT X
PRINT Z
PRINT _
"""

executeProgram(sampleProgram)