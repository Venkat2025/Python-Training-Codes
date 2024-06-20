def missing(input_string):
    alpha_char=set('abcdefghijklmnopqrstuvwxyz')
    present_char=set(input_string.lower())
    miss_char=sorted(alpha_char-present_char)
    return ' '.join(miss_char)
input_string='geekfforgeeks'
print(missing(input_string))