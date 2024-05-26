def maximumSubarraySum(n: int, v: list[int]) -> int:
   # Write your code here.
   s = 0
   for i in v:
      if (i > 0):
         s = s+i
   print(s) 
   return s

n = 5
a = [1,-5,1,1,4]
maximumSubarraySum(n, a)
