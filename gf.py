mylist = [1,2,3,4,5,6]
for i in range(1,6):
    mylist[i-1] = mylist[i]
    for i in range(0,6):
        print(mylist[i], end= "")
    
	
