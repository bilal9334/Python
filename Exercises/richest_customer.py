def maximumWealth(accounts: list[list[int]]) -> int:
    
    totalWealth = 0
    
    for account in accounts:
        customer_wealth = sum(account)

        if customer_wealth > totalWealth:
            totalWealth = customer_wealth
    
    return totalWealth
        
        


accounts = maximumWealth([[1,5], [7,3], [3,5]])
print(accounts)

