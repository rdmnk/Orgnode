import Orgnode.Orgnode
import json

filename = "/home/roma/projects/pyOrgmode/1.org"
nodelist = Orgnode.Orgnode.makelist(filename)

json_data3 = Orgnode.Orgnode.toJSON(nodelist)

print json_data3
