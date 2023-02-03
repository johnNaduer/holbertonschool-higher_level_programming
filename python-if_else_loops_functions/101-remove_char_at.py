def remove_char_at(str, n):
    if n >= 0:
        string = str[0:n] + str[n+1:]
        return string
    else:
        return str
