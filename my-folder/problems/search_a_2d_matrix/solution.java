class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int mid;
        int left;
        int right;
        for(int i = 0; i < matrix.length; i++) {
       left = 0;
       right = matrix[i].length-1;
        while (left <= right) {
            mid = (left+right)/2;
            if(matrix[i][mid] > target) {
                right = mid-1;
            }
            else if(matrix[i][mid] < target) {
                left = mid+1;
            }
            else {
                return true;
            }
        }
        }
        return false;
    }
}