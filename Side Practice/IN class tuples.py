def update_frequencies(sequ, frequ):
    result = []
    
    for nuclu_tupu in frequ:
        nucleo, count = nuclu_tupu[0], nuclu_tupu[1]
        result += (nucleo, count)
        count += sequ.count(nucleo)
        result.append((nucleo, count))
    
    return result
    
    
    
    
    
new_sequence = 'AACCTTAGG'
current_frequencies = [('A',2),('C',6), ('T',4),('G',1)]

current_frequences = update_frequencies(new_sequence, current_frequencies)


print(update_frequencies)