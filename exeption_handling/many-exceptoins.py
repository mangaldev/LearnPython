try:
  print(1/0)
except NameError as ne:
  print("Error ------ ", ne)
except:
  print("Something else went wrong")