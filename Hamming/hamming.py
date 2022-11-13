flag = 1
k, s = input("Число: "), []
if len(k) != 7:
    flag = 0
    print("Неправильный формат числа")
else:
    for i in range(7):
        if k[i] == '0' or k[i] == '1':
            s.append(int(k[i]))
        else:
            print("Неправильный формат числа")
            flag = 0
            break
if flag == 1:
    s1 = (s[0] + s[2] + s[4] + s[6]) % 2
    s2 = (s[1] + s[2] + s[5] + s[6]) % 2
    s3 = (s[3] + s[4] + s[5] + s[6]) % 2
    t = int(str(s3) + str(s2) + str(s1), 2)
    if t != 0:
        print("Ошибка в бите", t)
        if s[t - 1] == 1:
            s[t - 1] = 0
        else:
            s[t - 1] = 1
        print("Правильное сообщение(только информационные биты): ", s[2], s[4], s[5], s[6], sep = "")
    else:
        print("Нет ошибок ", s[2], s[4], s[5], s[6], sep = "")
