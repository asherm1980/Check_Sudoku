# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 21:54:36 2022

@author: asher
"""

l=[]
f1=0
f2=0
f3=0
for i in range(0,9):
    s=input('Please enter number in row #' + str(i)+':')
    ls=[s[j] for j in range(0,len(s))]
    ls.sort()
    f1+=ls==['1','2','3','4','5','6','7','8','9']
    l.append(s)
ll=''
l2=[]
l3=[]
for i in range(0,9):
    for j in range(0,9):
       ll+=l[j][i]
    l2.append(ll)
    ls=[ll[j] for j in range(0,len(ll))]
    ls.sort()
    f2+=ls==['1','2','3','4','5','6','7','8','9']
    ll=''

for j in range(0,9):
    for i in range(0,9):
       ll+=l[i//3+3*(j//3)][i%3+3*(j%3)]
    l3.append(ll)
    ls=[ll[j] for j in range(0,len(ll))]
    ls.sort()
    f3+=ls==['1','2','3','4','5','6','7','8','9']
    ll=''     

s

if f1==9 and f2==9 and f3==9:
    print('YES')
else:
    print('NO')

'''295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672'''