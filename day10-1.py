def format_name(fname, lname):
    formatted_name = fname.title()
    formatted_lastname = lname.title()
    if fname == '' or lname == '':
        return "No name or last name provided"

    return f"{formatted_name} {formatted_lastname}"

name = input("name: ")
last = input("last: ")
formatted = format_name(name, last)
print(formatted)
