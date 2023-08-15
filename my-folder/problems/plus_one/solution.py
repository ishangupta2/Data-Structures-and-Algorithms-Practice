class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]<9:
            digits[-1]+=1
            return digits
        else:
            car = 1
            m = len(digits)-1
            digits[m]=0
            m-=1
            while(m>=0 and digits[m]+car>9):
                
                digits[m]=0
                m-=1
            if m>=0:
                digits[m]+=car
            else:
                digits.insert(0, car)
            return digits
