class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #check first rectangles height
        # move right. if it goes down, then new baseline is new height and we check max of the old baseline then discard but keep that previous square
        # move right. if it goes up then new baseline is created and is rectangles height
        # move right. if it goes down, then new baseline is new height and we check max of the old baseline then discard but keep that previous rectangle

        # for each bar
        # if the bars height is larger than the height to track, make the new height to track equal to the height of the new bar
        # if the bars height is smaller than the height to track, find area by goign to each bar that is larger than new height. starting pos + current pos times its height. set it to max if you can and then stop tracking every bar that is larger than new height
        # return largest bar?

        my_stack = []

        max_area = 0
        for i, h in enumerate(heights):
            start = i

            while my_stack and my_stack[-1][1] > h:
                index, height = my_stack.pop()
                max_area = max(max_area, height * (i - index))

                start = index
            my_stack.append((start, h))

        for i, h in my_stack:
            max_area = max(max_area, h * (len(heights) - i))
        
        return max_area