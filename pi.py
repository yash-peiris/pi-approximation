from math import pi,sqrt

#BASELS PROBLEM
def basel(p_prec) : #the function used to carry out the basel problem, the paramters entered are the precision to which pi should be calculated

    #INITIALISING THE VARIABLES
  n=1
  x=0
  ans = 0
  count = 0

    #CALCULATING THE APPROXIMATION
  while ((pi - ans)> p_prec) :
    x= x + (1/n**2)
    ans = sqrt(x*6)
    n = n +1
    count = count + 1
  return ans,count

#TAYLORS EXPANSION  
def taylor(p_prec): #the function used to carry out the taylors expansion, the paramters entered are the precision to which pi should be calculated

    #INITIALISING THE VARIABLES
    x = 0
    count = 0
    ans = 0
    n=0
    
    #CALCULATING THE APPROXIMATION
    while (abs((pi-ans))> p_prec) :
        x = x + (((-1)**n)/(2*n+1))
        ans = x * 4
        count = count + 1
        n=n+1
    return ans,count

#WALLIS ALGORITHM
def wallis(p_prec): #the function used to carry out the Wallis algorithm, the paramters entered are the precision to which pi should be calculated

    #INITIALISING THE VARIABLES
    x=1
    n=1
    count = 0
    ans = 0

    #CALCULATING THE APPROXIMATION
    while ((pi - ans)>p_prec):
        x = x *(((2*n)**2)/((2*n-1)*(2*n+1)))
        ans =x*2
        count = count + 1
        n =n +1
    return ans,count

#SPIGOT ALGORITHM
def spigot(p_prec) : #the function used to carry out the Wallis algorithm, the paramters entered are the precision to which pi should be calculated

    #INTIALISING THE VARIABLES
    y = 1
    ans = 0
    count = 1

    #CALCULATING THE APPROXIMATION
    while ((pi-ans)>p_prec):
        x = 1
        n=1
        while(n<=count) :
            x = x * (n/(2*n + 1))
            n = n+ 1
        count = count + 1
        y = y + x
        ans = y * 2
    return ans,count

def race(precision,algorithm = []) : #This function runs each algorithm and sorts them according to the number of steps taken for the appoximation
  listAns = []
  for i in algorithm:
    a,b = i(precision)
    listAns.append((algorithm.index(i)+1,b))

  sorted_list =  sorted(listAns, key = lambda y: y[1])
  print_results(sorted_list)
  return sorted_list

def print_results(results=[]):
  for i in results:
    algorithm= i[0]
    steps=i[1]
    print("Algorithm ",algorithm, " finished in ", steps, " steps")
