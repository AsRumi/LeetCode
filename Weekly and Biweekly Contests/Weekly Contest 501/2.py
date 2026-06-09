from collections import defaultdict

class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        # Create a dictionary with words and counts:
        wordsCounts = defaultdict(int)
        
        # Iterate over all words from chunks and join them into a string:
        mainString = ""
        for word in chunks:
            mainString += word
        
        # Create words on the following principle:
            # If current char is a white space: end current word and add it to dict if not empty word, then reset current word.
            # If current char is a hyphen: 
                # If there are letters on either side of the hyphen, add hyphen to current word and continue.
                # Else end current word and add it to dict if not empty word
            # If current char is a letter: add letter to current word and continue
        currentWord = ""
        length = len(mainString)
        for i, char in enumerate(mainString):
            
            # Skip boundary hyphens:
            if char == "-" and (i == 0 or i == length - 1):
                continue
            
            if char == " ":
                if currentWord:
                    wordsCounts[currentWord] += 1
                    currentWord = ""
            elif char == "-":
                if (mainString[i-1] not in {" ", "-"}) and (mainString[i+1] not in {" ", "-"}):
                    currentWord += char
                else:
                    if currentWord:
                        wordsCounts[currentWord] += 1
                        currentWord = ""
            else:
                currentWord += char
        if currentWord:
            wordsCounts[currentWord] += 1
                
        # Append counts to a result list based on queries:
        result = []
        for query in queries:
            result.append(wordsCounts[query])
        
        return result
    
answer = Solution()
countWordOccurrences = answer.countWordOccurrences(chunks = ["a-b a--b ","a-","b"], queries = ["a-b","a","b"])
print(f"Count Word Occurrences: {countWordOccurrences}")
countWordOccurrences = answer.countWordOccurrences(chunks = ["-cat dog- mouse"], queries = ["cat","dog","mouse","cat-dog"])
print(f"Count Word Occurrences: {countWordOccurrences}")