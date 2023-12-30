# File: MyListFunctions.py
# Student: Sanjitha Venkata
# UT EID: sv28325
# Course Name: CS303E
# 
# Date: 10/24/2023
# Description of Program: Multiple functions that run actions on lists.

def myAppend( lst, x ):
    # Return a new list that is like lst but with 
    # the element x at the right end
    return lst + [x]

def myExtend( lst1, lst2 ):
    # Return a new list that contains the elements of
    # lst1 followed by the elements of lst2 in order.
    return lst1+lst2

def myMax( lst ):
    # Return the element with the highest value.
    # If lst is empty, print "Empty list: no max value"
    # and return None.  You can assume that the list
    # elements can be compared.
    max=0
    if len(lst) == 0:
        print("Empty list: no max value")
        return None
    else:
        max=lst[0]
        for i in range(len(lst)):
            if(lst[i]>max):
                max=lst[i]
        return max

def mySum( lst ):
    # Return the sum of the elements in lst.  Assume
    # that the elements are numbers.
    sum=0
    for i in range(len(lst)):
        sum+= lst[i]
    return sum

def myCount( lst, x ):
    # Return the number of times element x appears
    # in lst.
    count=0
    for i in range (len(lst)):
        if(x==lst[i]):
            count+=1
    return count

def myInsert( lst, i, x ):
    # Return a new list like lst except that x has been
    # inserted at the ith position.  I.e., the list is now
    # one element longer than before. Print "Invalid index" if
    # i is negative or is greater than the length of lst and 
    # return None.
    if(i<0 or i>len(lst)):
        print("Invalid index")
    else:
        return lst[:i]+[x]+lst[i:]


def myPop( lst, i ):
    # Return two results: 
    # 1. a new list that is like lst but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is negative or is greater than
    # or equal to len(lst), and return lst unchanged, and None
    if(i<0 or i>=len(lst)):
        print("Invalid index")
        return lst, None
    else:
        lst1= lst[:i]+lst[i+1:]
        return lst1, lst[i]

def myFind( lst, x ):
    # Return the index of the first (leftmost) occurrence of 
    # x in lst, if any.  Return -1 if x does not occur in lst.
    if(x not in lst):
        return -1
    else:
        for i in range(len(lst)):
            if(x==lst[i]):
                return i    

def myRFind( lst, x ):
    # Return the index of the last (rightmost) occurrence of 
    # x in lst, if any.  Return -1 if ch does not occur in lst.
    if(x not in lst):
        return -1
    else:
        for i in range(len(lst)-1,-1,-1):
            if(x==lst[i]):
                return i

def myFindAll( lst, x ):
    # Return a list of indices of occurrences of x in lst, if any.
    # Return the empty list if there are none.
    if(x not in lst):
        return []
    else:
        lst1=[]
        for i in range(len(lst)):
            if(x==lst[i]):
                lst1=lst1+[i]
        return lst1

def myReverse( lst ):
    # Return a new list like lst but with the characters
    # in the reverse order.
    revLst=[]
    for i in range(len(lst)-1,-1,-1):
        revLst+=[lst[i]]
    return revLst

def myRemove( lst, x ):
    # Return a new list with the first occurrence of x
    # removed.  If there is none, return lst.
    if(x not in lst):
        return lst
    else:
        unwanted=0
        for i in range(len(lst)):
            if(x==lst[i]):
                unwanted=i
                break
        return lst[0:unwanted]+lst[unwanted+1:]    

def myRemoveAll( lst, x ):
    # Return a new list with all occurrences of x
    # removed.  If there are none, return lst.
    if(x not in lst):
        return lst
    else:
        unwanted=0
        while(x in lst):
            for i in range(len(lst)):
                if(x==lst[i]):
                    unwanted=i
                    lst=lst[0:unwanted]+lst[unwanted+1:]
                    break
        return lst

# Don't use slicing for this one:
def mySlice( lst, i, j ):
    # A limited version of the slice operations on lists.
    # If i and j are in [0..len(lst)], return the list 
    # [ lst[i], lst[i+1], ... lst[j-1] ].  I.e., 
    # the slice lst[i:j].  Print an error message if either
    # i or j is not in [0..len(lst)].  Notice that this is 
    # similar but not identical to the way Python slice behaves.
    if(i>len(lst) or j>len(lst) or i<0 or j<0):
        print("Illegal index value")
    else:
        lst1=[]
        for index in range(j-i):
            lst1+=[lst[i+index]]
        return lst1
