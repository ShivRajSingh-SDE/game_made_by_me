print('''      .--..--..--..--..--..--.
    .' \  (`._   (_)     _   \
  .'    |  '._)         (_)  |
  \ _.')\      .----..---.   /
  |(_.'  |    /    .-\-.  \  |
  \     0|    |   ( O| O) | o|
   |  _  |  .--.____.'._.-.  |
   \ (_) | o         -` .-`  |
    |    \   |`-._ _ _ _ _\ /
    \    |   |  `. |_||_|   |
    | o  |    \_      \     |     -.   .-.
    |.-.  \     `--..-'   O |     `.`-' .'
  _.'  .' |     `-.-'      /-.__   ' .-'
.' `-.` '.|='=.='=.='=.='=|._/_ `-'.'
`-._  `.  |________/\_____|    `-.'
   .'   ).| '=' '='\/ '=' |
   `._.`  '---------------'
           //___\   //___\
             ||       ||
             ||_.-.   ||_.-.
            (_.--__) (_.--__)''')
print("Hello Earth people welcome to treasur hunt game made by Master shiv. In this game u have to make decision's to hunt down the treasur if it's goes wrong u will be dead but if your chossen option become rigth u will advanced to go next level so good luck. Make your decision's wishelly ")
name=input("First tell us your name =  ")
bank=input("which bank do you have account on =  ")
ans1=input("\n u are currently in a bulding which  is about to break down in 60 sec so u have two option for exit from this buliding 1rst 'go through stares' or 2nd 'go through lift' it's up to u to decide  \n == stares/lift   =   ").lower()
if ans1 == "stares":
 ans2=input(f" \n {name} look like u succeed to escape from level 1 so now lets go to level 2 \n you are currently on a road after escaping from bulding crash so now u are in middel of the road where are two people standing in front of you one of them have knife on his hand and second one of them  have a rope in his solder  which one of them do wana ask for help \n knife man or rope man = ").lower()
 if ans2 == "rope man":
  ans3 =input(f"\n {name} looks like u servive over 1rst and 2nd trial both so lets go to ower last trial  so let's get going \n there is three gate in front of you one of them is full of fire second is full of ice last one is way of exit choose whislly may god wish u luck \n option 1. Orange Door 2. Green Door 3. Blue Door =  ").lower()
  if ans3 == "green door":
    print(f" \n oohoh {name} you finally able to succed my all trial you are champian now👑")
    print(f"Your {bank} account balance is ₹10,00,000 ")
  else:
    print(f"{name} Game is over You are dead🔪 ")
   
  
 
 else:
   print(f"{name} you are dead buddy try next time 🩸🩸🔪🔪 ")
  
   
   
  
  
  
else:
  print(f"{name} you are dead buddy 🤣 be carefull next time")