import requests
import json
log="smustafin"
pasw="12as34df"
user="smustafin"
reqq=""
user=raw_input("Pass username: ")
while 1:
 try:
  ch=input("""Pass 1 and Enter for show info about user\nPass 2 and Enter for show user`s repos\n""")
  if ch==1: 
   reqq='/users/%s' % (user)  
   break
  if ch==2: 
   reqq='/users/%s/repos' % (user) 
   print "wait..."
   break
  print "Pass again...."
 except NameError:  
  print "Pass again...."
 except SyntaxError:  
  print "Pass again...."
print "wait..."
host="https://api.github.com%s" % (reqq)
r = requests.get(host, auth=(log,pasw))
print r.headers['content-type']
print "\n"
print r.content
print "\n"
# all content divided on small part )
slov=json.loads(r.content)
try:
 print "email=", slov['email']
except KeyError:
 print "Not found"
#weiuweoriuweior
 
