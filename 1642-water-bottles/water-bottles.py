class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        max_drink = numBottles
        while numExchange <= numBottles:
            empty_bottles = numBottles
            numBottles = (empty_bottles // numExchange)
            max_drink += numBottles
            
            numBottles += (empty_bottles % numExchange) 
        return max_drink