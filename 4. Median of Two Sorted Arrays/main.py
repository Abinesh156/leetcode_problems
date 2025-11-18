nums1 = [1,3]
nums2 = [2]
    

def findMedianSortedArrays(num1,num2) :
    array=sorted(nums1+nums2)
    if len(array)%2==1:
        return float(array[len(array)//2])
    else:
        mid1=float(array[len(array)//2])
        mid2=((array[(len(array)//2)-1]))
        return (float(array[len(array)//2])+(array[(len(array)//2)-1]))/2


print(findMedianSortedArrays(nums1,nums2))