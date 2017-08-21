class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = maxlen = 0
        characterBefore = {}
        l = len(s)
        for i in range(l):
            if s[i] in characterBefore and start <= characterBefore[s[i]]:
                start = characterBefore[s[i]] + 1
            else:
                maxlen = max(maxlen, i - start + 1)
            characterBefore[s[i]] = i
        return maxlen
