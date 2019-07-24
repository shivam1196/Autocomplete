class TrieNode:
    def __init__(self):
        is_word = False
        childrens = {}




## Add a child node in this Trie

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()

    ## Initialize this Trie (add a root node)

    def insert(self, word):


        current_node = self.root


        for i in word:
            if i not in current_node.childrens :
                current_node.children[i] = TrieNode()

            current_node = current_node.children[i]


        current_node.is_word = True

    ## Add a word to the Trie

    def find(self, prefix):
        pass
## Find the Trie node that represents this prefix