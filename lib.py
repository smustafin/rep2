import requests
import json
log="smustafin"
pasw="12as34df"
host="https://api.github.com/"
nameorg="orgtest1"
def delete(user):
 reqq='orgs/%s/members/%s' % (nameorg,user)
 ur=host + "%s" % (reqq)
 r = requests.delete(ur, auth=(log,pasw))
 if r.status_code==204:
  resp="User "+user+" was deleted"
 else:
  resp="Error "+ r.headers['status']  
 return resp
#user=raw_input("Pass username: ") 
#print delete(user)

