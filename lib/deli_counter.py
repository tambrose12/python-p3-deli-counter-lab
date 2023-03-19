
katz_deli = []


def line(the_line):
    if len(the_line) == 0:
        print("The line is currently empty.")
    else:
        printed_line = []
        for index, name in enumerate(the_line, start=1):
            printed_line.append(f"{index}. {name}")
        print(f"The line is currently: {' '.join(printed_line)}")


def take_a_number(the_line, person):
    the_line.append(person)
    for index, name in enumerate(the_line, start=1):
        if person == name:
            print(f"Welcome, {name}. You are number {index} in line.")


def now_serving(line):
    if len(line) == 0:
        print("There is nobody waiting to be served!")
    else:
        for name in line:
            if name == line[0]:
                print(f"Currently serving {name}.")
                line.remove(name)
