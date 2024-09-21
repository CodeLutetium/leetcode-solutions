class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def time_diff(t1: int, t2: int) -> int:
            return min(abs(t2 - t1), abs(t2 + (24 * 60) - t1), abs(t1 + (24 * 60) - t2))
        
        def parse_time(timePoint: str) -> int:
            return int(timePoint[0:2]) * 60 + int(timePoint[3:])

        # Convert timePoints to minutes
        timePoints = [parse_time(t) for t in timePoints]

        timePoints.sort()
        res = math.inf
        
        # Compare each time point with the one after
        for t in range(len(timePoints) - 1):
            res = min(res, time_diff(timePoints[t], timePoints[t + 1]))

        # Compare last and first time
        res = min(res, time_diff(timePoints[0], timePoints[-1]))

        return res


"""
Time complexity: O(n logn) due to sorting
Space complexity: O(1) (not using extra space)
"""