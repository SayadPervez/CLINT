#               PLUS
import sys
sys.path.insert(0,'P:\Pvz_Program_Files\Drag_On_Program_Files\Drag_On_Spec_Functions')
import Pvz_Functions as P
file="P:\\Pvz_Program_Files\\Common trial notepad file.txt"
import re
from Modular_Functions import *#

def RUN(arg):
    arg,ret=segregate(arg,keys(),'plus')

    i=arg.index("plus")
    pre_=arg[:i]
    post_=arg[i+4:]
    pre=re.findall(r'[-+]?\d*\.?\d+|[-+]?\d+',pre_)
    post=re.findall(r'[-+]?\d*\.?\d+|[-+]?\d+',post_)
    pre=[float(i) for i in pre]
    post=[float(i) for i in post]

    result = float(sum(pre)) + float(sum(post))
    print(str("")+str(result)+" "+str(ret))


if len(sys.argv)>1:
    RUN(sys.argv[1])
