import requests
response = requests.get("https://random-word-api.herokuapp.com/word?")
word = (response.json()[0])
#word = input()
lives = 5
length = len(word)
op = '_'*length
ext = [i for i in op]
flag = 0




while lives != 0:
    guess=input("Guess the letter of word: ")
    pos = []
    if guess in word: #will search for the input character in the word generated randomnly
        for i in range(length):
            if word[i]==guess:
                    pos.append(i)
        else:
            for k in pos:
                for x in range(length):
                    if x==k:
                        ext[k]=guess
            op = ''.join(ext)
            print(op)
            if op==word:
                print("Kudos! I knew it you are a genius")
                break
                        
    else:
        lives -= 1
        print("Only {} lives remaining, observe carefully and re-guess".format(lives))
        print(op)
    
else:
    print("Maximum attempts reached...Sorry you were unable to guess the word")
    
    
    

    

        
    
      



    
    
    
    
    
 
    
    
    
    
    
    
    
    
    
    
    
    
    
