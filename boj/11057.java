import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int input = sc.nextInt();
        int[][] dp = new int[10][1001];
        for (int i = 0; i < 10; i++)
            dp[i][1] = 1;
        for (int j = 2; j <= input; j++) {
            for (int i = 0; i < 10; i++) {
                if (i == 0)
                    dp[i][j] = 1;
                else
                    dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 10007;
            }
        }
        int result = 0;
        for (int i = 0; i < 10; i++)
            result = (result + dp[i][input]) % 10007;
        System.out.println(result);
    }
}