def organize_into_profits_losses(lst):
    new_list = []
    streak = [lst[0]]
    
    for index in range(1, len(lst)):
        if (lst[index] >= 0 and streak[-1] >= 0) or (lst[index] < 0 and streak[-1] < 0):
            streak.append(lst[index])
        else:
            new_list.append(streak)
            streak = [lst[index]]
            
    new_list.append(streak)
    return new_list




def spending_statistics(lst_lsts):
    pcount = 0
    ncount = 0
    total = 0
    
    for index in lst_lsts:
        if index[0] > 0:
            pcount += 1
            
    for index in lst_lsts:
        if index[0] < 0:
            ncount += 1
            
    for index in lst_lsts:
        total += sum(index)
    
    print(f"You have had {pcount} periods of subsequent profit.")
    print(f"You have had {ncount} periods of subsequent losses.")
    print(f"Total balance: {total}")
    
    if total > 0:
        print("You're doing great! Keep it up!")
    else:
        print("Consider revising your spending habits to improve your financial situation.")
    


def main():
    weeks_lst = [1, 4, -2, 3, -3, -5, 3]
    organized_weeks_lst = organize_into_profits_losses(weeks_lst)
    print("Here are your spending habits over the last few weeks:", organized_weeks_lst)
    spending_statistics(organized_weeks_lst)

main()
