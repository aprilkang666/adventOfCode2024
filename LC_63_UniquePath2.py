class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)        # Number of rows
        n = len(obstacleGrid[0])     # Number of columns
        # define grid
        dp=[]
        for i in range(m):
            row=[]
            for j in range(n):
                row.append(0)
            dp.append(row)
        # if start or end is the obstacles -> return 0
        if obstacleGrid[0][0] == 1:
            return 0
        # set the starting point has to be 1
        dp[0][0] = 1   
        # Fill first row and column
        for i in range(1,m):
            # if i,0 is not obstacle, and the above is not obstacle then there is one way to get there
            if obstacleGrid[i][0]==0 and dp[i-1][0]==1:
                dp[i][0]=1
        for j in range(1,n):
            # if 0,j is not obstacle, and the left is not obstacle then there is one way to get there
            if obstacleGrid[0][j]==0 and dp[0][j-1]==1:
                dp[0][j]=1
        
        # Fill the rest
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]

        return(dp[m-1][n-1])
