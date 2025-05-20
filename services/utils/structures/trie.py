class Node:
    def __init__(self):
        self.children = dict()
        self.wordEnd = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        word = word.lower()
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        curr.wordEnd = True
    
    def search(self, word):
        word = word.lower()
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return None
            curr = curr.children[ch]
        return curr
    
    def autocomplite(self, prefix):
        res = [prefix]
        if len(prefix) < 1:
            return prefix
        w = self.search(prefix)
        if w is not None:
            self.DFSRecursive(w, prefix, res, prefix)
        
        return res
    
    def DFSRecursive(self, node, prefix, ls, prefixCopy):
        prefix = prefix.lower()
        if node is None:
            return
        
        if node.wordEnd:
            ls.append(prefix.replace(prefix[:len(prefixCopy)], prefixCopy))
        
        for ch in node.children:
            self.DFSRecursive(node.children[ch], prefix+ch, ls, prefixCopy)
 