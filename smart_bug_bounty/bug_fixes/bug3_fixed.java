// Intended: Calculate average of an integer array

public class bug3 {
    public static double average(int[] nums) {
        int sum = 0;

        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }

        return (double) sum / nums.length; // FIXED
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4};
        System.out.println(average(arr)); // Expected output: 2.5
    }
}