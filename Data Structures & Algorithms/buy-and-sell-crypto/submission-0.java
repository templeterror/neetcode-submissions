class Solution {
    public int maxProfit(int[] prices) {
        int hi=0;
        int lo=0;
        int dif=0;
        int answer=0;

        for (int i=0; i<prices.length; i++) {
            lo = prices[i];
            for (hi = i+1; hi<prices.length; hi++) {
                if (dif < (prices[hi]-lo) && ((prices[hi]-lo)>=0)) {
                    dif = prices[hi]-lo;
                }
            }
        }
        return dif;
    }
}
