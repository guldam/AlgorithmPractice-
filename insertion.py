'''
insertion sort in python 
'''
import copy 

def insert(array,element):
    '''
    insert element to array in an appropriate position where array is sorted in ascending order 
    '''
    if not isinstance(array,list):
    	raise ValueError('array is not of type list')
	if len(array)==0:
		raise ValueError('array is empty')
	for i in range(len(array)):
		if not isinstance(array[i],(int,long,float)):
			raise ValueError('element is not of type numeric') 
	for i in range(len(array)):
		if element<=array[i]:
			array.insert(i,element)
			return array 
	return array+[element]
	
def insertion_sort(array):
    if not isinstance(array,list):
    	raise ValueError('array is not of type list')
	if len(array)==0:
		raise ValueError('array is empty')
	for i in range(1,len(array)):
		temp = insert( copy.deepcopy(array)[:i] , element ) 
		array[:i+1] = temp 
	return array 
	
	
	
