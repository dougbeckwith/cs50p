def main():
     # Define the accepted coin denominations and the amount due
    coins_accepted = [5, 10, 25]
    amount_due = 50
    
    while True:
        # Prompt the user to insert a coin
        coin_amount = int(input("Insert a Coin: "))

        if coin_amount in coins_accepted:
            amount_due -= coin_amount

            if amount_due <= 0:
                # Display the change owed and exit
                print("Change Owed:", abs(amount_due))
                break

        # Display the updated amount due
        print("Amount Due:", amount_due)
        
    
main()