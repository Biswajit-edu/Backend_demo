
harry = ""

def get_first_name(names):
    """Returns the first name from a list of names."""
    global harry
    harry = names[1]
    if names:
        return names[0]
    return None



def printing():
    print("Here is your ---->  "+harry)