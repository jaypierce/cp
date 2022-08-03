class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        doubled = {}
        
        for i in arr:
            if i * 2 in doubled or i / 2 in doubled:
                return True
            doubled[i] = 1
        return False