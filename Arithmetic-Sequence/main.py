q = int(input("Enter first number in the sequnce: "))
w = int(input("Enter second number in the sequnce: "))
b = [q, w]
# b is an Arithmetic sequece 

a = b[0]
# a is the First term is the sequence
l = 0
# l is the last term in the sequence
n = 0
# n is the no. of terms in the sequence 
d = b[1] - b[0]
# d is common difference of the sequence
tn = 0
# tn is the sequence

r = int(input("Choose an option 1) to get tn 2) to get n : "))

if r == 1:
    n = int(input("Enter the term number: "))
    tn = a + (n - 1) * d 
    print(tn)
else:
    l = int(input("Enter the sequence: "))
    n = ((l - a) / d) + 1
    print(n)
