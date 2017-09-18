

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



def in_lower(seq):
    if not seq:
        return ""
    elif seq[0].islower() or seq[0] in secrets_lower:
        return seq[0] + in_lower(seq[1:])
    else:
        return in_lower(seq[1:])


def in_upper(seq):
    if not seq:
        return ""
    elif seq[0].isupper() or seq[0] in secrets_upper:
        return seq[0] + in_upper(seq[1:])
    else:
        return in_upper(seq[1:])


def split_rec(seq):
    return in_lower(seq), in_upper(seq)


def split_rec_two(seq, res_low = "", res_high = ""):
    if not seq:
        return res_low, res_high
    elif seq[0].islower() or seq[0] in secrets_lower:
        res_low += seq[0]
        return split_rec_two(seq[1:], res_low, res_high)
    
    elif seq[0].isupper() or seq[0] in secrets_upper:
        res_high += seq[0]
        return split_rec_two(seq[1:], res_low, res_high)
    
    else:
        return split_rec_two(seq[1:], res_low, res_high)
    










