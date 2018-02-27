'''
merge sort 
'''

def merge_sort(array):
	if not isinstance(array,list):
		raise TypeError
	n = len(array)
	if n==0:
		raise ValueError 
	for i in range(n):
		if not isinstance(array[i],(int,long,float)):
			raise ValueError 
	
	if n==1:
		return array
	if n==2:
		return array.sort()
	if n%2 ==0:
		m = n/2 
	else:
		m = (n+1)/2 
	
	temp1 = merge_sort(array[:m])
	temp2 = merge_sort(array[m:])
	result = [] 
	while True:
		if len(temp1)==0:
			result.extend(temp2)
			temp2 = [] 
		if len(temp2)==0:
			result.extend(temp1)
			temp1 = [] 
		if len(temp1)==0 or len(temp2)==0:
			return result 
		if temp1[0]>temp2[0]:
			result.append(temp2.pop(0))
		else:
			result.append(temp1.pop(0))
	return result 
	
