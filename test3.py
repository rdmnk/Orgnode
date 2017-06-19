import Orgnode.Orgnode
import json

filename1 = "1.org"
nodetree1 = Orgnode.Orgnode.maketree(filename1)

filename2 = "2.org"
nodetree2 = Orgnode.Orgnode.maketree(filename2)

nodetree3 = Orgnode.Orgnode.jointrees('top', [nodetree1, nodetree2])

json_data_tree = Orgnode.Orgnode.toJSON(nodetree3)
print json_data_tree


