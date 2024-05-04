def create_word_pyramid(string,levels):
    
    ordinal = ord(string) -1
    pyramid = ""
    
    for index in range (0,levels +1):
        
        for char in range (index, 0,-1):
            pyramid += (chr(ordinal))
            
        ordinal += 1
        pyramid += "\n"
        
    return pyramid


def add_pyramid_level(string):
    if not string:
        return ""
    
    last_char = string[-2]
    line = string.count("\n") + 2
    ordinal = ord(last_char) + 1
    new_char = chr(ordinal)
    new_line = string  + new_char*line
    
    return new_line


char = "B"
levels = 5

word_pyramid = create_word_pyramid(char, levels)
print("Word Pyramid:")
print(word_pyramid)
updated_pyramid = add_pyramid_level(word_pyramid)
print("\nUpdated Word Pyramid:")
print(updated_pyramid)