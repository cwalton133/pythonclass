try:
    tunde = open("tunde.txt", "w")
    try:
        tunde.write("Welcome to Digital Fortress")
    except:
        print("Something went wrong with the creation of the file")
    else:
        print("file created successfully")
except NameError:
    print("Something went wrong with the creation of the file")
finally:
    tunde.close()
    
    
    
