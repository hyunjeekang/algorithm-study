import java.util.*;

public class Solution3629 {
    public int minJumps(int[] nums) {
        int n = nums.length;
        if (n <= 1) return 0;
        
        // max value
        int maxVal = 0;
        for (int num : nums) {
			if (num > maxVal) maxVal = num;
		}
        
        // spf 
        int[] spf = new int[maxVal + 1];
        for (int i = 2; i <= maxVal; i++) {
            spf[i] = i; 
        }
        
        for (int i = 2; i * i <= maxVal; i++) {
            if (spf[i] == i) {
                for (int j = i * i; j <= maxVal; j += i) {
                    if (spf[j] == j) {
                        spf[j] = i;
                    }
                }
            }
        }
        
        // hashmap 
        Map<Integer, List<Integer>> primeToIndices = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int temp = nums[i];
            while (temp > 1) {
                int p = spf[temp];
                primeToIndices.computeIfAbsent(p, k -> new ArrayList<>()).add(i);
                while (temp % p == 0) {
                    temp /= p;
                }
            }
        }
        
        // bfs
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{0, 0});
        
        boolean[] visitedIndices = new boolean[n];
        visitedIndices[0] = true;
        
        boolean[] visitedPrimes = new boolean[maxVal + 1];

        while (!q.isEmpty()) {
            int[] current = q.poll();
            int curr = current[0];
            int steps = current[1];

            if (curr == n - 1) {
                return steps;
            }

            int[] nextPositions = {curr - 1, curr + 1};
            for (int nxt : nextPositions) {
                if (nxt >= 0 && nxt < n && !visitedIndices[nxt]) {
                    if (nxt == n - 1) {
                        return steps + 1;
                    }
                    visitedIndices[nxt] = true;
                    q.offer(new int[]{nxt, steps + 1});
                }
            }

            int val = nums[curr];
            if (val > 1 && spf[val] == val) {
                if (!visitedPrimes[val]) {
                    visitedPrimes[val] = true;
                    if (primeToIndices.containsKey(val)) {
                        for (int nxt : primeToIndices.get(val)) {
                            if (!visitedIndices[nxt]) {
                                if (nxt == n - 1) {
                                    return steps + 1;
                                }
                                visitedIndices[nxt] = true;
                                q.offer(new int[]{nxt, steps + 1});
                            }
                        }
                    }
                }
            }
        }

        return 0;
    }
}