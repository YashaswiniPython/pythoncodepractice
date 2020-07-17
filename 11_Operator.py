# Python file Created By Bibhuti

"""
Assign Ment operator
"""

# i=14;
# j=5;
# print(i/j);
# print(i//j);  # i devided by j result without taking value after decimal

# i=2;
# j=3;
# print(2*3);
# print(i**j);  # i to the power of j

"""
comparision operator
"""

# print(1==2);
# print(1=="1");
# print(1==1);
# print("hi"=="hi");
# print("ih"=="hi");
# print(True==1);
# print(False==1);


"""
Logical Operator
"""

# a=True;
# b=False;
# c=True;
# d=False;
#
# print(a and b);
# print(a and c);
# print(a or b);
# print(b or d);
# print(not a);

"""
Bitwise Logical Operator
"""

# a=7;    # 7 means 111 in binary
# b=5;    # 5 means 101 in binary
# print(a & b);   # if both bit is 1 then output is 1 otherwise 0
# print(a | b);   # any of the bit is 1 then output is 1 otherwise 0
# print(a ^ b);

"""
Assign ment operator
"""

# a=5;
# print(a);

# a=5;
# print(a);
# a+=6;       # a+=6 means a=a+6
# print(a);


"""
Identity Operator
"""
# use to check memory location are same or not

# a=12;
# b=12;
# print(a is b);

# a=12;
# b=13;
# print(a is b);

# a=12;
# b=13;
# print(a is not b);

"""
Memebership Operator
"""
# it is used to check a element present in the sequance or not

list=[1,2,"python"];
str="Python";
tuple=(1,2,"python");
set={1,2,"python"};
dic={
    1:"value of 1",
    4:"value of 4",
    "ab":"value of ab",
    3:2
}

# print(2 in list);
# print(2 not in list);
# print(3 in list);
# print("py" in list);
# print("python" in list);

# print("2" in str);
# print(3 in str);  # Error if int,float value present for checking with string
# print("Py" in str);
# print("Python" in str);
# print("yt" in str);

# print(2 in tuple);
# print(3 in tuple);
# print("py" in tuple);
# print("python" in tuple);

# print(2 in set);
# print(3 in set);
# print("py" in set);
# print("python" in set);

# print(3 in dic);
# print(2 in dic);
# print("b" in dic);
# print("ab" in dic)
# print("value of 1" in dic);

