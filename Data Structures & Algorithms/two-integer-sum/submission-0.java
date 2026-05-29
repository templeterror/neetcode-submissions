class Solution {
    public static int[] twoSum(int[] nums, int target) {
        HashMap <Integer, Integer> work = new HashMap<>();
        for (int i=0; i<nums.length; i++) {
            int element = nums[i];
            int complement = target - element;
            if (work.containsKey(complement)) {
                int[] result = {work.get(complement), i};
                return result;
            } else {
                work.put(element, i);
            }
        }
        return null;
    }
    public static void main(String[] args) {
        int[] example = {2,7,11,15};
        System.out.println(Arrays.toString(twoSum(example, 9)));
    }
}
