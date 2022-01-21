import java.util.*;

class Code_3_07_1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] H = new int[N+1];
        for(int i = 0;i<=N;i++){
            H[i] = sc.nextInt();
        }

        // 動的計画法
        int[] dp = new int[N+1];
        dp[1] = 0;
        for(int i=2;i<=N;i++){
            if(i==2){
                dp[i] = Math.abs(H[i-1]-H[i]);
            }
            if(i>=3){
                dp[i] = Math.min(dp[i - 1] + Math.abs(H[i - 1] - H[i]),dp[i - 2] + Math.abs(H[i - 2] - H[i]));
            }
        }
    }
}