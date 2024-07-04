import heapq

def find_union(nums1, nums2):
    heap = []
    for num in nums1:
        heapq.heappush(heap, num)
    for num in nums2:
        heapq.heappush(heap, num)
    return union_result
nums1 = [1, 2, 4, 5, 9]
nums2 = [2, 5, 6, 7]
union_result = find_union(nums1, nums2)

print("합집합 결과:", union_result)