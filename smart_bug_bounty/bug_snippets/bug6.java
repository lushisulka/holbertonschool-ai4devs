public class bug6 {

    // Returns true if two strings are equal, ignoring case.
    public static boolean stringsEqual(String a, String b) {
        return a.toUpperCase() == b.toUpperCase(); // Bug: == compares references, not values. Should use .equals()
    }

    // Returns the number of words in a sentence.
    public static int wordCount(String sentence) {
        if (sentence == null || sentence.isEmpty()) {
            return 0;
        }
        String[] words = sentence.trim().split(" ");
        return words.length; // Bug: multiple spaces between words produce empty strings in the array, inflating the count
    }

    // Computes n! (factorial) and returns it as an int.
    public static int factorial(int n) {
        int result = 1;
        for (int i = 1; i <= n; i++) {
            result *= i; // Bug: int overflows for n >= 13, should use long or BigInteger
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(stringsEqual("Hello", "hello")); // Should print true, prints false
        System.out.println(wordCount("hello   world")); // Should print 2, prints 4
        System.out.println(factorial(15)); // Should print 1307674368000, prints wrong value due to overflow
    }
}