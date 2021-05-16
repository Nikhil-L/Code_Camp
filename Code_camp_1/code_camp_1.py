
def isSubsetSum(set, n, rsum):
 
    if (rsum == 0):
        return 1
    if (n == 0):
        return -1
 
    if (set[n - 1] > rsum):
        return isSubsetSum(set, n - 1, rsum)
    else:
        if isSubsetSum(set, n-1, rsum) == 1 or isSubsetSum(set, n-1, rsum-set[n-1]) == 1:
            return 1
        else:
            return -1

def main():
	arr = list(map(int, input().split()))
	n = len(arr)
	sum_ = int(input())
	print(isSubsetSum(arr, n, sum_)) 

if __name__ == '__main__':
	main()
 
