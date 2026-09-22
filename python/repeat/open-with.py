
with open("repeat/scores.txt", "r") as my_text_file:
    output1 = my_text_file.read()
    if output1:
        output2 = output1.strip().split('\n')
        for name_age in output2:
            str_name_age = name_age.split(',')
            name = str_name_age[0]
            age = int(str_name_age[1])
            if age >= 60:
                print(name)

with open("repeat/scores.txt", "a") as my_text_file:
    name_age = input()
    my_text_file.write(name_age + "\n")