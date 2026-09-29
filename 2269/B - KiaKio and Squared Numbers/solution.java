import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.HashMap;
import java.util.Map;
 
public class Solution {
 
    private static long getNext(long x) {
        long sum = 0;
        while (x > 0) {
            long d = x % 10;
            sum += d * d;
            x /= 10;
        }
        return sum;
    }
 
    public static void main(String[] args) throws IOException {
        FastScanner sc = new FastScanner();
        
        if (!sc.hasNext()) return;
        int t = sc.nextInt();
        
        final int STEPS = 2000;
        StringBuilder sb = new StringBuilder();
 
        while (t-- > 0) {
            int n = sc.nextInt();
            long[] a = new long[n];
            
            for (int i = 0; i < n; i++) {
                a[i] = sc.nextLong();
            }
 
            Map<Long, Long> freq = new HashMap<>();
 
            for (int i = 0; i < n; i++) {
                long val = a[i];
                for (int step = 0; step < STEPS; step++) {
                    val = getNext(val);
                }
                freq.put(val, freq.getOrDefault(val, 0L) + 1);
            }
 
            long totalPairs = 0;
            for (long count : freq.values()) {
                totalPairs += count * (count - 1) / 2;
            }
 
            sb.append(totalPairs).append("
");
        }
 
        System.out.print(sb.toString());
    }
 
    static class FastScanner {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
 
        boolean hasNext() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    String line = br.readLine();
                    if (line == null) return false;
                    st = new StringTokenizer(line);
                } catch (IOException e) {
                    return false;
                }
            }
            return true;
        }
 
        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
 
        int nextInt() {
            return Integer.parseInt(next());
        }
 
        long nextLong() {
            return Long.parseLong(next());
        }
    }
}