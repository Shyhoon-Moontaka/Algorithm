public class Nqueen{
    public static void main(String[] args){
        Solution s=new Solution();
        int n=4;
        System.out.println(s.totalNQueens(n));
    }
}
class Solution {
    int total = 0;
    
    public int totalNQueens(int n) {
        boolean[] cols = new boolean[n];
        boolean[] diag1 = new boolean[2 * n - 1];
        boolean[] diag2 = new boolean[2 * n - 1];
        backtracking(0, cols, diag1, diag2, n);
        return total;
    }
    
    private void backtracking(int row, boolean[] cols, boolean[] diag1, boolean[] diag2, int n) {
        if (row == n) {
            total++;
            return;
        }
        
        for (int col = 0; col < n; col++) {
            int d1 = row + col;
            int d2 = row - col + n - 1;
            if (cols[col] || diag1[d1] || diag2[d2]) continue;
            
            cols[col] = true;
            diag1[d1] = true;
            diag2[d2] = true;
            backtracking(row + 1, cols, diag1, diag2, n);
            cols[col] = false;
            diag1[d1] = false;
            diag2[d2] = false;
        }
    }
}