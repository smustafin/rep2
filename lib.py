import requests
import json
try:
    f=open('conf','r')
except IOError:
    print "File 'conf' not found"
    exit()
lin=f.readlines()
f.close()
if lin[0][0:6]=="login=":
    login=lin[0][6:]
if lin[1][0:5]=="pass=":
    passw=lin[1][5:]
if lin[2][0:9]=="org_name=":
    nameorg=lin[2][9:]
try:
    tm1,tm2,tm3=login, passw, nameorg
    print tm1,tm2,tm3
except NameError:
    print "Bad srtucture 'conf' file"
    exit()
host="https://api.github.com/"
login, passw, nameorg="smustafin","12as34df","orgtest1"
#delete user from org
def del_from_org(user):
    reqq='orgs/%s/members/%s' % (nameorg,user)
    url=host + reqq
    r = requests.delete(url, auth=(login,passw))
    if r.status_code==204:
        resp="User "+user+" was deleted"
    else:
        resp="Error "+ r.headers['status']  
    return resp
#user=raw_input("Pass username: ") 
#print delete(user)
#create team\
def create_team(team_name,permission,repo_name):
    reqq = 'orgs/%s/teams' % nameorg
    url = host + reqq
    try:
        r = requests.post(url,auth = (login,passw),data = '{"name":"%s", "repo_names":["%s/%s"], "permission":"%s"}' % (team_name,nameorg,repo_name,permission))
    except r.status_code != 201:
        return "Error "+ r.headers['status']
    else:
        return "%s was created" % team_name
# create repo
def create_repo(namerep,descrip): #withot private
    #tmp=private
    #if (tmp<>"true"):
    # if (tmp<>"false"):
    #  print "Second parametr could be 'true' or 'false'"
    # else: 
    reqq='orgs/%s/repos' % (nameorg)
    url=host + reqq
    tmp='{"name":"%s","description":"%s"}' % (namerep,descrip)
    r = requests.post(url, auth=(login,passw),data=tmp)
    if r.status_code==201:
        res="Done!!! Repo '"+namerep+"' created"
        # creat 3 teams
        create_team(namerep,"pull",namerep)
        create_team(namerep+"-guests","push",namerep)
        create_team(namerep+"-owners","admin",namerep)
  
    else:
        res="Error "+ r.headers['status']  
    return res
#search id_team by name
def search__id_team(team_name):
    reqq='orgs/%s/teams' % (nameorg)
    url=host + reqq
    r = requests.get(url, auth=(login,passw))
    cont=json.loads(r.content)
    i=0    
    while 1:
        try:
            if cont[i]['name']==team_name:
                break
            i+=1
        except IndexError:
            return "Team not found"            
    return cont[i]['id']  
#  
def del_from_team(team_name):
    #/teams/:id/members/:user
    #reqq='teams/%s/members/'+user % (id_team)
    #url=host + reqq
    #r = requests.delete(url, auth=(login,passw))
    return
print search__id_team("repoooooooo-owners")
    

