/*package whatever //do not write package name here */

import java.io.*;
import java.util.HashMap;
import java.lang.Integer;
class GFG {
	public static void main (String[] args) {
		int arr[] = {10, 20, 20, 10, 10, 20, 5, 20};
		HashMap<Integer,Integer> list=new HashMap<>();
		for(int i=0;i<arr.length;i++){
		    int c=0;
		    for(int j=0;j<list.size();j++){
		       
		        if(arr[i]!=list.get(j))
		            list.put(arr[i],0);
		        else{
		             c+=1;
		            list.put(arr[i],c);
		        }
		    }
		}
		
		System.out.print(list);
	}
	
}