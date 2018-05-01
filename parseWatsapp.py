#The purpose of this code is to 
# Read input from whatsapp chat


import csv
from os import path
from transcript import *
import glob

#if you want all .txt files to .csv files in same directory


def parse_whatsapp():
    if len(sys.argv)!=1:
        print ("Run: python parse_whatsapp.py")
        sys.exit(1)
    files_list=glob.glob(".../*.txt") #put your directory
    files=[]
    for i in files_list:
	    st=i.replace(".../","")      ##put your directory
	    st=(st.lstrip()).rstrip()
	    files.append(st)
    for file_var in files:
		output=file_var.replace(".txt",".csv")
		c = Transcript(file_var, output)
		c.open_file()
		c.feed_lists()
		c.write_transcript()
		data = pd.read_csv(output)

if __name__ == "__main__":
    parse_whatsapp()
   	