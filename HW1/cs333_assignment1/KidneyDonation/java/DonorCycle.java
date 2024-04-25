import java.io.*;
import java.util.*;

public class DonorCycle{

	public static boolean isInCycle(int[][] matchScores, int[] donorFriends, int query){
		return false;
	}

	public static void main(String[] args){

		Scanner s = new Scanner(System.in);

		int n = s.nextInt();
		int m = s.nextInt();

		String donorsLine = s.next();
		String[] donorsArray = donorsLine.split(",",0);
		int[] donorsFriends = new int[donorsArray.length];
		for(int i=0; i<m; i++){
			donorsFriends[i] = Integer.parseInt(donorsArray[i]);
		}

		int[][] matchScores = new int[m][n];
		for(int i=0; i<m; i++){
			String matchscoreLine = s.next();
			String[] matchscoreArray = matchscoreLine.split(",",0);
			for(int j=0; j<n; j++){
				matchScores[i][j] = Integer.parseInt(matchscoreArray[j]);
			}	
		}
		int query = s.nextInt();
		System.out.println(isInCycle(matchScores, donorsFriends, query));
	}


}
