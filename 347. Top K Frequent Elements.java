import java.util.HashMap;

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> topElements = new HashMap<>();

        // Loop over nums
        for (int i : nums) {
            // Check if exists in map
            if (topElements.containsKey(i)) {
                topElements.put(i, topElements.get(i) + 1);
            } else {
                topElements.put(i, 1);
            }
        }

        // Sort into List
        List<Integer> result = new ArrayList<>(topElements.keySet());
        result.sort((a, b) -> topElements.get(b) - topElements.get(a));

        // Results array
        int[] res = new int[k];
        for (int i = 0; i < k; i++)
            res[i] = result.get(i);

        return res;
    }
}