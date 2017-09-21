

def true_excep(expr, dic, oper):
    if oper == "AND": 
        if (expr[0] == "true" or dic[expr[0]] == "true") and (expr[2] == "true" or dic[expr[2]] == "true"):
            return "true"
        else:
            return "false"
    elif oper == "OR":
        if (expr[0] == "true" or dic[expr[0]] == "true") or (expr[2] == "true" or dic[expr[2]] == "true"):
            return "true"
        else:
            return "false"
    elif oper == "NOT":
        if dic[expr[1]] == "true" or expr[1] == "true":
            return "false"
        else:
            return "true"
        
        
def is_list(expr):
    if isinstance(expr, list):
        return True
    else:
        return False
        
def op_checker(expr):
    if len(expr) == 2:
        if expr[0] == "NOT":
            return "NOT"
    if len(expr) == 3:
        if expr[1] == "AND":
            return "AND"
        elif expr[1] == "OR":
            return "OR"
        

def interpret(expr, dic):
    if isinstance(expr, str):
        return dic[expr]
    elif op_checker(expr) == "NOT":
        if is_list(expr[1]):
            return interpret(expr[1])
        return true_excep(expr, dic, )
