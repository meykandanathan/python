def is_valid_number(string):
    def is_integer(string):
        if string == "":
            return False
        if string[0] == "+" or string[0] == "-":
            string = string[1:]
        if string == "":
            return False
        for char in string:
            if char < "0" or char > "9":
                return False
        return True

    def is_decimal(string):
        if string == "":
            return False
        if string[0] == "+" or string[0] == "-":
            string = string[1:]
        if string == "":
            return False
        has_dot = False
        for char in string:
            if char == ".":
                if has_dot:
                    return False
                has_dot = True
            elif char < "0" or char > "9":
                return False
        return True

    if string == "":
        return False
    e_index = string.find("e")
    if e_index == -1:
        e_index = string.find("E")
    if e_index == -1:
        return is_decimal(string)
    else:
        return is_decimal(string[:e_index]) and is_integer(string[e_index + 1:])


print(is_valid_number("0"))
