def oxford_comma(items):
    if len(items) == 1:
        return "".join(items)
    elif len(items) == 2:
        return " and ".join(items)
    elif len(items) > 2:
        string_with_commas = ", ".join(items[0:-1])
        print(string_with_commas)
        string_with_and = ", and "+items[-1]
        print(string_with_commas + string_with_and)
        return string_with_commas + string_with_and


oxford_comma(["fiddleheads", "okra", "fiddleheads", "okra", "kohlrabi""kohlrabi"])