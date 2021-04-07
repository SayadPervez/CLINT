import sys

def RUN(arg):
    print(f"""
$-$
import os
os.chdir('P://Songs//')
liplay(os.listdir())
""")

if len(sys.argv)>1:
    RUN(sys.argv[1])
