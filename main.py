# Name the lyrics game

print("""
Name of the lyrics game

Fill in the blank lyrics!
(Type in the blank lyrics and see if you are as cool as me.)
""")
restart = True
counter = 0
lyric = ""
while restart == True :
  print("Me desespera la fauna _____________, etílica y farlopera")
  print()
  lyric = input("")
  if lyric == "discotequera":
    restart = False
    break
  else:
    print("Nope, try again")
    counter += 1
print("Well done! It only took you",counter,"attempts!")
  
  