class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # initialize stack
        stack = []
        times = []

        # sort the position list (closest to target -> farthest)
        sorted_pairs = sorted(zip(position, speed), reverse=True)

        for pos, spd in sorted_pairs:
            # create a time list
            time = (target - pos) / spd
            times.append(time)


        for index in range (len(times)):
            if len(stack) == 0 or times[index] > stack[-1]:
                stack.append(times[index])
        return len(stack)
