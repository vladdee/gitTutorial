def is_list(expr):
    if isinstance(expr, list):
        return True
    else:
        return False


def dic_true_checker(expr, dic, index):
    if isinstance(expr[index], str):
        if expr[index] in dic:
            if dic[expr[index]] == "true":
                return "true"
            else:
                return "false"
    else:
        return "false"

def not_doer(expr, dic):
    if is_list(expr[1]):
        return interpret(["NOT", interpret(expr[1], dic)], dic)
    elif (expr[1] == "true") or (dic_true_checker(expr, dic, 1) == "true"):
        return "false"
    elif (expr[1] == "false") or (dic_true_checker(expr, dic, 1) == "false"):
        return "true"

def and_doer(expr, dic):
    if (expr[0] == "true" or dic_true_checker(expr, dic, 0) == "true") and (expr[2] == "true" or dic_true_checker(expr, dic, 2) == "true"):
        return "true"
    elif is_list(expr[0]):
        return interpret([interpret(expr[0], dic), "AND", expr[2]], dic)
    elif is_list(expr[2]):
        return interpret([expr[0], "AND", interpret(expr[2], dic)], dic)
    else:
        return "false"

def or_doer(expr, dic):
    if is_list(expr[0]):
        return interpret([interpret(expr[0], dic), "OR", expr[2]], dic)
    elif is_list(expr[2]):
        return interpret([expr[0], "OR", interpret(expr[2], dic)], dic)
    elif (expr[0] == "true" or dic_true_checker(expr, dic, 0) == "true") or (expr[2] == "true" or dic_true_checker(expr, dic, 2) == "true"):
        return "true"
    else:
        return "false"

def interpret(expr, dic):
    if isinstance(expr, str):
        if expr == "true" or expr == "false":
            return expr
        else:
            return dic[expr]
    elif len(expr) == 2:
        return not_doer(expr, dic)
    else:
        if expr[1] == "AND":
            return and_doer(expr, dic)
        elif expr[1] == "OR":
            return or_doer(expr, dic)
