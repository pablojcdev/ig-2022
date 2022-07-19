#### FIGURAS ####

def figura1(b):
    for f in range(0,b):
        for c in range(0,b):
            if f == c:
                print(" *", end="")
            else:
                print(" ", end="")
        print()
"""
 *    
  *   
   *  
    * 
     *
"""
        
figura1(5)

def figura2(b):
    for f in range(0,b):
        for c in range(0,b):
            if f+c == b-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
figura2(5)
"""
    *
   * 
  *  
 *   
*
"""
def figura3(b):
    for f in range(0,b):
        for c in range(0,b):
            if c==0:
                print("*", end="")
            else:
                print(" ", end="")
        print()
figura3(5)
"""
*    
*    
*    
*    
*    
*
"""
def figura4(b):
    for f in range(0,b):
        for c in range(0,b):
            if f==0:
                print("*", end="")
            else:
                print(" ", end="")
        print()
figura4(5) #*****

def figura5(b):
    for f in range(0,b):
        for c in range(0,b):
            if c==b-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
figura5(7)

"""
      *
      *
      *
      *
      *
      *
      *
"""
def figura5(b):
    for f in range(0,b):
        for c in range(0,b):
            if f==b-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
figura5(7)
"""
      
       
       
       
       
       
*******
"""

def figura6(b):
    for f in range(0,b):
        for c in range(0,b):
            if c==b//2:
                print("*", end="")
            else:
                print(" ", end="")
        print()
figura6(7)
"""
   *   
   *   
   *   
   *   
   *   
   *   
   *
"""
def figura7(b):
    for f in range(0,b):
        for c in range(0,b):
            if f==b//2:
                print("*", end="")
            else:
                print(" ", end="")
        print()
figura7(7)
"""
       
       
       
*******
       
       
"""
def figura7(b):
    for f in range(0,b):
        for c in range(0,b):
            if f<=c:
                print("*", end="")
            else:
                print(" ", end="")
        print()
figura7(7)

"""
*******
 ******
  *****
   ****
    ***
     **
      *
"""
def figura8(b):
    for f in range(0,b):
        for c in range(0,b):
            if f+c>=b-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
figura8(7)

"""
       
       
       
*******
*******
*******
*******
"""
print()
def figura9(b):
    for f in range(0,b):
        for c in range(0,b):
            #if f<=c+(b//2) and f>=c-(b//2) and f+c>=b-1-(b//2) and f+c<=b-1+(b//2):
            #if f<=c+(b//2) and f>=c-(b//2) and f+c>=b-1-(b//2) and f+c<=b-1+(b//2):
            if f<=c+(b//2) and f>=c-(b//2) and f+c<=b-1+(b//2) and f+c>=b-1-(b//2):    
                print("*", end="")
            else:
                print(" ", end="")
        print()
figura9(7)

#f<=c+(b//2) and f >=c-(b//2) and f+c<=b-1+(b//2) and f+c>=b-1-(b//2)





