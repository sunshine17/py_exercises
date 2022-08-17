#
# 1. The matrix(mxn) array is sorted.
# 2. We can use binary search in row and cols
# 
#    m == matrix.length
#    n == matrix[i].length
#    1 <= m, n <= 100
# search in rows(the first number in each row)
#
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
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

