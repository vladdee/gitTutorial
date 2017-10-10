def logic_constant(expr):
    if expr == "true" or expr == "false":
        return True
    else:
        return False

def is_string(expr):
    if isinstance(expr, str):
        return True
    else:
        return False

def NOT(value):
    if value == "true":
        return "false"
    else:
        return "true"

def OR(value0, value1):
    if value0 == "true" or value1 == "true":
        return "true"
    else:
        return "false"

def AND(value0, value1):
    if value0 == "true" and value1 == "true":
        return "true"
    else:
        return "false"

def interpret(expr, dic):
    if logic_constant(expr):
        return expr
    elif is_string(expr):
        return dic[expr]
    elif len(expr) == 2:
        return NOT(interpret(expr[1], dic))
    elif expr[1] == "OR":
        return OR(interpret(expr[0], dic), interpret(expr[2], dic))
    elif expr[1] == "AND":
        return AND(interpret(expr[0], dic), interpret(expr[2], dic))
