import java.util.Random;

public class CoinToss {
    public static void main(String[] args) {
        Random random = new Random();

        // Simulate tossing three coins
        boolean coin1 = random.nextBoolean(); // true for heads, false for tails
        boolean coin2 = random.nextBoolean();
        boolean coin3 = random.nextBoolean();

        System.out.println("Coin 1: " + (coin1 ? "Heads" : "Tails"));
        System.out.println("Coin 2: " + (coin2 ? "Heads" : "Tails"));
        System.out.println("Coin 3: " + (coin3 ? "Heads" : "Tails"));
    }
}
In this code, the Random class is used to generate random boolean values. nextBoolean() generates either true or false randomly. If it's true, it represents heads; if it's false, it represents tails. Each coin toss result is then printed to the console. Each time you run the program, you will get different random outcomes for the three coins.





