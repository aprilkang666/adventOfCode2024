class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    # creat the grid
        dp=[]
        for i in range(m): #creat row
            row=[]
            for j in range(n):#create column
                row.append(0)
            dp.append(row)
    # fill first row and first column
        for i in range(m):
            # fill the entire first row with 1 because only one way to get there is by moving right
            dp[i][0]=1
        
        for j in range(n):
             # fill the entire first column with 1 because only one way to get there is by moving right
            dp[0][j]=1
        
    # fill the entire table
        for i in range(1,m):
            for j in range(1,n):
                #either come from up or left
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        
        return(dp[m-1][n-1])
