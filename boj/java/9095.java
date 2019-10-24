import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int[] dp = new int[11];
        int numOfTest = sc.nextInt();
        int[] input = new int[numOfTest + 1];
        for (int i = 1; i <= numOfTest; i++) {
            input[i] = sc.nextInt();
        }
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;
        for (int i = 4; i <= 10; i++)
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
        for (int i = 1; i <= numOfTest; i++)
            System.out.println(dp[input[i]]);
    }
}