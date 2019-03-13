#https://www.hackerearth.com/practice/algorithms/searching/ternary-search/practice-problems/algorithm/small-factorials/
for i in range(int(input())):
    num = int(input())
    factorial = 1
    for j in range(1,num+1):
        factorial *= j
    print (factorial)