class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word):
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.isWord = True
    
    def startsWith(self, prefix):
        cur = self.root
        word = ''
        
        for c in prefix:
            word += c
            if c not in cur.children:
                return prefix
            cur = cur.children[c]
            if cur.isWord:
                return word
        return prefix
    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
            
        s = sentence.split(' ')
        for i in range(len(s)):
            s[i] = trie.startsWith(s[i])
            
        out = ' '.join(s)
        
        return out