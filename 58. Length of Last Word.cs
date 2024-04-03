public class Solution {
    public int LengthOfLastWord(string s) {
        int length = 0;
        
        // Remove trailing spaces
        s = s.TrimEnd();

        // Loop over characters in string from the back
        for (int i = s.Length - 1; i >= 0; i--) {
            if (s[i] == ' ')
                return length;
            length++;
        }
        return length;
    }
}

/* 
    Complexity analysis:
    Time: O(n), where `n` is the length of the given string `s`.
    Space: O(1), since we do not use any extra space.
*/