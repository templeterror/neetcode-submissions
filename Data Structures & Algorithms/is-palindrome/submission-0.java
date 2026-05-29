class Solution {
  public boolean isPalindrome(String word) {
        int i=0; // i is the starter pointer
        int j= word.length()-1; // is the end point pointer

        if (word.length()==1) { return true; }
        char[] array = word.toCharArray();
        
        while (i < j) {
            while (i < j && !Character.isLetterOrDigit(array[i])) i++;
            while (i < j && !Character.isLetterOrDigit(array[j])) j--;
        
            if (Character.toLowerCase(array[i]) != Character.toLowerCase(array[j])) return false;
        
            i++;
            j--;
        }
        return true;
    }
}