from Orgnode import myorgnode
import json

filename = "1.org"
nodetree = myorgnode.maketree(filename)
nodelist = myorgnode.makelist(filename)

json_data_list = myorgnode.toJSON(nodelist)
print "list\n"
print json_data_list

print "======================="
json_data_tree = myorgnode.toJSON(nodetree)
print "tree\n"
print json_data_tree


