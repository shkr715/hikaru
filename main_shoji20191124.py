import urllib2
import time
import sys

def query(url):
	res = urllib2.urlopen(url)
	return res.read()

token = "Z7tBMvakiKcLl7TLCp0VC0y4ctmQ8pPl"

#for i in range(0, 2):
str    = sys.argv[1]
url    = "https://runner.team-lab.com/q?token=%s&str=%s" % (token, str)
result = query(url)

print result
print(len(str))

file = "result.txt"
with open(file, mode="a+") as f:
  f.writelines(str + " " + result + "\n")

time.sleep(1)
