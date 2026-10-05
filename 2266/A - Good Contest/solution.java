import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        if(sc.hasNextInt()){
            int t = sc.nextInt();
            while(t-- > 0){
                int n = sc.nextInt();
                int a1 = sc.nextInt();
                int a2 = sc.nextInt();
                int a3 = sc.nextInt();
                int strong = Math.min(a1, Math.min(a2, a3));
                int weak = n-strong;
                System.out.println(weak);
            }
        } 
        sc.close();
    }
}