test_sttring="there are 2 bananas and 5 apples in 1 basket"
L1=[]
for i in test_sttring:
    if i.isdigit():
        if i not in L1:
            L1.append(int(i))
print(sorted(L1))