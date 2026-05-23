class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        my_stack = []

        cars = [[p, s] for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        for p, s in cars:
            my_stack.append((target - p) / s)
            if len(my_stack) >= 2 and my_stack[-1] <= my_stack[-2]:
                my_stack.pop()
        
        return len(my_stack)