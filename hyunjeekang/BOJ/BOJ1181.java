import java.io.*;
import java.util.*;

public class BOJ1181 {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());

        // 중복 제거
        HashSet<String> set = new HashSet<>();
        for (int i = 0; i < N; i++) {
            set.add(br.readLine());
        }

        // Set -> List
        List<String> list = new ArrayList<>(set);

        // 정렬 
        list.sort((s1, s2) -> {
            if (s1.length() == s2.length()) {
                return s1.compareTo(s2); // 2. 사전순
            }
            return s1.length() - s2.length(); // 1. 길이순
        });

        // 출력
        for (String word : list) {
            sb.append(word).append("\n");
        }
        System.out.println(sb);
    }
}