from typing import List

def findSubsets(arr, n)-> List[str]:
    # Function to find all subsets of given set.
    # Any repeated subset is considered only
    # once in the output
    ans = []
    from itertools import combinations
    for i in range(0,len(arr)+1):
        for x in combinations(arr,i):
            if i < len(arr):
                if arr[i] in ans:
                    ans.remove(arr[i])
                    ans.append(arr[i])
            ans.append(x)

    return ans
 
# R E A D M E
# DO NOT CHANGE the code below, we use it to grade your submission. If changed your submission will be failed automatically.
if __name__ == '__main__':
#    line = input()
#    components = line.strip().split()
    components = ['1','2','3']

    n = len(components )
    print('[[' + '],['.join([','.join(['{:1}'.format(item) for item in row]) 
      for row in findSubsets(components,n)]) + ']]')
