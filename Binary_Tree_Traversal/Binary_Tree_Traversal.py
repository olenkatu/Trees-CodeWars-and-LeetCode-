# Pre-order traversal
def pre_order(node):
    if node:
        return [node.data] + pre_order(node.left) + pre_order(node.right)
    return []

# In-order traversal
def in_order(node):
    if node:
        return in_order(node.left) + [node.data] + in_order(node.right)
    return []

# Post-order traversal
def post_order(node):
    if node:
        return post_order(node.left) + post_order(node.right) + [node.data]
    return []
