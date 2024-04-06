def main():
    print("Second Module's Name :{}".format(__name__))

if __name__== '__main__':
    #main()
    print("Run directly")
else:
    print("Run From Import")
