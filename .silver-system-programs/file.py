import subprocess
class color():
   purple = '\033[95m'
   cyan = '\033[96m'
   darkcyan = '\033[36m'
   blue = '\033[94m'
   blued = '\033[92m'
   yellow = '\033[93m'
   red = '\033[91m'
   silver = '\033[3;30;47m'
   orange= '\033[31;43m'
   bold = '\033[1m'
   green = '\033[32m'
   underline = '\033[4m'
   end = '\033[0m'
ch = 'Y'
while ch == 'Y':
	path = input(color.purple+'Enter path of folder:\t'+color.end)
	subprocess.run(['ls',path])
	ch = input(color.darkcyan+'Do you want to continue(Y/n):\t'+color.end)
