from __future__ import print_function
import time
#global numTicks
def drop_bomb(arr,r,lt,rt,flag):        #function made to plant the bomb at its initial position and make a flag to remember whether a bomb is active or not
    for i in range(0,4):
        arr[r][lt+i] = 3
        arr[r+1][lt+i] = 3
    flag = 0
    return flag  
def checkBomber(arr,r,lt,rt,row,Lt,Rt): #function made to check whether the bomberman is in the vicinity of the bomb when it explodes so that the game can be called over
    flag = 0
    if r == row and (lt == Lt or lt-4 == Lt or rt+1== Lt): #r->bombRow; lt->bombLt; rt->bombRt ;row->bomberMan's row ;Lt->bMan's Lt ;Rt->bMan's Rt
        flag = 1
    if r-2 == row and lt == Lt:
        flag = 1
    if r+2 == row and lt == Lt:
        flag = 1
    return flag
def checkEnemy(arr,r,lt,rt,row,Lt,Rt):
    flag = 0
    for i in range(0,4):
        if r == row[i] and (lt == Lt[i] or lt-4 == Lt[i] or rt+1== Lt[i]): #r->bombRow; lt->bombLt; rt->bombRt ;row->bomberMan's row ;Lt->bMan's Lt ;Rt->bMan's Rt
            for j in range(0,4):
                arr[row[i]][Lt[i]+j] = " "
                arr[row[i]+1][Lt[i]+j] = " "
            flag += 1
            row[i] = -1                                          #corresponding coordinates made -1 so that we can keep track of it
            Rt[i] = -1
            Lt[i] = -1
        if r-2 == row[i] and lt == Lt[i]:
            for j in range(0,4):
                arr[row[i]][Lt[i]+j] = " "
                arr[row[i]+1][Lt[i]+j] = " "
            flag += 1
            row[i] = -1                                          #corresponding coordinates made -1 so that we can keep track of it
            Rt[i] = -1
            Lt[i] = -1
        if r+2 == row[i] and lt == Lt[i]:
            for j in range(0,4):
                arr[row[i]][Lt[i]+j] = " "
                arr[row[i]+1][Lt[i]+j] = " "
            flag += 1
            row[i] = -1                                          #corresponding coordinates made -1 so that we can keep track of it
            Rt[i] = -1
            Lt[i] = -1
    
    return flag
    
    


    