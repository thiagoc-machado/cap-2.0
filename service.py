class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper() or word.islower() or word.istitle():
            print("True")
        print("False")

    detectCapitalUse(0,'OLA')

    # if word.isupper() or word.islower() or word.istitle():
    #     return True
    # return False