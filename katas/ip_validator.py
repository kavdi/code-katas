def is_valid_IP(strng):
    """An algorithm that will identify valid IPv4 addresses in dot-decimal format."""
    x = strng.split('.')
    if len(x) != 4:
        return False
    for i in range(len(x)):
        if x[i][0] == '0' and len(x[i]) > 1 or x[i].isalpha():
            return False
        elif ' ' in x[i]:
            return False
        elif int(x[i]) > 255 or int(x[i]) < 0:
            return False
    return True
