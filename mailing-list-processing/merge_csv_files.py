with open('cleaned/merged.csv', 'a', newline='') as fout:
    
    with open('cleaned/new_list_0.csv', 'r') as g:
        for line in g:
            fout.write(line)

    for i in range(1, 5):
        with open('cleaned/new_list_{}.csv'.format(str(i)), 'r') as fread:
            next(fread)
            for line in fread:
                fout.write(line)
