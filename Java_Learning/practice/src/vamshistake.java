
public class vamshistake {

    public static void main(String[] args) {
        float ratio1 = 1.70f;
        float ratio2 = 1.95f;
        int budget = 1200;
        int[] ans = betAmount(ratio1, ratio2, budget);
        int a1 = ans[1];
        int a2 = ans[2];
        float p1 = a1 * ratio1;
        float p2 = a2 * ratio2;
        System.out.println("Loss exp = " + ans[0]);
        System.out.println("Amount 1 = " + a1 + " Ratio 1 = " + ratio1);
        System.out.println("Amount 2 = " + a2 + " Ratio 2 = " + ratio2);
        System.out.println("Profit 1 = " + p1);
        System.out.println("Profit 2 = " + p2);
        System.out.println("If 6 promo works = " + ((p1 + p2) - budget));
        System.out.println("Loss 1 = " + (p1 >= budget ? 0 : budget - p1));
        System.out.println("Loss 2 = " + (p2 >= budget ? 0 : budget - p2));
    }

    static int[] betAmount(float r1, float r2, int budget) {
        int[] ans = { Integer.MAX_VALUE, 0, 0 };
        int amount1 = budget;
        int amount2 = 0;
        int totalLoss;
        while (amount1 >= 0) {
            int profit1 = (int) (amount1 * r1);
            int profit2 = (int) (amount2 * r2);
            // System.out.println("amount -> " + amount1 + " profit -> " + profit1);
            // System.out.println("amount -> " + amount2 + " profit -> " + profit2);
            // System.out.println();
            if (profit1 < 2150 && profit2 < 2150) {
                int loss1 = profit1 >= budget ? 0 : budget - profit1;
                int loss2 = profit2 >= budget ? 0 : budget - profit2;

                // totalLoss = loss1 + loss2;
                totalLoss = Math.max(loss1, loss2);
                if (totalLoss < ans[0]) {
                    ans[0] = totalLoss;
                    ans[1] = amount1;
                    ans[2] = amount2;
                }
            }
            amount1 -= 1;
            amount2 += 1;
        }
        return ans;
    }
}
