def factorial(facLimit):
  if (facLimit <= 1):
    return 1
  else:
    return facLimit * \
      factorial(facLimit - 1)

def summation(upper):
  if (upper == 1):
    return 1;
  else:
    return upper + \
      summation(upper - 1)

if __name__ == "__main__":
  print("Module testing")
  print("Test factorial(5). Should be 120")
  print(factorial(5))
  print("Test summation(8). Should be 36")
  print(summation(8))
