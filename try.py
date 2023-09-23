example = "6/4"
i = len(example) - 1
while i >= 0 and example[i].isdigit():
    i -= 1
son_rakam = example[i + 1:]
print(son_rakam)


