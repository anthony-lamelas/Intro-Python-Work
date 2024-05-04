"""
Author: [Anthony Lamelas]
Assignment / Part: HW9 - Q2, Q3
Date due: April 11, 11:59pm
I pledge that I have completed this assignment without collaborating with
anyone else, in conformance with the NYU School of Engineering Policies and
Procedures on Academic Misconduct.
"""

def is_haiku(str):
    
    if str.count("/") == 2:
        split_str = str.split(",")
        if ("/" in split_str[4]):
            if ("/" in split_str[10]):
                if (split_str[10] is split_str[-5]):
                    return True
                else:
                    print("WARNING: The third line is not 5 syllables long.")
                    return False
            else:
                print("WARNING: The second line is not 5 syllables long.")
                return False
                
        else:
            print("WARNING: The first line is not 5 syllables long.")
            return False
        
    else:
        return("WARNING: The haiku does not contain 3 lines. \n", False)
        

def haiku_string_parser(str):
    haiku = ""
    if is_haiku(str):
        haiku = str.replace(" ,", " ").replace(",","").replace("/", "\n")
        return haiku
    else:
        return haiku


        
def main():
    haiku_string = "clouds ,mur,mur ,dark,ly/it ,is ,a ,blin,ding ,ha,bit/ga,zing ,at ,the ,moon"
    formatted_haiku = haiku_string_parser(haiku_string)
    print(formatted_haiku)
main()
