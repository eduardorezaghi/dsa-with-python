class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []

        for op in operations:
            if op == '+':
                record.append(sum(record[-2:]))
            elif op == 'D':
                record.append(2 * record[-1])
            elif op == 'C':
                if record:
                    record.pop()
            elif op.isdigit() or op[0] == '-':
                record.append(int(op))

        return sum(record)


if __name__ == '__main__':
    s = Solution()
    print(s.calPoints(["5","2","C","D","+"]))  # 30
