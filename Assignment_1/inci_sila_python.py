# CHANGE EVERYTHING 
# question 1 & 7 & 3 & 4
exampleList = ["book","pencil", "paper","notebook","ruler"] #heap-dynamic (accessed until the program terminates)
print(exampleList)
print(exampleList[1])
print("-------")
# question 5
raggedList = [
        [7, 7, 7, 7],
        [7, 7, 7],
        [7, 7, 7, 7,7],
        [7],
        [],
        [7,7]
]
for row in raggedList:  #ragged array
        for seven in row:
                print(seven, end = " ")
        print()
print("-------")
arrays = [] #rectangular array

for k in range(7):
        array = []
        for j in range(7):
                row = []
                for i in range(7):
                        layer = []
                        for m in range(7):
                                layer.append(0)
                        row.append(layer)
                array.append(row)
        arrays.append(array)

arrays[5][3][1][2] = 5
print(arrays[5][3][1][2]) 
print("-------")
# # question 6
mult_arr = []

for k in range(7):
        arr = []
        for j in range(7):
                rows = []
                for i in range(7):
                        layers = []
                        for m in range(7):
                        		dim = []
                        		for n in range(7):
                        				dim.append(0)
                        		layers.append(dim)
                        rows.append(layers)
                arr.append(rows)
        mult_arr.append(arr)

mult_arr[3][5][5][4][2] = 1
print(mult_arr[3][5][5][4][2]) # as seen here you can access many number of subscripts, no limits


print("-------")
# question 8
print(exampleList[2:4])
# question 2
print("Checks range of array, gives error message.")
print("-------")
x = exampleList[7]
print(x)
