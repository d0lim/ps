import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int[][] dp = new int[10][101];
        int input = sc.nextInt();
        for (int i = 1; i <= 9; i++)
            dp[i][1] = 1;
        for (int i = 2; i <= input; i++) {
            for (int j = 0; j <= 9; j++) {
                if (j == 0)
                    dp[j][i] = dp[1][i - 1];
                else if (j == 9)
                    dp[j][i] = dp[8][i - 1];
                else
                    dp[j][i] = (dp[j - 1][i - 1] + dp[j + 1][i - 1]) % 1000000000;
            }
        }
        long res = 0;
        for (int i = 0; i <= 9; i++) {
            res += dp[i][input];
        }
        System.out.println(res % 1000000000);

    }
}