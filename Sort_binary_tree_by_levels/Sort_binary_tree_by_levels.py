def tree_by_levels(node):
    if node:
        return [i.value for i in [node] + children(node) + gen(children(node))]
    return []

def gen(anc):
    if anc != []:
        ret = []
        for nod in anc:
            if nod:
                ret += children(nod)
        return ret + gen(ret)
    return []


def children(node):
    if node:
        firstgen = []
        if node.left:
            firstgen.append(node.left)
        if node.right:
            firstgen.append(node.right)
        return firstgen
    return []
