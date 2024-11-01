from random import choice


# making the winning ticket
def get_winning_ticket(possibilities):
    '''Return the winning ticket from options from possibilities'''
    winning_ticket=[]

    # we dont want repeating number or letters

    while len(winning_ticket) < 4:
        pulled_ticket = choice(possibilities) # the current ticket is chosen from possibilites

        # only add the pulled ticket if it hasnt been pulled already

        if pulled_ticket not in winning_ticket:
            winning_ticket.append(pulled_ticket)# put the current ticket into winning ticket if it isnt in there already
    return winning_ticket
    
def check_ticket(played_ticket, winning_ticket):
    # check elements in the played ticket. if they have none in the winning ticket then return false

    for element in played_ticket:
        if element not in winning_ticket:
            return False # if an element isnt in winning ticket, keep it false
        
    return True #if all elements are in the ticket


def make_random_ticket(possibilites):
    '''make a random ticket from possibilites'''
    ticket = []
    #no repeating letters or numbers
    while len(ticket) < 4:
        pulled_ticket = choice(possibilities) # the ticket is a choice from possibilities

        #only add the ticket in ticket if it hasnt been pulled yet
        if pulled_ticket not in ticket:
            ticket.append(pulled_ticket) # If not ticket hasnt been repeated, it is put in ticket

    
    return ticket


possibilities = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e']
winning_ticket = get_winning_ticket(possibilities)

plays = 0 #how many times it starts
won = False 


while not won: # this is when the won hasnt been toggled true
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays+= 1
    


if won:
    print("Your ticket won!")
    print(f"Your Ticket is: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")



    
    