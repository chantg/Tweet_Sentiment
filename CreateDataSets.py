def main():
    file = open("Bad Words Unformated.txt","r")
    new_file = open("Bad Words Formatted.txt","w")
    count = 1
    num_added = 0
    for line in file:
        print(count)
        if(line != "\n"):
            print(line)
            utf = (line.lower().strip().encode("ascii")+",0,0,1\n")
            new_file.write(utf)
            num_added+=1
        count+=1
        if(num_added == 1000):
            break
    file.close()
    new_file.close()
main()
