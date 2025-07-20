class TrieNode():
    def __init__(self):
        self.children = {}
        self.take = False

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root  = TrieNode()
        seen = defaultdict(list)

        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = TrieNode()
                node = node.children[folder]
        print(root.children.keys())

        def dfs(node):
            if not node.children:
                return ""
            serials = []
            for name in sorted(node.children):
                serials.append(name + '(' + dfs(node.children[name]) + ')' )
            serial = ''.join(serials)
            print(serial)
            seen[serial].append(node)
            return serial
            
        dfs(root)
        
        for nodes in seen.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.take = True
                
        res = []

        def collect(node,path):
            for name,child in node.children.items():
                if child.take:
                    continue
                path.append(name)
                res.append(list(path))
                collect(child,path)
                path.pop()
        
        collect(root,[])
        return res