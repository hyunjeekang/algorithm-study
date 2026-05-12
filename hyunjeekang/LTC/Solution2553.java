import java.util.ArrayList;
import java.util.List;

class Solution2553 {
    public int[] separateDigits(int[] nums) {
        List<Integer> list = new ArrayList<>();

        for (int num : nums) {
            separate(num, list);
        }

        return list.stream().mapToInt(i -> i).toArray();
    }

    public void separate(int num, List<Integer> list) {
        int insertIdx = list.size();

        while (num >= 10) {
            list.add(insertIdx, num % 10);
            num /= 10;
        }
        list.add(insertIdx, num);
    }
}