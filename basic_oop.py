# -*- coding: utf-8 -*-
"""Basic OOP

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cFUUIjX0_zmottl5HXCFZyNqbbOhn78M
"""

class Dog:
  def __init__(self,name,age): # Similar to as java constructor, where you pass the initial attributes while creating a class
    self.name=name # No need to create variables before defining the constructor(As we do in java), self.v creates the variable v 
    self.age=age

  def printInfo(self): #use self keyword in every function, its similar to as 'this'
    print("Name of the Dog is "+ self.name + ", Age is: "+ str(self.age)+".") # to access the variables, use this.v

dog1=Dog("Lame",20)
dog1.printInfo()
dog1.age=5 # attributes can be changed from outside
dog1.printInfo()

class Dog:
  def __init__(self,name,age): # Similar to as java constructor, where you pass the initial attributes while creating a class
    self.name=name # No need to create variables before defining the constructor(As we do in java), self.v creates the variable v 
    self.age=age

  def printInfo(self): #use self keyword in every function, its similar to as 'this'
    print("Name of the Dog is "+ self.name + ", Age is: "+ str(self.age)+" , Height is: "+ str(self.height)+".") # to access the variables, use this.v 

  def birthday(self):
    self.age +=1

  def getHeight(self,height):
    self.height=height

dog2=Dog("Lame",20)
dog2.getHeight(10)
dog2.printInfo()

dog2.birthday()
dog2.printInfo()



"""## #Operation Between two numpy arrays"""

#general approach

import numpy as np

def multiply(a,b):
  c=a*b
  return c

def add(a,b):
  c=a+b
  return c

def diff(a,b):
  c=a-b
  return c

a=np.random.random((5,5))
b=np.random.random((5,5))
print(multiply(a,b))
print(add(a,b))
print(diff(a,b))

#OOP approach


class matrix:
  import numpy as np
  def __init__(self,size1,size2):
    self.size1=size1
    self.size2=size2
    self.a=np.random.random((size1,size1))
    self.b=np.random.random((size2,size2))

  def multiply(self):
    c=self.a * self.b 
    return c
  def add(self):
    c=self.a+self.b
    return c

mat=matrix(5,5)
print(mat.multiply())





"""## Gaussian Method"""

class gausssian:
  import numpy as np
  def __init__(self,A,B,d):
    self.A=A
    self.B=B
    self.d=d
    self.x=np.append(A,B,axis=1)
    self.n=A.shape[0]


  def solver(self):
    if(self.coincident()==True):
      return
    elif(self.parallel()==True):
      return

    #partial pivot 
    for j in range(0,self.n):
        
        
        for p in range(j+1,self.n):
            if(self.x[p][j]>self.x[j][j]):
                self.x[[j,p]]=self.x[[p,j]]
        
       
            
        i=j+1
            
        for i in range(i,self.n):
            self.x[i]=self.x[i]-self.x[j]*self.x[i][j]/self.x[j][j]
            if(self.d==1):   
                self.A,self.B=self.x[:,:self.n],self.x[:,self.n]
                print("Matrix A after eliminating column: ",j, ", row:  ",i)
                print(self.A)
                print("Matrix B after eliminating column: ",j, ", row:  ",i)
                print(self.B)
                print('\n')
        
            result=np.zeros((self.n,))
  
        for index in range(self.n-1,-1,-1):
            res=0
            for i in range(index,self.n-1):
               res=res+ result[i+1]*self.x[index][i+1]
            
               
            result[index]=(self.x[index][self.n]-res)/self.x[index][index]

          
    print("Final Output: ")
    for res in result:
        print(res)    





  def coincident(self):
    for i in range(0,self.n):
        for j in range(i+1,self.n):
            p=self.x[i]/self.x[j]
            if(np.all(p==p[0])):
                print("INFINITE SOLUTION")
                return True

    return False

  def parallel(self):
    for i in range(0,self.n):
        for j in range(i+1,self.n):
            p=self.x[i]/self.x[j]
            if(np.all(p[:-1]==p[0])==True and np.all(p[:]==p[0])==False):
                print("NO SOLUTION")
                return True
    return False

A=np.array([[1,2,3],[4,5,1],[7,5,3]])
B=np.array([10,15,30]).reshape((3,1))

solve=gausssian(A,B,1)
solve.solver()

