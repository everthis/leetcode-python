class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        words = sorted(words,key=lambda t:len(t))
        word_dict = set()
        def isQualify(w):
            if w in word_dict:return True
            for i in range(1,len(w)):
                if w[:i] in word_dict and isQualify(w[i:]):return True
            return False
        res = []
        for w in words:
            if isQualify(w):res.append(w)
            word_dict.add(w)
        return res
