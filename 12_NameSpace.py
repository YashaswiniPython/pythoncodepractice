# Python file Created By Bibhuti

# Based on the value its change adress

# a=2;
# b=3;
# c=2;

# print(id(a));
# print(id(b));
# print(id(c));   # adress of a and c is same because value is same

# print(id(2));
# print(id(2));

# a=12;
# def outer():
#     b=13;
#     print("Outer Function");
#     def inner():
#         c=14;
#         print("Inner Function");
#         print(a,b,c);
#     inner();
#     # print(a,b,c); # Inner Function variable acessing is not possible without global keyward
# outer();

# def m1():
#     return lambda a:print(a+5);
#
# m1()(10);

# def m1():
#     print("Hii");
#     return 10;
#
# def m2():
#     print("Hello");
#     return m1;
#
# print(m2());
# print(m2()());

