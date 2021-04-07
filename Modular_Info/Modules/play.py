from subprocess import check_output
import sys
sys.path.insert(0,'P:\Pvz_Program_Files\Drag_On_Program_Files\Drag_On_Spec_Functions')
import Pvz_Functions as P
from Modular_Functions import *

def navigate():
    os.chdir("P:\\Songs")

def RUN(arg):
    arg=P.akapi(remSymb(arg))
    arg,rets=segregate(arg,keys(['and','then']),['play','close'])
    possibleOutcomes=[]
    songName=remSymb(arg[arg.index('play')+5:].lower())    # sn => songName
    try:
        a=songName.split(" ")
        if a==songName:
            raise Exception("null")
    except Exception as e:
        a=[]
    try:
        b=songName.split("-")
        if b==songName:
            raise Exception("null")
    except Exception as e:
        b=[]
    try:
        c=songName.split("_")
        if c==songName:
            raise Exception("null")
    except Exception as e:
        c=[]
    try:
        d=songName.split(".")
        if d==songName:
            raise Exception("null")
    except Exception as e:
        d=[]
    sn=list(set(a+b+c+d))
    navigate()
    allSongs=[(os.listdir()[_]).lower() for _ in range(len(os.listdir()))]
    m=len(sn)
    n=len(allSongs)
    i,j=0,0
    while(i<m):
        while(j<n):
            if sn[i] in allSongs[j]:
                possibleOutcomes.append(allSongs[j])
            j+=1
        i+=1
    matchCount=[]
    for _ in range(len(possibleOutcomes)):
        m=0
        for __ in range(len(sn)):
            if(sn[__] in possibleOutcomes[_]):
                m+=1
        matchCount.append(m)
    try:
        toPlay=(possibleOutcomes[matchCount.index(max(matchCount))])
        hell=check_output(f'{toPlay}',shell=True,timeout=1)
        print(f'Streaming {toPlay}\n%-%-%'+rets)
        exit()
    except Exception as e:
        try:
            toPlay=(possibleOutcomes[matchCount.index(max(matchCount))])
            hell=check_output(f'{toPlay}',shell=True,timeout=1)
            print(f'Streaming {toPlay}\n%-%-%'+rets)
            exit()
        except Exception as e:
            try:
                toPlay=(possibleOutcomes[matchCount.index(max(matchCount))])
                hell=check_output(f'{toPlay}',shell=True,timeout=1)
                print(f'Streaming {toPlay}\n%-%-%'+rets)
                exit()
            except Exception as e:
                print(e)


if len(sys.argv)>1:
    RUN(sys.argv[1])
