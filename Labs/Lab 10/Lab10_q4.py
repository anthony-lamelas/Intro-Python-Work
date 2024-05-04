def merge_databases(sky, form):
    
    for formkey, formvalue in form.items():
        newkey = formkey
        
        while newkey in sky:  
            newkey += 1
            
        if newkey != formkey:
            sky[newkey] = formvalue
            print(formvalue[0], "had their employee ID changed from", formkey, "to", newkey)
        else:
            sky[formkey] = formvalue
        
        
    merge = dict(sorted(sky.items()))      
        
    return merge
    
    
def main():
    skyward_database = {100: ["Alice", "Manager", "HR"], 101:
    ["Arnold", "Team Lead", "IT"], 102: ["Chris", "Developer", "IT"]}
    
    formulaic_database = {101: ["Lucas", "Developer", "IT"], 102:
    ["Anna", "Intern", "Marketing"], 103: ["Muhammad", "Research Analyst", "Marketing"], 200: ["Dave", "Research Analyst", "Marketing"], 90: ["Bob", "Research Analyst", "Marketing"]}
    
    merged_database = (merge_databases(skyward_database, formulaic_database)
)
    print(merged_database)
    

main()
    
    
    
    
    
    
    
   