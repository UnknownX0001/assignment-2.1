step = int(input('Enter step value : '))
 
list_1 = ["start", 5, 4, 1, 6, 10, 101, 7, "end"]

if step>8:

   print("The step is beyond my understandings")


for i in range(0, len(list_1), step):
    print(list_1[i])
