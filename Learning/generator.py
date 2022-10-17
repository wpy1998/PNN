import math

cri = 1
c1 = 0
c2 = 0
print(math.pi / 6)
for i in range(21):
    for j in range(21):
        for k in range(21):
            a = (i - 10) / 10
            b = (j - 10) / 10
            c = (k - 10) / 10
            input1 = a * a
            input2 = b * b
            input3 = c * c
            input4 = input1 + input2
            input5 = input1 + input3
            input6 = input2 + input3
            input7 = a * b
            input8 = a * c
            input9 = b * c
            input10 = input1 + input7
            input11 = input2 + input8
            input12 = input3 + input9
            input13 = a + 0.1
            input14 = b + 0.1
            input15 = c + 0.1
            input16 = 0
            if((input1 + input2 + input3) <= cri):
                val = 0
                c1 += 1
            elif(a > 0):
                val = 1
                c2 += 1
            else:
                val = 2
                c2 += 1
            print(cri, (input1 + input2 + input3), val, c1, c2)
            result = str(input1) + ',' + str(input2) + ',' + \
                str(input3) + ',' + str(input4) + ',' + \
                str(input5) + ',' + str(input6) + ',' + \
                str(input7) + ',' + str(input8) + ',' + \
                str(input9) + ',' + str(input10) + ',' + \
                str(input11) + ',' + str(input12) + ',' + \
                str(input13) + ',' + str(input14) + ',' + \
                str(input15) + ',' + str(input16) + ',' + str(val) + '\n'
            with open("train_data.csv", "a") as file:
                file.write(result)
            # print(result)