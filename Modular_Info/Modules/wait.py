###############################################################################################################################################
'''$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   PRE-REQUIREMENTS   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'''
###############################################################################################################################################
import sys
sys.path.insert(0,'P:\Pvz_Program_Files\Drag_On_Program_Files\Drag_On_Spec_Functions')
import Pvz_Functions as P
from Modular_Functions import *

'''$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   PRE-REQUIREMENTS   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'''

def RUN(arg):

    arg=P.akapi(remSymb(arg))
    arg,rets=segregate(arg,keys('then'),['wait','for'])
    while("half an" in arg):
        arg=arg.replace("half an","0.5")
    while("half a" in arg):
        arg=arg.replace("half a","0.5")
    while("half" in arg):
        arg=arg.replace('half','0.5')
    li=arg.split(' ')
    n=li.count('')
    for _ in range(n):
        li.remove("")
    for _ in range(len(li)):
        if(li[_]=="a"):
            li[_]=li[_].replace(li[_],'1')
        if(li[_]=="an"):
            li[_]=li[_].replace(li[_],'1')
        if(li[_]=="quarter"):
            li[_]=li[_].replace(li[_],'0.25')

    s,m,h=0,0,0
    x=li.count("hrs")
    y=li.count('mins')
    z=li.count('secs')
    if(x==y==z==0):
        import re
        import time
        time.sleep(float(re.findall(r'[-+]?\d*\.\d+|\d+',arg)[0]))
        print(f"""
$-$ %-%-%{rets}""")

    else:
        for _ in range(max(x,y,z)):
            if ('secs' in li):
                q=float(li[li.index('secs')-1])
                li[li.index('secs')]=li[li.index('secs')].replace(li[li.index('secs')],"!!!")
                s+=q
            if ('mins' in li):
                q=float(li[li.index('mins')-1])
                li[li.index('mins')]=li[li.index('mins')].replace(li[li.index('mins')],"!!!")
                m+=q
            if ('hrs' in li):
                q=float(li[li.index('hrs')-1])
                li[li.index('hrs')]=li[li.index('hrs')].replace(li[li.index('hrs')],"!!!")
                h+=q
        print((h*3600)+(m*60)+s)
        import time
        time.sleep((h*3600)+(m*60)+s)
        print(f"""
$-$ %-%-%{rets}""")



if len(sys.argv)>1:
    RUN(sys.argv[1])
