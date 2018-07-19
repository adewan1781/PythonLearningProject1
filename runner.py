# pip install -U allure-behave
# pip install -U json2html

import os

currentPath = os.getcwd()
print(currentPath)
cmd = "cd com//behave && behave -t @add,@sub,@div,@mul --junit"
os.system(cmd)
