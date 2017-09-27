secrets_lower = "_."
secrets_upper = " |"

def split_it(seq):
    hidden_l_und_dot = ""
    hidden_u_bl_pipe = ""
    for i in seq:
        if i.islower() or i in secrets_lower:
            hidden_l_und_dot  += i
        elif i.isupper() or i in secrets_upper:
            hidden_u_bl_pipe += i
    return hidden_l_und_dot, hidden_u_bl_pipe

def split_rec(seq):
    first_message = ""
    second_message = ""
    if not seq:
        return first_message, second_message
    elif seq[0] in secrets_lower or seq[0].islower():
        first_message, second_message = split_rec(seq[1:])
        return seq[0] + first_message, second_message
    elif seq[0] in secrets_upper or seq[0].isupper():
        first_message, second_message = split_rec(seq[1:])
        return first_message, seq[0] + second_message
    else:
        return split_rec(seq[1:])
