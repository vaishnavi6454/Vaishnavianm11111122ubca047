def linearSearchProduct(productList,
targetproduct):
  indices=[]

  for index,product in enumerate(productList):
   if product==targetproduct:
     indices.append(index)
  return indices

products=["leafs","blossoms","stem","leafs","buds","leafs"]
target = "leafs"
target2 = 'apple'
result=linearSearchProduct(products,target)
print(result)