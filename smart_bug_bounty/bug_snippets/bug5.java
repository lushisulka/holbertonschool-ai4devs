import java.util.ArrayList;
import java.util.List;

public class bug5 {

    // Returns the first element of a list, or null if empty.
    public static String getFirst(List<String> items) {
        if (items.isEmpty()) {
            return null;
        }
        String result = items.get(0);
        System.out.println(result.toUpperCase()); // Bug: if result is null this throws NullPointerException
        return result;
    }

    // Reverses an array in place.
    public static void reverseArray(int[] arr) {
        int n = arr.length;
        for (int i = 0; i <= n / 2; i++) { // Bug: should be i < n / 2, swaps middle element with itself on odd-length arrays (harmless but incorrect intent), and overshoots on even
            int temp = arr[i];
            arr[i] = arr[n - i - 1];
            arr[n - i - 1] = temp;
        }
    }

    // Calculates the sum of integers from 1 to n.
    public static int sumToN(int n) {
        int sum = 0;
        for (int i = 1; i < n; i++) { // Bug: should be i <= n, misses the last number
            sum += i;
        }
        return sum;
    }

    public static void main(String[] args) {
        System.out.println("Sum 1-5: " + sumToN(5)); // Should print 15, prints 10

        int[] arr = {1, 2, 3, 4, 5};
        reverseArray(arr);
        for (int x : arr) System.out.print(x + " ");
    }
}