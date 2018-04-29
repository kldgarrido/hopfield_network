

def convert_vector_to_graph(clasified_pattern):
    i=0
    result = ""
    for character in clasified_pattern[0]:
        if i%5==0:
            result+='\n'
        if character == 1:
            result += '0'
        else:
            result += '.'
        i+=1
    return result