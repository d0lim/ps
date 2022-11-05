package programmers;

import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String integers = sc.next();

        int[] counts = new int[10];

        for (char c : integers.toCharArray()) {
            int i = Integer.parseInt(String.valueOf(c));
            counts[i]++;
        }

        for (int i = 9; i >= 0; i--) {
            for (int j = 0; j < counts[i]; j++) {
                System.out.print(i);
            }
        }

        System.out.print('\n');
    }
}
