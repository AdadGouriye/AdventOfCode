text = [int(line) for line in open("input.txt","r").read().split("\n")]


for index1 in range(len(text)):
    for index2 in range(len(text)):
        if text[index1] + text[index2] == 2020 :
            print(text[index1] * text[index2])
        



for index1 in range(len(text)):
    for index2 in range(len(text)):
        for index3 in range(len(text)):
            if text[index1] + text[index2] + text[index3] == 2020 :
                print(text[index1] * text[index2] * text[index3])