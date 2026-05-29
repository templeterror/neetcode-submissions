class Solution {
    public int maxProfit(int[] prices) {
        int lo=100;
        int dif=0;
        int answer=0;

        for (int i=0; i<prices.length; i++) {
            if (lo> prices[i])
                lo = prices[i];
            dif = prices[i]- lo;
            if (dif> answer)
                answer = dif;
        } return answer;
    }
}
