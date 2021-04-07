class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        '''
        Here we make a ternary representation of given n
        If n has '2' in it return False, else return True
        [See: hint]
        '''
        
        ternary = ''                       #ternary string is the reverse representation of original ternary
        
        while n>0:
            ternary+=str(n%3)              #ternary means base 3
            n=n//3
            
        if '2' in ternary:
            return False
        return True
