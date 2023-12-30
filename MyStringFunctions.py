# File: MyStringFunctions.py
# Student: Sanjitha Venkata
# UT EID: sv28325
# Course Name: CS303E
# 
# Date: 10/11/2023
# Description of Program: Multiple functions are defined to manipulate strings. 

def myAppend( s, ch ):
    # Return a new string that is like s but with 
    # character ch added at the end
    return s + ch

def myCount( s, ch ):
    # Return the number of times character ch appears
    # in s.
    count=0

    for i in range(len(s)):
        if (ch==s[i]):
            count+=1
    return count

def myExtend( s1, s2 ):
    # Return a new string that contains the elements of
    # s1 followed by the elements of s2, in the same
    # order they appear in s2.
    return s1+s2

def myMin( s ):
    # Return the character in s with the lowest ASCII code.
    # If s is empty, print "Empty string: no min value"
    # and return None.
    if(s==""):
        print("Empty string: no min value")
        return None
    else:
        strMin=ord(s[0])
        for i in range(len(s)):
            if(strMin>ord(s[i])):
                strMin=ord(s[i])

        return chr(strMin)

def myInsert( s, i, ch ):
    # Return a new string like s except that ch has been
    # inserted at the ith position. I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of s and return None.
    if(len(s)<i):
        print("Invalid index")
        return None
    else:
        return s[0:i]+ch+s[i:]
        
def myPop( s, i ):
    # Return two results: 
    # 1. a new string that is like s but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or 
    # equal to len(s), and return s unchanged and None
    if(i>=len(s)):
        print("Invalid Index")
        return s, None
    else:
        one=s[0:i]+s[i+1:]
        two=s[i]
        return one, two

def myFind( s, ch ):
    # Return the index of the first (leftmost) occurrence of 
    # ch in s, if any. Return -1 if ch does not occur in s.
    if(ch not in s):
        return -1
    else:
        for i in range(len(s)):
            if(ch==s[i]):
                return i
        
def myRFind( s, ch ):
    # Return the index of the last (rightmost) occurrence of 
    # ch in s, if any. Return -1 if ch does not occur in s.
    if(ch not in s):
        return -1
    else:
        for i in range(len(s)-1,-1,-1):
            if(ch==s[i]):
                return i
        
def myRemove( s, ch ):
    # Return a new string with the first occurrence of ch 
    # removed. If there is none, return s.
    if(ch not in s):
        return s
    else:
        unwanted=0
        for i in range(len(s)):
            if(ch==s[i]):
                unwanted=i
                break
            
        return s[0:unwanted]+s[unwanted+1:]

def myRemoveAll( s, ch ):
    # Return a new string with all occurrences of ch.
    # removed. If there are none, return s.
    if(ch not in s):
        return s
    else:
        unwanted=0
        while(ch in s):
            for i in range(len(s)):
                if(ch==s[i]):
                    unwanted=i
                    s=s[0:unwanted]+s[unwanted+1:]
                    break
        return s

def myReverse( s ):
    # Return a new string like s but with the characters
    # in the reverse order.
    revStr=""
    for i in range(len(s)-1,-1,-1):
        revStr+=s[i]

    return revStr
