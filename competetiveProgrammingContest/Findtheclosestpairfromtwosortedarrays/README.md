Find the closest pair from two sorted arrays

    Difficulty Level : Medium

Given two sorted arrays and a number x, find the pair whose sum is closest to x and the pair has an element from each array. 
We are given two arrays ar1[0…m-1] and ar2[0..n-1] and a number x, we need to find the pair ar1[i] + ar2[j] such that absolute value of (ar1[i] + ar2[j] – x) is minimum.
Example: 

Input:  ar1[] = {1, 4, 5, 7};
        ar2[] = {10, 20, 30, 40};
        x = 32      
Output:  1 and 30

Input:  ar1[] = {1, 4, 5, 7};
        ar2[] = {10, 20, 30, 40};
        x = 50      
Output:  7 and 40

        l=0
        r=len(ar2)-1
        while l<len(ar1) and r>0:
                sum=ar1[l]+ar2[r]
                diff=abs(sum-x)
                if diff<minDiff:
                        minDiff=diff
                        result=[nums[l],nums[r]]
                if sum<x:
                        l+=1
                elif sum>x:
                        r-=1
                else:
                        return [nums[l],nums[r]]
        return result
        