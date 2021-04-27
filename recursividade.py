def fibonacci(n, count = 0, string_antepenultima = 'b', string_penultima = 'a'):
    
    if count > 1:
        
        if count != n:
            count = count+1
            string_auxiliar = string_penultima
            string_penultima = string_penultima+string_antepenultima
            string_antepenultima = string_auxiliar
            return fibonacci(n, count, string_antepenultima, string_penultima)
        
        else:
            return string_penultima+string_antepenultima
    
    elif count == 0:
        
        if count == n:
            return string_antepenultima
        
        else:
            count = count+1
            return fibonacci(n, count)
    
    else:
        
        if count == n:  
            return string_penultima
        
        else:
            count = count+1
            return fibonacci(n, count)

n = int(input(""))
string_final = fibonacci(n)
print(string_final)