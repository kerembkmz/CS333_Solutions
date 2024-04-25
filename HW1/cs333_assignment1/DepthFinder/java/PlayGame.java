import java.io.*;
import java.util.*;

public class PlayGame{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);
        int boardsize = s.nextInt();
        GameBoard gb = new GameBoard(boardsize);
        int trench = GamePlayer.playgame_dc(gb, 0, boardsize-1);
        gb.finalAnswer(trench);
	System.out.println(gb.toString());
    }
}
