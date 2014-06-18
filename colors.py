def obj(color='green', attrs=[]):
    import string, termcolor
    obj = {}
    for i in string.letters:
            obj[i] = termcolor.colored(i, color=color, attrs=attrs)
    return obj
