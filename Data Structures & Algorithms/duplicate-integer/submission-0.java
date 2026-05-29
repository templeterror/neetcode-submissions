
class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> joma = new HashSet<>();
        for (int i = 0; i<nums.length; i++) {
            if (joma.contains(nums[i])) {
                return true;
            } else {
                joma.add(nums[i]);
            }
        }
        return false;
    }
}