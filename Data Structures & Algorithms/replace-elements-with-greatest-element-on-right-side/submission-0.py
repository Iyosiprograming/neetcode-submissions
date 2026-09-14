class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length_of_array = len(arr)

        for i in range(length_of_array - 1):
            greatest_number = 0

            for j in range(i + 1, length_of_array):
                if arr[j] > greatest_number:
                    greatest_number = arr[j]

            arr[i] = greatest_number

        arr[-1] = -1

        return arr