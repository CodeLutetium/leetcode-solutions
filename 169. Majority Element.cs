public class Solution {
    public int MajorityElement(int[] nums) {
        // Create hashmap
        Dictionary <int, int> countMap = new Dictionary<int, int>();

        // Loop through nums and update count to countMap
        foreach (int n in nums) {
            if (countMap.ContainsKey(n))
                countMap[n]++;
            else
                countMap[n] = 1;
        }

        // Return majority element
        return countMap.MaxBy(entry => entry.Value).Key;
    }
}

/*
    Complexity analysis:
    Time: O(n), where `n` is the length of the given nums array.
    Space: O(n), since we store the count of each element in a hashmap.
*/