import os
from subprocess import check_output

currentPath = os.getcwd()
print(currentPath)
cmd = "cd com\\behave && behave"
os.system(cmd)


