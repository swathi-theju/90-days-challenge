
def search(arr,x,n):
	for i in range(0,n):
		if(arr[i]==x):
			return i
	return -1
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
n=len(arr)
result=search(arr,x,n)
if(result==-1):
	print("element not found")
else:
	print("element found at",result)