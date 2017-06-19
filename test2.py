import Orgnode.Orgnode
import json

filename = "/home/roma/myhelp/org/notes.org"
nodetree = Orgnode.Orgnode.maketree(filename)

json_data_tree = Orgnode.Orgnode.toJSON(nodetree)
print json_data_tree


