class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int right = 1;
       for (int pile : piles) {
            right = Math.max(right, pile);
        }
        int left = 1;
        int mid;
        while(left<= right) {
            double hourSpent = 0;
            mid = (left+right)/2;
              for (int pile : piles) {
                hourSpent += Math.ceil((double) pile / mid);
            }

            // Check if middle is a workable speed, and cut the search space by half.
            if (hourSpent <= h) {
                right = mid-1;
            } else {
                left = mid + 1;
            }
        }
         return left;
        }
       
    }
   