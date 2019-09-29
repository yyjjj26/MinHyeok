# 1주차 코딩 과제 - 산모양 별 찍기

a = int(input())

for i in range(a):
    print("o"*(a-1-i)+"*"*(2*i+1))
