# Encode and Decode Strings

class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += "%" + str(len(word)) + "%" + word
        return encoded_string
    
    def decode(self, s: str) -> list[str]:
        i = 0
        string = s
        decoded_list = []
        while i < len(string):
            if string[i]=="%":
                i+=1
                length = ""
                while string[i] != "%":
                    length += string[i]
                    i += 1
                length = int(length)
                i += 1
                decoded_list.append(string[i:i+length])
                i += length
        return decoded_list
    
# answer = Solution()
# encodedString = answer.encode(["neet","code","love","you"])
# print(f"Encoded String: {encodedString}")
# decodedString = answer.decode(encodedString)
# print(f"Decoded String: {decodedString}")

string = "%4%neet%4%code%4%love%3%you"
i = 0
decoded_list = []
while i < len(string):
    if string[i]=="%":
        i+=1
        length = ""
        while string[i] != "%":
            length += string[i]
            i += 1
        length = int(length)
        i += 1
        decoded_list.append(string[i:i+length])
        i += length
print(decoded_list)