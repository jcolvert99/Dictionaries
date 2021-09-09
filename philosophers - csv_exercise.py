# This program writes three lines of data # to a file.
def main(): 
    
    # Open a file named philosophers.txt.
    outfile = open('philosophers.txt','w')

    # write the name of three philosophers to the file
    outfile.write('John Locke'+'\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke')

    #close the file
    outfile.close


main()



#add your nane to the file - RUN SEPARATELY
outfile = open('philosophers.txt','a')
outfile.write('\nJohn Colvert')
outfile.close


#display the contents of philosophers.txt
def main():
    infile = open('philosophers.txt', 'r')
    
    #read the file's contents
    file_contents = infile.read()

    print(file_contents)


    #you can also use infile.readline() to read one line at a time:
    #line1 = infile.readline().rstrip("\n")
    #print(line1)

main()