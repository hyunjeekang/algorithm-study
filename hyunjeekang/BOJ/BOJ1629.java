import java.io.*;
import java.util.*;

public class BOJ1629 {
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        System.out.println(recur(A, B, C));
    }

    private static long recur(int a, int n, int c){

        if(n == 1) return a%c;

        long rpt = recur(a, n/2, c)%c;
        long rtn = rpt * rpt % c;

        if(n%2 == 1) return rtn * a % c;
        else return rtn;
    }
}
