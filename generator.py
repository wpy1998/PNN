for i in range(10):
    for j in range(10):
        for m in range(10):
            for n in range(10):
                input1 = (i + 1) * (j + 1) / 100
                input2 = (i + 1) * (m + 1) / 100
                input3 = (i + 1) * (n + 1) / 100
                input4 = (j + 1) * (m + 1) / 100
                input5 = (j + 1) * (n + 1) / 100
                input6 = (m + 1) * (n + 1) / 100
                input7 = (i + 1) * (j + 1) * (m + 1) / 1000
                input8 = (i + 1) * (j + 1) * (n + 1) / 1000
                input9 = (i + 1) * (m + 1) * (n + 1) / 1000
                input10 = (j + 1) * (m + 1) * (n + 1) / 1000
                result = str(input1) + ',' + str(input2) + ',' + str(input3) + ',' + str(input4) + \
                         ',' + str(input5) + ',' + str(input6) + ',' + str(input7) + ',' + str(input8) + \
                         ',' + str(input9) + ',' + str(input10) + ',' + str(input6) + ',' + str(input5) + \
                         ',' + str(input4) + ',' + str(input3) + ',' + str(input2) + ',' + str(input1) + '\n'
                with open("train_data.csv", "a") as file:
                    file.write(result)
                print(result)

                # if i == 9:
                #     val_1 = 1
                # else:
                #     val_1 = 0
                #
                # if j == 9:
                #     val_2 = 1
                # else:
                #     val_2 = 0
                #
                # if m == 9:
                #     val_3 = 1
                # else:
                #     val_3 = 0
                #
                # if n == 9:
                #     val_4 = 1
                # else:
                #     val_4 = 0
                #
                # result = val_1 * 8 + val_2 * 4 + val_3 * 2 + val_4
                # print(result)