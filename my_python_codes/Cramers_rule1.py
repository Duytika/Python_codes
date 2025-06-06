#Cramer's Rule
'''[[a, b],
    [c, d]] Here (a*b) is named "first_term", and b*c is named "second_term". These functions are common for both 2X2 and 3X3 matrices


    
'''

def first_term(l):
    i=0
    count=1
    while i<len(l):
        count=count*l[i][i]
        i=i+1
    return(count)


#first_term()        
def second_term(l):
    i=0
    count=1
    while i<len(l):
        count=count*l[i][len(l)-(i+1)]
        i=i+1
    return(count)

#second_term()


def main_1(): #2X2 matrix
    d1= first_term(l1)-second_term(l1)
    d2= first_term(l2)-second_term(l2)
    d3= first_term(l3)-second_term(l3)
    print("The value of x is: ", d2/d1)
    print("The value of y is: ", d3/d1)

#main()
'''

def derterminant():
    pass

'''
#for 3X3 matrix
def slice_1():
    s=[]
    for i in range(3):
        l=[[a2,a3],  #Here the matrix should have been [[a2, b2, c2],[a3, b3, c3]]. But for useful purpose, I inverted it. XD
           [b2,b3],
           [c2,c3]]
        _l=[a1,b1,c1]
        l_slice=l.pop(i)
        l_new=((-1)**i)*(_l[i]*(first_term(l)-second_term(l)))
        s.append(l_new)
    return(sum(s))


def slice_2():
    s=[]
    for i in range(3):
        l=[[d2,d3], #Same inverted matrix.
           [b2,b3],
           [c2,c3]]
        _l=[d1,b1,c1]
        l_slice=l.pop(i)
        l_new=((-1)**i)*(_l[i]*(first_term(l)-second_term(l)))
        s.append(l_new)
    return(sum(s))

def slice_3():
    s=[]
    for i in range(3):
        l=[[a2,a3], #Inverted matrix
           [d2,d3],
           [c2,c3]]
        _l=[a1,d1,c1]
        l_slice=l.pop(i)
        l_new=((-1)**i)*(_l[i]*(first_term(l)-second_term(l)))
        s.append(l_new)
    return(sum(s))

def slice_4():
    s=[]
    for i in range(3):
        l=[[a2,a3], #Inverted matrix
           [b2,b3],
           [d2,d3]]
        _l=[a1,b1,d1]
        l_slice=l.pop(i)
        l_new=((-1)**i)*(_l[i]*(first_term(l)-second_term(l)))
        s.append(l_new)
    return(sum(s))


def main_2(): #For 3X3
    x=slice_2()/slice_1()
    y=slice_3()/slice_1()
    z=slice_4()/slice_1()
    print("x= ",x)
    print("y= ",y)
    print("z= ",z)

#main_2()



print("Hello! I am BoB(Brother of Beluga) and I can solve linear equations. :) ")
print(f"\n Press: \n (2) To solve linear equations in 2 variables. \n (3) To solve linear equations in 3 variables.")
choice=int(input("Enter choice: "))
if choice==2:
    print("Enter equations: (coefficient)x + (coefficient)y = (constant_term)")
    print("\n Equation(1): ")
    x1=int(input("Enter coefficient of x: "))
    y1=int(input("Enter coefficient of y: "))
    z1=int(input("Enter constant term: "))
    print(f"\t Equation(1):\t({x1})x + ({y1})y = ({z1})")

    print("\n Equation(2): ")
    x2=int(input("Enter coefficient of x: "))
    y2=int(input("Enter coefficient of y: "))
    z2=int(input("Enter constant term: "))
    print(f"\t Equation(2):\t({x2})x + ({y2})y = ({z2})")
    
    l1=[[x1, y1],
        [x2, y2]]
    l2=[[z1, y1],
        [z2, y2]]
    l3=[[x1, z1],
        [x2, z2]]

    main_1()


elif choice==3:
    print("Enter equations: (coefficient)x + (coefficient)y + (coefficient)z = (constant_term)")
    print("\n Equation(1): ")
    a1=int(input("Enter coefficient of x: "))
    b1=int(input("Enter coefficient of y: "))
    c1=int(input("Enter coefficient of z: "))
    d1=int(input("Enter constant term: "))
    print(f"\t Equation(1):\t({a1})x + ({b1})y + ({c1})z = ({d1}) ")
 
    print("\n Equation(2): ")
    a2=int(input("Enter Coefficient of x: "))
    b2=int(input("Enter coefficient of y: "))
    c2=int(input("Enter coefficient of z: "))
    d2=int(input("Enter constant term: "))
    print(f"\t Equation(2):\t({a2})x + ({b2})y + ({c2})z = ({d2}) ")

    print("\n Equation(3): ")
    a3=int(input("Enter coefficient of x: "))
    b3=int(input("Enter coefficient of y: "))
    c3=int(input("Enter coefficient of z: "))
    d3=int(input("Enter constant term: "))
    print(f"\t Equation(3):\t({a3})x + {b3})y + ({c3})z = ({d3}) ")
    
    main_2()

else:
    print("Oops! Something went wrong.")

    












      






#slice_1()
#slice_2()
#slice_3()
#slice_4()
    









