import requests, sys
 
server = "http://rest.ensembl.org"
ext = "/sequence/id/ENSG00000157764?"

hdrs={ "Content-Type" : "text/plain"}

r = requests.get(server+ext, headers=hdrs)

if not r.ok:
    r.raise_for_status()
    sys.exit()
 
print r.text
