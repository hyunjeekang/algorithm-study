class Solution2553 {
    public int[] separateDigits(int[] nums) {
        
        // 총 자릿수 계산
        int totalDigits = 0;
        for (int num : nums) {
            while (num > 0) {
                totalDigits++;
                num /= 10;
            }
        }

        // 결과 배열 할당
        int[] result = new int[totalDigits];
        int idx = totalDigits - 1;

        // 뒤부터 채우기
        for (int i = nums.length - 1; i >= 0; i--) {
            int num = nums[i];
            while (num > 0) {
                result[idx--] = num % 10;
                num /= 10;
            }
        }

        return result;
    }
}