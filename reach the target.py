"""Reach The Target
In a specific game, list of player-names, respective points scored by the players and Target-score has been given.
print any two player names whose sum of scores is equal to the given target.

Example:
Given players=['abc','pqr','xyz','jhg'] scores = [2, 7, 11, 15], target = 9,

Because scores[0] + scores[1] = 2 + 7 = 9,
print players[0],players[1] i.e. abc pqr

Input format
First line contains the number of players in the game.
next line contains the player names space separated
next line contains the respective scores space separated
next line is the target score

Output format
print the names of the players whose sum of the scores reach to the target(space separated), else print "None"

Input
4
abc pqr mno xyz
25 64 100 200
300
Output
mno xyz
----------------
Input
4
abc pqr xyz mno
25 36 89 78
100
Output
None
""" import numpy
no_players=int(input())
a=input().split(' ')
b=input().split(' ')
target=int(input())
flag=0
for i in range(0,no_players):
    j=no_players-1
    while(j>i):
        if(int(b[i])+int(b[j])==target):
            print(str(a[i])+" "+str(a[j]))
            flag=1
            j=j-1
        else:
            j=j-1
    
if(flag==0):
    print('None')   