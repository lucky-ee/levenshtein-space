class BKNode:
    def __init__(self, word: str):
        self.word = word
        self.children = {}

class BKTree:
    def __init__(self, distance_func):
        self.root = None
        # We pass the distance function in so the tree doesn't care 
        # if we use Levenshtein, Hamming, or anything else!
        self.distance_func = distance_func
        
    def add(self, word: str):
        if self.root is None:
            self.root = BKNode(word)
            return
            
        current = self.root
        while True:
            dist = self.distance_func(current.word, word)
            if dist == 0:
                return 
                
            if dist in current.children:
                current = current.children[dist]
            else:
                current.children[dist] = BKNode(word)
                break
                
    def search(self, query: str, tolerance: int) -> list:
        results = []
        if self.root is None:
            return results
            
        candidates = [self.root]
        
        while candidates:
            node = candidates.pop()
            dist = self.distance_func(node.word, query)
            
            if dist <= tolerance:
                results.append((dist, node.word))
                
            lower_bound = dist - tolerance
            upper_bound = dist + tolerance
            
            for edge_dist, child_node in node.children.items():
                if lower_bound <= edge_dist <= upper_bound:
                    candidates.append(child_node)
                    
        results.sort(key=lambda x: x[0])
        return results