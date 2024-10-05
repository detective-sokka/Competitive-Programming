class Exam:
    def _init_(self, a, ans, work, show):
        self._a = a
        self._ans = ans
        self._work = work
        self._show = show
        Algorithm(self)

    def _len_(self):
        return len(self._a)

    def _getitem_(self, i):
        return self._a[i]

    def setAns_As_Heavier(self):
        self._ans[0] = True

    def setAns_As_Lighter(self):
        self._ans[0] = False

    def show(self):
        return self._show

    def weigh(self, left, right):
        l_sum = sum(self._a[i] for i in left)
        r_sum = sum(self._a[i] for i in right)
        self._work[0] += 1
        if l_sum > r_sum:
            return '>'
        elif l_sum < r_sum:
            return '<'
        else:
            return '='


class Algorithm:
    def _init_(self, s):
        self._s = s
        self._alg()

    def compareLeftRight(self, left_index, right_index):
        if (left_index + right_index) % 2 != 0:
            # If n is odd, compare the first n-1 elements
            left = list(range(left_index, (left_index + right_index) // 2))
            right = list(range(((left_index + right_index) // 2) + 1, right_index))
        else:
            # If n is even, split into two equal halves
            left = list(range((left_index + right_index) // 2))
            right = list(range((left_index + right_index) // 2, right_index))
        
        return self._s.weigh(left, right)
        
    def _alg(self) -> 'None':
        n = len(self._s)
        
        left = 0
        right = n-1
        
        while left < right:
            mid = (left + right) // 2
            
            if not (arr[left] == arr[mid] == arr[right]):
                break
            
            left_result = compareLeftRight(0, mid)
            right_result = compareLeftRight(mid + 1, right)
        
            if left_result == '=':
                left = mid + 1
            else:
                right = mid - 1
                
        if num1 != num2 and num1 != num3:
            different_number = num1
        elif num2 != num1 and num2 != num3:
            different_number = num2
            
        if different_number < num1 and different_number < num2:
            self._s.setAns_As_Lighter()
        elif different_number > num1 and different_number > num2:
            self._s.setAns_As_Heavier()
        
def main():
    a = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2]
    ans = [False]  # Placeholder for the answer
    work = [0]  # Placeholder for the amount of work done
    show = True  # Show the process
    Exam(a, ans, work, show)
    print(f"Work done: {work[0]}, Fake coin is {'heavier' if ans[0] else 'lighter'}.")


if __name__ == "__main__":
    main()