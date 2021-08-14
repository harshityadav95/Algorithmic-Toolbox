import java.util.Scanner;
import java.util.*;


public class FractionalKnapsack {

    private static double getOptimalValue(int capacity, int[] values, int[] weights) {
        double value = 0;
        //write your code here
        ItemValue[] iVal = new ItemValue[weights.length];

        for(int i=0;i<weights.length;i++)
        {
            iVal[i]= new ItemValue(weights[i], values[i], i);
        }

        // sorting items by value 
        Arrays.sort(iVal , new Comparator<ItemValue>(){

            @Override
            public int compare(ItemValue o1, ItemValue o2)
            {
                return o1.cost.compareTo(o2.cost);
            }
            
        });

        double totalvalue=0d;

        for(ItemValue i: iVal)
        {
            
        }









        return value;
    }

    static class ItemValue{

        Double cost;
        double  wt,val,ind;


        public ItemValue(int wt, int val , int ind)
        {
            this.wt=wt;
            this.val=val;
            this.ind=ind;

            cost = (double)(val/wt);
        }


    }


    public static void main(String args[]) {
        /*
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int capacity = scanner.nextInt();
        int[] values = new int[n];
        int[] weights = new int[n];
        for (int i = 0; i < n; i++) {
            values[i] = scanner.nextInt();
            weights[i] = scanner.nextInt();
        }
        */
     
        int capacity=50;
        int[] values = new int[]{60,100,120};
        int[] weights= new int[]{20,50,30};


        System.out.println(getOptimalValue(capacity, values, weights));
    }
} 
