import xmlrpclib
import libvirt
SPACE='ITST'
TOP_PAGE='Home' #name top page
WIKI_USER='smustafin'
WIKI_PASS='12as34df'
p = "h1." + "TEST" + "\n"
p = p + "||id||date||title||author||samary||\n"
# cycle for, or while 
vm={
		"id":"00000",# value data sqlite
		"date":"000001we12",
		"title":"12000002",
		"author":"qweqw",
		"samary":"sdf0000gsdf"
	} 
p=p+"|["+vm["id"]  + "|" + vm["date"]+"|"+vm["title"]+"|"+vm["author"]+"|"+vm["samary"]+"|\n"
#end cycle
print p

host = "Well Done Python 222" # name news
print host

server = xmlrpclib.ServerProxy('https://wiki.griddynamics.net/rpc/xmlrpc');
token = server.confluence1.login(WIKI_USER, WIKI_PASS);
print token
try:
	page = server.confluence1.getPage(token, SPACE, host); 
	# if page no exists, then go to except
	
except:
	parent = server.confluence1.getPage(token, SPACE, TOP_PAGE); #create page
	page={
		'parentId': parent['id'],
		'space': SPACE,
		'title': host,
		'content': p
		 }
	server.confluence1.storePage(token, page);
else:
	page['content'] = p; #continue try (if page exists)
	server.confluence1.updatePage(token, page,{'versionComment':'','minorEdit':1});
	#weelll done)))) 
