class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        U:
        Edge cases:
        if strs = [""] then return "" 
        """

        # intialize an empty string
        encoded_string = ""
        # loop through the list
        for word in strs:
            # find the length of word
            length = str(len(word))
            # create a str which inludes the length + # + word
            encoded_string += length + "#" + word

        print("encoded_string: ", encoded_string)
        return encoded_string

    def decode(self, s: str) -> List[str]:
        """
        U:
        Edge cases:
        if s = "" then return [""] 
        """
        
        decoded_strs = []
        i = 0
        # loop through the string
        while i < len(s):
            # find what index is # at (j) starting from index i
            j = s.find("#", i)
            # length of the word is everything from i:j
            length = int(s[i:j])
            # extract the word string[j+1:j+1+length]
            word = s[j+1 : j+1+length] 
            # append word to result list
            decoded_strs.append(word)
            # move i to j+1+length
            i = j+1+length
        # return decoded list
        return decoded_strs 