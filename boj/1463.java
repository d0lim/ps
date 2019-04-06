import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int[] dp = new int[1000001];
        int input = sc.nextInt();
        dp[1] = 0;
        dp[2] = 1;
        dp[3] = 1;
        for (int i = 4; i <= input; i++) {
            int tmp = 0;
            if (i % 3 == 0) {
                if (dp[i / 3] != 0) {
                    tmp = dp[i / 3] + 1;
                }
            }
            if (i % 2 == 0) {
                if (dp[i / 2] != 0) {
                    if (tmp != 0)
                        tmp = dp[i / 2] + 1 < tmp ? dp[i / 2] + 1 : tmp;
                    else
                        tmp = dp[i / 2] + 1;
                }
            }
            if (dp[i - 1] != 0)  {
                if (tmp != 0)
                    tmp = dp[i - 1] + 1 < tmp ? dp[i - 1] + 1 : tmp;
                else
                    tmp = dp[i - 1] + 1;
            }
            dp[i] = tmp;
        }
        System.out.println(dp[input]);
    }
}