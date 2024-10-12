class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for asteroid in asteroids:                
            if asteroid < 0:
                while len(stack) > 0 and stack[-1] > 0:
                    if stack.pop() < abs(asteroid):
                        continue
                        
                    asteroid = 0
                    break

                if asteroid == 0:
                    continue

            stack.append(asteroid)

        return stack

sol = Solution()

print(sol.asteroidCollision([-2,1,1,-1]))