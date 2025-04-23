
a = ["play", "willing", "to"]
for i in a:
  x = len(i)
  b = i
  print (x)
#   print (b)
  if x > 3 and not(b.endswith("ing")):
    result = b + "ing"
    print("Text re:",result)
  elif x >3 and b.endswith("ing"):
     result1 = b + "ly"
     print("Text with Ing :",result1)
  else:
     print("Text: " ,b)




