import unittest
from engine import levenshtein_distance
from bktree import BKTree

class TestAutocompleteEngine(unittest.TestCase):
    
    def test_levenshtein_distance(self):
        # 1. Identity: Distance to itself should be 0
        self.assertEqual(levenshtein_distance("apple", "apple"), 0)
        
        # 2. Symmetry: Order shouldn't matter
        self.assertEqual(levenshtein_distance("kitten", "sitting"), 3)
        self.assertEqual(levenshtein_distance("sitting", "kitten"), 3)
        
        # 3. Known cases (Insertions, Deletions, Substitutions)
        self.assertEqual(levenshtein_distance("book", "books"), 1) # 1 insertion
        self.assertEqual(levenshtein_distance("cake", "bake"), 1)  # 1 substitution
        self.assertEqual(levenshtein_distance("", "hello"), 5)     # Empty string
        
    def test_bktree_search(self):
        tree = BKTree(levenshtein_distance)
        
        # Add a mini-dictionary
        for word in ["book", "books", "cake", "boo", "cook"]:
            tree.add(word)
            
        # Search for 'kook' with a tolerance of 1
        # The only valid matches should be 'book' and 'cook'
        results = tree.search("kook", tolerance=1)
        
        # Extract just the words from the (distance, word) tuples
        matched_words = [word for dist, word in results]
        
        # Verify the tree pruned properly and found the right matches
        self.assertEqual(len(matched_words), 2)
        self.assertIn("book", matched_words)
        self.assertIn("cook", matched_words)

if __name__ == '__main__':
    unittest.main()