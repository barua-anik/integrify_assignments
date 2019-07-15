# Array right shifting

#Initialize and Displays array     
arr = [0,1, 2, 3, 4, 5];    
print("Original array: ", arr);    
n = int(input("How many time you want to Shift? "));    
     
#Rotate the given array by n times toward right    
for i in range(0, n):    
    #Stores the last element of array
    last = arr[len(arr)-1];    
  
    for j in range(len(arr)-1, 0, -1):    
        #Shift element of array by one    
        arr[j] = arr[j-1];    
            
    #Last element of the array will be added to the start of the array.    
    arr[0] = last;    
     
print("After rotation: ", arr);  
