import java.io.*;
import java.util.*;

public class BOJ1931 {

    public static class Meet implements Comparable<Meet> {
        int start, end;

        public Meet(int start, int end) {
            this.start = start;
            this.end = end;
        }

        @Override
        public int compareTo(Meet o) {
            // 1. 종료 시간
            if (this.end == o.end)
                // 2. 시작 시간
                return Integer.compare(this.start, o.start);
            return Integer.compare(this.end, o.end);
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        List<Meet> list = new ArrayList<>();
        int N = Integer.parseInt(br.readLine());
        
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            list.add(new Meet(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }
        
        Collections.sort(list);

        int count = 0;
        int endTime = 0; // 직전 회의 종료 시간

        for (int i = 0; i < list.size(); i++) {
            Meet m = list.get(i);
            
            // 지금 회의 시작 시간이 이전 회의 종료 시간보다 같거나 크면 됨 
            if (m.start >= endTime) {
                endTime = m.end;
                count++;
            }
        }

        System.out.println(count);
    }
}