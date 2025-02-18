

class -- The class is Blue print for creating object 


Student -  name , age , gender , get_name(), get_age()

initialise = Student()

initialise.name
initialise.get_name()




inheritance 


The Child class is derived from Base class , and it is having (inherits ) all properties of base class


class A():
    pass

class B(A):
    Super()



Encapsulation:

    Protecting the attributes 

__ 


Polymorphism:

multiple class having same method names . Method overriding 


---------------

Abstraction 

class A(ABC)

    @abstractmethod
    def ab_method():
        pass

    password 


class ConnectMSSQL(A):
    def ab_method():
        user_name


 class ConnectMySQL(A):
    def ab_method():
        user_name   
    
 class ConnectMySQL(A):
    def ab_method():
        user_name  



-----------------------


Single  - 
Multiple

class A()
    PASS
class B()
    pass

 #Child is derived from multiple base class
class c(A, B)
    pass


------

multi level
class A()
    PASS
class B(A)
    pass

class C(B)
    pass

class D(C)
    pass

---------------

Hybrid Inheritance 

class A()
    PASS
class B(A)
    pass

class C(B, A)
    pass

class D(C)
    pass


---------------

class A()
    PASS
class B(A)
    pass
class C(A)
    pass

class D(A)
    pass







