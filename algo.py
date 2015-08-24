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

	