import java.util.Scanner;

public class stake {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        double bigRatio = sc.nextDouble();
        double smallRatio = sc.nextDouble();
        int budget = sc.nextInt();
        sc.close();

        double minLoss = Double.MAX_VALUE;
        int per1 = 45, per2 = 55;
        double bet1 = 0 , bet2 = 0;
        while (per1 <= per2) {
            double tempBet1 = (per1 * budget / 100.0) * bigRatio;
            double tempBet2 = (per2 * budget / 100.0) * smallRatio;
            double loss = Math.abs(tempBet1 - tempBet2);

            if (loss < minLoss) {
                minLoss = loss;
            } else {
                break; // Stop if the loss starts increasing
            }

            per1++;
            per2--;
        }
        bet1 = (per1 - 1)*budget / 100.0;
        bet2 = (per2 + 1)*budget / 100.0;
        System.out.printf("%.2f\n%.2f\n", bet1, bet2);
        double minlossonbet1 = budget - (bigRatio*bet1);
        double minlossonbet2 = budget - (smallRatio*bet2);
        System.out.printf("%.2f\n%.2f\n", minlossonbet1,minlossonbet2);
    }
}
