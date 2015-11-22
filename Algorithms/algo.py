def SelectionSort(items):
	x=0
	while(x<len(items)-1):
		y=x+1
		while(y<len(items)):
			if (items[x]>items[y]):
				temp=items[x]
				items[x]=items[y]
				items[y]=temp
			y=y+1
		x=x+1
	return items

def BubbleSort(items):
	x=0
	while(x<len(items)-1):
		y=0
		while(y<len(items)-1):
			if(items[y]>items[y+1]):
				temp=items[y]
				items[y]=items[y+1]
				items[y+1]=temp
			y=y+1
		x=x+1

def BinarySearch(items,key):
	try:
		sum(items)
	except Exception, e:
		print "Not an all number array"
		return -1
	else:
		pass
	finally:
		pass
	BubbleSort(items)
	low=0
	high=len(items)-1
	while(low<=high):
		mid=(low+high)/2
		if(items[mid]==key):
			return mid
		if(key>items[mid]):
			low=mid+1
		if(key<items[mid]):
			high=mid-1
	return -1

def SequentialSearch(items,key):
	i=0
	while i<len(items):
		if key==items[i]:
			return i
		i=i+1
	return -1

def MergeSOrt(items):
	
