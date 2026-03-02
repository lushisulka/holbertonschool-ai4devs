public class Bug3 {
    public static int divideNumbers(int a, int b) {
        return a / b;
    }

    public static void main(String[] args) {
        int x = 10;
        int y = 0;

        System.out.println("Result: " + divideNumbers(x, y));
    }
}