class Solution {
    public boolean isAnagram(String s, String t) {
        if ((s.length()) != (t.length())){
            return false;
        }

        int[] array1 = new int[26];
        int[] array2 = new int[26];

        for (char z : s.toCharArray()) {
            int index = z - 'a';
            array1[index]++;
        }
         for (char z : t.toCharArray()) {
            int index = z - 'a';
            array2[index]++;
        }
        for (int i = 0; i<26; i++) {
            if (array1[i] != array2[i]) {
                return false;
            }
        }
        return true;
    }
}
