import java.util.Scanner;

public class Main {
	
	
	static int N, totalCnt;
	static boolean[] col, slash, bSlash;
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		totalCnt = 0;
		
		col = new boolean[N+1];
		slash = new boolean[2*N+1];
		bSlash = new boolean[2*N];
		
		setQueen(1);
		System.out.println(totalCnt);
	}
	
	static void setQueen(int row) {
		
		if(row > N) {
			++totalCnt;
			return;
		}
		
		for(int c = 1; c <= N; c++) {
			// if col에 이미 있거나, 대각선 라인에 있다면 (행+열 합 / 행-열 + N으로 값 보정)
			if(col[c] || slash[row + c] || bSlash[row - c + N]) continue;
			
			col[c] = slash[row + c] = bSlash[row - c + N] = true;
			setQueen(row+1); 
			col[c] = slash[row+c] = bSlash[row - c + N] = false;
			
		}
	}

}
