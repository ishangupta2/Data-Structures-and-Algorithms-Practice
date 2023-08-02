class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        indx = 0
        for i in position: 
            arr.append([i, speed[indx]])
            indx+=1
        stack = []
        arr.sort(reverse=True)
        for i, v in arr:
            dist = ((target-i)/v)
            if(stack and stack[-1] >= dist):
                continue
            else:
                stack.append(dist)
        return len(stack)
        