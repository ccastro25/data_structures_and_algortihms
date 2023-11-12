#import math , inorder to use math.floor
import math

#create function along with parameters
#arr is for the array to be searched 
# t is for the item that we will be looking for
def bs(arr,target):

    # set low  as 0
    low =0 

    #set high as length of the array
    high = len(arr)

    # run loop until high is not longer bigger than low
    while low <high :

        # get the middle index of array
        middle = math.floor(low+(high-low)/2)

        #if array at middle index is equal to target 
        #return that index 
        if target==arr[middle]:
            return middle 

        #else if the target is bigger than the current index 
        # low index equals middle index plus one
        elif target>arr[middle]:
            low = middle+1
        
        #else , the item in the middle array is larger than the target
        # make high equal the middle index 
        else: 
            high =middle 

    #if target dos not exist return negative four
    return -4
