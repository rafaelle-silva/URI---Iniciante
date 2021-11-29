caso_testes = int(input())
for i in range(1,caso_testes + 1):
    x = input().split()
    number_1,number_2,number_3 = x
    media = (float(number_1)* 2 + float(number_2) * 3 + float(number_3) * 5) / 10
    print(round(media,1))
