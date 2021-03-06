
#insertion sort
''' check 3rd place with 2nd exchange if larger then check 2nd with 1st and repeat for 4
best case time- theta(n)
worst case time-theta(n squared)
average time- theta(n sq)
like selection but performs better as the list is sorted as we go butrequires more writes than selection
great for small or mostly-sorted arrays

stable-inplace-online-internal memory-non recursive
'''

def insertionsort(a):
    
    for index in range(1,len(a)):
        
        value=a[index]
        position = index-1
        
        while position>=0 and value<a[position]:
            a[position+1]=a[position]
            position-=1
        
        a[position+1]=value

a = [1,100,2345,56,76,89,0,3]
insertionsort(a)
print(a)
