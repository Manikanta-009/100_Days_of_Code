# 100 Days of Code Challenge

## Day 8: find_last_served_person Challenge

### Challenge Description
"""
You are given a list of meatball weights and you need to distribute them among a certain number of participants.
Each day, a fixed quantity of meatballs is taken from the front of the list and served to the current participant.
If the remaining weight of a meatball is positive, it's put back at the end of the list for the next day.
The process continues until all meatballs are completely consumed.
Determine the index of the last person to be served.

Input:
- meatball_weights (list of integers): A list of integers representing the weights of the meatballs.
- num_participants (integer): The number of participants.
- daily_quantity (integer): The quantity of meatballs served to each participant daily.

Output:
- last_served_person (integer): The index of the last person to be served.

Example Input:
meatball_weights = [8, 9, 3, 5]
num_participants = 4
daily_quantity = 2

Example Output:
Index of the Last Served Person: 3
"""
### Solution Code

def find_last_served_person(meatball_weights, num_participants, daily_quantity):
    current_person = 1

    while meatball_weights:
        current_meatball = meatball_weights[0]  # Serve the meatball from the front of the list
        meatball_weights = meatball_weights[1:]  # Remove the served meatball from the list
        current_meatball -= daily_quantity
        
        if current_meatball > 0:
            meatball_weights.append(current_meatball)  # If meatball remains, add it back to the list
        
        print(f"Remaining Meatballs for Person {current_person + 1}: {meatball_weights if meatball_weights != [] else [0]}")
        current_person = (current_person + 1) % num_participants  # Move to the next person's index

    return current_person

def main():
    meatball_weights = [8, 9, 3, 5]
    print("Initial Meatballs for Person 1:", meatball_weights)
    
    num_participants = 4
    daily_quantity = 2

    last_served_person = find_last_served_person(meatball_weights, num_participants, daily_quantity)
    print("\nIndex of the Last Served Person:", last_served_person)

if __name__ == "__main__":
    main()

"""
Connect with me on 
[LinkedIn](https://www.linkedin.com/in/manikanta-nallam/) 
for more coding challenges, updates on my 100 days of code journey.

Stay tuned for tomorrow's coding challenge. Happy coding!
"""
