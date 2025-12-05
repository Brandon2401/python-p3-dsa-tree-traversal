# lib/tree.py

class Tree:
    def __init__(self, root):
        """
        Initialize the tree with a root node.
        The root node should be a dict with keys:
        'tag_name', 'id', 'text_content', 'children'
        """
        self.root = root

    def get_element_by_id(self, target_id):
        """
        Depth-first search (DFS) for a node with the given id.
        Returns the node dict if found, else None.
        """
        def dfs(node):
            if node['id'] == target_id:
                return node
            for child in node.get('children', []):
                result = dfs(child)
                if result:
                    return result
            return None
        
        return dfs(self.root)

    def get_element_by_id_bfs(self, target_id):
        """
        Breadth-first search (BFS) for a node with the given id.
        Returns the node dict if found, else None.
        """
        nodes_to_visit = [self.root]

        while nodes_to_visit:
            node = nodes_to_visit.pop(0)
            if node['id'] == target_id:
                return node
            nodes_to_visit.extend(node.get('children', []))
        
        return None
