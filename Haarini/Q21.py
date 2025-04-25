#  print("\nTask 21:")

no = [-3, -2, 0, 1, 2, 4, 5, 7]
def positive_numb(nums):
 for n in nums:
      if n >= 0:
         yield (n)
      else :
        print("negative",n)
             
for value in positive_numb(no):
  print("positives",value)