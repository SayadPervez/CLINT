import sys
sys.path.insert(0,'P:\Pvz_Program_Files\Drag_On_Program_Files\Drag_On_Spec_Functions')
import Pvz_Functions as P
from Modular_Functions import *
from getpass import getpass as gp
import subprocess

def RUN(arg):
    arg,ret=segregate(arg,keys(['and','then',',']),'flushdns')
    os.chdir("P:\\Pvz_Program_Files\\Other programs\\")
    subprocess.getoutput('python "flushDns.py"')
    print(ret)

if len(sys.argv)>1:
    RUN(sys.argv[1])
else:
    RUN("flushdns")
