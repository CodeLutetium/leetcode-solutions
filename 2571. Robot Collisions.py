"""
SOLUTION COPIED FROM EDITORIAL
"""
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        num_robots = len(positions)
        indices = list(range(num_robots))   # Keep track of original positions of the robots
        result = []         # Store health of remaining robots
        stack = deque()     # Double ended queue

        # Sort robots based on their positions to make sure they are processed from left to right
        indices.sort(key = lambda x: positions[x])
        # print(indices)

        for current_index in indices:
            # Right moving robots: Add to the stack
            if directions[current_index] == 'R':
                stack.append(current_index)

            else: 
                while stack and healths[current_index] > 0:
                    # Pop the top robot from the stack for collision check
                    top_index = stack.pop()

                    if healths[top_index] > healths[current_index]:
                        # Top robot survives, current robot is destroyed
                        healths[top_index] -= 1
                        healths[current_index] = 0
                        stack.append(top_index)

                    elif healths[top_index] < healths[current_index]:
                        # Current robot survives, top robot is destroyed
                        healths[current_index] -= 1
                        healths[top_index] = 0

                    else:
                        # Both robots are destroyed
                        healths[current_index] = 0
                        healths[top_index] = 0

        # Collect surviving robots
        for i in range(num_robots):
            if healths[i] > 0:
                result.append(healths[i])

        return result