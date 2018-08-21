#operating system dependent functionality
import os

# Ask the user to enter directory path
search_path = raw_input("Enter directory path to search : ")
# Ask the user to enter type of file
file_type = raw_input("File Type : ")
# Ask the user to enter string to be searched
search_str = raw_input("Enter the search string : ")

# Add a directory separator if user didn't gave it in input
if not (search_path.endswith("/") or search_path.endswith("\\") ): 
        search_path = search_path + "/"
                                                          
# If path does not exist, set search path to Home directory
if not os.path.exists(search_path):
        search_path ="/home/aj/"

# Repeat for each file in the directory 
for fname in os.listdir(search_path):

   # open only file with given extension    
   if fname.endswith(file_type):

        # Open file
        fo = open(search_path + fname)

        # Read the first line from the file
        line = fo.readline()

        # counter for line number
        line_no = 1

        # Loop until last line of file
        while line != '' :
                # Search for string in line number
                index = line.find(search_str)
                if ( index != -1) :
                    print 'file name:',fname, '[', 'line no',line_no, ',','index',index, ']', line

                # Read next line
                line = fo.readline()  

                # Increment line counter
                line_no += 1
        # Close the file
        fo.close()
