class Solution {
    public void reverseString(char[] s) {
        if (s.length == 1)
            return;

        int left = 0;
        int right = s.length - 1;

        while (left < right) {
            // Swap characters
            char temp = s[left];
            s[left] = s[right];
            s[right] = temp;

            // Increment left and right
            left++;
            right--;
        }
    }
}

/*
 * Time complexity: O(n)
 * Space complexity: O(1)
 */