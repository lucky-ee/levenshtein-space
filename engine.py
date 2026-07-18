import time
from bktree import BKTree

def levenshtein_distance(s1: str, s2: str) -> int:
    
    m, n = len(s1), len(s2) 
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
        
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,      
                dp[i][j - 1] + 1,      
                dp[i - 1][j - 1] + cost 
            )
    return dp[m][n]

def load_dictionary(filepath: str) -> list:
    with open(filepath, 'r', encoding='utf-8') as file:
        return [line.strip().lower() for line in file if line.strip()]


if __name__ == "__main__":
    dict_path = "/usr/share/dict/words" 
    
    print("Loading dictionary...")
    try:
        english_words = load_dictionary(dict_path)
    except FileNotFoundError:
        print(f"Error: Could not find dictionary at {dict_path}")
        exit(1)
        
    print("Building BK-Tree (This takes a few seconds)...")
    tree = BKTree(levenshtein_distance)
    for word in english_words:
        tree.add(word)
        
    print("Tree built successfully!\n")
    

    while True:
        print("-" * 40)
        word = input("Enter a word to check (or type 'quit' to exit): ").strip().lower()
        
        if word == 'quit':
            print("Goodbye!")
            break
        if not word:
            continue
            

        tolerance_input = input("Enter tolerance level (Press Enter for 2): ").strip()
        
        try:
            tolerance = int(tolerance_input) if tolerance_input else 2
            if tolerance < 0:
                raise ValueError
        except ValueError:
            print("That wasn't a valid number! Defaulting tolerance to 2.")
            tolerance = 2
            
        start_time = time.time()
        tree_matches = tree.search(word, tolerance)
        search_time = (time.time() - start_time) * 1000 
        
        
        print(f"\nFound {len(tree_matches)} matches in {search_time:.2f} ms:")
        for dist, match in tree_matches:
            print(f"  -> {match} (Distance: {dist})")