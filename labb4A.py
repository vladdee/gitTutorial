def split_rec(seq):
    first_message = ""
    second_message = ""
    if not seq:
        return first_message, second_message
    elif seq[0] in secrets_lower or seq[0].islower():
        first_message, second_message = split_rec_three(seq[1:])
        return seq[0] + first_message, second_message
    elif seq[0] in secrets_upper or seq[0].isupper():
        first_message, second_message = split_rec_three(seq[1:])
        return first_message, seq[0] + second_message
    else:
        return split_rec_three(seq[1:])