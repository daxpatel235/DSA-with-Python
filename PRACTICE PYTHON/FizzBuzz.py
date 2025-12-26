class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        int(input("enter the value of i: "))
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                int.append("FizzBuzz")
            elif i % 3 == 0:
                int.append("Fizz")
            elif i % 5 == 0:
                int.append("Buzz")
            else:
                int.append(str(i))
        
        return int

