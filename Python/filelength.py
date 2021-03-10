f_names = ['Ping.txt', 'siddhartha.txt', 'moby_dick.txt','range.txt','little_women.txt'] 
for f_name in f_names: # Report the length of each file found. 
    try: 
        with open(f_name) as f_obj: 
            lines = f_obj.readlines() 
    except FileNotFoundError: # Just move on to the next file. 
        pass 
    else: 
            num_lines = len(lines) 
            msg= "{0} has {1} lines.".format( f_name, num_lines) 
            print(msg)