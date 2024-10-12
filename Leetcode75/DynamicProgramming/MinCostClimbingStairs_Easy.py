# Note: There is an easier iterative solution. 
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        min_cost_from_step_dictionary = {}

        def recurseClimbingStairs(index):
            if index >= len(cost):
                return 0

            if index not in min_cost_from_step_dictionary:
                step_size_1_cost = recurseClimbingStairs(index + 1)
                step_size_2_cost = recurseClimbingStairs(index + 2)
                min_cost_from_step_dictionary[index] = min(step_size_1_cost, step_size_2_cost) + cost[index]
            
            return min_cost_from_step_dictionary[index]
        
        return min(recurseClimbingStairs(0), recurseClimbingStairs(1))
