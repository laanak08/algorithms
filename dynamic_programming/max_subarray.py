"""
1. Characterize the structure of an optimal solution.
For the maximum subarray problem, 
an optimal solution consists of the max value in a series of sums
of various combinations of elements from the starting array.
The various combinations occurr in two groups:
    -Combinations made from consecutive elements.
    -Combinations made from non-consecutive elements.
Mathematically speaking:
    // not sure how exactly to notate these
    consecutive elements: max(sum(x0,..,xi),..,sum(x0,..,xn))
    non-consecutive elements: max(sum(x0,..,xi),..,sum(x0,..,xn)) 

    N.B.
    Since dynamic programming is based on mathematical induction,
    consider the problem in terms of an inductive proof.

    In the current case, we seek to maximize the sum of the values within a non-empty list.
    Given a list of only one value, the maximum sum is max(sum(x0)).
    Given a list of 2 values, the maximum sum is max(sum(x0), sum(x0, x1))
    Given a list of 3 values, the maximum sum is max(sum(x0), sum(x0, x1), sum(x0, x1, x2))
    Given a list of N values, the maximum sum is max(sum(x0), .. , sum(x0, .., xn))

2. Recursively define the value of an optimal solution.
max_subarr(arr) = max(sum(xi)+ max_subarr([xi+1..xn])) // This is really incorrect.

break the array down from the last element back to its first element
ex. n, n-1, n-2...etc.
max_sub = -INF
for i in arr:
    max_sub = max( max_sub, sum(arr[i] + max_subarr(arr[i+1:]) 

max_sub = max( max_sub, sum(arr[i] + max_subarr(arr[i+1:]) 

3. Compute the value of an optimal solution, typically in a bottom-up fashion.

4. Construct an optimal solution from computed information.
"""
def main():
    for caseNum in range(0,int(raw_input())):
        case_len = int(raw_input())
        case = raw_input().split()
        print max_subarray(case)

def max_subarray(arr):
    max_arr = []
    
    return max_arr

main()