class D:
    def __init__(self):
        print("Cons D");

    def m4(self):
        print("Hello-D")

class B(D):
    def __init__(self):
        print("B");
        super(B,self).__init__();
        print("Cons B");

    def m2(self):
        print("Hello")

class A(D):
    def __init__(self):
        print("A");
        super(A,self).__init__();
        print("Cons A");

    def m1(self):
        print("Hii")

class E(D):
    def __init__(self):
        print("E");
        # super(E,self).__init__();
        print("Cons E");

    def m6(self):
        print("H--m6")

class C(A,E,B):
    def __init__(self):
        print("C");
        super(C,self).__init__();
        print("Cons C");

    def m3(self):
        print("Hello-B")

C();