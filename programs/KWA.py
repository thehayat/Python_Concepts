def find_occurence(num):
    """
    1122223346611288891
    """
    num = str(num)
    count = 1
    prev = num[0]
    data = []
    for each in num[1:]:
        if each == prev:
            count += 1
        else:
            if not prev in data and int(prev) % 2 == 0 and count % 2 == 0:
                data.append((prev, count))
            count = 1
            prev = each
    print(data)
    return data


find_occurence('1122223346611288891')
