class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        #operations = list(map(str, input().split()))
        x = 0
        for i in operations:
            if i[1] == "-":
                x -= 1
            elif i[1] == "+":
                x += 1
        return x
            
            
                