from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        features = []
        copies = 0
        
        # Creating features list: [factor, cost, initial copies, copies per dollar]
        for i in range(len(items)):
            initial_copies = 1
            features.append(items[i])
            for j in range(len(items)):
                if i != j and items[j][0] % items[i][0] == 0:
                    initial_copies += 1
            features[i].append(initial_copies)
            features[i].append(initial_copies/items[i][1])
        
        # Sorting the list according to copy per dollar and cost respectively:
        features.sort(key = lambda x: x[3], reverse = True)
        items.sort(key = lambda x: x[1], reverse = True)
        
        # Greedy selecting from features till either features are exhausted, budget is exhausted or budget is less:
        while features and budget > 0 and features[0][1] <= budget:
            budget -= features[0][1]
            copies += features[0][2]
            features.pop(0)
            
        # Greedy selecting copies using remaining budget:
        copies += budget // items[0][1]
            
        return copies
    
answer = Solution()
maxItems = answer.maximumSaleItems(items = [[2,4],[3,2],[4,1],[6,4],[12,4]], budget = 8)
print(f"Max Items From Sale: {maxItems}")