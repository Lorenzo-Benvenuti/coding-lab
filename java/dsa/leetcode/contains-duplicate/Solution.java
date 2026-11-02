class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();

        for (int n : nums) {
            // add() returns false if n is already in the set
            if (!seen.add(n)) {
                return true;
            }
        }
        return false;
    }
}
