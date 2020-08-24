f =open("demofile2.txt" , "r")

print("Contents are =====")
print(f.readline())
f.close()
f =open("demofile2.txt","a")
f.write("Now the file has more content!")
f.close()
#open and read the file after the appending:

print("after write ---")
f =open("demofile2.txt", "r")

print(f.read())
f.close()
