import pprint

series = ['1', '11', '21', '1211']

count = 1

for index in range(3, 30):
    count = 1
    new_series = ''
    temp_series = str(series[index])
    flag = False
    # print(len(temp_series))
    # print("temp_series: ", end='')
    # print(temp_series)
    prevChar = ''

    # print("----------------------------------------")
    for charIndex in range(0, len(temp_series)-1):

        if temp_series[charIndex] == temp_series[charIndex + 1]:
            prevChar = temp_series[charIndex]
            count = count + 1
            # print('if')
            flag = True
        else:
            # print('else: ', end='')
            new_series = new_series + str(count) + str(temp_series[charIndex])
            prevChar = temp_series[charIndex+1]
            # print(temp_series[charIndex])
            count = 1
            flag = False

    if flag is True:
        # print("inside flag")
        new_series = new_series + str(count) + str(prevChar)
    else:
        # print("inside flag")
        new_series = new_series + str(count) + str(prevChar)

    series.append(new_series)

pprint.pprint(len(series[30]))