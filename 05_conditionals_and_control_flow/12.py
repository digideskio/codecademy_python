def using_control_once():
    if True or False:
        return "Success #1"

def using_control_again():
    if 12 < 15:
        return "Success #2"

print using_control_once()
print using_control_again()
