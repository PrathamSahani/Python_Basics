import java.util.*;
public class tut{
    public static void main(String[] args) {
        // int max = 3;
        // boolean res = true;
        // for(int i=2; i<=Math.sqrt(max); i++){
        //     if(max%i==0){
        //         res = false;
        //         break;
        //     }
        // }
        // if(res){
        //     System.out.print(max+"ok");
        // }

        Scanner s = new Scanner(System.in);
		int n =s.nextInt();
		for(int i=0; i<n; i++){
		    int a =s.nextInt();
		    int b = s.nextInt();
		    int c = s.nextInt();
		    int arr[] = new int[a];
		    for(int j=0; j<a; j++){
		        arr[j] = s.nextInt();
		    }
            int ans =0;
		    for(int j=arr.length-1-c+1; j>=0; j=j-b){
		        ans+=arr[j];
                System.out.print(arr[j]+" ");
		    }
            System.out.print(ans);
		}
        
    }
        
    }
