class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # initialize a hashmap
        my_dict = {}

        # initialize left pointer
        left = 0

        # intialize max freq
        max_freq = 0

        longest = 0

        # for loop, right as index, length of str
        for right in range (len(s)):
            window_size = right - left + 1

            # add to frequency and update hashmap
            if s[right] not in my_dict:
                my_dict[s[right]] = 1
            else:
                my_dict[s[right]] += 1
        
            max_freq = max(max_freq, my_dict[s[right]])
        
            # if (window_size - max_freq > k) → shrink (move left)
            if (window_size - max_freq > k):
                # dec frequency
                my_dict[s[left]] -= 1
                left += 1
    
            # track longest valid window
            longest = max(longest, right-left + 1)
            print("longest: ", longest)
        return longest

        