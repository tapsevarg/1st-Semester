import io


def input_file():
    grades = []
    f = io.StringIO("Name,Score\nJoe Besser,70\n"
                    "Curly Joe DeRita,0\nLarry Fine,80\n"
                    "Curly Howard,65\nMoe Howard,100\n"
                    "Shemp Howard,85\n")
    try:
        next(f)
        for line in f:
                line = line.strip()
                grades.append(line)
        print(grades[0])
    except:
        print("error")
    return grades
        

def process_file(grades):
    tacos = []
    for each in grades:
        each = each.split(",")
        tacos.append(each[1])
    print(tacos[1])


grades = input_file()
each = process_file(grades)
