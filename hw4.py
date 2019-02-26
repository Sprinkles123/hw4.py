# import only standard Python 3 modules here

'''
INSTRUCTIONS.
========================================================
For each for the following six functions, the input
consists of a set, A, and a relation R on set A. Function
"isPropertyX(A,R)" returns True if R has property X, and
False otherwise. You can assume A is a finite list of ints,
e.g. [1,3,5,7,9], and R is valid relation on A, e.g. [(1,3),
(3,1),(3,7)].
========================================================
'''

def isReflexive(A, R)
    '''TODO: Your code here'''
    check = []
    a=[]
    b=[]
    for a1, a2 in R:
    	if (a1==a2):
    	    check.append((a1,a2))
    	    b.append(a1)
    	if(a1 not in a):
    	    a.append(a1)
    if (set(a)==set(b)):
    	return True
    else:
    	return False

def isIrreflexive(A, R):
    '''TODO: Your code here'''
    for a1, a2 in R:
    	if (a1==a2):
    	    return False
    return True

def isTransitive(A, R):
    '''TODO: Your code here'''
    for (a,b) in R:
    	for(c,d) in R:
    	    if b==c and (a,d) not in R:
    		return False
    return True

def isAntisymmetric(A, R):
    '''TODO: Your code here'''
    for (a,b) in R:
    	if (a,b) in R and (b,a) in R and a!=b:
    		return False
    return True
    
def isSymmetric(A, R):
    '''TODO: Your code here'''
    for(a1, a2) in R:
        if (a1,a2) in R and (a2, a1) in R:
            return False
    return True
    
def isAsymmetric(A, R):
    '''TODO: Your code here'''
    for (a1,a2) in R:
	if (a1,a2) in R and (a1,a2) in R:
	    return False
    return True
	
if __name__ == '__main__': ''' Delete this line and the ones below it, or
    write code in this if-block which will not run by the autograder.'''
    pass
