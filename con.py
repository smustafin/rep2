import requests
import json
log="smustafin"
pasw="12as34df"
res=""
while 1:
 try:
  ch=input("""Pass 1 and Enter for show info about user\nPass 2 and Enter for show user`s repos\n""")
  if (ch==1)|(ch==2): 
   break
  print "Pass again...."
 except NameError:  
  print "Pass again...."
 except SyntaxError:  
  print "Pass again...."
while res!="Done":
 user=raw_input("Pass username: ")
 if ch==1:
   reqq='/users/%s' % (user)  
 if ch==2: 
   reqq='/users/%s/repos' % (user)
 print "wait..."
 host="https://api.github.com%s" % (reqq)
 r = requests.get(host, auth=(log,pasw))
 slov=json.loads(r.content)
 try:    
  if slov['message']!="":
   print "username ",slov['message']
   res="Fail"
 except KeyError:
  res="Done"
 except TypeError:
  res="Done" 
print
print r.content
#weiuweoriuweior
 
