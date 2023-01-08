import os
username = 'Jack'
#os.chdir(r'C:\Users\Trillion\Desktop\Hercules\DailyRead\DailyRead')
#os.system("scrapy crawl project --nolog")
print('Hello ' + username)
print('Loading up your daily read .....')
urls = []
with open('/home/cuckoo/urls.txt','r') as handle:
    urls = handle.readlines()
v = 1
for read in urls:
    print('['+str(v)+'] Article : ' + read + '  ')
    v += 1