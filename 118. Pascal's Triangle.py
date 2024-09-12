class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        for r in range(1, numRows + 1):
            row = [1] * r

            for i in range(r):
                if i == 0 or i == r - 1:
                    continue
                else:
                    row[i] = res[r-2][i-1] + res[r-2][i]

            res.append(row)

        return res
