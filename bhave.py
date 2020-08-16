# import matplotlib.pyplot as plt 

with open('silicon_data.txt') as f:
    x = f.readlines()
    data = []
    for i in range(len(x)):
        line = x[i]
        # Split on any whitespace (including tab characters)
        row = line.split()
        print(row)
        if i > 0:
            row[0] = int(row[0])
            row[1] = float(row[1])
            row[2] = int(row[2])
            row[3] = tuple(int(j) for j in row[3].split(','))

        # Append to our list of lists:
        data.append(row)
    first = data[1:]
    first.sort(key = lambda x: (x[3][0], x[3][1]))
    data[1:] = first
    print(len(data))
    # x = []
    # y = []
    # for d in range(1, len(data)):
    #     x.append(data[d][1])
    #     y.append(data[d][2])
    # plt.plot(x, y)
    # plt.xlabel('Voltage') 
    # plt.ylabel('Frequency') 
    # plt.title('My first graph!') 
    # plt.show() 

    # with open('output.txt', 'w') as fo:
    #     fo.write(str(data[0][0]) + ' ' + str(data[0][1]) + ' ' + str(data[0][2]) + ' ' + str(data[0][3]) + '\n')      
    #     for l in range(1,len(data)):
    #         fo.write(str(data[l][0]) + '\t' + str(data[l][1]) + '\t' + str(data[l][2]) + '\t\t' + str(data[l][3]) + '\n')