#Absolute distict count 

from collections import Counter 
import numpy as np 

sampleArray = [-5,-3,-1,0,3,6] 
print("Sample array: ", sampleArray)
absoluteArray = np.absolute(sampleArray)
print("Absolute array: ", absoluteArray)

def countDistinct(absoluteArray): 
  
    # counter method gives dictionary of elements in list with their corresponding frequency. 
    # using keys() method of dictionary data structure we can count distinct values in array  
    return len(Counter(absoluteArray).keys())     

if __name__=="__main__": 
    print ("Distinct count: ",countDistinct(absoluteArray))