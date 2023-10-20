import time

print('-------Chatbot-----')
print("what is your name?")
print("what kind of food do you like ?")
print("what is your favorite color?")

def printSlowly(str):
    for i in str:
        time.sleep(0.15)
        print(i,end='')
        print()
request= ''

while request != 'exit':
    request= input( 'Ask Me A Question ')
    request= request.lower()
    if request == "what is your name?":
        printSlowly('naomi')
   
    elif request == "what kind of food do you like ?":
        print('cheesecake')
    elif request == "what is your favorite color?":
        printSlowly('lavender')
    elif request == 'exit': 
        print("Thanks for using CahtBot")
   
print('Sorry, I do not understand your question')