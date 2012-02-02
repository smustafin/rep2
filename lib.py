import requests
import json
try:
    f=open('conf','r')
except IOError:
    print "File 'conf' not found"
    exit()
lin=f.readlines()
f.close()
st=lin[0].split("=")[1]
login=st[0:len(st)-1]
st=lin[1].split("=")[1]
passw=st[0:len(st)-1]
st=lin[2].split("=")[1]
org_name=st[0:len(st)-1]
try:
    tm1,tm2,tm3=login, passw, org_name
except NameError:
    print "Bad srtucture 'conf' file"
    exit()
host="https://api.github.com/"
#delete user from org
def del_from_org(user):
    reqq='orgs/%s/members/%s' % (org_name,user)
    url=host + reqq
    r = requests.delete(url, auth=(login,passw))
    if r.status_code==204:
        res="User "+user+" was deleted"
    else:
        res="Error "+ r.headers['status']  
    return res
#create team
def create_team(team_name,permission,repo_name):
    reqq = 'orgs/%s/teams' % org_name
    url = host + reqq
    try:
        r = requests.post(url,auth = (login,passw),data = '{"name":"%s", "repo_names":["%s/%s"], "permission":"%s"}' % (team_name,org_name,repo_name,permission))
    except r.status_code != 201:
        return "Error "+ r.headers['status']
    else:
        return "%s was created" % team_name
# create repo
def create_repo(namerep,descrip): #without private
    #tmp=private
    #if (tmp<>"true"):
    # if (tmp<>"false"):
    #  print "Second parametr could be 'true' or 'false'"
    # else: 
    reqq='orgs/%s/repos' % (org_name)
    url=host + reqq
    tmp='{"name":"%s","description":"%s"}' % (namerep,descrip)
    r = requests.post(url, auth=(login,passw),data=tmp)
    if r.status_code==201:
        res="Done!!! Repo '%s' created" % (namerep)
        # creat 3 teams
        create_team(namerep,"pull",namerep)
        create_team(namerep+"-guests","push",namerep)
        create_team(namerep+"-owners","admin",namerep) 
    else:
        res="Error "+ r.headers['status']  
    return res
#search id_team by name
def search_id_team(team_name):
    reqq='orgs/%s/teams' % (org_name)
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
#  delete member from org
def del_from_team(user,team_name):
    #/teams/:id/members/:user
    if search_id_team(team_name)=="Team not found":
        return "Team not found"
    reqq='teams/%s/members/%s' % (str(search_id_team(team_name)),user)
    url=host + reqq
    r = requests.delete(url, auth=(login,passw))
    if r.status_code==204:
        res="User '"+user+"' was deleted from team '"+team_name+"'"
    else:
        res="Error "+ r.headers['status']  
    return res
#print search_id_team("Owners")
