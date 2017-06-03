import Orgnode.Orgnode
import json

filename = "1.org"
nodetree = Orgnode.Orgnode.maketree(filename)
nodelist = Orgnode.Orgnode.makelist(filename)

json_data_list = Orgnode.Orgnode.toJSON(nodelist)
print "list\n"
print json_data_list

print "======================="
json_data_tree = Orgnode.Orgnode.toJSON(nodetree)
print "tree\n"
print json_data_tree


