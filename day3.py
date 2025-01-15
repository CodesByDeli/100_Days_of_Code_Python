print(r'''
                __
                             .d$$b
                           .' TO$;\
                          /  : TP._;
                         / _.;  :Tb|
                        /   /   ;j$j
                    _.-"       d$$$$
                  .' ..       d$$$$;
                 /  /P'      d$$$$P. |\
                /   "      .d$$$P' |\^"l
              .'           `T$P^"""""  :
          ._.'      _.'                ;
       `-.-".-'-' ._.       _.-"    .-"
     `.-" _____  ._              .-"
    -(.g$$$$$$$b.              .'
      ""^^T$$$P^)            .(:
        _/  -"  /.'         /:/;
     ._.'-'`-'  ")/         /;/;
  `-.-"..--""   " /         /  ;
 .-" ..--""        -'          :
 ..--""--.-"         (\      .-(\
   ..--""              `-\(\/;`
     _.                      :
                             ;`-
                            :\                           
*******************************************************************************
''')
print("Will you be able to complete the journey?")
print("You are lost! So naturally your job is to get to safety and save your life. If you can't manage to get to safety, it doesn't matter! ... Well I mean... it only bothers you, but good news is that if you dont make it, it won't bother you anymore.")
print(".... you finally woke up, the first thing you feel is the cold, apparently the snow under you is responsible for that, but where are you? You raise your head and see the trees covered with frost all around you, behind them the foothills of some mountains covered in fog and the setting sun.")
print("How do you decide? Will you get up to gather wood and start a fire? or you decide to follow the path with lies before you?")
decides1 = input("Type 'fire' to start a fire or type 'path' for get a path:")

if decides1 == "fire":
    print("You've survived until dawn and avoid freeze to death, but you're still cold, and now the hunger and thirst are starting to remind of their existence.")
    decides2 = input("What will you do? You can follow the 'path' and hope that you find some of civilisation or you can try to somehow satisfy your 'hunger' and thirst.")
    if decides2 == 'path':
        print("You follow the path that lay before you, it is a small winding track that slowly disappears. You start to panic. The path has completely disappeared and you turn around several times, you are confused where you actually came from. So you set off in some direction and ran a few of kilometers. You can't catch your breath, you are trying to calm down, looking around.")
        decides3 = input("On your 'left' side you can see a steep slope, on your 'right' side there is chasm, in 'front' of you there is a thicket, which looks like someone has gone through broken branches, and 'behind' you there is a less dense thicket. Where are you going ? ")
        if decides3 == 'right':
            print("You proceed carefully down the steep hill, the ground is damp, the moss on the stones is slippery. The sun is setting again, your throat starts to tighten with fear, but the fog slowly begins to disappear and above the tree tops at the bottom of the ravine you see something that is definitely not trees. You try to get down faster, you can't believe, it can't be true ... but it's there, it's only supposed to be in legends, it doesn't exist, but you know it's it!  The valley of Imladris. In common tongue it's known by another name......Rivendell...")
        elif decides3 == 'left':
            print("You decide to head upwards, at least you can look around where you are. The road is steep and unpleasant, but you see a strange crack at the foot of the mountain, you go to see it closer. It's a cave! So tonight's place to lay down is clear. You spread the fire, you're glad it doesn't blow on you, and you fall asleep in the domain of safety. However, this cave hides a hidden path. Today, the goblins are sure of their prey. >> GAME OVER")
        elif decides3 == 'front':
            print("The broken branches in the thicket caught your attention, so you set out straight behind your nose, following all the tracks that lead you deeper and deeper into the forest. Your end was very quick. The footprints belonged to the orcs who hung you and attacked you from behind. Following the rules was never a strong point they cared about >> GAME OVER")
        elif decides3 == 'behind':
            print("You had the feeling that when you go back, you will find the path that gradually disappeared and you will try to reach its other end. But the Beorn have a different opinion on that, he never was a fan of dwarves >> GAME OVER")
    else:
        print("In an attempt to find something to eat, you decided to go off the road, you went through the forest valley where you found the river. While trying to catch a salmon that was jumping against the current through the sluice, your foot slipped on the smooth stones...you were swept away by the current >> GAME OVER.")
else:
    print("You froze to death >> GAME OVER ")