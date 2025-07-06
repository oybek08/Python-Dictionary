permissions = {"read": True, "write": False, "delete": True}


for item in permissions.item():
 if item[1]:
  print(item[0])
  