class Solution:
    def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
        n = len(source)
        if len(target) != n:
            return -1
            
        R = [(p, r, c + p.count('*')) for (p, r), c in zip(rules, costs)]
        
        INF = float('inf')
        dp = [0] + [INF] * n

        for i in range(1, n+1):
            if dp[i-1] < INF and source[i-1] == target[i-1]:
                dp[i] = dp[i-1]
                
            for p, r, c in R:

                
                L = len(p); j = i-L
                if j < 0 or dp[j] == INF or target[j:i] != r:
                    continue

                
                if all(pc == '*' or pc == sc for pc, sc in zip(p, source[j:i])):
                    dp[i] = min(dp[i], dp[j] + c)
                    
        return dp[n] if dp[n] < INF else -1