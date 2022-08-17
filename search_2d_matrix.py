def searchMatrix(matrix: List[List[int]], target: int) -> bool:
'''
The matrix(mxn) array is sorted, so we can refactor our solution to use binary search if we have enough time. 

**Solution:**
We can first locate the row in rows, and then search the row for target directly. 
1. Here we use python's list comprehension to extract the rows array ( space complexity: m ), then loop it to find the row index for target.
2. Since n <= 100, so we search for it directly with python's list search: "target in row"

**Loop times:** m + m + m + n
**Time complexity: O(m+n)**
**Runtime:** 86 ms
'''
	m = len(matrix)
	n = len(matrix[0])

	if m == 1:
		return target in matrix[0]
	
	head_list = [x[0] for x in matrix]
	if target in head_list:
		return True

	r_index = -1
	for i in range(m):
		val = head_list[i]
		if target < val:
			break
		r_index = i
		
	if r_index < 0:
		return False

	row = matrix[r_index]
	return target in row

