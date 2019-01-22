global index = 0

def kToLast(root, k):
    if root.next == None:
        return None
    else:
        node = kToLast(root.next, k)
        index += 1
        if index == k:
            return root
        return node
