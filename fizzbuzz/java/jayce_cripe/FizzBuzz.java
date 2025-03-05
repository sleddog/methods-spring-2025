public class FizzBuzz {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Please provide a number as an argument.");
            return;
        }

        int n = Integer.parseInt(args[0]);
        System.out.println("Input: n = " + n);

        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println("BobCat");
            } else if (i % 3 == 0) {
                System.out.println("Bob");
            } else if (i % 5 == 0) {
                System.out.println("Cat");
            } else {
                System.out.println(i);
            }
        }
    }
}