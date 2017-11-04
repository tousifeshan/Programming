class Solution(object):
    
    def recur(self, digits,num2word):
        if len(digits)==0:
            return ['']
        else:
            return [c+d for c in list(num2word[digits[0]]) for d in self.recur(digits[1:],num2word)]
        
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num2word={'1':'*','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz','0':' '}
        if len(digits)==0:
            return []
        else:
            return self.recur(digits,num2word)