import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int[] dp = new int[1001];
        int input = sc.nextInt();
        dp[1] = 1;
        dp[2] = 3;
        for (int i = 3; i <= input; i++)
            dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 10007;
        System.out.println(dp[input]);
    }
}