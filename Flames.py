def flames(name1, name2):
    name1 = name1.replace(' ','').lower()
    name2 = name2.replace(' ','').lower()

    for ch in name1[:]:
        if ch in name2:
            name1 = name1.replace(ch, "", 1)
            name2 = name2.replace(ch, "", 1)

    count = len(name1) + len(name2)
    flames_list = ["Friends", "Lovers", "Affection", "Marriage", "Enemy", "Sibling"]

    while len(flames_list) > 1:
        split_index = (count % len(flames_list)) - 1

        if split_index >= 0:
            flames_list = flames_list[split_index + 1:] + flames_list[:split_index]
        else:
            flames_list = flames_list[:len(flames_list) - 1]

    return flames_list[0]

name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")
print("Relatioship:", flames(name1, name2))







