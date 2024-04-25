import java.io.*;
import java.util.*;

public class GameBoard{

    public int size;
    protected int minLocation;
    protected double minValue;
    protected int queriesRemaining;
    protected double[] board;

    GameBoard(int boardsize){
	Random rand = new Random();
        this.size = boardsize;
        this.queriesRemaining = 3*(int) Math.ceil(Math.log(boardsize) / Math.log(2));	
        this.board = new double[boardsize];
        this.minLocation = rand.nextInt(boardsize-4)+2;
        this.minValue = rand.nextInt(boardsize*boardsize*boardsize)+10;
        this.board[0] = 1;
        this.board[1] = 2;
        this.board[boardsize-1] = 3;
        this.board[boardsize-2] = 4;
    }

    public String toString(){
        String s = "[";
        for (double d : this.board){
            if (d > 0){s += d + ",";}
            else{s += "??,";}
        }
        return s+"]";
    }

    public double ping(int location){
        --this.queriesRemaining;
        if (this.queriesRemaining < 0){
            System.out.println("out of pings");
            return 0;
        }
        if (this.board[location] > 0){return this.board[location];}
        if (location == this.minLocation){
            this.board[location] = this.minValue;
            return this.board[location];
        }
        double depth = 0;
        int pinged_left = 1;
        for (int i = 0; i < this.size; i++){
            depth = this.board[i];
            if (i < location && depth > 0){
                pinged_left = i;
            }
        }
        depth = 0;
        int pinged_right = this.size-2;
        for (int i = this.size-1; i > 0; i--){
            depth = this.board[i];
            if (i > location && depth > 0){
                pinged_right = i;
            }
        }
        if (location < this.minLocation){
	    if (pinged_right > this.minLocation){
                this.board[location] = (this.board[pinged_left] + this.minValue) / 2;
	    }
            else{
                this.board[location] = (this.board[pinged_left] + this.board[pinged_right]) / 2;
	    }

        }
        else{
	    if (pinged_left < this.minLocation){
                this.board[location] = (this.board[pinged_right] + this.minValue) / 2;
	    }
	    else{
                this.board[location] = (this.board[pinged_left] + this.board[pinged_right])/2;
	    }
	}
        return this.board[location];
    }

    public void finalAnswer(int location){
        if (this.queriesRemaining < 0){
            System.out.println("out of pings");
        }
	else if (this.board[location-1] <= 0 || this.board[location] <= 0 || this.board[location+1] <= 0) {
            System.out.println("neighbors not queried");
        }
        else if (this.board[location-1] < this.board[location] && this.board[location] > this.board[location+1]){
            System.out.println("trench found!");
        }
        else{
            System.out.println("not a trench");
        }
    }
}














