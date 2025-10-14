# The script of the game goes in this file.
# last changed 5am on 20/09/2025
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Tao = Character("Tao")
define Aria = Character("Aria")
define Melody = Character("Melody", color="#6f068ad3")
define Melody2 = Character("Melody", color="#6f068ad3")
define Rex = Character("Rex")
define Xander = Character("Xander")
define Eileen = Character("Eileen")
define Alice = Character("Alice")
define NotAlice = Character("NotAlice")
define Narrator = Character("")

# List of possible locations (optional, for reference)
define PlayerLocation = ("Dormitory", "Atrium", "Corridor", "Greenhouse", "Alchemy Lab", "Courtyard", "Artificing Lab", "Library", "Archive", "Forest", "Teacher's Lounge", "Clearing", "Grotto")#grotto only has night, clearing only has night, teachers lounge is just corridor night
default Location = "Dormitory"
# Variable to track the player's current location

default planted_seeds = []
default seed_options = ["Winged Jasmine", "Snapjaw Orchid", "Moon Melon", "Sanguine Lily"]
default book_collected = []

#Seed Variables
$ planted_seeds = []
$ seed_options = ["Winged Jasmine", "Snapjaw Orchid", "Moon Melon", "Sanguine Lily"]
$ Flag_WingedJasminePlanted = "Winged Jasmine" in planted_seeds
$ Flag_SnapjawOrchidPlanted = "Snapjaw Orchid" in planted_seeds
$ Flag_MoonMelonPlanted = "Moon Melon" in planted_seeds
$ Flag_SanguineLilyPlanted = "Sanguine Lily" in planted_seeds
# Now you can reference planted_seeds[0] as 'seed 1' and planted_seeds[1] as 'seed 2' in dialogue

# Book Variables
$ book_collected = []
$ book_options = ["The Illustrated Botanical", "The Woodwitch Guide to Home Gardening", "Carnivorous Plants of Viordia and their Many Applications"]
$ Flag_IllustratedBotanical = "The Illustrated Botanical" in book_collected
$ Flag_WoodwitchGuide = "The Woodwitch Guide to Home Gardening" in book_collected
$ Flag_CarnivorousPlants = "Carnivorous Plants of Viordia and their Many Applications" in book_collected
default Flag_IllustratedBotanical = False
default Flag_WoodwitchGuide = False
default Flag_CarnivorousPlants = False
# Now you can reference book_collected[0] as 'book 1' and book_collected[1] as 'book 2' in dialogue

# Sabotage Variables
$ sabotaged_plant = []
$ sabotaged_options = ["Aria", "Xander", "Tao", "Rex", "Melody"]
$ Flag_AriaPlantSabotaged = "Aria" in sabotaged_plant
$ Flag_XanderPlantSabotaged = "Xander" in sabotaged_plant
$ Flag_TaoPlantSabotaged = "Tao" in sabotaged_plant
$ Flag_RexPlantSabotaged = "Rex" in sabotaged_plant
$ Flag_MelodyPlantSabotaged = "Melody" in sabotaged_plant
######referencing sabotaged plants######


#### CHARACTER SACRIFICED ###
$ sacrificed_character = []
$ sacrificed_options = ["Aria", "Xander", "Tao", "Rex", "Melody"]
$ Flag_Sacrificed_Aria = "Aria" in sacrificed_character
$ Flag_Sacrificed_Xander = "Xander" in sacrificed_character
$ Flag_Sacrificed_Tao = "Tao" in sacrificed_character
$ Flag_Sacrificed_Rex = "Rex" in sacrificed_character
$ Flag_Sacrificed_Melody = "Melody" in sacrificed_character
#############



# Character Flags
define Flag_TaoMet = False
define Flag_MelodyMet = False
define Flag_AriaMet = False
define Flag_RexMet = False
define Flag_XanderMet = False
define Flag_NotAliceMet = False
define Flag_AliceMet = False
define Flag_EileenMet = False


# Smaller Flags
define Flag_MelodyWave = False
define Flag_PlayerMoonInspect = False
define Flag_LightSpellNotLearned = False
define Flag_MelodySabotage = False
define Flag_Morning1Xander = False #morning1 the player spoke to xander
define Flag_Morning1Aria = False #morning1 the player spoke to aria
define Flag_Morning1Tao = False #morning1 the player spoke to tao
define Flag_XanderFarmer = False #player has found out that xander's family are farmers
define Flag_MageAuthority = False
define Flag_PlayerSeedsInspected = False #player has inspected the seeds in the greenhouse.
define Flag_AdventureGuild = False
define Flag_C3TaoFather = False
define Flag_TaoXanderFriendship = False
define Flag_RexArtificing = False
define Flag_DemoAliceJob = False
define Flag_MelodyCaughtPlayerStealing = False #Melody caught the player unlocking the potion cabinet.
define Flag_EileenLibraryDay2 = False # eileen is in the library on night 1
define Flag_RexSneakDay1 = False #Rex has snuck out on Night 1
define Flag_AriaWantsBook = False #Aria is bored and wants something to read in the dorms.

define Flag_TaoDormitoryChat2 = False 
define Flag_AriaDormitoryChat2 = False
define Flag_XanderDormitoryChat2 = False 
define Flag_RexDormitoryChat2 = False
define Flag_MelodyDormitoryChat2 = False




define Flag_AriaAliceOpinion = False #player has asked aria's opinion on alice.
define Flag_AriaEileenOpinion = False #player has asked aria's opinion on eileen
define Flag_XanderEileenOpinion = False #player has asked Xander's opinion on eileen.
define Flag_XanderAliceOpinion = False #player has asked Xander's opinion on alice.
define Flag_TaoEileenOpinion = False
define Flag_TaoAliceOpinion = False
define Flag_HREX12 = False #player has gone through HREX12


define Flag_ArchivesDiscovered = False # player has discovered the archives.
define Flag_ArchivesArtifice = False #player has discovered that the lock on the archives is artifice.
define Flag_ArchivesUnlocked = False #player has unlocked the archives.
define Flag_ArchivesArtifice_Xander = False #player has talked to Rex and found out that Xander might be able to break the Archive lock.

define Flag_EntranceDoor1 = False #hints that the door has more to it and can be unlocked via some artifact.
define Flag_TaoDormitoryDay2 = False #The player talks to Tao morning 2


define AriaBookAcquired = False #the player grabbed a book for Aria on day1. 

define Flag_XanderWatched = False #Xander told the player that something knocked on his window in the night.
define Flag_TheWatcher = False #The player has seen something at the edge of the forest, stalking them.


# Important Visited Flags
define AtriumVisitedDay1 = False
define Flag_Day2PlantsWatered = False #did the player tend to their plants on day2?
define Flag_Afternoon2Tao = False #Player has spoken to Tao on Afternoon Day 2
define Afternoon2CourtyardVisited = False #player heard the conversation between Aria and Alice.
define Afternoon2ArtificingLabVisited = False # player hasn't visited the Artificing Lab on Afternoon2
define Afternoon2Aria = False #the player spoke to Aria on Day2 in the Courtyard
define Night2AtriumVisited = False #the player visited the atrium and saw the porcelain fragments.
define Night2Explored = False #the player has got to the courtyard on night 2. Meaning if they leave, the demo ends.

# Teachers Lounge Discovery
define Flag_TeachersLoungeQuestioned = False # the player has questioned where Eileen and Alice stay.
define Flag_DiscoveredTeachersLounge = False #You have been told about the Teachers lounge.
define TeachersLounge = False #you have discovered the teachers lounge. a new room to access in the next episodes.
##### I had an idea that the way Eileen gets into the Archives is through the Teacher's lounge. It's not explained to the player but they can test it out.


### Archive Opened ###
define ArchiveOpened = False # the archive is opened -- a new location for future episodes.
####

define Flag_LockBreakerNeeded = False #player is alerted that they need a lockbreaker to break the lock.
define Flag_PotionNotStolen = False #player has decided not to steal something.
define Flag_LockBreakerUsed = False #Player has used the lockbreaker, leading to them potentially being caught.
define Flag_GreenhouseTunnel = False #Player has found out that there's a tunnel covered by roots that leads outside.
define Flag_GreenhouseTunnelUnlocked = False #The tunnel is unlocked and can be used via the Greenhouse starting at Night 2.
define Flag_XanderPoisoned = False # You've found out that Xander's plants were poisoned.
define Flag_ForestDiscovered = False #The player can access the forest on night2.

# Spells
define Spell_Light = False
define Spell_Unlocking = False
define Spell_Telekinesis = False



############################# EXAM RECIPES ##################
# Created Potion Recipes Variables
$ potion_recipe = []
$ potionrecipe_options = ["Potion of Calming", "Potion of Hydration", "Potion of Frog Polymorph"]
$ Flag_CalmingPotion = "Potion of Calming" in potion_recipe
$ Flag_HydrationPotion = "Potion of Hydration" in potion_recipe
$ Flag_FrogPotion = "Potion of Frog Polymorph" in potion_recipe
$ Flag_MelodySabotagedPotion = "Potion of Night Vision" in potion_recipe


# Stolen Potion Variables
$ potion_stolen = []
$ stolenpotion_options = ["Potion of Cleansing", "Potion of Frog Polymorph", "Potion of Sleepless Night"]
$ Flag_CleansingPotion = "Potion of Cleansing" in potion_stolen
$ Flag_FrogPolymorphPotion = "Potion of Frog Polymorph" in potion_stolen
$ Flag_SleeplessNightPotion = "Potion of Sleepless Night" in potion_stolen
# Now you can reference potion_stolen[0] as 'potion 1' and potion_stolen[1] as 'potion 2' in dialogue


# Created Artifice Recipe Variables
$ artifice_options = []
$ artificecreated_options = ["Light Machine", "Delivery Bird"]
$ Flag_ArtificeLightMachine = "Light Machine" in artifice_options
$ Flag_ArtificeDeliveryBird = "Delivery Bird" in artifice_options
## Recipe Parts that increase grade ##
define Flag_ArtificeParts = False

################################################################

### Flower Quality ###
define Quality_Flower = 50




#Quest Flags
define Quest_XanderProgress = False
define Quest_XanderComplete = False
define Quest_XanderFailed = False

define Quest_AriaProgress = False
define Quest_AriaComplete = False
define Quest_AriaFailed = False

define Quest_TaoProgress = False
define Quest_TaoComplete = False
define Quest_TaoFailed = False

define Quest_RexProgress = False
define Quest_RexComplete = False
define Quest_RexFailed = False
define Quest_RexPlanStopped = False
define Quest_RexPlanRejected = False

define Quest_MelodyProgress = False
define Quest_MelodyComplete = False
define Quest_MelodyFailed = False

define Quest_NotAliceProgress = False
define Quest_NotAliceComplete = False
define Quest_NotAliceFailed = False


#Exam Flags
define Flag_CombatExamCompleted = False
define Flag_MelodySabotagedPotion = False### Potion of Night Vision
define Flag_PotionSubmitted = False
define Flag_PotionExamCompleted = False
define Flag_ArtificingExamCompleted = False



# Character Affinity between 0 - 50
define Affinity_Tao = 0
define Affinity_Aria = 0
define Affinity_Melody = 0
define Affinity_Xander = 0
define Affinity_Alice = 10
define Affinity_Eileen = 0
define Affinity_Rex = 0

# Character Romance
define RomanceTao = False
define RomanceAria = False
define RomanceMelody = False
define RomanceXander = False
define RomanceRex = False

# Days
define Day0Afternoon = False
define Day0Night = False

define Day1Morning = False
define Day1Afternoon = False
define Day1Night = False

define Day2Morning = False
define Day2Afternoon = False
define Day2Night = False

define Day3Morning = False
define Day3Afternoon = False
define Day3Night = False

define Day4Morning = False
define Day4Afternoon = False
define Day4Night = False

define Day5Morning = False
define Day5Afternoon = False
define Day5Night = False

define Day6Morning = False
define Day6Afternoon = False
define Day6Night = False

define Day7Morning = False
define Day7Afternoon = False
define Day7Night = False


transform half_size:
    zoom 0.5 #adjust as required

transform quarter_size:
    zoom 0.25 #adjust quarter size

# syntax for music
# play music "filename" ## plays music
# stop music ## stops anything that's playing on the music channel
# play sound "filename"
# stop sound "filename" #most of the specific sound channel plays once and stops.

# The game starts here.


#####################
# Game Introduction #
#####################
label start:
    ###################################
    ## Do not remove this portion
    show border onlayer UI 
    ###################################    
    scene bg room with fade
    $ Day0Afternoon = True
    $ cinematic = True
    $ Location = "Courtyard"
    ### here should be an image of the players letter that invited them to the Scholomance ###
    show acceptance letter at half_size
    Narrator "You stuff the letter in your bag as the carriage comes to a stop."
    hide acceptance letter
    Narrator "Bells chime behind you as you step onto the stone path and look up at the great structure before you." 
    Narrator "It's nothing like the Scholomance, it's quainter. A great tower atop an impossibly steep mountain, overlooking nothing but forests and rivers."
    Narrator "Far in the distance, over the horizon, you imagine your old home. It warms you." 
    Narrator "Looking around, the other carriages seem empty. Like usual, you're the last to arrive." 
    Narrator "An older woman waits at the entrance: {b}Alice{/b}. You'd taken a few of her classes at the Scholomance." 
    Narrator "As you move closer, you become aware that it's not quite Alice -- it's one of her dolls."
    Narrator "You wipe the rain from your eyes. The doll turns her gaze to you."
    $ cinematic = False
    #removed at half size below
    show alice sprite with dissolve:
        xalign 0.5
        yalign 0.3
    $ Flag_AliceMet = True
    $ journal__bio_alice.isUnlocked = Flag_AliceMet
    Alice "You took your time. I was getting close to sending out a search party."
    Alice "The ceremony hasn't begun yet. Your fellow classmates are in the atrium. Leave your luggage, I'll get someone to take them to your dorm."
    Alice "Go on in. I must lock the doors behind you. Find your classmates."
    hide alice sprite
    play music "audio/project_w_class.mp3"
    $ Location = "Courtyard"
    scene atrium with fade
    $ cinematic = True
    Narrator "The doors open as you approach. You enter the atrium."
    play sound "audio/moon_sparkle.mp3"
    Narrator "What first catches your eye is two floating moons. More specifically, moon replicas. The Matron and Son, one large, battered and carved, and orbited by a smaller, more pristine one."
    Narrator "They hover in the air, bobbing as they rotate, shining dull light across the room."
    stop sound
    Narrator "As you look around, you notice the statues built into alcoves in the wall, tall and protective, each has an altar at the base."
    Narrator "The Saints, you assume for a moment... until you see that one is still in construction."
    Narrator "It looks like Eileen."
    Narrator "You hear water, but can't quite find it, so instead you allow your eyes to follow the pillars supporting a glass ceiling. Moonlight shines down on you..."
    Narrator "and your classmates."
    show melody sprite at left with dissolve
    Narrator "A familiar woman waves at you, inviting you to join the line of other examinees."
    $ cinematic = False
    menu:
        "(Join Her)":
            $ Flag_MelodyWave = True
            hide melody sprite
            pass
        "(Join the Group)":
            hide melody sprite
            pass
    
    $ cinematic = True
    Narrator "As the chatter of the students dies down, you hear the sharp clink of footsteps against the marble floor."
    Narrator "As you look at the moons once more, you see a woman pass below them, standing on the platform before the students. You recognise her instantly: Inquisitor Eileen."
    show eileen sprite at right
    $ Flag_EileenMet = True
    $ journal__bio_eileen.isUnlocked = Flag_EileenMet
    Narrator "Rather than stand still, she turns, as if summoning the woman behind her. Inquisitor Alice, the woman who crafted the dolls. This isn't the first time you've seen her in person, but it still strikes you as odd."
    #add x and y positioning to adjust sprite alignment
    show alice sprite:
        xalign 0.5 
        yalign 0.3
    Narrator "The woman lives through a half-dozen dolls, it's very odd to see her in person. You notice another doll beside the staircase leading to a great green window."
    $ cinematic = False
    Alice "Good evening, pupils. I know the journey here wasn't smooth, but you all seem to have made it from the Scholomance in one piece."
    Alice "I'm Inquisitor Alice, and beside me is Inquisitor Eileen. We've come to the Summit to fulfil our duties as examiners. We authorise your exams and will determine whether you pass..."
    $ cinematic = True
    play sound "audio/main_hall_gentle_water.mp3"
    Narrator "She looks over the room. You hear droplets fall."
    stop sound
    $ cinematic = False
    Alice "Or if you fail."
    Alice "The six of you have been carefully selected by the Council and deemed worthy, trained, and old enough to attempt your Mage Licence Exam."
    Alice "Upon receiving this title you will be not only authorised, but also assisted in departing the Scholomance and joining society as a Town Mage." 
    Alice "Some of you have honed your Magecraft for over a decade for this moment. So I implore you to take the opportunity seriously."
    Alice "Failure will result in your dismissal back to the Scholomance for further training."
    $ cinematic = True
    show rex sprite angry at left with moveinleft
    Narrator "You hear a grunt. Turning, you notice a man scowl, his arms crossed tight as he stares up at Eileen."
    $ cinematic = False
    hide rex sprite angry
    Alice "I'm sure you all know what is on the line."
    Alice "Your future as a Mage depends on your performance here. Beginning tomorrow, over the next seven days you will be going through various exams."
    Alice "Potions..."
    Alice "Artificing..."
    Alice "And importantly, combat..."
    Alice "Do your best."
    Alice "Eileen, would you like to say a few words."
    hide alice sprite
    hide eileen sprite
    $ cinematic = True
    show eileen sprite #annoyed
    Narrator "Eileen raises an eyebrow, she seems uninterested, if a little annoyed."
    Narrator "She clears her throat."
    $ cinematic = False
    Eileen "It could be {i}years{/i} before you have another chance to leave the Scholomance. If you botch it, I assure you, you {i}will{/i} regret it."
    Eileen "Your peers will pity you and use your story to fuel their aspirations."
    Eileen "Your life will remain in stagnation. Studying and learning under lecturers who care little for you, with ambitions to leave a place you barely grew beyond."
    Eileen "Consider this your only chance at life."
    hide eileen sprite
    $ cinematic = True
    Narrator "You notice Alice's smile fade as she bites the inside of her cheek."
    $ cinematic = False
    show alice sprite with moveinright:
        xalign 0.5 
        yalign 0.3
    Alice "Great... Great. Thank you for your advice, Inquisitor Eileen."
    Alice "As for my own advice... Every licensed Mage has been through the Summit. It's the final test we undertake as student mages." 
    Alice "I have unwavering trust that you each have it in you to succeed."
    Alice "You're only here for {i}seven days{/i}, pupils. Make those days count."
    Alice "And remember to ask yourself. What is it you desire from this place? Let that motivate you."
    $ cinematic = True
    Narrator "You wonder whether she'd prepared that speech. Her demeanor seemed to shift almost as a counterpoint to Inquisitor Eileen."
    Narrator "Alice clears her throat once more, clasping her hands together to wait for the room to settle. Inquisitor Eileen glares at the white-haired student to your right. The room quiets."
    $ cinematic = False
    Alice "As it is your first night here, I'll allow you all to settle a bit." 
    Alice "However... curfew is 9pm. You should be in your dorms by then. Whether you study the night away or sleep the moment your pretty little heads touch your bed does not matter to me."
    Alice "But I implore you to please, remain in your dorms. The Summit is an ancient place, filled with ancient spells that we have little control over."
    Alice "If you're out past curfew and something awful happens to you..."
    show eileen sprite at right with moveinleft
    Eileen "I will write your parents and tell them you died being an imbecile."
    Eileen "Stay in your dorms. Understood?"
    $ cinematic = True
    Narrator "Eileen looks around the room."
    $ cinematic = False
    Eileen "Good."
    hide eileen sprite with moveoutright
    Alice "We'll be in the teachers lounge." 
    hide alice sprite with moveoutright
    $ cinematic = True
    Narrator "The two of them step away, climbing the staircase only to disappear through a heavy oaken door."
    Narrator "Still damp from the rain, you look around you at the students you only vaguely know."
    show tao sprite
    Narrator "A mage with black hair stares up at the moons... seemingly in a trance."
    hide tao sprite
    show aria sprite worried
    Narrator "A woman in a pink, almost frilly, uniform looks down at her feet."
    hide aria sprite worried
    show rex sprite
    Narrator "The man with tattoos is the one you noticed earlier. He still seems annoyed."
    hide rex sprite
    show xander sprite
    Narrator "A short man with messy, white hair looks around the atrium with an aloof look in his eye..."
    hide xander sprite
    show melody sprite 
    Narrator "Lastly you see the raven-haired woman who waved you over earlier..."
    hide melody sprite
    Narrator "They're acquaintances..." 
    Narrator "You shouldn't be surprised... the Scholomance holds every training mage. None of your friends were chosen alongside you to take the exam. Part of you feels alone."
    $ cinematic = False
    if Flag_MelodyWave == True:
        call BMEL01 from _call_BMEL01 #melody introduction
    else:
        "You wonder whether you should break the ice."
        jump introduction_menu

    label introduction_menu:
        $ cinematic = True
        Narrator "What should you do?"
        $ cinematic = False
        
        menu:
            "(Talk to the raven-haired woman.)" if Flag_MelodyMet == False:
                call BMEL01 from _call_BMEL01_1
                jump introduction_menu

            "(Talk to the Mage staring up at the moons.)" if Flag_TaoMet == False:
                call BTAO01 from _call_BTAO01
                jump introduction_menu

            "(Talk to the woman in the pink uniform.)" if Flag_AriaMet == False:
                call BARI01 from _call_BARI01
                jump introduction_menu

            "(Talk to the man with tattoos.)" if Flag_RexMet == False:
                call BREX01 from _call_BREX01
                jump introduction_menu

            "(Talk to the man with white hair.)" if Flag_XanderMet == False:
                call BXAN01 from _call_BXAN01
                jump introduction_menu

            "(Go to bed.)" if Flag_AriaMet and Flag_MelodyMet and Flag_RexMet and Flag_TaoMet and Flag_XanderMet:
                $ cinematic = True
                Narrator "You make your way to bed."
                $ cinematic = False
                $ Day0Afternoon = False
                stop music fadeout 3.0
                jump Night0Dorms


#####################
#  Night 0 Dorms    #
#####################
label Night0Dorms:
    ###################################
    ## Do not remove this portion
    show border onlayer UI
    ###################################
    scene dormitory night with fade
    play music "audio/project_w_dorms.mp3" fadein 1.0
    $ Day0Night = True
    $ cinematic = True
    $ Location = "Dormitory"
    Narrator "The dormitory isn't what you expected. Rather than the individual rooms you had back at the Scholomance, stuffy and cramped, there is an exposed dormitory." 
    Narrator "A floor separated into enclosed bed-spaces and study areas -- visible to one another from certain angles."
    Narrator "At least the beds look comfortable. You notice your luggage at the foot of a sprawling, purple, curtained bed. Looking up you notice the sky is still visible, though it doesn't seem to be through glass."
    Narrator "It's a spell. You feel it as you analyse it. Swirling patterns, images, all moving to form the illusion of a night sky. Looking at it makes you tired."
    Narrator "A few other students are already unpacking as you get to your bed. You notice Melody, sleepmask on as she sits in bed. You can't tell if she's sleeping."
    $ cinematic = False
    
    label Night0DormsMenu:
        menu:
            "(Talk to Melody.)" if Flag_MelodyMet == True:
                #Melody Dormitory Night 0
                    label BMEL05:
                    show melody sprite
                    Melody "Oh, you're still up. I'm usually in bed pretty early, but I spend a lot of time reading under the covers." 
                    Melody "Not saying you have to be quiet if you're walking around, I sleep like the dead. Honestly, learning that light spell back at the Scholomance made my life a million times easier."
                    menu:
                        "Light spell?":
                            pass
                    show melody sprite excited
                    Melody "Yeah... wait, do you not know it? Maybe you missed that class, I should have it somewhere in my bag."
                    $ cinematic = True
                    Narrator "Melody rummages through a pristine purple bag. You're surprised it survived the years in the Scholomance."
                    Narrator "After a few moments, she gives up."
                    $ cinematic = False
                    Melody "I know it's in here somewhere..."
                    Melody "I'll find it tomorrow morning..."
                    $ Flag_LightSpellNotLearned = True
                    Melody "If you want it, let me know."
                    menu:
                        "Thanks.":
                            pass
                    hide melody sprite excited
                    Melody "No worries. Is there something you wanted to talk about? You know, since you're here and all?"
                    menu:
                        "(Continue) There is...":
                            call melodyhub_main from _call_melodyhub_main
                            jump Night0DormsMenu

                        "(End Conversation) Not really...":
                            $ cinematic = True
                            show melody sprite happy
                            Narrator "Melody smiles warmly. You can tell that she isn't all that tired."
                            hide melody sprite happy
                            $ cinematic = False
                            jump Night0DormsMenu
                    return

            "Talk to raven-haired woman." if Flag_MelodyMet == False:
                call BMEL01 from _call_BMEL01_2 ###Takes you back to her intro scene. In case someone hasn't done it.
                jump Night0DormsMenu

            "(Talk to Xander.)" if Flag_XanderMet == True:
                call BXAN12 from _call_BXAN12 ###Xander node in Arcweave
                jump Night0DormsMenu

            "(Talk to the man with white hair.)" if Flag_XanderMet == False:
                call BXAN01 from _call_BXAN01_1
                jump Night0DormsMenu

            "(Talk to Rex.)" if Flag_RexMet == True:
                call BREX22 from _call_BREX22
                jump Night0DormsMenu

            "(Talk to the man with tattoos.)" if Flag_RexMet == False:
                call BREX01 from _call_BREX01_1
                jump Night0DormsMenu

            "(Talk to Aria.)" if Flag_AriaMet == True:
                call BARI28 from _call_BARI28
                jump Night0DormsMenu

            "(Talk to the woman in the pink uniform.)" if Flag_AriaMet == False:
                call BARI01 from _call_BARI01_1
                jump Night0DormsMenu

            "(Talk to Tao.)" if Flag_TaoMet == True:
                call BTAO20 from _call_BTAO20
                jump Night0DormsMenu

            "(Talk to the deadpan mage.)" if Flag_TaoMet == False:
                call BTAO01 from _call_BTAO01_1
                jump Night0DormsMenu

            "(Go to Sleep)":
                $ cinematic = True
                Narrator "You get into the bed. The fresh-linen scent hits you as you sink deeper in. Above you, the illusory stars twinkle and move ever so slightly toward a fake horizon. The world around you seems to fade..."
                $ cinematic = False
                $ Day0Night = False
                stop music fadeout 1.0
                scene fadeout 1.0
                jump Morning1Dorms

            "(Explore the Summit)":
                $ cinematic = True
                Narrator "Sneaking out on the first night... even your gut tells you that's not wise."
                Narrator "You stand up. The other students turn their gaze away from you. Perhaps they don't want to be witnesses."
                Narrator "You step along the floor, your shoes quiet against the polished marble. When you reach the door you hear nothing but silence."
                Narrator "Your hand twists the handle. Are you sure you want to proceed?"
                $ cinematic = False
                menu:
                    "(Explore the Summit)":
                        $ cinematic = True
                        Narrator "You turn the handle. It's unlocked."
                        Narrator "You exit the dormitory."
                        $ cinematic = False
                        jump Night0Corridor

                    "(Go back to bed)":
                        $ cinematic = True
                        Narrator "You turn back. It's probably wise to sleep."
                        $ cinematic = False
                        $ Day0Night = False
                        stop music fadeout 1.0
                        scene fadeout 1.0
                        jump Morning1Dorms

        return
    return



label Night0Corridor:
    ###################################
    ## Do not remove this portion
    show border onlayer UI
    #########################
    scene corridor night with fade
    play music "audio/project_w_main_theme_concept_02_fade.mp3"
    $ Location = "Corridor"
    $ cinematic = True
    Narrator "The dull midnight moonlight casts through the windows and along the marble at your feet. You notice that the windowed cloisters overlooking the courtyard are now clear."
    Narrator "Allowing you to view the Great Mage tree in it's centre. You've read about the tree before. Some say it's enchanted, others say it's much older than Mages."
    Narrator "Whatever the answer, it's not something you want to question."
    Narrator "You press along the corridor, ignoring the feeling of eyes on your back."
    $ cinematic = False
    label Night0CorridorChoices:
        $ cinematic = True
        Narrator "Where are you going?"
        $ cinematic = False
        menu: 
            "Back to the {b}Atrium{/b}" if Location != "Atrium":
                stop music
                call Night0Atrium from _call_Night0Atrium
                return

            "To the {b}Library{/b}" if Location != "Library":
                stop music
                call Night0Library from _call_Night0Library
                return

            "To the {b}Greenhouse{/b}." if Location != "Greenhouse":
                call Night0Greenhouse from _call_Night0Greenhouse
                return

            "Back to the {b}Dormitory{/b}." if Location != "Dormitory":
                stop music
                $ cinematic = True
                scene dormitory night
                Narrator "You return to the dormitory and get into the bed. The fresh-linen scent hits you as you sink deeper in. Above you, the illusory stars twinkle and move ever so slightly toward a fake horizon. The world around you seems to fade..."
                $ cinematic = False
                $ Day0Night = False
                jump Morning1Dorms




    label Night0Atrium:
        scene atrium night with fade
        play music "audio/Oratory_MASTER_LOOPED.mp3"
        $ Location = "Atrium"
        $ cinematic = True
        Narrator "The Atrium is still magnificent. You see moonlight flicker through the stain glass window..."
        Narrator "But you also notice that the spell conjuring the two, twin moons, is in effect, casting faux-moonlight along the floor."
        Narrator "It's quiet. Quieter than you remember."
        Narrator "It takes you a moment to place the difference... the water, there's no longer the sound of running water."
        Narrator "All you hear is your footsteps, and the distant wind as it caresses the entrance."
        Narrator "Part of you wonders whether you could simply escape. Run off to a distant land."
        Narrator "Whether you could run into the woods and never think of the Summit, or the Scholomance again."
        Narrator "Or whether you'd simply die trying to descend."
        Narrator "Then you hear something break the silence."
        play sound "audio/main_hall_gentle_water.mp3"
        Narrator "A splash. The pitter-patter of feet against water. Sloshing like emerging from a bathtub."
        $ cinematic = False
        menu:
            "(Hide)":
                $ cinematic = True
                Narrator "You follow the noise, hiding behind a pillar. You still your breath."
                $ cinematic = False
                pass
            "(Stand your ground)":
                $ cinematic = True
                Narrator "You stay stood out in the open. You expect Eileen or Alice to emerge." 
                Narrator "To toss you back to the Scholomance like a discarded ragdoll."
                $ cinematic = False
                pass
        $ cinematic = True
        Narrator "Your heart races. You try and find the source of the noise. Looking over at the large, green, window -- expecting at any moment see Eileen."
        Narrator "{i}{b}slosh, slosh, slosh.{/b}{/i}"
        play sound "audio/moon_sparkle.mp3"
        Narrator "The noise moves to the moons. More specifically, to the grate below them. You listen as something pushes the grate up, and with effort, tries to push through."
        $ cinematic = False
        menu: 
            "(Investigate)":
                $ cinematic = True
                Narrator "You creep closer, noticing a white hand twist upward. Whatever is down there isn't small enough to squeeze through."
                Narrator "You move closer. Crouching below the moons, gingerly shuffling until you can see something below."
                Narrator "Staring up at you, is a silhouette. You can't make out features in the darkness, but you can hear it move in the shallow water."
                $ cinematic = False
                menu:
                    "Hello?":
                        $ cinematic = True
                        Narrator "You call out into the darkness, your voice barely above a whisper."
                        Narrator "The silhouette stirs. You feel its eyes meet yours, you feel like prey."
                        Narrator "After a moment, as the moonlight twists and turns as the moons rotate, a shaft pushes into the darkness."
                        show notalice sprite
                        Narrator "Revealing another Doll. Alice. Trapped below the sewer grates."
                        $ cinematic = False
                        menu:
                            "Alice?":
                                NotAlice "Good evening, pupils."
                                NotAlice "I'm Inquisitor Alice."
                                $ Flag_NotAliceMet = True
                                menu: 
                                    "Are you alright?":
                                        NotAlice "Great... Great."
                                        NotAlice "The ceremony hasn't begun yet."
                                        menu: 
                                            "We had the ceremony earlier.":
                                                $ cinematic = True
                                                Narrator "The doll talks in an awkward cadence. It's almost detached as it looks up at you."
                                                Narrator "The doll reaches up once more."
                                                $ cinematic = False
                                                NotAlice "We had the ceremony earlier."
                                                NotAlice "What is it you desire..."
                                                $ cinematic = True
                                                Narrator "You become aware that the doll is asking something of you."
                                                Narrator "The intensity of its gaze only strengthens as its eyes fixate on you."
                                                $ cinematic = False
                                                NotAlice "What is it you desire..."
                                                NotAlice "... from this place?"
                                                menu:
                                                    "I want to pass.":
                                                        $ Quest_NotAliceProgress = True
                                                        pass

                                                    "I want to escape.":
                                                        $ Quest_NotAliceProgress = True
                                                        pass

                                                    "I want nothing.":
                                                        pass
                                                NotAlice "Find... Inquisitor Alice... past curfew... I implore you... ancient place..."
                                                $ cinematic = True
                                                Narrator "The hand points behind you. To the entry way you first arrived through. The Summit's entrance."
                                                $ cinematic = False
                                                NotAlice "I must lock the doors behind you."
                                                NotAlice "Find... Inquisitor Alice"
                                                $ cinematic = True
                                                hide notalice sprite with dissolve
                                                Narrator "The doll dips down into the shadows once more -- arm retracting back as though an invisible puppetmaster yanked its string."
                                                Narrator "You hear the sound of the water return once more."
                                                Narrator "You stand, heart pounding in your chest."
                                                Narrator "It's late. You know it's time to go to sleep."
                                                scene dormitory night with fade
                                                Narrator "You return to the dormitory and get into the bed." 
                                                Narrator "The fresh-linen scent hits you as you sink deeper in. Above you, the illusory stars twinkle and ebb ever so slowly toward a fake horizon. The world around you seems to fade..."
                                                Narrator "But you can't help but wonder..." 
                                                Narrator "...what was that?"
                                                Narrator "And why do you still feel its gaze?"
                                                $ cinematic = False
                                                $ Day0Night = False
                                                $ AtriumVisitedDay1 = True
                                                stop music
                                                jump Morning1Dorms

                        

                    "(Leave it there)":
                        $ cinematic = True
                        Narrator "Something in you stirs. You know this place isn't for you."
                        Narrator "You turn, walking away from the moons, from the grate, and from whatever calls itself Alice beneath it."
                        Narrator "You turn back for one last glimpse -- its hand upreaching, glowing in the moonlight, as though it's holding the moons in place."
                        Narrator "You leave the Atrium."
                        $ cinematic = False
                        stop music
                        play music "audio/project_w_main_theme_concept_02_fade.mp3"
                        jump Night0CorridorChoices


            "(Run)":
                $ cinematic = True
                Narrator "You turn and run, heart pounding in your chest."
                Narrator "When you make it to the Atrium entrance, you take a look back to see a hand twisting below the moons."
                Narrator "You run."
                Narrator "You leave the Atrium."
                $ cinematic = False
                stop music
                play music "audio/project_w_main_theme_concept_02_fade.mp3"
                jump Night0CorridorChoices





    label Night0Library:
        scene library night
        play music "audio/project_w_concept_04_fminor.mp3"
        $ Location = "Library"
        $ cinematic = True
        Narrator "The library door is heavy as you push it open. Inside is complete darkness."
        $ cinematic = False
        if Spell_Light == True:
            $ cinematic = True
            Narrator "You summon a light to your hands, Melody's spell resonating. You're surprised how simple it is."
            $ cinematic = False
            pass
        else:
            $ cinematic = True
            Narrator "It's too dark to see anything. Without a light, you cannot enter."
            $ cinematic = False
            stop music
            jump Night0CorridorChoices
        $ cinematic = True
        Narrator "The spell casts eerie light over the library. The silence seems uncanny as you step inside -- looking over the stacks of thick books and tomes."
        Narrator "Shadows dance along the walls -- remnants clouds through the skylight."
        Narrator "Despite the prickly feeling on your neck, you know you're alone."
        Narrator "In the distance, you notice a gated door, a great padlock stopping you."
        Narrator "Yet you can't help but approach it. There's an aura to it. You feel as though you're moving towards honey-scented wood." 
        Narrator "You can feel great magic, as though spectral fingers are luring you closer. Twisting and spiralling."
        Narrator "You breathe it in..."
        Narrator "Whatever is behind the door is old magic."
        Narrator "Those scents, dewdrops on grass, honey warmed up, feel intrinsic to you."
        Narrator "They feel intimate."
        Narrator "More a part of you than your beating heart."
        Narrator "You lift your light higher and look over the old paper label above the door."
        Narrator "{b}The Archives{/b}."
        $ Flag_ArchivesDiscovered = True
        $ cinematic = False
        menu:
            "(Try the door.)":
                $ cinematic = True
                Narrator "The chains are strong. The lock seems unbreakable."
                Narrator "You need a key."
                $ cinematic = False
                pass
            "(Leave.)": 
                $ cinematic = True
                Narrator "You kill the urge to move closer. You don't know where you found the determination."
                Narrator "You know there is nothing for you here."
                Narrator "Nothing yet..."
                $ cinematic = False
                pass
        $ cinematic = True
        Narrator "The moonlight reminds you how late it's getting. You head back to the corridor."
        $ cinematic = False
        stop music
        jump Night0Corridor
        




    label Night0Greenhouse:
        scene corridor night
        $ cinematic = True
        Narrator "As you walk around the corridors, you realise there is no way into the greenhouse."
        Narrator "The tree at its centre has its own energy. The more you look at it, the more you feel watched."
        Narrator "You're certain it's locked in there for the best."
        Narrator "You should go somewhere else."
        $ cinematic = False
        jump Night0Corridor










label Morning1Dorms:
    ###################################
    ## Do not remove this portion
    show border onlayer UI
    #########################
    scene dormitory morning with fade
    play music "audio/project_w_dorms.mp3" fadein 1.0
    $ Day1Morning = True
    $ Location = "Dormitory"
    $ cinematic = True
    Narrator "You notice Alice enter the dormitory before she announces herself. The morning light pours in through the curtained windows..."
    Narrator "It seems no student decided to close them."
    Narrator "You look around, waiting for someone to make a move."
    $ cinematic = False
    show alice sprite happy:
        xalign 0.5 
        yalign 0.3     
    Alice "Good morning, pupils."
    Alice "I hope you're all rested and ready. Today is a busy day."
    Alice "You are going to be planting the materials you'll be using for your potion exam."
    hide alice sprite happy
    show alice sprite with dissolve:
        xalign 0.5 
        yalign 0.3  
    Alice "When you're ready, please make your way to the Greenhouse."
    Alice "Don't dawdle."
    $ cinematic = True
    hide alice sprite
    Narrator "She turns and leaves. You look around, a few opening the curtains around their beds to investigate."
    $ cinematic = False
    show rex sprite
    Rex "What are we, gardeners now?"
    show tao sprite at left with moveinleft
    Tao "Well, if you get placed in a small town, you might not have access to rare herbs... so I suppose so."
    show xander sprite at right with moveinright
    Xander "It'll be fine."
    Tao "Are we going to be graded on the planting itself or..."
    hide xander sprite with moveoutright
    show melody sprite at right with moveinright
    Melody "I'd imagine so. Half of the quality of a potion is in its components."
    hide tao sprite with moveoutleft
    Rex "Fuck me, I'm surrounded by--"
    show aria sprite at left with moveinleft
    Aria "Morning everyone... did I hear Alice just now?"
    menu: 
        "We need to head to the Greenhouse to do some planting, apparently.":
            pass
    hide rex sprite with moveoutleft
    show tao sprite with moveoutright
    Tao "It's the first day... if we're planting the herbs now are we expected to make them usable within seven days? What day is the potion exam?"
    Melody "We're {i}Mages{/i}, I'm sure we'll figure out a way."
    hide tao sprite with moveoutright
    show xander sprite at right with moveinright
    Xander "Maybe Aria knows a few spells... you kept flowers in the Scholomance, didn't you?"
    Aria "Just the dangly ones. They're easy to keep."
    $ cinematic = True
    Narrator "You watch Tao's face tighten as Aria shrugs."
    hide xander sprite with moveoutright
    Narrator "The Scholomance is beneath the Great Lake. There's no sunlight. The temperature and light is controlled by complex spells..."
    Narrator "You wonder whether Aria took that into account when she kept her flowers, or whether she never needed to."
    $ cinematic = False
    show rex sprite with moveinleft
    Rex "Screw it."
    $ cinematic = True 
    Narrator "Rex stands up, pulling on his vest. You notice the tattoos that creep up his neck -- hellflame."
    Narrator "They look like burns, but the ink outlining it is thick enough to reassure you it isn't."
    Narrator "Without saying a word, he leaves the Dormitory."
    hide rex sprite with moveoutleft
    $ cinematic = False
    Melody "I believe that's the first time he's ever been early to anything. That can't be a good sign."
    Aria "He probably just wants to stand out in the sunlight."
    Aria "It's nice, isn't it? After all these years."
    hide aria sprite
    show xander sprite at left with moveinleft
    Xander "I didn't even know I missed it."
    Melody "I guess..."

    menu:
        "You guess?":
            hide xander sprite
            show melody sprite at center
            Melody "I didn't notice it. I suppose it won't feel real until I {i}know{/i} we're not going back to the Scholomance."
            Tao "There's not much of a chance of {i}us{/i} going back."
            Melody "You never know, Tao."
            jump Day1DormsChat1
        "Xander, you don't seem that fazed by planting.":
            hide aria sprite
            show xander sprite at center
            Xander "I grew up on a farm."
            menu: 
                "Ah.":
                    jump Day1DormsChat1
        "I saw something in the Atrium last night..." if Quest_NotAliceProgress:
            hide xander sprite
            show melody sprite at center
            Melody "What did you see?"
            menu:
                "Something below the moons. Under the grate.":
                    "It looked like Alice's doll."
                    Melody "Maybe one of them got trapped under there..."
                    Melody "Are they autonomous?"
                    show tao sprite at left with moveinleft
                    Tao "I doubt it."
                    hide tao sprite with moveoutleft
                    show aria sprite at right with moveinright
                    Aria "Maybe talk to Alice about it."
                    show xander sprite at left with moveinleft
                    Xander "Don't do that. Being out past curfew will get you shipped back to the Scholomance."
                    Aria "Ah... right."
                    hide aria sprite with moveoutright
                    Melody "It's probably nothing."
                    show tao sprite at right with dissolve
                    Tao "It could be something established to scare us if we're unaccounted for past curfew."
                    Tao "Alice's dolls have eyes everywhere."
                    Xander "Seems cruel..."
                    Xander "Then again... they {i}are{/i} cruel."
                    menu:
                        "...":
                            jump Day1DormsChat1
    label Day1DormsChat1:
        $ cinematic = True
        hide melody sprite with dissolve
        hide aria sprite with dissolve
        hide xander sprite with dissolve
        hide tao sprite with dissolve
        Narrator "The group seems to quiet at that. Melody is the second to leave. You wonder whether you should follow. Time seems to be running out."
        pass
        $ cinematic = False
        menu:
            "(Go to the {b}Greenhouse{/b})":
                stop music
                jump Morning1Greenhouse
            
            "(Speak to Xander)" if not Flag_Morning1Xander:
                call Morning1DormsXander from _call_Morning1DormsXander
                jump Day1DormsChat1

            "(Speak to Aria)" if not Flag_Morning1Aria:
                call Morning1DormsAria from _call_Morning1DormsAria
                jump Day1DormsChat1

            "(Speak to Tao)" if not Flag_Morning1Tao:
                call Morning1DormsTao from _call_Morning1DormsTao
                jump Day1DormsChat1


                label Morning1DormsXander:
                    show xander sprite at center
                    Xander "Hey... can we do this later? I'm kinda jittery in the morning."
                    Xander "Didn't realise we were gonna be up {i}this{/i} early."
                    Xander "I thought we'd get a day to just... relax. Ya know, before exams."
                    menu:
                        "I don't think this is an exam.":
                            Xander "That's a relief... but it's still gonna contribute to our potion exam so I'm kinda nervous."
                            pass
                    Xander "In fact... I think I'll head out."
                    hide xander sprite with moveoutleft
                    $ Flag_Morning1Xander = True
                    return



                label Morning1DormsAria:
                    show aria sprite at center
                    Aria "How are you feeling about everything?"
                    $ Flag_Morning1Aria = True
                    menu:
                        "Fine, so far.":
                            Aria "Good... good. Wish I could say the same."
                            show aria sprite sad at center
                            Aria "I'm sort of homesick."
                            Aria "As much as I hated the Scholomance... it's weird to have it suddenly change."
                            Aria "The air's different here. Thinner."
                            menu: 
                                "We {i}are{/i} on a mountain.":
                                    Aria "That's probably it."
                                    hide aria sprite sad
                                    pass

                        "Overwhelmed.":
                            Aria "You and me both."
                            pass
                    show aria sprite
                    Aria "I should probably get to the Greenhouse."
                    hide aria sprite with moveoutleft
                    return



                label Morning1DormsTao:
                    show tao sprite at center
                    Tao "Right..."
                    $ Flag_Morning1Tao = True
                    if Flag_PlayerMoonInspect == True:
                        Tao "While I'm sure you have something interesting to say..."
                        Tao "I'm currently engaged."
                        menu:
                            "As in 'to-marry'?":
                                Tao "How do you not fall over more often?"
                                hide tao sprite with moveoutleft
                                return

                            "Right. Got it.":
                                hide tao sprite with moveoutleft
                                return
                            
                    else:
                        Tao "Is this necessary?"
                        Tao "I'd rather not chat right now."
                        menu:
                            "Got it.":
                                hide tao sprite with moveoutleft
                                return



label Morning1Greenhouse:
    ###################################
    ## Do not remove this portion
    show border onlayer UI
    #########################
    scene greenhouse morning with fade
    play music "audio/project_w_concept_03_gmajor.mp3"
    $ Day1Morning = True
    $ Location = "Greenhouse"
    $ cinematic = True
    Narrator "You're the last to arrive at the Greenhouse -- a great garden at the centre of the Summit, surrounded on all four sides by hallways with a domed, glass ceiling on top."
    Narrator "At its centre is the Great Mage Tree, a tree said to be enchanted. Its boughs rattle the glass as it sleeps."
    Narrator "You notice Alice beneath the tree with Aria, the two of them deep in conversation. At the back of the Greenhouse, seemingly bored, is Eileen."
    Narrator "Alice turns to you, counting to see whether all of the students had arrived."
    if Flag_NotAliceMet == True:
        Narrator "In the light of day, you wonder whether the thing you saw in the sewer last night was real."
        Narrator "Or whether it was just a dream."
        pass
    else:
        pass
    Narrator "She clears her throat."
    $ cinematic = False
    show alice sprite with moveinleft:
        xalign 0.5 
        yalign 0.3  
    Alice "I won't keep you long. I'm sure you have plenty of studying to do."
    Alice "I've taken the liberty of bringing you all a selection of seeds to plant."
    Alice "You will be using these crops for your potion exam, so please, take good care of them."
    hide alice sprite
    $ cinematic = True
    Narrator "You move over to a table where a few small sacks of seeds sit."
    ### if we ever have an image it would go here
    $ cinematic = False
    menu:
        "(Collect Seeds)":
            play sound "audio/clue_found_item_alert.mp3"
            pass
    $ cinematic = True
    Narrator "You pluck the seeds from the table and feel their weight in your hand."
    Narrator "Very quickly, you become aware that these seeds are magical, not only from the way they feel like electricity on your skin..." 
    Narrator "...but also from the smell of honey that washes over you."
    Narrator "This one is sickly sweet."
    $ cinematic = False
    show alice sprite with dissolve:
        xalign 0.5 
        yalign 0.3  
    Alice "We've given you a small plot to work with. Try not to overcrowd the area."
    Alice "For now, I would simply plant one type of seed at most -- that's my recommendation."
    Alice "We've labeled the seeds -- you should know what sort of care they require."
    Alice "If not... well, consider it part of the test."
    Alice "I've taken the liberty of asking Miss Aria to avoid tending to your flowers. If you allow her to do so, both of you will be given a fail on your Potions exam."
    hide alice sprite
    $ cinematic = True
    show aria sprite with dissolve
    Narrator "You notice Aria looking uncomfortable, her fingers clutching the frills of her dress."
    hide aria sprite
    show melody sprite with dissolve
    Narrator "Melody is already planting, while Xander looks over the seeds he's unbagged, like a child counting pennies."
    hide melody sprite
    show rex sprite with dissolve
    Narrator "Rex seems oblivious to what's going on. Instead, focusing his attention on the ceiling -- as though he could break the sky open with a glare."
    hide rex sprite
    show tao sprite with dissolve
    Narrator "One at a time, Tao lifts the seeds, examining them against the strong morning light."
    hide tao sprite
    show xander sprite with dissolve
    Narrator "Xander bounces the bag of seeds in his hand as if he's attempting to juggle..."
    hide xander sprite
    Narrator "You become aware, as the light hits you, that after this you won't see everyone together in the same room except during exams..."
    Narrator "...and during the night in the dorms."
    Narrator "You wonder what you should do."
    $ cinematic = False
    label GreenhouseMorning1Choices:
        menu:
            "(Inspect the Seeds)":
                call BSID1GH from _call_BSID1GH
                return

            "(Talk to Alice.)":
                call BSID1GH2 from _call_BSID1GH2
                return

            "(Talk to Melody)":
                call BSID1GH3 from _call_BSID1GH3
                return

            "(Talk to Aria)":
                call BSID1GH4 from _call_BSID1GH4
                return

            "(Talk to Rex)":
                call BSID1GH5 from _call_BSID1GH5
                return

            "(Talk to Tao)":
                call BSID1GH6 from _call_BSID1GH6
                return

            "(Talk to Xander)":
                call BSID1GH8 from _call_BSID1GH8
                return

            "(Plant the Seeds)" if Flag_PlayerSeedsInspected:
                call BSID1GH7 from _call_BSID1GH7
                return
            

        label BSID1GH: # Inspecting seeds
            $ cinematic = True
            Narrator "You pour the sack out onto your hand."
            play sound "audio/fertilizer_add.mp3"
            Narrator "You expected them to be labelled, or at least separated."
            Narrator "But it seems that whoever assembled them, mixed them all together in one."
            Narrator "With the seeds comes a rolled-up bit of paper that, as you unfurl it, reveals a few names."
            menu:
                "Inspect the names":
                    play sound "audio/clue_found_item_alert.mp3"
                    Narrator "- {b}Winged Jasmine{/b}: A magical flower you remember from your days at the Scholomance. You can't remember its applications, or which seed it is, but you remember it."
                    play sound "audio/clue_found_item_alert.mp3"                   
                    Narrator "- {b}Snapjaw Orchid{/b}: You don't recognise it."
                    play sound "audio/clue_found_item_alert.mp3"
                    Narrator "- {b}Moon Melon{/b}: You don't recognise it."
                    play sound "audio/clue_found_item_alert.mp3"
                    Narrator "- {b}Sanguine Lily{/b}: You remember that one is incredibly difficult to manage."
                    $ Flag_PlayerSeedsInspected = True
                    pass
            Narrator "Have you always been this ill-prepared? You wonder."
            Narrator "You place the seeds back in the sack."
            $ cinematic = False
            jump GreenhouseMorning1Choices

        label BSID1GH2: # Talk to Alice
            $ cinematic = True
            show alice sprite with dissolve:
                xalign 0.5 
                yalign 0.3  
            Narrator "Alice's mood seems to shift as you approach, a stressed expression melting away."
            Narrator "You wonder whether she's feigning it."
            $ cinematic = False
            Alice "Pupil, what do you need help with?"
            menu:
                "What were you and Aria talking about?":
                    Alice "That's between Aria and I."
                    menu:
                        "She seems upset.":
                            Alice "That's not what I {i}wanted{/i}."
                            $ cinematic = True
                            Narrator "Alice seems genuinely saddened."
                            $ cinematic = False
                            Alice "It's for her own good. Know that."
                            hide alice sprite
                            jump BSID1GH2

                        "Alright...":
                            hide alice sprite
                            jump BSID1GH2
                "I need some help with my seeds.":
                    Alice "I'm not permitted to help you anymore than I already have."
                    Alice "If you're struggling to understand which seed is which and the care they need, perhaps the library should be your next stop."
                    hide alice sprite
                    jump BSID1GH2

                "I saw one of your dolls in the sewers." if Flag_NotAliceMet == True:
                    Alice "In the sewers..."
                    Alice "I doubt that."
                    Alice "None of my dolls leave the grounds. That's too many things to keep track of. Are you sure that you saw one? It just seems... unlikely."
                    menu: 
                        "I'm certain.":
                            Alice "I'll talk to Eileen. I recommend you don't leave the grounds or engage with it."
                            hide alice sprite
                            jump BSID1GH2
                        "Maybe I was mistaken.":
                            Alice "You're under a lot of stress. Take care of yourself, pupil."
                            hide alice sprite
                            jump BSID1GH2
                
                "Nothing. Nevermind.":
                    hide alice sprite
                    jump GreenhouseMorning1Choices



        label BSID1GH3: #Talk to Melody
            show melody sprite with dissolve
            $ cinematic = True
            Narrator "Melody smiles as you approach."
            Narrator "As you reach her, she plants the last of her seeds."
            $ cinematic = False
            Melody "Oh, hi."
            Melody "Do you need something?"
            menu:
                "Help would be nice.":
                    Melody "With planting?"
                    Melody "I {i}would{/i} but I'm pretty sure Alice will get mad at the both of us."
                    Melody "From what I understand, though, try and not plant the one with the obscure sounding name." 
                    Melody "I think that one's carnivorous."
                    show melody sprite laugh
                    Melody "Lest you become it's next meal..."
                    hide melody sprite laugh
                    Melody "I'm sure it makes some great potions, though."
                    $ cinematic = True
                    Narrator "She looks back at the seeds, beginning to place her fingers thoughtfully on each little mound."
                    Narrator "You can't help but wonder if she's casting some sort of spell on them."
                    Narrator "Perhaps you should do something else..."
                    $ cinematic = False
                    menu:
                        "...":
                            hide melody sprite
                            jump GreenhouseMorning1Choices





        label BSID1GH4: # Talk to Aria
            show aria sprite with dissolve
            $ cinematic = True
            Narrator "Aria is kneeling with her seeds as you approach. She barely notices you as you stand beside her."
            $ cinematic = False
            menu: 
                "(Lean down)":
                    $ cinematic = True
                    Narrator "Even when she doesn't know she's being perceived, she still glows."
                    Narrator "As though the magic inside her pricks through her skin. Like a million needles."
                    Narrator "Glowing. Shimmering."
                    pass                             

                "Aria?":
                    Aria "Oh, hello."
                    pass
            $ cinematic = True
            Narrator "Now that you are closer, you notice the intricate patterns forming along Aria's seeds."
            Narrator "It's as though each one is forming its own extra shell. A blanket of magic, weaving itself."
            $ cinematic = False
            menu:
                "How are you doing that?":
                    Aria "I don't know."
                    $ cinematic = True
                    Narrator "You can tell she's telling the truth."
                    $ cinematic = False
                    Aria "Things happen when I get emotional."
                    pass
            menu: 
                "Do you want to talk about it?":
                    Aria "It's just a feeling. It'll pass."
                    Aria "Something about this place... it's beautiful but I can't help but feel..."
                    Aria "Muted. Like someone's sucked the air out from around me."
                    Aria "I know you noticed Alice speaking to me."
                    Aria "It wasn't her. I think she was just checking on me."
                    Aria "Like you are..."
                    menu:
                        "I wouldn't say I'm checking on you.":
                            Aria "Hmm."
                            pass

                        "That's what friends do, right?":
                            Aria "I guess so."
                            Aria "I wouldn't know, to tell the truth."
                            Aria "Other than my dormmate, I don't really get the chance to talk at the Scholomance."
                            $ Affinity_Aria += 10
                            pass
            Aria "Did you want something? I don't want to keep you."
            if Flag_PlayerSeedsInspected:
                menu:
                    "Would you mind explaining the seeds?":
                        Aria "They're just seeds. I don't know how else to explain them."
                        Aria "I know things about them... implicitly."
                        Aria "It isn't something I can teach or show you."
                        Aria "Just know, that seeds are potential. They can become anything."
                        menu:
                            "I don't think that's quite right...":
                                Aria "You'll see. Just plant them."
                                menu:
                                    "...":
                                        hide aria sprite
                                        jump GreenhouseMorning1Choices
                            "Right...":
                                hide aria sprite
                                jump GreenhouseMorning1Choices
            else:
                menu:
                    "Plants...":
                        Aria "Hmm? Isn't the greenhouse amazing? I've never worked in one this big. If you need help just ask me. Growth magic is kind of my specialty..."
                        Eileen "You certainly should {i}not{/i} ask Aria for help. Or anybody else. Aria - you don't condone cheating on exams, do you?"
                        Aria "...Uh... well, of course not. Sorry, I -- I wasn't thinking."
                        hide aria sprite
                        jump GreenhouseMorning1Choices

                    "I guess not.":
                        Aria "I'm here if you need me."
                        hide aria sprite
                        jump GreenhouseMorning1Choices


        label BSID1GH5: # Talk to Rex
            show rex sprite with dissolve
            $ cinematic = True
            Narrator "Rex does not want to talk to you."
            Narrator "You're sure of that as he flicks dirt your way."
            $ cinematic = False
            menu: 
                "Don't be a dick.":
                    Rex "I'm busy. Bozo."
                    menu:
                        "...":
                            hide rex sprite
                            jump GreenhouseMorning1Choices
                        
                
                "...":
                    hide rex sprite
                    jump GreenhouseMorning1Choices


        label BSID1GH6: # Talk to Tao
            show tao sprite with dissolve
            $ cinematic = True
            Narrator "Tao looks over at you as you approach."
            Narrator "For a moment, you wonder if they've had a change of heart."
            $ cinematic = False
            Tao "Do you need something?"
            menu:
                "Can you help me understand these seeds?":
                    Tao "No. I shan't."
                    Tao "It's not my fault you spent your time at the Scholomance in a drunken stupor..."
                    menu:
                        "Me?":
                            pass
                        
                        "So you can't help?":
                            Tao "Not can't. Won't."
                            pass
                    Tao "You realise that we're in an exam, correct?"
                    menu:
                        "I'd help you, if you asked.":
                            Tao "Your 'better' nature isn't something to brag about. {i}Shoo{/i}. I have things to do."
                            menu:
                                "{i}Shoo...{/i}":
                                    hide tao sprite
                                    jump GreenhouseMorning1Choices

                        "Right.":
                            Tao "Now you're understanding."
                            menu:
                                "I guess I am.":
                                    hide tao sprite
                                    jump GreenhouseMorning1Choices


        label BSID1GH7: # Plant seeds (move on)
            $ cinematic = True
            Narrator "You take the seeds from the sack once more."
            Narrator "Which seed do you want to plant?"
            $ cinematic = False
            menu:
                "Winged Jasmine." if "Winged Jasmine" not in planted_seeds:
                    $ planted_seeds.append("Winged Jasmine")
                "Snapjaw Orchid." if "Snapjaw Orchid" not in planted_seeds:
                    $ planted_seeds.append("Snapjaw Orchid")
                "Moon Melon." if "Moon Melon" not in planted_seeds:
                    $ planted_seeds.append("Moon Melon")
                "Sanguine Lily." if "Sanguine Lily" not in planted_seeds:
                    $ planted_seeds.append("Sanguine Lily")
            play sound "audio/seed_place_small.mp3"
            play sound "audio/watering_can_pick_up.mp3"
            play sound "audio/watering_can_put_down.mp3"
            $ cinematic = True
            Narrator "With the [planted_seeds] planted, you watch your classmates funnel out of the greenhouse without you."
            show alice sprite with dissolve:
                xalign 0.5 
                yalign 0.3  
            Narrator "Alice looks over at you."
            $ cinematic = False
            Alice "You have the rest of the day to prepare for you upcoming exams."
            Alice "I suggest you do so."
            menu:
                "Where might I find information on plants?":
                    Alice "The library is always open."
                    Alice "I'd say you could ask us... but we're not allowed to tell you much."
                    menu:
                        "Right.":
                            hide alice sprite
                            jump Afternoon1DecisionMenu


        label BSID1GH8: # Talk to Xander
            $ cinematic = True
            show xander sprite with dissolve
            Narrator "Xander looks at you as you approach."
            $ cinematic = False
            Xander "Hey... I don't recognize any of these... I think one's Moon Melon. Hope I plant that one."
            Xander "Did you need something?"
            menu:
                "Any tips?":
                    Xander "Water them in the mornings..."
                    Xander "The soil here looks fertile, so we don't have to feed it anything. That's great cuz that stuff stinks."
                    Xander "Other than that... uhh... I don't have much advice."
                    show alice sprite at left with moveinleft
                    Alice "Less chitter chatter, more working... you aren't here to socialise."
                    hide alice sprite
                    Xander "Got it..."
                    Xander "We'll talk later."
                    hide xander sprite with dissolve
                    jump GreenhouseMorning1Choices
                    


    label Afternoon1DecisionMenu:
        $ cinematic = True
        Narrator "The morning has passed."
        $ Day1Morning = False
        $ Day1Afternoon = True
        $ cinematic = False
        menu:
            "(Go to the {b}Library{/b})" if Location != "Library":
                stop music
                jump Afternoon1Library

            "(Go to the {b}Dormitory{/b})" if Location != "Dormitory":
                stop music
                jump Afternoon1Dorms

            "(Go to the {b}Alchemy Lab{/b})" if Location != "Alchemy Lab":
                stop music
                jump Afternoon1AlchemyLab

            "(Go to the {b}Atrium{/b})" if Location != "Atrium":
                stop music
                jump Afternoon1Atrium

            "(Go to the {b}Artificing Lab{/b})" if Location != "Artificing Lab":
                stop music
                jump Afternoon1ArtificingLab

            "(Go to the {b}Courtyard{/b})" if Location != "Courtyard":
                stop music
                jump Afternoon1Courtyard

            "({b}Explore{/b})":
                stop music
                $ result = renpy.random.randint(1, 6)
                if result == 1:
                    $ cinematic = True
                    Narrator "Your exploration takes you to the {b}Library{/b}."
                    $ cinematic = False
                    jump Afternoon1Library
                if result == 2:
                    $ cinematic = True
                    Narrator "After a long while in the Greenhouse, you find yourself back in your {b}bed{/b}."
                    Narrator "You needed that."
                    $ cinematic = False
                    jump Afternoon1Dorms
                if result == 3:
                    $ cinematic = True
                    Narrator "Your stroll leads you to the {b}Alchemy Lab{/b}."
                    $ cinematic = False
                    jump Afternoon1AlchemyLab
                if result == 4:
                    $ cinematic = True
                    Narrator "You find yourself in the {b}Atrium{/b}."
                    $ cinematic = False
                    jump Afternoon1Atrium
                if result == 5:
                    $ cinematic = True
                    Narrator "Perhaps you're feeling the urge to tinker as you've ended up in the {b}Artificing Lab{/b}."
                    $ cinematic = False
                    jump Afternoon1ArtificingLab
                if result == 6:
                    $ cinematic = True
                    Narrator "You breathe in the fresh air of the {b}Courtyard{/b}."
                    $ cinematic = False
                    jump Afternoon1Courtyard

            "({b}Pass Time{/b})":
                stop music
                $ Day1Morning = False
                $ cinematic = True
                Narrator "You go back to your dorm and take a nap."
                $ cinematic = False
                $ Location = "Dormitory"
                jump Night1DecisionMenu





################################################
#                Morning 1 Areas               #
################################################




    label Afternoon1Library:
        scene library afternoon
        play music "audio/project_w_concept_04_fminor.mp3"
        $ cinematic = True
        Narrator "You enter the {b}Library{/b}. The air is stuffy, and in the distance you hear the unmistakable sound of turning pages."
        Narrator "As you make your way through, you spot Tao in the stacks."
        Narrator "They hold the book open as they stand, reading, seemingly oblivious to their surroundings."
        $ cinematic = False        
        jump Afternoon1Library_Choices

        label Afternoon1Library_Choices:
            $ cinematic = True
            Narrator "You take a moment..."
            $ cinematic = False
            menu:
                "Look around for books on Botany." if Flag_PlayerSeedsInspected and not Flag_IllustratedBotanical or Flag_WoodwitchGuide or Flag_CarnivorousPlants:
                    call Afternoon1Library_Botany from _call_Afternoon1Library_Botany
                    return
                "(Talk to Tao)" if Flag_TaoMet:
                    call Afternoon1Library_Tao from _call_Afternoon1Library_Tao
                    return
                "(Leave the Library)":
                    stop music
                    play music "audio/project_w_scholomance_map.mp3"
                    $ Location = "Corridor"
                    scene corridor afternoon
                    jump Afternoon1DecisionMenu



            label Afternoon1Library_Botany:
                $ cinematic = True
                Narrator "You check for the books on botany, all of which seem somewhat tattered and dated."
                Narrator "Not by misuse, or a lack of care, but by age."
                Narrator "It seems as though every book in this library comes with it's own layer of dust."
                Narrator "It doesn't help that parts of the wooden floor seem to have warped over years, leaving some bookshelves angular."
                Narrator "Nevertheless, you poke around, trying not to disturb Tao, who seems very aware of your presence."
                Narrator "You find a few books that seem relevant to your needs."
                $ cinematic = False
                label Afternoon1Library_BotanyBooks:
                    menu:
                        "(Read '{b}The Illustrated Botanical{/b}')":
                            $ cinematic = True
                            Narrator "Overall, the Illustrated Botanical is exactly what it says on the cover."
                            Narrator "A list of local flora and garden plants you're vaguely aware of with instruction on how to tend to them."
                            Narrator "You saw {i}Winged Jasmine{/i} and {i}Moon Melon{/i} as a part of that."
                            $ cinematic = False
                            jump Afternoon1Library_BotanyBooks
                    
                        "(Read '{b}The Woodwitch Guide to Home Gardening{/b}')":
                            $ cinematic = True
                            Narrator "This book seems to go into not plants such as {i}Snapjaw Orchids{/i} and {i}Winged Jasmine{/i}, but also their applications."
                            Narrator "There's a section on potions that you'd imagine would be quite useful."
                            $ cinematic = False
                            jump Afternoon1Library_BotanyBooks
                    
                        "(Read '{b}Carnivorous Plants of Viordia and their Many Applications{/b}')":
                            $ cinematic = True
                            Narrator "The book seems to be a catalogue of carnivorous plants found in the wilds of Viordia."
                            Narrator "More than that, it has a few lists of historical uses for these plants."
                            Narrator "You see {i}Sanguine Lily{/i} mentioned here, as well as a few other plants you don't recognise."
                            Narrator "Sanguine Lily is mentioned as requiring blood in it's rearing."
                            Narrator "Not much, but enough to make you queezy."
                            Narrator "You close the book."
                            $ cinematic = False
                            jump Afternoon1Library_BotanyBooks
                    
                        "That's enough reading...":
                            pass

                    $ cinematic = True
                    Narrator "You know that you can only take one. The system this place seems to use is the same as in the Scholomance."
                    Narrator "One book can be withdrawn per pupil."
                    Narrator "Which book do you take?"
                    $ cinematic = False
                    menu:
                        "{b}The Illustrated Botanical{/b}." if "The Illustrated Botanical" not in book_collected:
                            $ book_collected.append("The Illustrated Botanical")
                            $ Flag_IllustratedBotanical = True
                            $ cinematic = True
                            Narrator "You take the book and head to the checkout desk."
                            Narrator "As you approach, you feel the book pulled onto the counter, where an invisible hand stamps the inner page and pushes it back to you.."
                            $ cinematic = False
                            jump Afternoon1Library_Exit

                        "{b}The Woodwitch Guide to Home Gardening{/b}." if "The Woodwitch Guide to Home Gardening" not in book_collected:
                            $ book_collected.append("The Woodwitch Guide to Home Gardening")
                            $ Flag_WoodwitchGuide = True
                            $ cinematic = True
                            Narrator "You take the book and head to the checkout desk."
                            Narrator "As you approach, you feel the book pulled onto the counter, where an invisible hand stamps the inner page and pushes it back to you.."
                            $ cinematic = False
                            jump Afternoon1Library_Exit

                        "{b}Carnivorous Plants of Viordia and their Many Applications{/b}." if "Carnivorous Plants of Viordia and their Many Applications" not in book_collected:
                            $ book_collected.append("Carnivorous Plants of Viordia and their Many Applications")
                            $ Flag_CarnivorousPlants = True
                            $ cinematic = True
                            Narrator "You take the book and head to the checkout desk."
                            Narrator "As you approach, you feel the book pulled onto the counter, where an invisible hand stamps the inner page and pushes it back to you.."
                            $ cinematic = False
                            jump Afternoon1Library_Exit
                        
                        "(Look through the options once again)":
                            jump Afternoon1Library_BotanyBooks

                    label Afternoon1Library_Exit:
                        menu:
                            "(Leave the Library)":
                                stop music
                                play music "audio/project_w_scholomance_map.mp3"
                                $ Location = "Corridor"
                                scene corridor afternoon
                                jump Afternoon1DecisionMenu

            label Afternoon1Library_Tao:
                show tao sprite with dissolve
                $ cinematic = True
                Narrator "Tao's eyes dull as they see you."
                Narrator "You can tell they are deeply invested in whatever book they're reading."
                Narrator "However, as you get closer, they close the book and meet your gaze."
                $ cinematic = False
                Tao "I suppose you're here to study too... the books here aren't exactly easy to read." 
                Tao "I'm not suggesting that you're stupid, but avoid dense books, they're too old to be useful."
                label Afternoon1Library_TaoConvo:
                menu:
                    "Do you have a moment to chat?":
                        Tao "I have a minute. Don't waste it, {i}please{/i}."
                        call taohub_main from _call_taohub_main
                        jump Afternoon1Library_TaoConvo

                    "How are you doing?":
                        Tao "How am I doing?"
                        Tao "..."
                        $ cinematic = True
                        Narrator "Tao seems, almost taken aback by your words."
                        $ cinematic = False
                        Tao "I'm..."
                        Tao "I'm studying."
                        Tao "Sorry, what is it you want to know?"
                        menu:
                            "...How you are?":
                                Tao "I get that point. But what's your angle?"
                                menu:
                                    "No angle.":
                                        Tao "Right."
                                        $ Affinity_Tao += 10
                                        $ cinematic = True
                                        Narrator "Tao seems pleased for a moment. A little glint of a smile crosses their face."
                                        $ cinematic = False
                                        Tao "Well, I'm fine. I'm studying. As I will be doing every day this week."
                                        menu:
                                            "I'll leave you to it, then.":
                                                Tao "Appreciated."
                                                jump Afternoon1Library_Choices

                                            "That seems a bit intense.":
                                                Tao "It's a week that defines the rest of our lives."
                                                Tao "You'll kick yourself if you screw it up."
                                                Tao "A little bit of burnout when I'm young won't kill me."
                                                Tao "And if it does, then I'm not worth my aspirations."
                                                $ cinematic = True
                                                Narrator "You know you should say something, but the look in their eye tells you to drop it."
                                                Narrator "You hold your tongue."
                                                $ cinematic = False
                                                Tao "Was there something else you wanted?"
                                                menu:
                                                    "No. I'll be going.":
                                                        hide tao sprite
                                                        jump Afternoon1Library_Choices

                                                    "I've collected this book, what do you think?" if book_collected:
                                                        Tao "Let me see it."
                                                        $ cinematic = True
                                                        Narrator "You hand Tao [book_collected]."
                                                        Narrator "They flip through the pages, seemingly unenthused."
                                                        $ cinematic = False
                                                        Tao "You had issues with the seeds, I'm guessing..."
                                                        Tao "I suppose that's one avenue of filling in the blanks."
                                                        Tao "You understand that I do not want to help you excel your exams."
                                                        Tao "Just being frank."
                                                        Tao "I don't think many of the others {i}should{/i}, either."
                                                        Tao "You should be less open with people."
                                                        Tao "It really only ever leads to... well, failure."
                                                        Tao "Still, I appreciate that you wear whatever this is on your sleeve."
                                                        $ Affinity_Tao += 5
                                                        Tao "Do me a favour, spend less time talking with me and more time studying so that you pass."
                                                        menu:
                                                            "Alright.":
                                                                hide tao sprite
                                                                jump Afternoon1Library_Choices

                    "I'll be going now.":
                        Tao "Hmm..."
                        hide tao sprite
                        jump Afternoon1Library_Choices






    label Afternoon1Dorms:
        scene dormitory afternoon with fade
        play music "audio/project_w_dorms.mp3"
        $ cinematic = True
        Narrator "You enter the {b}Dormitory{/b}."
        Narrator "Nothing has changed since you left this morning..."
        Narrator "Your bed is still unmade. Lights still dulled as the curtains are drawn."
        Narrator "From a cursory look around, you notice... nothing."
        Narrator "No one else is here. Perhaps the rest of the students are out doing productive things this afternoon."
        $ cinematic = False
        $ Location = "Dormitory"
        jump Afternoon1Dorms_Choices


        label Afternoon1Dorms_Choices:
            $ cinematic = True
            Narrator "You sit at the edge of your bed."
            Narrator "What do you want to do?"
            $ cinematic = False
            menu:
                "(Go to the {b}Library{/b})":
                    stop music
                    jump Afternoon1Library

                "(Go to the {b}Alchemy Lab{/b})":
                    stop music
                    jump Afternoon1AlchemyLab

                "(Go to the {b}Atrium{/b})":
                    stop music
                    jump Afternoon1Atrium

                "(Go to the {b}Artificing Lab{/b})":
                    stop music
                    jump Afternoon1ArtificingLab
                
                "(Go to the {b}Courtyard{/b})":
                    stop music
                    jump Afternoon1Courtyard

                "({b}Explore{/b})":
                    stop music
                    $ result = renpy.random.randint(1, 5)
                    if result == 1:
                        $ cinematic = True
                        Narrator "Your exploration takes you to the {b}Library{/b}."
                        $ cinematic = False
                        jump Afternoon1Library
                    if result == 2:
                        $ cinematic = True
                        Narrator "Your stroll leads you to the {b}Alchemy Lab{/b}."
                        $ cinematic = False
                        jump Afternoon1AlchemyLab
                    if result == 3:
                        $ cinematic = True
                        Narrator "You find yourself in the {b}Atrium{/b}."
                        $ cinematic = False
                        jump Afternoon1Atrium
                    if result == 4:
                        $ cinematic = True
                        Narrator "Perhaps you're feeling the urge to tinker as you've ended up in the {b}Artificing Lab{/b}."
                        $ cinematic = False
                        jump Afternoon1ArtificingLab
                    if result == 5:
                        $ cinematic = True
                        Narrator "You breathe in the fresh air of the {b}Courtyard{/b}."
                        $ cinematic = False
                        jump Afternoon1Courtyard

                "({b}Pass Time{/b})":
                    $ Day1Morning = False
                    $ cinematic = True
                    Narrator "You curl up in your bed and close your eyes."
                    Narrator "Sleep takes you quickly..."
                    $ cinematic = False
                    $ Location = "Dormitory"
                    jump Night1DecisionMenu




    label Afternoon1AlchemyLab:
        scene alchemylab afternoon
        play music "audio/Potion_Theme.mp3"
        $ cinematic = True
        Narrator "You enter the {b}Alchemy Lab{/b}."
        Narrator "The air is thick with the smell of sterile chemicals. You wonder who was last in here?"
        Narrator "A faint sound catches your attention. At the back, tinkering over a bubbling pot, is Melody, seemingly immersed in whatever it is she's doing."
        $ cinematic = False
        $ Location = "Alchemy Lab"
        jump Afternoon1AlchemyLab_Choices



        label Afternoon1AlchemyLab_Choices:
            $ cinematic = True
            Narrator "You take a moment to wonder what you should do..."
            $ cinematic = False
            menu:
                "(Look at Potions)":
                    jump Afternoon1AlchemyLab_Potions
                "(Talk to Melody)" if Flag_MelodyMet:
                    jump Afternoon1AlchemyLab_Melody
                "(Leave the Alchemy Lab)":
                    stop music
                    jump Afternoon1DecisionMenu


            label Afternoon1AlchemyLab_Melody:
                $ cinematic = True
                Narrator "As you approach Melody, she turns to look over her shoulder. She must've heard your footsteps."
                Narrator "She quickly puts an ingredient in the pot, lowers the temperature, and covers it with a heavy ceramic lid."
                $ cinematic = False
                show melody sprite with dissolve
                Melody "Hey, I didn't think I'd have company."
                Melody "I'm glad to see you. Ecstatic, actually. I think I'm going a little mad. Haha."
                Melody "I'm just checking this place out, you know, getting ready for the exam. Do you like potions too?"
                menu:
                    "I think so.":
                        Melody "That makes two of us."
                        pass
                    "Not really.":
                        Melody "That's a shame, there's a lot to love."
                        pass
                Melody "Potion making is, like, the best thing. I remember when I was a little girl and I'd mix powders and soaps in my bathtub to try and get the right colour." 
                Melody "I did it so much I got in trouble for staining the ceramic." 
                Melody "My mum liked it, obviously, but I think she kept me away from the paints after that."
                menu:
                    "Sounds nice.":
                        Melody "I guess so. Growing up with supportive parents was great." 
                        Melody "In a place like this I feel like I'm in the minority."
                        pass

                    "...":
                        Melody "Anyway..."
                        pass
                Melody "When I found out one of the roles of Mages is potion mixing I can't say I wasn't giddy." 
                Melody "I don't like to brag... but I'm pretty good at it..." 
                Melody "I know we all have our talents and I just know you're probably great at this stuff too but if you need a little help let me know."
                menu:
                    "That's very kind.":
                        Melody "What are friends for?"
                        pass
                    "I should be okay.":
                        Melody "I'm sure you will be."
                        pass
                Melody "Anyway... I'm yapping."
                jump Afternoon1AlchemyLab_MelodyChoices
                
                label Afternoon1AlchemyLab_MelodyChoices:
                    Melody "Is there something you wanted?"
                    menu:
                        "(Potion) What are you brewing?":
                            Melody "It's {i}supposed{/i} to be a calming potion. I don't sleep all too well."
                            Melody "I'm a ball of energy but that's not always great when I need to {i}focus{/i}."
                            Melody "I say {i}supposed{/i} because I don't have half the ingredients and I think this is far beyond salvaging."
                            Melody "I'm good at Potions... don't let whatever monstrosity is bubbling over there fool you."
                            Melody "It's one of the two things I'm good at. The other is light Magic -- my forte."
                            menu:
                                "Did you need some help with it?":
                                    Melody "I think it's beyond help... but thanks for offering."
                                    jump Afternoon1AlchemyLab_MelodyChoices
                                "Do you have the recipe?":
                                    Melody "Are you thinking of using it for the Potion Exam?"
                                    Melody "I wouldn't recommend it..."
                                    menu:
                                        "Why?":
                                            Melody "It's not exactly a calming potion if it smells like burnt hair."
                                            Melody "I'm not even sure if it's possible to make it with the materials we'll get in the exam."
                                            Melody "I planted {i}some{/i}of the ingredients... but I doubt we'll be allowed to share."
                                            Melody "Know what, if you don't have any other option... here, let me write down the recipe for you."
                                            $ cinematic = True
                                            Narrator "Melody pulls out her notepad, which seems absolutely stuffed with notes, papers, and even a few imprints of flowers."
                                            Narrator "She takes a moment to scribble down some notes, and then hands it to you."
                                            play sound "audio/dialogue_information_default.mp3"
                                            $ cinematic = False
                                            $ Flag_CalmingPotionRecipe = True
                                            Melody "I wouldn't risk it... but if you don't have another choice it should scrape you a pass."
                                            Melody "At least I hope it does."
                                            menu:
                                                "What if it doesn't?":
                                                    Melody "Then I guess we'll both be in trouble."
                                                    Melody "But hey, no pressure, right?"
                                                    jump Afternoon1AlchemyLab_MelodyChoices
                                                "Thanks, Melody.":
                                                    Melody "Hey, we're friends, you know? I'll try and help you as much as I'm {i}allowed{/i} to. I know you'll do the same."
                                                    Melody "It's nice having someone I can trust in."
                                                    Melody "I know we didn't chat much in the Scholomance, but that doesn't mean I never liked you."
                                                    menu:
                                                        "Likewise.":
                                                            jump Afternoon1AlchemyLab_MelodyChoices

                                                        "I'm sure we both had other things going on.":
                                                            Melody "Exactly."
                                                            jump Afternoon1AlchemyLab_MelodyChoices


                        "I had some questions...":
                            Melody "I'm an open book."
                            call melodyhub_main from _call_melodyhub_main_1

                        "Nothing. I should get going.":
                            Melody "Anyway, don't be a stranger."
                            Melody "I'll probably spend a lot of time here."
                            Melody "If you need to chat, you know where to look."
                            hide melody sprite
                            $ cinematic = True
                            Narrator "As you leave, you hear Melody begin working on her potion again."
                            $ cinematic = False
                            jump Afternoon1DecisionMenu




            label Afternoon1AlchemyLab_Potions:
                $ cinematic = True
                Narrator "Inside a locked glass cupboard, you see rows and rows of potions. Each meticulous label still readable under a layer of dust."
                Narrator "You wonder when any of them were last used."
                Narrator "As you look over them, you hear Melody stir her potion -- the unmistakable smell of burned hair filling the room."
                $ cinematic = False
                show melody sprite
                Melody "Crap..."
                hide melody sprite with dissolve
                menu:
                    "(Inspect the Potions)":
                        $ cinematic = True
                        Narrator "You ignore it."
                        Narrator "You notice a few you recognise from your time in the Scholomance."
                        Narrator "A potion of cleansing - soap, basically."
                        Narrator "A potion of sleepless night... which you can only assume is caffeine."
                        Narrator "A frog potion... whatever that is..."
                        Narrator "A lot of their labels are quite... undescriptive."
                        Narrator "You wonder why they're locked away, and if so, who has the key?"
                        $ cinematic = False
                        menu:
                            "(Magic: Unlock the Potions)" if Spell_Unlocking:
                                $ cinematic = True
                                Narrator "You focus on the lock, feeling the magic within you stir."
                                Narrator "With a few whispered words, the cabinet unlocks with a loud {b}{i}clunk{i}{b}. It's clearly not been touched in a while."
                                play sound "audio/reveal_magic_spell.mp3"
                                show melody sprite with dissolve
                                Narrator "Melody looks over at you. A knowing look in her eye."
                                $ Flag_MelodyCaughtPlayerStealing = True
                                hide melody sprite
                                Narrator "You know you can only take one. Any more and it'd be noticeable."
                                $ cinematic = False
                                menu: 
                                    "(Take the {b}Potion of Cleansing{/b})" if "Potion of Cleansing" not in potion_stolen:
                                        $ potion_stolen.append("Potion of Cleansing")
                                        pass
                                    "(Take the {b}Potion of Frog Polymorph{/b})" if "Potion of Frog Polymorph" not in potion_stolen:
                                        $ potion_stolen.append("Potion of Frog Polymorph")
                                        pass
                                    "(Take the {b}Potion of Sleepless Night{/b})" if "Potion of Sleepless Night" not in potion_stolen:
                                        $ potion_stolen.append("Potion of Sleepless Night")
                                        pass
                                $ cinematic = True
                                Narrator "You slip the potion into your bag."
                                Narrator "A part of you feels a thrill of excitement."
                                Narrator "Melody still watches over her shoulder."
                                $ cinematic = False
                                show melody sprite
                                Melody "My lips are sealed."
                                menu:
                                    "Thanks.":
                                        hide melody sprite
                                        jump Afternoon1AlchemyLab_Choices


                            "(Test the Lock)":
                                $ cinematic = True
                                Narrator "You pull the handle -- it doesn't give."
                                $ cinematic = False
                            
                            "(Leave it alone)":
                                jump Afternoon1AlchemyLab_Choices


                    "(Talk to Melody)":
                        jump Afternoon1AlchemyLab_Melody





    label Afternoon1Atrium:
        scene atrium afternoon
        play music "audio/project_w_class.mp3"
        play ambience "audio/main_hall_ambience.mp3"
        $ cinematic = True
        Narrator "You enter the {b}Atrium{/b}."
        Narrator "Sunlight filters through the glass ceiling. The moons are dim, bobbing gently in the air."
        Narrator "Along a bench, with a book in his hand, is Xander. He looks focused, or at least intense."
        Narrator "Beyond it, you see the courtyard -- the doorway open and light pooling in through it."
        $ cinematic = False
        $ Location = "Atrium"
        jump Afternoon1Atrium_Choices

        label Afternoon1Atrium_Choices:
            $ cinematic = True
            Narrator "What do you want to do?"
            $ cinematic = False
            menu:
                "(Check Beneath the Moons)" if Flag_NotAliceMet:
                    call Afternoon1Atrium_NotAlice from _call_Afternoon1Atrium_NotAlice
                    return

                "(Inspect the Moons)":
                    call Afternoon1Atrium_Moons from _call_Afternoon1Atrium_Moons
                    return

                "(Talk to Xander)":
                    call Afternoon1Atrium_Xander from _call_Afternoon1Atrium_Xander
                    return

                "(Leave the Atrium)":
                    stop music
                    call Afternoon1DecisionMenu from _call_Afternoon1DecisionMenu




        label Afternoon1Atrium_Xander:
            show xander sprite with dissolve
            $ cinematic = True
            Narrator "Xander looks up at you as you approach."
            $ cinematic = False
            Xander "Hi..." 
            Xander "I've been trying to get a head start on studying -- I can't take my eyes off those moons though!" 
            Xander "I know the others like the Archives, but it's way more relaxing here."
            jump Afternoon1Atrium_XanderChoices

            label Afternoon1Atrium_XanderChoices:
                Xander "What did you wanna chat about?"
                menu:
                    "(Ask about Botany)":
                        Xander "Oh. Yeah, I know how to take care of plants. I grew up on a farm."
                        Xander "I think I ended up planting a whole bunch of different herbs."
                        Xander "No idea what sorta potion I'll be making."
                        Xander "Guess I'll find out..."
                        Xander "The more I think about it the more hair I lose."
                        menu:
                            "You're losing hair?":
                                Xander "What's the word... hypothetical? Yeah, I'm hypothetically losing hair."
                                Xander "Weirdly, studying's helping relieve it."
                                Xander "Or maybe it's the moons. Magic {i}that{/i} crazy has to have some impact on feelings and crap."
                                menu:
                                    "Could be...":
                                        pass

                                    "Your hypothetical hair looks great.":
                                        Xander "Ha. Thanks."
                                        Xander "It survived a lot of burns..."
                                        Xander "Not intentional ones... but you can only dodge a few pyromancies before one grazes you."
                                        $ Affinity_Xander +=10
                                        pass

                            "Sounds like you got through step one alright.":
                                Xander "Yeah, I guess so..."
                                pass

                        Xander "Ever feel like you know diddly squat about magic? I'm feeling that right now..."
                        Xander "Maybe I should have studied more in the Scholomance."
                        Xander "Potions... Artifice... at least I know I'll score top marks on the combat exam."
                        Xander "Crap. I'm probably not helping with {i}your{/i} nerves, right?"
                        Xander "You'll do great."
                        menu:
                            "You'll do great, too.":
                                Xander "Saints, I hope so. I don't wanna go back under the lake. The Scholomance ain't something I {i}ever{/i} wanna go back to."
                                Xander "First time sunlight hit my head yesterday felt like I was waking up from a decade long coma."
                                $ cinematic = True
                                Narrator "He looks down at the book again, now closed."
                                $ cinematic = False
                                Xander "I can't believe I survived that place."
                                Xander "Even Tao got through that. Guess some people are built to thrive in that sorta environment."
                                menu:
                                    "What's that got to do with it?":
                                        Xander "Ah... ignore me. Tao and I go way back."
                                        Xander "I don't wanna get into all that... you know, a week before we {i}hopefully{/i} graduate."
                                        hide xander sprite
                                        jump Afternoon1Atrium_XanderChoices

                            "Lets talk about something else.":
                                Xander "Direct... I guess."
                                hide xander sprite
                                jump Afternoon1Atrium_XanderChoices
                    
                    "I've got stuff I wanna ask you.":
                        Xander "Really? Let's hear it."
                        call xanderhub_main from _call_xanderhub_main
                        hide xander sprite
                        jump Afternoon1Atrium_Choices

                    "Nevermind.":
                        hide xander sprite
                        jump Afternoon1Atrium_Choices




        label Afternoon1Atrium_Moons:
            play sound "audio/moon_sparkle.mp3"
            $ cinematic = True
            Narrator "You look up at the moons as their light dances along the stone floor."
            Narrator "You still can't decipher the spell weaving around it."
            Narrator "Perhaps you never will."
            $ cinematic = False
            jump Afternoon1Atrium_Choices


        label Afternoon1Atrium_NotAlice:
            play sound "audio/main_hall_gentle_water.mp3"
            $ cinematic = True
            Narrator "You look below the moons, down, into the grate."
            Narrator "You don't {i}hope{/i} to see the thing that looks like Alice, but curiosity lures you closer."
            Narrator "As you stare down the grate, you see nothing. Just an inky blackness. The occasional shaft of light illuminating a steady stream of water."
            Narrator "Whatever was down there won't come out in the daylight. That much you're sure of."
            $ cinematic = False
            jump Afternoon1Atrium_Choices










    label Afternoon1Courtyard:
        scene courtyard afternoon
        play music "audio/project_w_concept_03_gmajor.mp3"
        $ cinematic = True
        Narrator "You enter the {b}Courtyard{/b}."
        Narrator "While a bitter chill nibbles at your fingers, you breathe in the fresh air -- it smells of grass and honey."
        Narrator "Magic woven with nature."
        Narrator "You know you need to preserve this moment."
        Narrator "As you look around, you notice Aria staring off down the mountain, into the dark forest." 
        Narrator "You know she wouldn't try and escape. It would be suicide."
        Narrator "Yet you can't help but feel anxious around the prospect. You try and turn you eyes back to the open sky..." 
        Narrator "...something you haven't seen since your admittance to the Scholomance."
        $ cinematic = False
        $ Location = "Courtyard"
        jump Afternoon1Courtyard_Choices


        label Afternoon1Courtyard_Choices:
            $ cinematic = True
            Narrator "What do you want to do?"
            $ cinematic = False
            menu:
                "Approach Aria.":
                    jump Afternoon1Courtyard_Aria

                "Enter the Forest.":
                    jump Afternoon1Forest_Attempt

                "Leave the Courtyard.":
                    stop music
                    jump Afternoon1DecisionMenu



            label Afternoon1Courtyard_Aria:
                $ cinematic = True
                Narrator "Aria seems oblivious to the fact that she's not alone. Her mind adrift."
                Narrator "She sits in the grass. You can't help but notice the flowers turning towards her."
                Narrator "To them, she's the sun."
                Narrator "You step closer, and finally, she turns to look up at you."
                show aria sprite with dissolve
                $ cinematic = False
                Aria "Hello."
                Aria "Did you want to sit down?"
                jump Afternoon1Courtyard_AriaChoices

                label Afternoon1Courtyard_AriaChoices:
                    menu:
                        "(Take a seat)":
                            $ cinematic = True
                            Narrator "You sit down beside her. The flowers tickle your skin as the afternoon sun warms you."
                            Narrator "Aria seems... lost, as she looks into the forest. The darkness beneath the boughs capturing her focus."
                            Narrator "You can't tell if she's lost in thought, or whether she is giving herself a moment of reprieve."
                            $ cinematic = False
                            Aria "I think I want to go in the forest."
                            menu:
                                "Why?":
                                    Aria "I feel something there."
                                    Aria "Every time I get close, something calling out to me."
                                    Aria "Calm. For the first time since before the Scholomance..."
                                    pass

                                "I don't think that's safe.":
                                    Aria "I'm sure I'll be okay."
                                    Aria "Animals don't {i}want{/i} to harm people."
                                    Aria "And I'm a Mage... I'm sure they'll understand me."
                                    pass
                            Aria "I don't belong here."
                            Aria "Maybe I belong somewhere out there..."
                            menu:
                                "Where do you think you belong?":
                                    Aria "Nowhere. Not back at the village, not in the Scholomance..." 
                                    Aria "... {i}definitely{/i} not here."
                                    Aria "Maybe out there, in nature."
                                    Aria "It's like the forest is calling me home."
                                    Aria "I grew up on a mountain, the forests there were endless."
                                    menu:
                                        "Maybe you're nostalgic":
                                            Aria "I can't go home, even if I graduate from this place."
                                            Aria "I'm not welcome..."
                                            pass

                                "You belong here, believe it or not.":
                                    Aria "I don't think that's true."
                                    Aria "I'm called names, avoided and... told I'm crazy."
                                    Aria "All while people watch me."
                                    Aria "You know. The 'worrying eyes', the 'fearful eyes'. They know I'm unstable so they talk around me, talk through me, talk over me."
                                    Aria "Never listening, but nodding as though they agree."
                                    Aria "I don't want to be placated or reprimanded for something I cannot control."
                                    Aria "As much as you all despise Eileen, at least she's blunt with me."
                                    Aria "I'm a potential monster for her to kill."
                                    pass
                            $ cinematic = True
                            Narrator "Aria seems to deflate a little."
                            Narrator "Then, almost as if some magic had touched her, she perks up again."
                            show aria sprite happy
                            $ cinematic = False
                            Aria "I think I'll go in there tomorrow."
                            hide aria sprite happy
                            jump Afternoon1Courtyard_Choices


                        "I have a lot of questions.":
                            Aria "Ask away."
                            call melodyhub_main from _call_melodyhub_main_2
                            hide aria sprite
                            jump Afternoon1Courtyard_Choices


                        "(Leave Aria be.)":
                            Aria "Oh, you're going?"
                            Aria "Well, I'll be around."
                            hide aria sprite
                            stop music
                            jump Afternoon1Courtyard_Choices
                        



            label Afternoon1Forest_Attempt:
                $ cinematic = True
                Narrator "You walk towards the forest. A long stretch of grass acting as the threshold between the Summit and all that surrounds it."
                Narrator "The trees seem to sway in the wind. It's just enough that you feel time passing."
                Narrator "You take a step into the grass..."
                $ cinematic = False
                show alice sprite:
                    xalign 0.5 
                    yalign 0.3  
                Alice "No. Absolutely not. Come back here."
                menu:
                    "Okay...":
                        hide alice sprite
                        jump Afternoon1DecisionMenu
                        







    label Afternoon1ArtificingLab:
        scene artificing lab afternoon
        play music "audio/Marigold District_MASTER2_LOOPED.mp3"
        $ cinematic = True
        Narrator "You enter the {b}Artificing Lab{/b}."
        Narrator "It smells like burnt metal. The windows are steamed up, obscuring your view outside."
        show rex sprite
        Narrator "As you look around, you notice Rex, hunched over a workbench. It's like he's in the centre of a tornado, with dozens of tools discarded around him."
        Narrator "Though, as you look closer you see that the tools are organized by segments -- hammers with hammers, chisels with chisels..."
        Narrator "He turns to look at you as you step into the eye of it all."
        $ cinematic = False
        Rex "Hmm. Done with planting?"
        $ cinematic = True
        Narrator "Before you can respond he points over at a table covered in various tools and materials."
        $ cinematic = False
        Rex "Pass me the graver set."
        $ cinematic = True
        Narrator "You have no idea what that is."
        $ cinematic = False
        menu:
            "(Hand him the small, sharp tool with a balled end.)":
                Rex "Thanks."
                $ cinematic = True 
                Narrator "He shaves a mote of glowing metal and places the tool down. Turning to give you his full attention."
                $ Affinity_Rex += 10
                pass

            "(Hand him the long file)":
                Rex "That's a needle file."
                $ cinematic = True
                Narrator "He drops the tool in his hand and moves past you to grab another."
                Narrator "As he passes, you notice that he smells like solder."
                Narrator "When he returns, he places his back against the workbench, giving you his full attention."
                $ cinematic = False
                pass

            "(Hand him the small hammer with a small, flat end.)":
                Rex "That's a jeweler's hammer."
                $ cinematic = True
                Narrator "He drops the tool in his hand and moves past you to grab another."
                Narrator "As he passes, you notice that he smells like solder."
                Narrator "When he returns, he places his back against the workbench, giving you his full attention."
                $ cinematic = False
                pass
        Rex "I needed a break anyway."
        $ Location = "Artificing Lab"
        jump Afternoon1ArtificingLab_Choices


        label Afternoon1ArtificingLab_Choices:
            show rex sprite with dissolve
            Rex "What do you need?"
            menu:
                "(Ask Rex about Artifice)":
                    call Afternoon1ArtificingLab_Artifice from _call_Afternoon1ArtificingLab_Artifice

                "(Ask Rex what he's working on)":
                    call Afternoon1ArtificingLab_WorkingOn from _call_Afternoon1ArtificingLab_WorkingOn

                "Can I ask you some stuff?":
                    call rexhub_main from _call_rexhub_main

                "(Investigate the Artificing Lab)":
                    hide rex sprite
                    call Afternoon1ArtificingLab_Explore from _call_Afternoon1ArtificingLab_Explore

                "(Leave the Artificing Lab)":
                    stop music
                    hide rex sprite
                    jump Afternoon1DecisionMenu
        
        
        
        label Afternoon1ArtificingLab_Artifice:
            Rex "Artifice... it's machines and crap."
            Rex "Magic machines."
            Rex "Automating crap, but also augmenting spells..."
            Rex "...basically anything that alters magic with a machine is Artifice."
            Rex "You aren't prepared at all, are you?"
            menu:
                "I'll be fine.":
                    Rex "You'll be fine but you're asking me what Artifice is."
                    Rex "At least own up to it, loser."
                    $ Affinity_Rex -= 5
                    pass

                "I'm {i}absolutely{/i} not prepared.":
                    Rex "Ha. You're honest, at least."
                    Rex "Only tip I can give is to use good materials and figure out the stuff you {i}can{/i} make soon, so you're prepped."
                    Rex "Artificing is simple... so long as you know what tools to use and what you're making."
                    Rex "My sister used to bake a lot... it's kinda like that."
                    $ Affinity_Rex += 5
                    pass
            Rex "Anyway... the exams isn't for a few days."
            return


        label Afternoon1ArtificingLab_WorkingOn:
            Rex "This? It's just some practice."
            Rex "It doesn't explode... if that's what you're worried about."
            Rex "I wanted to make something to water my plants every day..."
            Rex "Means I can sleep in."
            Rex "Maybe I can submit it for my Artificing Exam. That way I don't have to think about all this exam crap."
            menu:
                "Maybe...":
                    Rex "You don't sound convinced... then again, ain't my job to convince you."
                    return
                "Is now the time to relax?":
                    Rex "Never seems to be. Not like I'm trying to laze about but a guy needs rest."
                    Rex "We've been on a strict schedule for years now, course I've figured out ways to make that easier."
                    Rex "Outside of... you know, just rebelling."
                    return


        label Afternoon1ArtificingLab_Explore:
            $ cinematic = True
            Narrator "You take a look around the Artificing Lab."
            Narrator "There are a few messy tables and workstations -- tools placed in methodical spots."
            Narrator "In one of the corners, you notice a few scrolls, one of which is loose."
            Narrator "As you move over to it, unrolling one, you see that it's a blueprint of some sort of artifice."
            Narrator "{b}The Light Machine{/b}"
            $ cinematic = False
            menu:
                "(Take it with you)":
                    play sound "audio/clue_found_item_alert.mp3"
                    $ artifice_options.append("Light Machine")
                    $ cinematic = True
                    Narrator "You stash it in your bag."
                    $ cinematic = False
                    pass

                "(Leave it)":
                    pass
            Narrator "You also notice a few tools, scattered about the workstations."
            Narrator "They seem to be specialized for artificing tasks, with intricate designs and a well-used appearance."
            Narrator "You might be able to use them if you need to work on any artifice projects."
            if "Light Machine" in artifice_options:
                Narrator "You could work on the Light Machine... though you aren't sure if you should dedicate time to it right now."
                pass
            else:
                Narrator "You don't have a project to work on yet."
                pass
            Narrator "You move on."
            return











    label Night1DecisionMenu:
        scene dormitory night
        play music "audio/project_w_dorms.mp3"
        $ cinematic = True
        Narrator "You feel tired. Looking around you see the rest of the students sitting around the dorm. Some studying, others already in bed with their curtains drawn."
        Narrator "What do want to do?"
        $ cinematic = False
        menu:
            "(Talk to Tao)":
                $ cinematic = True
                Narrator "Tao's curtain's are drawn, but you hear pages turning behind it."
                Narrator "You clear your throat."
                $ cinematic = False
                Tao "I'm busy. Shoo."
                jump Night1DecisionMenu
                
            "(Talk to Aria)":
                show aria sprite with dissolve
                if Flag_AriaWantsBook:
                    $ cinematic = True
                    Narrator "Aria sits on her bed, staring out the window. In the distance, you see the trees wave in the wind."
                    $ cinematic = False
                    Aria "Shame curfew is so early. Night time is when nature is most itself."
                    Aria "Did you need something?"
                    menu:
                        "I don't think so."
                        "Are you okay?":
                            Aria "I'm okay. Not tired enough to sleep but not daring enough to sneak out like Rex."
                            menu:
                                "Rex snuck out?":
                                    Aria "Obviously. He's a night owl, these are the hours he's most active.."
                                    Aria "I haven't checked, but his curtain hasn't moved in a while and last night I heard him snoring..."
                                    Aria "It's only logical that he's out in the castle."
                                    Aria "I should've asked him to bring me a book from the library or something. I'm bored out of my mind."
                                    $ Flag_RexSneakDay1 = True
                                    $ Flag_AriaWantsBook = True
                                    menu:
                                        "Want me to get you one?":
                                            Aria "I wouldn't want you to get in trouble."
                                            Aria "If you {i}do{/i} go out... please. Something fictional. Maybe uplifting."
                                            hide aria sprite
                                            jump Night1DecisionMenu
                                        "Pick one up tomorrow, I guess.":
                                            Aria "Learned my lesson..."
                                            hide aria sprite
                                            jump Night1DecisionMenu
                else:
                    $ cinematic = True
                    Narrator "Aria is still sat on her bed when you enter the room."
                    $ cinematic = False
                    Aria "Oh, hi. Did you want something?"
                    menu:
                        "I brought you a book." if AriaBookAcquired:
                            Aria "Oh, that's so kind."
                            $ Affinity_Aria += 10
                            $ cinematic = True 
                            Narrator "She takes the book and opens it."
                            Narrator "You can tell she's tired, but she turns to page 1."
                            $ cinematic = False
                            menu:
                                "You're going to read it now?":
                                    Aria "Just a chapter. I'm bored, you know?"
                                    Aria "Did you mean to get me something this..."
                                    Aria "Know what, nevermind. I need something this... trashy."
                                    menu:
                                        "I'll leave you to it.":
                                            hide aria sprite
                                            jump Night1DecisionMenu

                        "No.":
                            hide aria sprite
                            jump Night1DecisionMenu



            "(Talk to Melody)":
                show melody sprite with dissolve
                $ cinematic = True
                Narrator "Melody sits at her desk, writing in her diary."
                $ cinematic = False
                Melody "Hey... nice to see you stay up late too."
                if Spell_Light == False:
                    Melody "I'm usually in bed pretty early, but I spend a lot of time reading under the covers."
                    Melody "Not saying you have to be quiet if you're walking around, I sleep like the dead."
                    Melody "Honestly, learning that light spell back at the Scholomance made my life a million times easier."
                    menu:
                        "Light spell?":
                            Melody "Yeah… wait, do you not know it? Maybe you missed that class, I should have it somewhere in my bag."
                            $ Spell_Light = True
                            Melody "Here it is."
                            menu:
                                "Thanks.":
                                    Melody "No worries. Is there something you wanted to talk about? You know, since you're here and all?"
                                    menu:
                                        "A few things...":
                                            call melodyhub_main from _call_melodyhub_main_3
                                            hide melody sprite
                                            jump Night1DecisionMenu
                                        "Nothing in particular.":
                                            Melody "Well, we'll chat tomorrow, I guess."
                                            hide melody sprite
                                            jump Night1DecisionMenu

                else:
                    Melody "I'm a little unsettled tonight. Dunno why. Maybe I'm just worried about my plants."
                    Melody "One more thing we have little control over, you know?"
                    menu:
                        "I know.":
                            Melody "Oh I'm sure."
                            Melody "I don't think there's anything happening tomorrow..."
                            Melody "Pretty sure the Artificing exam is the day after tomorrow, though... which is worrying."
                            Melody "Not sure what I'm making for that... guess I'll find out."
                            Melody "Either way, I'll let you get some sleep."
                            hide melody sprite
                            jump Night1DecisionMenu
                        "I might just head to bed.":
                            Melody "Oh, sure thing. Good night!"
                            hide melody sprite
                            jump Night1DecisionMenu


            "(Talk to Rex)":
                $ cinematic = True
                Narrator "Rex's curtains are drawn. You hear nothing behind them."
                $ cinematic = False
                if Flag_RexSneakDay1:
                    $ cinematic = True
                    Narrator "You know he's not there."
                    Narrator "You wonder where he snuck off to..."
                    $ cinematic = False
                    jump Night1DecisionsMenu

                else:
                    menu:
                        "(Leave)":
                            jump Night1DecisionMenu

            "(Talk to Xander)":
                show xander sprite with dissolve
                $ cinematic = True
                Narrator "Xander is sitting on his bed, staring at the wall."
                Narrator "He looks deep in thought."
                $ cinematic = False
                menu:
                    "You alright?":
                        Xander "I'm okay. I'm going to be up all night studying again..."
                        Xander "Don't let me keep you up."
                        menu:
                            "I'll be alright.":
                                Xander "Right..."
                                Xander "Must be nice."
                                pass

                            "Do you need some help?":
                                Xander "There's nothing to help with. Unless you can somehow fix my idiot brain so I can pass."
                                pass
                Xander "I won't keep you."
                menu:
                    "(Leave)":
                        hide xander sprite
                        jump Night1DecisionMenu


            "(Sneak Out)":
                $ cinematic = True
                Narrator "You pull your curtains closed and exit the dormitory."
                $ cinematic = False
                stop music
                jump Night1SneakDecision 

            "(Go to sleep)":
                $ cinematic = True
                Narrator "You pull the covers over you, looking up at the ceiling as it lulls you to sleep."
                Narrator "Moments after your eyes are closed, you fall asleep."
                $ cinematic = False
                $ Day1Night = False
                $ Flag_EileenLibraryDay2 = False
                stop music
                jump Morning2Dorms
    








    label Night1SneakDecision:
        $ Location = "Corridor"
        play music "audio/project_w_main_theme_concept_02_fade.mp3"
        $ cinematic = True
        Narrator "You enter the corridor, the dormitory door closing behind you."
        Narrator "It's cold, and in the dark you can only make out distant shapes."
        Narrator "You know you won't be able to explore without some form of light."
        $ cinematic = False    
        if Spell_Light:
            play sound "audio/light_spell.mp3"
            $ cinematic = True
            Narrator "You ignite a white orb of light in your hand, casting stark shadows along the walls."
            Narrator "You're thrilled, you realise. Your heart's racing."
            Narrator "You wonder where you should explore..."
            $ cinematic = False
            jump Night1SneakDecision_Choices
            label Night1SneakDecision_Choices:
                menu:
                    "(Go to the {b}Library{/b})" if Location != "Library":
                        if Flag_EileenLibraryDay2:
                            Narrator "Eileen is in there."
                            Narrator "It's better you don't get caught."
                            pass

                        else:
                            stop music
                            jump Night1Library
                        # can collect Aria a book (Flag_AriaWantsBook) (AriaBookAcquired)

                    "(Go to the {b}Alchemy Lab{/b})" if Location != "Alchemy Lab":
                        stop music
                        jump Night1AlchemyLab
                        # empty but gives the player the option to steal a potion if they didn't before.

                    "(Go to the {b}Atrium{/b})" if Location != "Atrium":
                        stop music
                        if Flag_NotAliceMet:
                            jump Night1Atrium
                            #another encounter with NotAlice

                        else:
                            jump Night1Atrium2
                            # can have a first encounter with NotAlice... if they haven't met her before.

                    "(Go to the {b}Artificing Lab{/b})" if Location != "Artificing Lab":
                        stop music
                        jump Night1ArtificingLab
                        ### Rex working on projects after hours.
                    
                    "(Go to the {b}Greenhouse{/b})" if Location != "Greenhouse":
                        stop music
                        jump Night1Greenhouse

                    "(Return to the {b}Dormitory{/b})" if Location != "Dormitory":
                        stop music
                        jump Night1DecisionMenu

        else:
            stop music
            $ cinematic = True
            Narrator "You can't see anything. It's too dangerous to go ahead without light."
            Narrator "You turn around."
            $ cinematic = False
            jump Night1DecisionMenu





        label Night1Library:
            scene library night
            play music "audio/project_w_concept_04_fminor.mp3"
            $ Location = "Library"
            $ cinematic = True
            Narrator "The library door is warm as you open it. Roots and vines from the greenhouse seem to have slowly made their way inside overnight."
            Narrator "You wonder if someone's plant has gone haywire."
            Narrator "Brushing them aside, you push in."
            Narrator "Carrying the light in your hands, you scan the room."
            $ cinematic = False
            if Flag_AriaWantsBook:
                Narrator "You remember Aria mentioning she wanted a book."
                Narrator "You look around, wondering if you can find something for her."
                Narrator "After a few moments of looking, you come across a tattered paperback, clearly left by a former student, or perhaps a staff member."
                Narrator "It's certainly nothing academic..."
                Narrator "The blurb reads:"
                "{i}Depressed after a bad breakup, a man falls in love with the ghost haunting his house...{/i}"
                Narrator "You pick it up."
                $ AriaBookAcquired = True
            else: 
                pass
            if Flag_ArchivesDiscovered:
                $ cinematic = True
                Narrator "The silence is almost welcoming. The eerie feeling you had when you last visited has evaporated into solace."
                Narrator "Rather than feeling the dread of being watched, you feel like you're centre-stage, with a hundred eyes watching you."
                Narrator "Perhaps the books have eyes..."
                Narrator "You turn your gaze to the Archive door."
                if Spell_Unlocking:
                    Narrator "You try the unlock spell."
                    Narrator "As expected, nothing happens."
                    Narrator "You're certain it needs something else to open..."
                    pass
                else: 
                    Narrator "You pull on the lock."
                    Narrator "It doesn't budge."
                    pass
                Narrator "You check the stacks for anything of interest..."
                if book_collected:
                    Narrator "...Finding nothing new. You're content with {book_collected}."
                    jump Night1SneakDecision_Choices

                else:
                    Narrator "You check for the books on botany, all of which seem somewhat tattered and dated."
                    Narrator "Not by misuse, or a lack of care, but by age."
                    Narrator "It seems as though every book in this library comes with it's own layer of dust."
                    Narrator "It doesn't help that parts of the wooden floor seem to have warped over years, leaving some bookshelves angular."
                    Narrator "Nevertheless, you poke around until -- trying not to disturb Tao, who seems very aware of your presence."
                    Narrator "You find a few books that seem relevant to your needs."
                    $ cinematic = False
                    label Night1Library_BotanyBooks:
                        menu:
                            "(Read '{b}The Illustrated Botanical{/b}')":
                                $ cinematic = True
                                Narrator "Overall, the Illustrated Botanical is exactly what it says on the cover."
                                Narrator "A list of local flora and garden plants you're vaguely aware of with instruction on how to tend to them."
                                Narrator "You saw {i}Winged Jasmine{/i} and {i}Moon Melon{/i} as a part of that."
                                $ cinematic = False
                                pass

                            "(Read '{b}The Woodwitch Guide to Home Gardening{/b}')":
                                $ cinematic = True
                                Narrator "This book seems to go into not plants such as {i}Snapjaw Orchids{/i} and {i}Winged Jasmine{/i}, but also their applications."
                                Narrator "There's a section on potions that you'd imagine would be quite useful."
                                $ cinematic = False
                                pass

                            "(Read '{b}Carnivorous Plants of Viordia and their Many Applications{/b}')":
                                $ cinematic = True
                                Narrator "The book seems to be a catalogue of carnivorous plants found in the wilds of Viordia."
                                Narrator "More than that, it has a few lists of historical uses for these plants."
                                Narrator "You see {i}Sanguine Lily{/i} mentioned here, as well as a few other plants you don't recognise."
                                Narrator "Sanguine Lily is mentioned as requiring blood in it's rearing."
                                Narrator "Not much, but enough to make you queezy."
                                Narrator "You close the book."
                                $ cinematic = False
                                pass

                        $ cinematic = True
                        Narrator "You know that you can only take one. The system this place seems to use is the same as in the Scholomance."
                        Narrator "One book can be withdrawn per pupil."
                        Narrator "Which book do you take?"
                        $ cinematic = False
                        menu:
                            "The Illustrated Botanical." if "The Illustrated Botanical" not in book_collected:
                                $ book_collected.append("The Illustrated Botanical")
                                $ Flag_IllustratedBotanical = True
                                $ cinematic = True
                                Narrator "You take the book and head to the checkout desk."
                                Narrator "As you approach, you feel the book pulled onto the counter, where an invisible hand stamps the inner page and pushes it back to you.."
                                $ cinematic = False
                                jump Night1SneakDecision_Choices

                            "The Woodwitch Guide to Home Gardening." if "The Woodwitch Guide to Home Gardening" not in book_collected:
                                $ book_collected.append("The Woodwitch Guide to Home Gardening")
                                $ Flag_WoodwitchGuide = True
                                $ cinematic = True
                                Narrator "You take the book and head to the checkout desk."
                                Narrator "As you approach, you feel the book pulled onto the counter, where an invisible hand stamps the inner page and pushes it back to you.."
                                $ cinematic = False
                                jump Night1SneakDecision_Choices

                            "Carnivorous Plants of Viordia and their Many Applications." if "Carnivorous Plants of Viordia and their Many Applications" not in book_collected:
                                $ book_collected.append("Carnivorous Plants of Viordia and their Many Applications")
                                $ Flag_CarnivorousPlants = True
                                $ cinematic = True
                                Narrator "You take the book and head to the checkout desk."
                                Narrator "As you approach, you feel the book pulled onto the counter, where an invisible hand stamps the inner page and pushes it back to you.."
                                $ cinematic = False
                                jump Night1SneakDecision_Choices
                            
                            "(Look through the options once again)":
                                jump Night1Library_BotanyBooks

                            "(Leave the Library)":
                                jump Night1SneakDecision_Choices


            else:
                $ cinematic = True
                Narrator "The spell casts eerie light over the library. The silence seems uncanny as you step inside -- looking over the stacks of thick books and tomes."
                Narrator "Shadows dance along the walls -- remnants clouds through the skylight."
                Narrator "Despite the prickly feeling on your neck, you know you're alone."
                Narrator "In the distance, you notice a gated door, a great padlock stopping you."
                Narrator "Yet you can't help but approach it. There's an aura to it, as though moving towards honey-scented wood." 
                Narrator "You can feel great magic, as though spectral fingers are luring you closer. Twisting and spiralling."
                Narrator "You breathe it in..."
                Narrator "Whatever is behind the door is old magic."
                Narrator "Those scents, dewdrops on grass, honey warmed up, feel intrinsic to you."
                Narrator "They feel intimate."
                Narrator "More a part of you than your beating heart."
                Narrator "You lift your light higher and look over the old paper label above the door."
                Narrator "{b}The Archives{/b}."
                $ Flag_ArchivesDiscovered = True
                $ cinematic = False
                menu:
                    "(Try the door.)":
                        $ cinematic = True
                        Narrator "The chains are strong. The lock seems unbreakable."
                        Narrator "You need a key."
                        $ cinematic = False
                        pass
                    "(Leave.)": 
                        $ cinematic = True
                        Narrator "You kill the urge to move closer. You don't know where you find the determination."
                        Narrator "You know there is nothing for you here."
                        Narrator "Nothing yet..."
                        $ cinematic = False
                        pass
                $ cinematic = True
                Narrator "The moonlight reminds you how late it's getting. You head back to the corridor."
                $ cinematic = False
                jump Night1SneakDecision_Choices




        label Night1Atrium:
            scene atrium night
            play music "audio/Oratory_MASTER_LOOPED.mp3"
            $ Location = "Atrium"
            $ cinematic = True
            Narrator "The atrium is quiet on this night. Even the moons don't make a noise as they bob -- their light is dimmer than you remember."
            Narrator "You see the grate, even in the darkness. It's a dull silver, with repeating spiral patterns etched into it."
            Narrator "You hear steps in water... you know it waits for you."
            $ cinematic = False
            menu:
                "(Go to the grate)":
                    $ cinematic = True
                    Narrator "You shuffle close to it -- confident partly, that whatever it is is trapped down there."
                    Narrator "With bated breath, you lean over the edge."
                    $ cinematic = False
                    menu:
                        "Hello?":
                            play sound "audio/main_hall_gentle_water.mp3"
                            Narrator "{i}{b}slosh, slosh, slosh...{/b}{/i}"
                            show notalice sprite
                            NotAlice "Good evening..."
                            $ cinematic = True 
                            Narrator "You see the doll come into view, it's porcelain skin glistening as shafts of moonlight pierce the shadows."
                            Narrator "Its eyes, dark and empty, seem to follow your every movement."
                            $ cinematic = False
                            if Quest_NotAliceProgress == True:
                                NotAlice "You took your time. I was getting close to sending out a search party."
                                NotAlice "Did... you... Find... Inquisitor Alice?"
                                menu: 
                                    "No.":
                                        NotAlice "...past curfew... ancient place."
                                        $ cinematic = True
                                        Narrator "You can feel the dolls gaze on you. It feels like being watched by a viper."
                                        $ cinematic = False
                                        NotAlice "...past curfew... ancient place."
                                        $ cinematic = True
                                        Narrator "The doll lift it's hands, pointing a delicate finger past you and through the grate."
                                        Narrator "It's direction lands at the door."
                                        $ cinematic = False
                                        menu:
                                            "It's locked.":
                                                $ cinematic = True
                                                Narrator "The doll moves out of view. You hear footsteps moving away from you."
                                                Narrator "The moons return to their usual brightness... you squint, unaccustomed to the light."
                                                Narrator "You wait a while... but the doll doesn't return."
                                                Narrator "Still... you can't help but wonder if there's a way out you aren't considering."
                                                $ cinematic = False
                                                menu:
                                                    "Look around the Atrium again.":
                                                        $ cinematic = True
                                                        Narrator "You take a moment to survey the room. Moving cautiously through the dark towards the doorway."
                                                        Narrator "It's locked, you quickly realise."
                                                        Narrator "There is no way out, but you feel magic eminating from the lock itself."
                                                        Narrator "You realise, very quickly, that the lock is, like the moons, tied to something greater than a single spell."
                                                        Narrator "You're sure that there's some way of opening it."
                                                        play sound "audio/dialogue_information_default.mp3"
                                                        $ Flag_EntranceDoor1 = True
                                                        $ cinematic = False
                                                        menu:
                                                            "(Leave)":
                                                                hide notalice sprite
                                                                stop music
                                                                jump Night1SneakDecision_Choices
                                                    "(Leave)":
                                                        hide notalice sprite
                                                        stop music
                                                        jump Night1SneakDecision_Choices

                                            "No.":
                                                $ cinematic = True
                                                Narrator "The doll moves out of view. You hear footsteps moving away from you."
                                                Narrator "The moons return to their usual brightness... you squint, unaccustomed to the light."
                                                Narrator "You wait a while... but the doll doesn't return."
                                                $ cinematic = False
                                                menu:
                                                    "(Leave)":
                                                        hide notalice sprite
                                                        stop music
                                                        jump Night1SneakDecision_Choices

                            else:
                                NotAlice "What is it you desire..."
                                NotAlice "... from this place?"
                                menu:
                                    "I want to pass.":
                                        $ Quest_NotAliceProgress = True
                                        pass

                                    "I want to escape.":
                                        $ Quest_NotAliceProgress = True
                                        pass

                                    "I want nothing.":
                                        pass
                                NotAlice "Find... Inquisitor Alice... past curfew... I implore you... ancient place..."
                                $ cinematic = True
                                Narrator "The hand points behind you. To the entry way you first arrived through. The Summit's entrance."
                                $ cinematic = False
                                NotAlice "I must lock the doors behind you."
                                NotAlice "Find... Inquisitor Alice"
                                $ cinematic = True
                                Narrator "The doll dips down into the shadows once more -- arm retracting back as though an invisible puppetmaster yanked its string."
                                Narrator "You hear the sound of the water return once more."
                                Narrator "You stand, heart pounding in your chest."
                                Narrator "It's late. You know it's time to go to sleep."
                                Narrator "You return to the dormitory and get into the bed." 
                                Narrator "The fresh-linen scent hits you as you sink deeper in. Above you, the illusory stars twinkle and ebb ever so slowly toward a fake horizon. The world around you seems to fade..."
                                Narrator "But you can't help but wonder..." 
                                Narrator "...what was that?"
                                Narrator "And why do you still feel its gaze?"
                                menu:
                                    "(Leave)":
                                        stop music
                                        hide notalice sprite
                                        jump Night1SneakDecision_Choices


                "(Leave)":
                    stop music
                    jump Night1SneakDecision_Choices


        
        label Night1Atrium2: #another encounter with NotAlice
            scene atrium night
            $ cinematic = True
            Narrator "The Atrium is still magnificent. You see moonlight flicker through the stain glass window..."
            Narrator "But you also notice that the spell conjuring the two, twin moons, is in effect, casting faux-moonlight along the floor."
            Narrator "It's quiet. Quieter than you remember."
            Narrator "It takes you a moment to place the difference... the water, there's no longer the sound of running water."
            Narrator "All you hear is your footsteps, and the distant wind as it caresses the entrance."
            Narrator "Part of you wonders whether you could simply escape. Run off to a distant land."
            Narrator "Whether you could run into the woods and never think of the Summit, or the Scholomance again."
            Narrator "Or whether you'd simply die trying to descend."
            Narrator "Then you hear something break the silence."
            Narrator "A splash. The pitter-patter of feet against water. Sloshing like emerging from a bathtub."
            $ cinematic = False
            menu:
                "(Hide)":
                    $ cinematic = True
                    Narrator "You follow the noise, hiding behind a pillar. You still your breath."
                    $ cinematic = False
                    pass
                "(Stand your ground)":
                    $ cinematic = True
                    Narrator "You stay stood out in the open. You expect Eileen or Alice to emerge." 
                    Narrator "To toss you back to the Scholomance like a discarded ragdoll."
                    $ cinematic = False
                    pass
            $ cinematic = True
            Narrator "Your heart races. You try and find the source of the noise. Looking over at the large, green, window -- expecting at any moment see Eileen."
            play sound "audio/main_hall_gentle_water.mp3"
            Narrator "{i}{b}slosh, slosh, slosh.{/b}{/i}"
            Narrator "The noise moves to the moons. More specifically, to the grate below them. You listen as something pushes the grate up, and with effort, tries to push through."
            $ cinematic = False
            menu: 
                "(Investigate)":
                    $ cinematic = True
                    Narrator "You creep closer, noticing a white hand twist upward. Whatever is down there isn't small enough to squeeze through."
                    Narrator "You move closer. Crouching below the moons, gingerly shuffling until you can see something below."
                    Narrator "Staring up at you, is a silhouette. You can't make out features in the darkness, but you can hear it move in the shallow water."
                    $ cinematic = False
                    menu:
                        "Hello?":
                            $ cinematic = True
                            Narrator "You call out into the darkness, your voice barely above a whisper."
                            Narrator "The silhouette stirs. You feel it's eyes meet yours, you feel like prey."
                            Narrator "After a moment, as the moonlight twists and turns as the moons rotate, a shaft pushes into the darkness."
                            Narrator "Revealing another Doll. Alice. Trapped below the sewer grates."
                            show notalice sprite
                            $ cinematic = False
                            menu:
                                "Alice?":
                                    NotAlice "Good evening, pupils."
                                    NotAlice "I'm Inquisitor Alice."
                                    $ Flag_NotAliceMet = True
                                    menu: 
                                        "Are you alright?":
                                            NotAlice "Great... Great."
                                            NotAlice "The ceremony hasn't begun yet."
                                            menu: 
                                                "We had the ceremony earlier.":
                                                    $ cinematic = True
                                                    Narrator "The doll talks in an awkward cadence. It's almost detached as it looks up at you."
                                                    Narrator "The doll reaches up once more."
                                                    $ cinematic = False
                                                    NotAlice "We had the ceremony earlier."
                                                    NotAlice "What is it you desire..."
                                                    $ cinematic = True
                                                    Narrator "You become aware that the doll is asking something of you."
                                                    Narrator "The intensity of its gaze only strengthens as its eyes fixate on you."
                                                    $ cinematic = False
                                                    NotAlice "What is it you desire..."
                                                    NotAlice "... from this place?"
                                                    menu:
                                                        "I want to pass.":
                                                            $ Quest_NotAliceProgress = True
                                                            pass

                                                        "I want to escape.":
                                                            $ Quest_NotAliceProgress = True
                                                            pass

                                                        "I want nothing.":
                                                            pass
                                                    NotAlice "Find... Inquisitor Alice... past curfew... I implore you... ancient place..."
                                                    $ cinematic = True
                                                    Narrator "The hand points behind you. To the entry way you first arrived through. The Summit's entrance."
                                                    $ cinematic = False
                                                    NotAlice "I must lock the doors behind you."
                                                    NotAlice "Find... Inquisitor Alice"
                                                    $ cinematic = True
                                                    Narrator "The doll dips down into the shadows once more -- arm retracting back as though an invisible puppetmaster yanked its string."
                                                    Narrator "You hear the sound of the water return once more."
                                                    Narrator "You stand, heart pounding in your chest."
                                                    Narrator "It's late. You know it's time to go to sleep."
                                                    Narrator "You return to the dormitory and get into the bed." 
                                                    Narrator "The fresh-linen scent hits you as you sink deeper in. Above you, the illusory stars twinkle and ebb ever so slowly toward a fake horizon. The world around you seems to fade..."
                                                    Narrator "But you can't help but wonder..." 
                                                    Narrator "...what was that?"
                                                    Narrator "And why do you still feel its gaze?"
                                                    $ cinematic = False
                                                    $ Day0Night = False
                                                    $ AtriumVisitedDay1 = True
                                                    stop music
                                                    hide notalice sprite
                                                    jump Morning2Dorms
                                
                                "(Leave it there)":
                                    $ cinematic = True
                                    Narrator "Something in you stirs. You know this place isn't for you."
                                    Narrator "You turn, walking away from the moons, from the grate, and from whatever calls itself Alice beneath it."
                                    Narrator "You turn back for one last glimpse -- it's hand upreaching, glowing in the moonlight, as though it's holding the moons in place."
                                    Narrator "You leave the Atrium."
                                    $ cinematic = False
                                    stop music
                                    hide notalice sprite
                                    jump Night1SneakDecision_Choices

                "(Run)":
                    $ cinematic = True
                    Narrator "You turn and run, heart pounding in your chest."
                    Narrator "When you make it to the Atrium entrance, you take a look back to see a hand twisting below the moons."
                    Narrator "You run."
                    Narrator "You leave the Atrium."
                    $ cinematic = False
                    stop music
                    jump Night1SneakDecision_Choices






        label Night1AlchemyLab:
            scene corridor night
            $ cinematic = True
            Narrator "The alchemy lab door is unlocked, much to your surprise. As you look over your shoulder you see a distant light moving through the corridors."
            $ cinematic = False
            menu:
                "(Enter the Alchemy Lab)":
                    $ cinematic = True
                    Narrator "You sneak into the alchemy lab, locking the door behind you."
                    $ cinematic = False
                    jump Night1AlchemyLab_Choices
                
                "(Sneak back to the dorms)":
                    $ cinematic = True
                    Narrator "You carefully make your way back to the dorms, avoiding the light of whoever else is awake."
                    $ cinematic = False
                    stop music
                    jump Night1DecisionMenu


                "(Investigate)":
                    $ cinematic = True
                    Narrator "You extinguish your light, keeping a close eye on whoever else is roaming the halls."
                    Narrator "After a moment, you notice that it's Eileen. She makes her way towards the {b}Library{/b}."
                    $ Flag_EileenLibraryDay2 = True
                    Narrator "You know that you shouldn't follow her."
                    $ cinematic = False
                    menu:
                        "(Return to the dorms)":
                            stop music
                            jump Night1DecisionMenu

            
##### IM GONNA BE SO REAL HERE I CANNOT THINK ABOUT THE LOGIC OF IT IT JUST DOESNT MAKE SENSE RN!!!####

            label Night1AlchemyLab_Choices:
                scene alchemylab night
                play music "audio/Potion_Theme.mp3"
                $ Location = "Alchemy Lab"
                $ cinematic = True
                Narrator "The first thing to hit you is the smell of sterile chemicals. It's been cleaned, at least."
                Narrator "In the dim light, you notice how the potions and chemicals glow "
                $ cinematic = False
                if not potion_stolen or not Flag_PotionNotStolen or Flag_LockBreakerNeeded:
                    $ cinematic = True
                    Narrator "You notice a glass cupboard, filled to the brim with potions."
                    $ cinematic = False
                    menu:
                        "(Investigate)":
                            call Night1AlchemyLab_Potions from _call_Night1AlchemyLab_Potions
                            stop music
                            jump Night1SneakDecision_Choices

                else:
                    Narrator "You notice the missing potions."
                    Narrator "You can't shake the feeling that something isn't right here."
                    Narrator "You look at the remnants of a potion on the cauldron."
                    Narrator "You're certain it belonged to Melody."
                    Narrator "You move over and investigate it."
                    Narrator "It doesn't smell great, in fact, it smells like something dead, reanimated, tossed away, and then reboiled."
                    Narrator "You know there's nothing for you here."
                    $ cinematic = False
                    stop music
                    jump Night1SneakDecision_Choices

        



            label Night1AlchemyLab_Potions:
                $ cinematic = True
                Narrator "Inside a locked glass cupboard, you see rows and rows of potions. Each meticulously label still readable under a layer of dust."
                Narrator "You wonder when any of them were last used."
                $ cinematic = False
                menu:
                    "(Inspect the Potions)":
                        $ cinematic = True
                        Narrator "You ignore it."
                        Narrator "You notice a few you recognise from your time in the Scholomance."
                        Narrator "A potion of cleansing - soap, basically."
                        Narrator "A potion of sleepless night... which you can only assume is caffeine."
                        Narrator "A frog potion... whatever that is..."
                        Narrator "A lot of their labels are quite... undescriptive."
                        Narrator "You wonder why they're locked away, and if so, who has the key?"
                        $ cinematic = False
                        menu:
                            "(Magic: Unlock the Potions)" if Spell_Unlocking:
                                play sound "audio/reveal_magic_spell.mp3"
                                $ cinematic = True
                                Narrator "You focus on the lock, feeling the magic within you stir."
                                Narrator "With a few whispered words, the cabinet unlocks with a loud {b}{i}clunk{i}{b}. It's clearly not been touched in a while."
                                Narrator "Melody looks over at you. A knowing look in her eye."
                                $ Flag_MelodyCaughtPlayerStealing = True
                                Narrator "You know you can only take one. Any more and it'd be noticeable."
                                $ cinematic = False
                                menu: 
                                    "(Take the {b}Potion of Cleansing{/b})" if not "Potion of Cleansing" not in potion_stolen:
                                        $ potion_stolen.append("Potion of Cleansing")
                                        pass
                                    "(Take the {b}Potion of Frog Polymorph{/b})" if not "Potion of Frog Polymorph" not in potion_stolen:
                                        $ potion_stolen.append("Potion of Frog Polymorph")
                                        pass
                                    "(Take the {b}Potion of Sleepless Night{/b})" if not "Potion of Sleepless Night" not in potion_stolen:
                                        $ potion_stolen.append("Potion of Sleepless Night")
                                        pass
                                $ cinematic = True
                                Narrator "You slip the potion into your bag."
                                Narrator "A part of you feels a thrill of excitement."
                                $ cinematic = False
                                menu:
                                    "(Leave)":
                                        return

                            "(Test the Lock)":
                                $ cinematic = True
                                Narrator "You pull the handle -- it doesn't give."
                                $ cinematic = False
                                pass
                            
                            "(Smash the Lock)":
                                $ cinematic = True
                                Narrator "You kick the lock, but it doesn't budge."
                                $ Flag_LockBreakerNeeded = True
                                if Flag_HammerAcquired:
                                    Narrator "You pull the hammer out from your bag and bring it down on the lock."
                                    Narrator "With a loud {i}clunk{/i} it unbolts, the metal feeling loose."
                                    $ Flag_AlchemyLabLockBroken = True
                                    menu: 
                                        "(Take the {b}Potion of Cleansing{/b})" if not "Potion of Cleansing" not in potion_stolen:
                                            $ potion_stolen.append("Potion of Cleansing")
                                            pass
                                        "(Take the {b}Potion of Frog Polymorph{/b})" if not "Potion of Frog Polymorph" not in potion_stolen:
                                            $ potion_stolen.append("Potion of Frog Polymorph")
                                            pass
                                        "(Take the {b}Potion of Sleepless Night{/b})" if not "Potion of Sleepless Night" not in potion_stolen:
                                            $ potion_stolen.append("Potion of Sleepless Night")
                                            pass
                                    $ cinematic = True
                                    Narrator "You slip the potion into your bag."
                                    play sound "audio/clue_found_item_alert.mp3"
                                    Narrator "A part of you feels a thrill of excitement."
                                    $ cinematic = False
                                    $ Flag_LockBreakerUsed = True
                                    menu:
                                        "(Leave)":
                                            stop music
                                            return 


                                else:
                                    $ cinematic = True
                                    Narrator "You probably need some sort of tool..."
                                    $ Flag_PotionNotStolen = True
                                    $ cinematic = False
                                    menu:
                                        "(Leave)":
                                            return 

                            "(Leave it alone)":
                                return


        label Night1ArtificingLab:
            scene artificing lab night
            play music "audio/Marigold District_MASTER2_LOOPED.mp3"
            $ Location = "Artificing Lab"
            $ cinematic = True
            Narrator "You sneak into the {b}Artificing Lab{/b}. Dusty workstations and half-finished projects litter the room."
            Narrator "The smell of oil and metal fills the air..."
            Narrator "There's a light in the corner as Rex tinkers with something at a workstation."
            show rex sprite with dissolve
            Narrator "He doesn't seem surprised to be interrupted. He looks over his shoulder at you, and returns to whatever he's doing."
            hide rex sprite
            $ cinematic = False
            jump Night1ArtificingLab_Choices

            ### Flag_LockBreakerNeeded alerts the player to needing to take the hammer from the lab to smash the lock in the alchemy lab.

            label Night1ArtificingLab_Choices:
                $ cinematic = True
                Narrator "You wonder what you should do."
                $ cinematic = False
                menu:
                    "(Talk to Rex)":
                        $ cinematic = True
                        show rex sprite with dissolve
                        Narrator "Rex looks up as you approach, a smirk on his face."
                        $ cinematic = False
                        Rex "Surprised I'm here?"
                        Rex "I know you think I'm dumb, or lazy, or whatever. I can study, just to be clear. But I do it on my terms."
                        menu:
                            "And what terms would those be?":
                                Rex "If it's something that's actually useful in the real world, for one. Like artificing."
                                menu:
                                    "A lot of what we learn is useful.":
                                        Rex "They give you the sterilized version of everything because they only want you to do things their way."
                                        menu:
                                            "Who's 'they'?":
                                                Rex "The Mage Council. Now beat it, I have actual work to do."
                                                pass
                                            
                                    "I'm not judging.":
                                        Rex "You'd be the first in this kind of place."
                                        Rex "The teachers, the Council, they all teach us only what they want us to know. Take artificing." 
                                        Rex "Lots of real world uses like combat and sabotage. We hardly do any of that stuff. And you know what pisses me off about that?" 
                                        Rex "Artificing's pretty much the only thing I'm good at. It clicks. It's stupid {i}I{/i} have to do an exam for it."
                                        $ Affinity_Rex += 10
                                        pass

                            "I'm not judging...":
                                Rex "You'd be the first in this kind of place."
                                Rex "The teachers, the Council, they all teach us only what they want us to know. Take artificing." 
                                Rex "Lots of real world uses like combat and sabotage. We hardly do any of that stuff. And you know what pisses me off about that?" 
                                Rex "Artificing's pretty much the only thing I'm good at. It clicks. It's stupid {i}I{/i} have to do an exam for it."
                                $ Affinity_Rex += 10
                                pass

                        $ cinematic = True
                        Narrator "Rex turns his back to you again, tinkering away at a machine that glows and flashes over and over."
                        $ cinematic = False
                        menu:
                            "What are you making?":
                                if Affinity_Rex <= 30:
                                    Rex "Something to submit to the exam..."
                                    Rex "A mechanical plant waterer... I'm using some conjuration runes mixed with a mechanical body."
                                    Rex "A little artifice to water my plants."
                                    menu:
                                        "That sounds lazy.":
                                            Rex "Sometimes people don't feel like getting outta bed."
                                            Rex "I know I don't... wouldn't call it laziness but I'm not always up to face the world."
                                            Rex "We can't all be Melody or Tao."
                                            Rex "...psychos."
                                            pass

                                        "That sounds brilliant.":
                                            Rex "You think so?"
                                            Rex "Huh. First time someone's called me that."
                                            $ Affinity_Rex += 5
                                            pass

                                        "That sounds useful.":
                                            Rex "I'm hoping people think that."
                                            Rex "You can't have the blueprint. I haven't made one."
                                            menu: 
                                                "Damn.":
                                                    Rex "There's always an angle with Scholomance students.."
                                                    menu:
                                                        "Said like someone who {i}isn't{/i} one.":
                                                            Rex "A man can dream."
                                                            pass
                                                "I wasn't wanting one.":
                                                    Rex "Good."
                                                    pass
                        $ cinematic = True
                        Narrator "Rex looks back down at his artifice. You can tell he doesn't want to talk anymore."
                        $ cinematic = False
                        hide rex sprite
                        jump Night1ArtificingLab_Choices



                    "(Search the Lab)":
                        if Flag_LockBreakerNeeded == True:
                            call Night1ArtificingLab_SearchLock from _call_Night1ArtificingLab_SearchLock
                            return

                        else:
                            call Night1ArtificingLab_Search from _call_Night1ArtificingLab_Search
                            return
                        
                    "(Look for Machine Parts)" if artifice_options:
                        call Night1ArtificingLab_MachinePart from _call_Night1ArtificingLab_MachinePart
                        return

                        label Night1ArtificingLab_MachinePart:
                            $ cinematic = True
                            Narrator "You search through the lab for any machine parts. Your [artifice_options] creation doesn't need much, but it doens't help to look."
                            Narrator "You find a small hammer beside some refined, malleable metal."
                            Narrator "You pick them both up and place them in your bag."
                            Narrator "You also find a few scraps of wire and a small gear."
                            Narrator "You add those to your bag as well."
                            play sound "audio/clue_found_item_alert.mp3"
                            $ cinematic = False
                            $ Flag_ArtificeParts = True
                            $ Flag_HammerAcquired = True
                            return

                    "(Leave the {b}Artificing Lab{/b})":
                        stop music
                        jump Night1SneakDecision_Choices
                        
                            

                label Night1ArtificingLab_SearchLock:
                    $ cinematic = True
                    Narrator "You give the Artificing Lab a look over, rummaging through cupboards and stacks of metal."
                    Narrator "After a moment, you notice a small hammer beside a half-built contraption you don't quite know how to make heads or tails of."
                    Narrator "You collect the hammer."
                    $ Flag_LockBreakerNeeded = False
                    $ Flag_HammerAcquired = True
                    Narrator "You take a moment to feel the weight of it in your hands."
                    Narrator "You wonder what you can do with it."
                    $ cinematic = False
                    menu:
                        "...":
                            return
                    

                label Night1ArtificingLab_Search:
                    $ cinematic = True
                    Narrator "You give the Artificing Lab a look over, rummaging through cupboards and stacks of metal."
                    Narrator "You don't find anything useful."
                    $ cinematic = False
                    menu:
                        "...":
                            return








        label Night1Greenhouse:
            scene greenhouse night with fade
            play music "audio/project_w_concept_03_gmajor.mp3"
            $ Location = "Greenhouse"
            $ cinematic = True
            Narrator "You step into the greenhouse, the air thick with humidity and the scent of damp earth."
            Narrator "Feet on the cobble, you move through, smelling the scents of flowers as moonlight blends through a tinted skylight."
            Narrator "In the night, the Great Mage Tree seems to take on a light of its own."
            Narrator "The dark grooves of its bark pulling the moonlight in..."
            Narrator "You look up at the corridor surrounding you. You know if someone is out there you'll be spotted easily."
            Narrator "You extinguish your light... the moonlight is bright enough for you to see."
            $ cinematic = False
            jump Night1Greenhouse_Choices

            label Night1Greenhouse_Choices:
                $ cinematic = True
                Narrator "You wonder what you should do."
                $ cinematic = False
                menu:
                    "(Check on your Plants)":
                        call GreenhousePlants_Night1 from _call_GreenhousePlants_Night1
                        jump Night1Greenhouse_Choices

                        label GreenhousePlants_Night1:
                            if planted_seeds == "Winged Jasmine":
                                $ cinematic = True
                                Narrator "You inspect your Winged Jasmine... you're surprised at how much it has already grown."
                                Narrator "You suppose that the soil here must be incredibly fertile... or perhaps potent due to some Magecraft."
                                Narrator "The flower is blue and white, it's petals delicate..."
                                Narrator "... somehow you're reminded of fractured ice."
                                Narrator "It seems so delicate."
                                $ cinematic = False
                                menu:
                                    "Water it.":
                                        play sound "audio/watering_can_water_soil.mp3"
                                        $ cinematic = True
                                        Narrator "You carefully water the Winged Jasmine, ensuring not to drown it."
                                        Narrator "It seems perk up a little..."
                                        Narrator "Perhaps it was thirstier than you thought."
                                        $ Quality_Flower += 10
                                        $ cinematic = False
                                        return 
                                    "Poke it.":
                                        $ cinematic = True
                                        Narrator "You poke the flower."
                                        Narrator "A petal falls off."
                                        $ cinematic = False
                                        $ Quality_Flower -= 5
                                        return

                                    "Leave it be.":
                                        return


                            if planted_seeds == "Snapjaw Orchid":
                                $ cinematic = True
                                Narrator "You inspect your Snapjaw Orchid... it looks a little sad."
                                Narrator "Still, you're surprised at how much it's grown in such a short amount of time."
                                Narrator "It's a little creepy, a green flower that seems to have developed plant-teeth and pink, fleshy gums."
                                Narrator "It looks hungry."
                                $ cinematic = False
                                menu:
                                    "Water it.":
                                        play sound "audio/watering_can_water_soil.mp3"
                                        $ cinematic = True
                                        Narrator "You carefully water the Snapjaw Orchid, taking good care to only water the soil."
                                        Narrator "It seems to perk up slightly... though as you move closer to inspect it, its jaw closes."
                                        Narrator "Maybe it wants something else..."
                                        $ cinematic = False
                                        return
                                    "Feed it an insect." if book_collected = "The Woodwitch Guide to Home Gardening":
                                        play sound "audio/bug_add_to_inventory.mp3"
                                        $ cinematic = True
                                        Narrator "Remembering what you learned from [book_collected], you look around, finding a few dead insects inside a container left by Alice."
                                        Narrator "You remove a few, placing them on the Snapjaw Orchid's pink gums."
                                        Narrator "It's mouth closes and the plant begins to glow..."
                                        $ Quality_Flower += 10
                                        $ cinematic = False
                                        return

                                    "Poke it.":
                                        $ cinematic = True
                                        Narrator "You poke the Snapjaw Orchid..."
                                        Narrator "It's mouth hooks onto your finger, drawing blood."
                                        Narrator "You pull your finger out... it doesn't seem satisfied."
                                        $ cinematic = False
                                        return
                                    "Leave it be.":
                                        return

                                


                            if planted_seeds == "Moon Melon":
                                $ cinematic = True
                                Narrator "You inspect your Moon Melon, a large, round plant that glows a deep blue."
                                Narrator "You're surprised how much it's already grown."
                                Narrator "There's something pleasing about it... a scent... the shape..."
                                Narrator "You can't put your finger on it, but you enjoy looking at it."
                                $ cinematic = False
                                menu:
                                    "Water it.":
                                        play sound "audio/watering_can_water_soil.mp3"
                                        $ cinematic = True
                                        Narrator "You carefully water the Moon Melon..."
                                        Narrator "It seems to squirm away from the liquid."
                                        $ Quality_Flower -= 5
                                        $ cinematic = False
                                        return
                                    "Poke it.":
                                        $ cinematic = True
                                        Narrator "You poke the Moon Melon... it seems to bob like a balloon."
                                        Narrator "It clearly isn't doing much... yet you're enjoying yourself."
                                        $ cinematic = False
                                        return

                                    "Sprinkle salt along the soil." if book_collected = "The Illustrated Botanical":
                                        play sound "audio/fertilizer_add.mp3"
                                        $ cinematic = True
                                        Narrator "You collect the salt left by Alice on the table..."
                                        Narrator "... and sprinkle it along the soil."
                                        Narrator "The Moon Melon seems to react, eminating a soothing fragrance."
                                        $ Quality_Flower += 10
                                        $ cinematic = False
                                        return
                                    
                                    "Leave it be.":
                                        $ Quality_Flower += 5
                                        return


                            if planted_seeds == "Sanguine Lily":
                                $ cinematic = True
                                Narrator "You inspect your Sanguine Lily... it has already grown tremendously since you planted it."
                                Narrator "The flower itself is rather interesting... long, thin petals stretch out and curl like spindling fingers."
                                Narrator "And between the strands, like spiderwebs, are little red threads."
                                Narrator "You've never seen anything like it before."
                                $ cinematic = False 
                                menu:
                                    "Water it.":
                                        play sound "audio/watering_can_water_soil.mp3"
                                        $ cinematic = True
                                        Narrator "You carefully water the Sanguine Lily... it doesn't seem to care for it."
                                        $ cinematic = False
                                        return

                                    "Poke it.":
                                        $ cinematic = True
                                        Narrator "You poke the Sanguine Lily."
                                        Narrator "As expected, it latches onto your finger, drawing blood."
                                        Narrator "You feel drained as its teeth latch into your skin."
                                        Narrator "Instinctivly, you pull away."
                                        $ Quality_Flower += 5
                                        $ cinematic = False
                                        return

                                    "Prick your finger and feed it." if book_collected = "Carnivorous Plants of Viordia and their Many Applications":
                                        $ cinematic = True
                                        Narrator "You take a thin needle and prick your skin, letting a few dozen drops of blood drop down onto the plant."
                                        Narrator "It lifts its head up, as though to catch them as a dog catches a thrown treat."
                                        Narrator "It seems to enjoy it."
                                        $ cinematic = False
                                        $ Quality_Flower += 10
                                        return

                                    "Leave it be.":
                                        $ Quality_Flower -= 5
                                        return
                                

                            else:
                                return

                        
                    "(Investigate the Great Mage Tree)":
                        play sound "audio/dialogue_information_default.mp3"
                        $ cinematic = True
                        Narrator "You look up at the Great Mage Tree..."
                        Narrator "While you can {i}feel{/i} something else about it... it seems like a tree."
                        Narrator "Trying to push out, magically, is like pushing into a fog."
                        Narrator "There's nothing decipherable. It's like trying to see an individual raindrop in a torrent."
                        $ cinematic = False
                        jump Night1Greenhouse_Choices

                    "(Leave the {b}Greenhouse{/b})":
                        stop music
                        jump Night1SneakDecision_Choices





### Morning 2 ###


label Morning2Dorms:
    scene dormitory morning with fade
    play sound "audio/project_w_dorms.mp3"
    $ Day2Morning = True
    $ Location = "Dormitory"
    $ cinematic = True
    Narrator "You wake up to the artifice alarm. A squaking, mechanical bird. You had one in the Scholomance, too." 
    Narrator "You don't remember placing it there, yet all the other beds you see seem to have one."
    Narrator "You listen to the rain beat the windows, the {i}drip, drip, drip{/i} of the water calming you as you watch the ceiling rotate and unfurl."
    Narrator "Before you can close your eyes again, you hear the door."
    $ cinematic = False
    if Flag_LockBreakerUsed:
        $ cinematic = True
        show eileen sprite
        Narrator "Eileen enters. Her long robe trailing behind her. In her hand, shards of glass, hovering delicately above the skin."
        $ cinematic = False
        Eileen "I'd say good morning but it certainly is {i}not{i} one. One of you troglodytes decided to break into the potion storage..."
        Eileen "I hope you understand that while I'm a very tolerant woman... this sort of transgression will not be swept under the rug."
        Eileen "I {i}will{/i} find out who did it, and they will be punished."
        $ cinematic = True
        Narrator "You can see the annoyance in her eyes, never quite boiling into anger."
        Narrator "She takes a long look around the room."
        $ cinematic = False
        Eileen "Out of bed."
        $ cinematic = True
        Narrator "Eileen turns around, disappearing into the corridor."
        hide eileen sprite with dissolve
        $ cinematic = False
        jump Morning2Dorms_Choices
    
    else:
        $ cinematic = True
        Narrator "You place your feet on the ground... you should start your day."
        $ cinematic = False
        jump Morning2Dorms_Choices


    label Morning2Dorms_Choices:
        menu:
            "(Talk to Tao)" if not Flag_TaoDormitoryChat2:
                call BTAO06 from _call_BTAO06
                return
            
            "(Talk to Aria)" if not Flag_AriaDormitoryChat2:
                call BARI29 from _call_BARI29
                return

            "(Talk to Rex)" if not Flag_RexDormitoryChat2:
                call BREX06 from _call_BREX06
                return

            "(Talk to Melody)" if not Flag_MelodyDormitoryChat2:
                call BMEL012 from _call_BMEL012
                return

            "(Talk to Xander)" if not Flag_XanderDormitoryChat2:
                call BXAN099 from _call_BXAN099
                return

            "(Leave the Dormitory)":
                stop music
                jump Morning2Choices
            

    label BTAO06:
        $ cinematic = True
        Narrator "Tao lifts their gaze from a book to look at you. You can see the stress in their eyes... something's on their mind."
        $ cinematic = False
        Tao "What is it? I need to study, so unless you're on your way to the library we'll have to chat another time."
        $ Flag_TaoDormitoryDay2 = True
        $ cinematic = True
        Narrator "Tao turns to read their book again."
        $ Flag_TaoDormitoryChat2 = True
        $ cinematic = False
        return

    label BARI29:
        $ cinematic = True
        Narrator "Aria looks at you tiredly. You can tell that within a few moments they're going to get back in bed and go to sleep."
        $ cinematic = False
        $ Flag_AriaDormitoryChat2 = True
        Aria "I woke up today feeling really fuzzy in my head. Not like me at all. I think it must be anxiety over our exams..." 
        Aria "Maybe I should eat a bit more. I've got to focus..."
        menu:
            "You should probably wake up.":
                Aria "I should... but I'm just so sleepy..."
                Aria "..."
                menu:
                    "Aria?":
                        Aria "Huh, what?"
                        menu:
                            "Wake up.":
                                Aria "Fine... fine..."
                                return
            "I'll leave you to it...":
                return

    label BREX06:
        $ cinematic = True
        Narrator "Rex is staring out the window beside his bed. You can't see much through the fog."
        Narrator "It's a cozy morning, cold outside, toasty inside."
        Narrator "Under different circumstances, it might be a good day."
        $ cinematic = False
        $ Flag_RexDormitoryChat2 = True
        Rex "Did you know we can't leave school grounds after 9 pm? Eileen might as well be running a prison, which I'm sure she'd love to do."
        menu:
            "I've noticed." if Flag_EntranceDoor1 and Affinity_Rex >= 40:
                Rex "It's not the most secure..."
                menu:
                    "You escaped?":
                        Rex "There's a tunnel in the Greenhouse... if that damn tree moves it's big roots you can get into the sewer and exit into the forest."
                        $ Flag_GreenhouseTunnel = True
                        menu:
                            "How do you know this?":
                                Rex "I sent one of my artifice down there. C'mere..."
                                Narrator "Rex looks over your shoulder, checking to see if Eileen has gone. When the coast is clear, he tugs at your shirt to pull you to the window."
                                Narrator "It's steamed up a little -- cold morning air stark against the warmth of the dormitory."
                                Narrator "As he wipes away the fog, you see a little metal sheep at the edge of the forest."
                                Rex "How else did it get out there?"
                                Rex "You aren't gonna tell anyone, are you?"
                                menu:
                                    "Course not.":
                                        Rex "Good."
                                        return
            "Can't say I've tried.":
                Rex "Guess you're just fine with being here..."
                Rex "I was gonna talk to you about something, but honestly, best not."
                return

    label BMEL012:
        $ cinematic = True
        Narrator "Melody looks as though she's about to start her day."
        Narrator "When she sees you approach, she smiles and stops, books still under her arm."
        $ cinematic = False
        Melody "Morning… make sure you water your crops today..." 
        Melody "They need to be in good shape for the exams and we can't all just have naturally perfect flowers with no effort like Aria."
        $ Flag_MelodyDormitoryChat2 = True
        menu:
            "What do you mean?":
                Melody "I didn't mean it badly. Aria's just very good with plants." 
                Melody "Her affinity is nature and all that so she doesn't really need to put much work into the growing part."
                Melody "Anyway, did you need something? I'm just about to start my day."
                menu:
                    "I had a few questions...":
                        call melodyhub_main from _call_melodyhub_main_4
                        return
                    "Just checking in.":
                        return
            "I'll water them...":
                Melody "Great."
                return


    label BXAN099: 
        $ cinematic = True
        Narrator "You look around for Xander... he's nowhere to be seen."
        Narrator "As you inspect his quarters, you hear Aria, half-asleep, speaking to you."
        $ cinematic = False
        Aria "He left earlier... he looked pale."
        Aria "I don't think he's handling the stress very well..."
        Aria "Then again... he might just be like that in the mornings."
        Aria "{i}yawn{/i}..."
        $ Flag_XanderDormitoryChat2 = True
        return




label Morning2Choices:
    scene corridor morning with fade
    $ Location = "Corridor"
    play music "audio/project_w_scholomance_map.mp3"
    $ Day2Morning = True
    $ cinematic = True
    Narrator "You stand in the corridor, pondering where to go."
    $ cinematic = False
    menu:
        "(Go to the {b}Library{/b})" if Location != "Library":
            stop music
            jump Morning2Library

        "(Return to the {b}Dormitory{/b})" if Location != "Dormitory":
            stop music
            jump Morning2Dorms2

        "(Go to the {b}Alchemy Lab{/b})" if Location != "Alchemy Lab":
            stop music
            jump Morning2AlchemyLab

        "(Go to the {b}Atrium{/b})" if Location != "Atrium":
            stop music
            jump Morning2Atrium

        "(Go to the {b}Artificing Lab{/b})" if Location != "Artificing Lab":
            stop music
            jump Morning2ArtificingLab

        "(Go to the {b}Greenhouse{/b})" if Location != "Greenhouse":
            stop music
            jump Morning2Greenhouse
        
        "(Go to the {b}Courtyard{/b})" if Location != "Courtyard":
            stop music
            jump Morning2Courtyard

        "({b}Explore{/b})":
            $ result = renpy.random.randint(1, 7)
            if result == 1:
                stop music
                $ cinematic = True
                Narrator "Your exploration takes you to the {b}Library{/b}."
                $ cinematic = False
                jump Morning2Library
            if result == 2:
                stop music
                $ cinematic = True
                Narrator "After a long while in the Greenhouse, you find yourself back in your {b}bed{/b}."
                Narrator "You needed that."
                $ cinematic = False
                jump Morning2Dorms
            if result == 3:
                stop music
                $ cinematic = True
                Narrator "Your stroll leads you to the {b}Alchemy Lab{/b}."
                $ cinematic = False
                jump Morning2AlchemyLab
            if result == 4:
                stop music
                $ cinematic = True
                Narrator "You find yourself in the {b}Atrium{/b}."
                $ cinematic = False
                jump Morning2Atrium
            if result == 5:
                stop music
                $ cinematic = True
                Narrator "Perhaps you're feeling the urge to tinker as you've ended up in the {b}Artificing Lab{/b}."
                $ cinematic = False
                jump Morning2ArtificingLab
            if result == 6:
                stop music
                $ cinematic = True
                Narrator "You breathe in the fresh air of the {b}Greenhouse{/b}."
                $ cinematic = False
                jump Morning2Greenhouse
            if result == 7:
                stop music
                $ cinematic = True
                Narrator "You feel the wind cut to your bone as you stand in the {b}Courtyard{/b}, overlooking the forest."
                $ cinematic = False
                jump Morning2Courtyard

        "({b}Pass Time{/b})":
            $ Day1Morning = False
            $ cinematic = True
            Narrator "You go back to your dorm and take a nap."
            $ cinematic = False
            stop music
            $ Location = "Dormitory"
            jump Afternoon2DecisionMenu
        


label Morning2Library:
    scene library morning with fade
    $ Location = "Library"
    play music "audio/project_w_concept_04_fminor.mp3"
    $ cinematic = True
    Narrator "You enter the {b}Library{/b}. The morning light filters through the tall windows, illuminating the dust motes dancing in the air."
    Narrator "You hear pages turn, the tapping of a frustrated foot against millenia-aged wood."
    Narrator "You aren't sure whether it was there before, but you notice the floor is warped, as though the roots of the Great Mage Tree push beneath it."
    if Flag_ArchivesDiscovered:
        $ cinematic = True
        Narrator "You look over at the archives... wondering whether there is a way of entering you aren't aware of."
        Narrator "In the daylight, this place takes on a new form -- one of maroon, stuffy academia. White, nearly transparent pages..."
        Narrator "...holding millions of words written for {b}you{/b}."
        $ cinematic = False
        pass
    else:
        $ cinematic = True
        Narrator "You look around, noticing a door you haven't seen before."
        Narrator "It's gated, a great padlock stopping you."
        Narrator "Yet you can't help but approach it. There's an aura to it, as though moving towards honey-scented wood." 
        Narrator "You can feel great magic, as though spectral fingers are luring you closer. Twisting and spiralling."
        Narrator "You breathe it in..."
        Narrator "Whatever is behind the door is old magic."
        Narrator "Those scents, dewdrops on grass, honey warmed up, feel intrinsic to you."
        Narrator "They feel intimate."
        Narrator "More a part of you than your beating heart."
        Narrator "You look up at the label above the door."
        Narrator "{b}The Archives{/b}."
        $ Flag_ArchivesDiscovered = True
        $ cinematic = False
        menu:
            "(Try the door.)":
                $ cinematic = True
                Narrator "The chains are strong. The lock seems unbreakable."
                Narrator "You need a key."
                $ cinematic = False
                pass
            "(Leave it be.)": 
                $ cinematic = True
                Narrator "You kill the urge to move closer. You don't know where you find the determination."
                Narrator "You know there is nothing for you here."
                Narrator "Nothing yet..."
                $ cinematic = False
                pass
        pass
    $ cinematic = True
    show tao sprite
    Narrator "You notice Tao, their head in a book."
    Narrator "For once, the scowl they wear is dissolved into a look of tired resolve."
    Narrator "Perhaps they're struggling with a topic."
    show tao sprite with dissolve
    $ cinematic = False
    jump Morning2Library_Choices


label Morning2Library_Choices:
    $ cinematic = True
    Narrator "You wonder what you should do..."
    $ cinematic = False
    menu:
        "(Talk to Tao)":
            show tao sprite with dissolve
            $ cinematic = True
            Narrator "Tao's head is deep in a book as you approach, left hand taking notes in a tattered notebook."
            Narrator "You wonder whether they need a new one."
            Narrator "They barely look up at you as you approach."
            $ cinematic = False
            call Morning2LibraryTao_Choices from _call_Morning2LibraryTao_Choices
            hide tao sprite
            jump Morning2Library_Choices

            label Morning2LibraryTao_Choices:
                Tao "What?"
                menu:
                    "Just checking in.":
                        Tao "I'm clearly studying. Aren't you?"
                        menu:
                            "Not particularly...":
                                Tao "You and Xander seem to share a braincell then."
                                return

                            "Sure I am.":
                                Tao "Oddly enough I've found silence and concentration to greatly assist in studying."
                                Tao "You should try it."
                                Tao "Right now, actually. Go on. {i}Shoo{/i}."
                                menu:
                                    "(Leave Tao be)":
                                        return
                                    "(Linger)":
                                        Tao "..."
                                        $ Affinity_Tao -= 5
                                        return
                    "Nothing.":
                        Tao "Then why are you {i}here{/i}..."
                        menu:
                            "Just am.":
                                Tao "Ok..."
                                Tao "Can you leave?"
                                return
                            "You're a very mean person, you know that?":
                                Tao "I don't owe you my time. In fact, you owe me time at this point, for wasting so much of it."
                                Tao "I could've read a chapter ahead if you kept away from me."
                                Tao "I understand that you must be worried about failing but clinging to me does nothing but annoy me."
                                Tao "There's the empathy you clearly need."
                                $ Affinity_Tao -= 10
                                return


        "(Inspect the Archives Door)":
            $ cinematic = True
            Narrator "You inspect the archives door. Tugging on the gate -- it rattles, but holds firm."
            Narrator "You kneel to inspect the lock itself, as it doesn't seem to even have a keyhole."
            Narrator "As you touch it, you feel a spark as whatever enchantment is on the piece of artifice meets the latent magic on your skin."
            Narrator "You now know that it's artifice... and that there's an enchantment on it."
            Narrator "You wonder if there's some sort of spell you could use to break it."
            $ Flag_ArchivesArtifice = True
            $ cinematic = False
            jump Morning2Library_Choices

        "(Look for books on Botany)" if not book_collected:
            $ cinematic = True
            Narrator "You check for the books on botany, all of which seem somewhat tattered and dated."
            Narrator "Not by misuse, or a lack of care, but by age."
            Narrator "It seems as though every book in this library comes with it's own layer of dust."
            Narrator "It doesn't help that parts of the wooden floor seem to have warped over years, leaving some bookshelves angular."
            Narrator "Nevertheless, you poke around until -- trying not to disturb Tao, who seems very aware of your presence."
            Narrator "You find a few books that seem relevant to your needs."
            $ cinematic = False
            call Afternoon1Library_BotanyBooks from _call_Afternoon1Library_BotanyBooks
            return

        "(Leave the Library)":
            stop music
            $ cinematic = True
            Narrator "You leave the {b}Library{/b}."
            $ cinematic = False
            jump Morning2Choices


label Morning2Dorms2:
    scene dormitory morning with fade
    play music "audio/project_w_dorms.mp3"
    $ Location = "Dormitory"
    $ cinematic = True
    Narrator "You sit in your bed... the dormitory is empty except for you."
    if Flag_Day2PlantsWatered:
        Narrator "Maybe it's okay to take a break..."
        pass
    else:
        Narrator "Isn't it too early to rest?"
        pass
    $ cinematic = False
    menu:
        "(Rest)":
            jump Afternoon2Choices
        
        "(Explore more)":
            stop music
            jump Morning2Choices

label Morning2AlchemyLab:
    scene alchemy lab morning with fade
    play music "audio/Potion_Theme.mp3"
    $ Location = "Alchemy Lab"
    $ cinematic = True
    Narrator "You enter the {b}Alchemy Lab{/b}."
    Narrator "The scent of herbs and chemicals fills the air, mingling with the faint hum of magical energy."
    Narrator "In the dim light, you notice how the potions and chemicals glow, casting soft shadows along the walls."
    $ cinematic = False
    if not potion_stolen or not Flag_PotionNotStolen or Flag_LockBreakerNeeded:
        $ cinematic = True
        Narrator "You notice a glass cupboard, filled to the brim with potions."
        $ cinematic = False
        menu:
            "(Investigate)":
                call Night1AlchemyLab_Potions from _call_Night1AlchemyLab_Potions_1
                jump Morning2AlchemyLab_Choices
    else:
        $ cinematic = True
        Narrator "You notice the missing potions."
        Narrator "There's a twinge of guilt that seems to sit with you..."
        Narrator "You ignore it."
        $ cinematic = False
        jump Morning2AlchemyLab_Choices
    
    label Morning2AlchemyLab_Choices:
        $ cinematic = True
        Narrator "There's not much for you here."
        Narrator "Despite Melody usually being in the Alchemy Lab, she's nowhere to be seen."
        Narrator "You pay attention to the silence..."
        $ cinematic = False
        menu:
            "(Leave the {b}Alchemy Lab{/b})":
                stop music
                jump Morning2Choices



label Morning2Atrium:
    scene atrium morning with fade
    play music "audio/project_w_class.mp3"
    $ Location = "Atrium"
    $ cinematic = True
    Narrator "You step into the {b}Atrium{/b}."
    Narrator "Looking up at the skylight, you notice a few dozen birds roosting."
    Narrator "When you close your eyes and focus, you can hear them... their soft coo's resonating throughout the empty air."
    Narrator "It's oddly calming."
    Narrator "By the bench, you see Xander. Book closed on the seat beside him with his head in his hands. His legs are shaking."
    $ cinematic = False
    jump Morning2Atrium_Choices

    label Morning2Atrium_Choices:
        $ cinematic = True
        Narrator "You wonder what you should do."
        $ cinematic = False
        menu:
            "(Talk to Xander)":
                call Morning2AtriumXander_Choices from _call_Morning2AtriumXander_Choices
                jump Morning2Atrium_Choices

                label Morning2AtriumXander_Choices:
                    show xander sprite with dissolve
                    $ cinematic = True
                    Narrator "You approach Xander, and as you do, you see him begin to compose himself."
                    Narrator "He takes a breath and looks up at you, pushing a pained smile to his face."
                    $ cinematic = False
                    Xander "Hey pal. You need something?"
                    $ cinematic = True
                    Narrator "He smiles up at you."
                    $ cinematic = False
                    menu:
                        "Are you okay?":
                            Xander "Sure I am. Just... studying, y'know."
                            $ cinematic = True
                            Narrator "He takes a breath."
                            $ cinematic = False
                            Xander "Yeah. I know, I look worse than I am... I've not had much sleep."
                            Xander "Someone knocked on my window last night and then I heard, who I'm guessing was, Rex leaving and coming back..."
                            $ Flag_XanderWatched = True
                            Xander "I'm just a little on edge. I'll be fine."
                            menu:
                                "I'm here if you need to chat.":
                                    Xander "I don't wanna eat your time... but thanks."
                                    $ Affinity_Xander += 5
                                    Xander "Just... ignore me, you know? You've gotta focus, too. Don't let me drag you down."
                                    menu:
                                        "You aren't 'dragging me down'...":
                                            Xander "Right... right."
                                            $ cinematic = True
                                            Narrator "He looks down at his book. You wonder if he heard you."
                                            $ cinematic = False
                                            hide xander sprite
                                            return
                                        "Just take care of yourself, Xander.":
                                            Xander "Right... right."
                                            $ cinematic = True
                                            Narrator "He looks down at his book. You wonder if he heard you."
                                            $ cinematic = False
                                            hide xander sprite
                                            return
                                "You're scaring me a little...":
                                    Xander "Sorry."
                                    Xander "I'll be quieter..."
                                    $ Affinity_Xander -= 5
                                    hide xander sprite
                                    return
                                "Someone knocked on your window?":
                                    Xander "Yeah. Freaked me out."
                                    Xander "I didn't look or anything."
                                    Xander "It's probably Rex. Or maybe Eileen trying to give me a heart attack."
                                    hide xander sprite
                                    return

            "(Explore the Atrium)":
                $ cinematic = True
                Narrator "You take a moment to explore the {b}Atrium{/b}."
                Narrator "The soft cooing of the birds above is almost hypnotic."
                Narrator "You notice a few interesting plants growing in the corners, their leaves vibrant against the stone. You linger on the details."
                Narrator "Part of you wonders how such an isolated place became an exam hall. It seems almost comical."
                Narrator "Perhaps decades and decades ago, Mages used places like this under kinder circumstances."
                Narrator "No more submerged prisons... no more rules."
                Narrator "Just magic and the open sky. All the power in the world and nothing to limit them."
                Narrator "Can a world like that exist anymore? Or has it all become too complex to return to simplicity."
                Narrator "You look up at the birds, resting on an ancient skylight... have you traded one prison for another?"
                Narrator "The thought hurts to linger on."
                $ cinematic = False
                jump Morning2Atrium_Choices

            "(Enter the Courtyard)":
                $ cinematic = True
                Narrator "You decide to leave the {b}Atrium{/b}, the frosty courtyard calling out to you."
                $ cinematic = False
                stop music
                jump Morning2Courtyard

            "(Leave the Atrium)":
                $ cinematic = True
                Narrator "You decide to leave the {b}Atrium{/b}."
                $ cinematic = False
                jump Morning2Choices
                stop music
                return


label Morning2ArtificingLab:
    scene artificing lab morning
    play music "audio/Marigold District_MASTER2_LOOPED.mp3"
    $ cinematic = True
    Narrator "You enter the {b}Artificing Lab{/b}."
    Narrator "It smells like burning metal and sweat."
    Narrator "You notice Rex hammering away at some metal, an odd contraption in front of him."
    jump Morning2ArtificingLab_Choices

    label Morning2ArtificingLab_Choices:
        menu:
            "(Talk to Rex)":
                show rex sprite
                if Flag_GreenhouseTunnel:
                    call Morning2ArtificingLab_RexA from _call_Morning2ArtificingLab_RexA
                    jump Morning2ArtificingLab_Choices

                    label Morning2ArtificingLab_RexA:
                        $ cinematic = True
                        Narrator "Rex turns to look over at you as you approach."
                        Narrator "He doesn't seem as secretive of whatever he is working as usual."
                        $ cinematic = False
                        Rex "Hey... what's up?"
                        menu:
                            "What are you working on?":
                                Rex "Something to help me get through those roots."
                                Rex "I don't wanna cut the tree... Aria might kill me if she finds out."
                                Rex "So I was thinking of this contraption... basically expanding arms that can... painlessly... spread the roots enough for me to fit through."
                                menu:
                                    "You're escaping?":
                                        Rex "No. I'm {i}rebelling{/i}... I wanna see what's out there after dark. I'm not suicidal."
                                        Rex "If I end up trapped out there I'll probably get eaten by something on the mountain."
                                        Rex "Either way... it's nearly done. Just needs a few tweaks. Maybe I'll have it done for the Artificing Exam."
                                        $ cinematic = True
                                        Narrator "He picks up the screwdriver and starts working again. You make a few noises to get his attention... he ignores you."
                                        $ cinematic = False
                                        return 

                else:
                    $ cinematic = True
                    Narrator "Rex keeps his back to you."
                    Narrator "As you approach, he tosses a tattered blanket over whatever he was working on.."
                    $ cinematic = False
                    Rex "Hey... what's up?"
                    menu:
                        "What you working on?":
                            Rex "Don't worry about it."
                            menu:
                                "I'm interested.":
                                    Rex "It's not something I'm interested in showing you. Buzz off."
                                    $ Affinity_Rex -= 5
                                    hide rex sprite
                                    jump Morning2ArtificingLab_Choices

                        "You doing okay?":
                            Rex "No complaints... well, no new complaints. Still hate it here, still hate Eileen, still hate this whole damn system."
                            Rex "I'm tinkering along. Keeps me sane. That and plotting."
                            menu:
                                "Plotting?":
                                    Rex "You'll see."
                                    menu:
                                        "I'm not gonna get hurt, am I?":
                                            Rex "If you ask me dumb questions, yes."
                                            Rex "Anyway, I need to get back to this... do you mind?"
                                            menu:
                                                "(Leave him be)":
                                                    hide rex sprite
                                                    jump Morning2ArtificingLab_Choices
            
            
            "(Explore the Lab)":
                $ cinematic = True
                Narrator "You take a closer look around the {b}Artificing Lab{/b}."
                Narrator "There are various tools and materials scattered about, each with its own purpose."
                Narrator "There isn't much you havent's een before... this place is scarily similar to the lab no one uses back at the Scholomance."
                $ cinematic = False
                jump Morning2ArtificingLab_Choices
            
            
            "(Leave the {b}Artificing Lab{/b})":
                $ cinematic = True
                Narrator "You leave the {b}Artificing Lab{/b}."
                $ cinematic = False
                stop music
                jump Morning2Choices





label Morning2Greenhouse:
    scene greenhouse morning with fade
    play music "audio/project_w_concept_03_gmajor.mp3"
    $ Location = "Greenhouse"
    $ cinematic = True
    Narrator "You enter the {b}Greenhouse{/b}."
    $ cinematic = False
    show aria sprite at left with dissolve
    show melody sprite at right with dissolve
    if Flag_Morning2GreenhouseVisited:
        $ cinematic = True
        Narrator "Aria and Melody still tend to their plants, barely looking at one another."
        Narrator "They seem like strangers, but you get the feeling there's history there."
        $ cinematic = False
        jump Morning2Greenhouse_Choices
    
    else:
        $ cinematic = True
        Narrator "Immediately as you enter, you realise that both Melody and Aria are tending to their crops."
        Narrator "Melody is beneath the tree, looking over at Aria who is looking over a few dead plants."
        Narrator "Both of them look worried."
        $ cinematic = False
        Melody "Leave it, Aria. If you mess with them you'll get us {i}both{/i}..."
        Melody "In fact, you'll get all three of us in trouble."
        $ cinematic = True
        Narrator "Melody looks over at you... quickly after so does Aria. She stands up, her arms crossed."
        Narrator "You walk over to join them, which is where you get a better look at what Aria is doing."
        Narrator "A few flowers lay dead, their petals blackened."
        $ cinematic = False
        Aria "Xander's flowers didn't make it."
        Melody "Aria is thinking of fixing them. I told her that if Eileen finds out we'll get in trouble."
        Aria "But it would be so simple to fix!"
        Melody "Aria, it doesn't matter how simple it would be. You'd get yourself, Xander, and probably me implicated."
        Melody "{i}You'd{/i} probably get dragged in too, just for being here."
        Aria "I don't understand how they died. He planted them yesterday."
        Melody "It's Xander. He probably tried to feed it with weed killer."
        Aria "He's not stupid. He grew up on a farm, you know?"
        Melody "He grew up with like fifty brothers, they probably split the tasks between them."
        Melody "Aria, please, for the sake of everyone in this room, do not reanimate them. I don't want all my hard work to go to waste."
        Melody "Do you want us to go back to the Scholomance?"
        Aria "I don't want Xander to go back there."
        Melody "Xander will be fine! He'll get top marks in the combat exam, we all know that."
        Melody "All we're guarenteeing by fixing this is that the rest of us fail and he's guarenteed to fail."
        Aria "Eileen and Alice won't find out."
        Melody "They wake up earlier than us. Chances are they already {i}know{/i} Xander's plants died."
        $ cinematic = True
        Narrator "You watch Aria pull her hand back. Stepping away from the flowers to turn and look up at the tree."
        $ cinematic = False
        Aria "We're horrible."
        Aria "He's going to be devestated."
        Melody "He will be okay."
        Melody "You can't live your life caring this much about everyone else, Aria."
        Melody "Are you even studying? All this time pouring over your flowers that we both know can't die with you around..."
        Melody "You need to focus. Care less about others and more about doing well."
        Melody "You don't want to go back to the Scholomance. None of us do."
        Aria "..."
        hide aria sprite
        $ cinematic = True
        Narrator "Aria looks up at the tree. Melody sighs and turns to you."
        $ cinematic = False
        Melody "Maybe you can talk some sense into her."
        hide melody sprite
        $ Flag_Morning2GreenhouseVisited = True
        jump Morning2Greenhouse_Choices
        
### melody is just tending to her plants but mentions that it looks like Xander's crops died -- Aria offers to fix them but Melody convinces her not to to save both of their grades.

    label Morning2Greenhouse_Choices:
        menu:
            "(Tend to your plants)" if not Flag_Day2PlantsWatered:
                call Morning1Greenhouse_Plants from _call_Morning1Greenhouse_Plants
                $ Flag_Day2PlantsWatered = True
                jump Morning2Greenhouse_Choices
                
                label Morning1Greenhouse_Plants:
                    $ cinematic = True                    
                    Narrator "You take a moment, kneeling over your plot."
                    $ cinematic = False
                    if "Winged Jasmine" in planted_seeds:
                        $ cinematic = True
                        Narrator "You inspect your Winged Jasmine... you're surprised at how much it has already grown."
                        Narrator "You suppose that the soil here must be incredibly fertile... or perhaps potent due to some Magecraft."
                        Narrator "The flower is blue and white, it's petals delicate..."
                        Narrator "...somehow you're reminded of fractured ice."
                        Narrator "It seems so delicate."
                        $ cinematic = False
                        menu:
                            "Water it.":
                                play sound "audio/watering_can_pick_up.mp3"
                                play sound "audio/watering_can_water_soil.mp3"
                                play sound "audio/watering_can_put_down.mp3"
                                $ cinematic = True
                                Narrator "You carefully water the Winged Jasmine, ensuring not to drown it."
                                Narrator "It seems perk up a little..."
                                Narrator "Perhaps it was thirstier than you thought."
                                $ Quality_Flower += 10
                                $ cinematic = False
                                return 
                            "Poke it.":
                                $ cinematic = True
                                Narrator "You poke the flower."
                                Narrator "A petal falls off."
                                $ cinematic = False
                                $ Quality_Flower -= 5
                                return

                            "Leave it be.":
                                return


                    if "Snapjaw Orchid" in planted_seeds:
                        $ cinematic = True
                        Narrator "You inspect your Snapjaw Orchid... it looks a little sad."
                        Narrator "Still, you're surprised at how much it's grown in such a short amount of time."
                        Narrator "It's a little creepy, a green flower that seems to have developed plant-teeth and pink, fleshy gums."
                        Narrator "It looks hungry."
                        $ cinematic = False
                        menu:
                            "Water it.":
                                play sound "audio/watering_can_pick_up.mp3"
                                play sound "audio/watering_can_water_soil.mp3"
                                play sound "audio/watering_can_put_down.mp3"
                                $ cinematic = True
                                Narrator "You carefully water the Snapjaw Orchid, taking good care to only water the soil."
                                Narrator "It seems to perk up slightly... though as you move closer to inspect it, its jaw closes."
                                Narrator "Maybe it wants something else..."
                                $ cinematic = False
                                return
                            "Feed it an insect." if book_collected == "The Woodwitch Guide to Home Gardening":
                                play sound "audio/bug_add_to_inventory.mp3"
                                $ cinematic = True
                                Narrator "Remembering what you learned from [book_collected], you look around, finding a few dead insects inside a container left by Alice."
                                Narrator "You remove a few, placing them on the Snapjaw Orchid's pink gums."
                                Narrator "It's mouth closes and the plant begins to glow..."
                                $ Quality_Flower += 10
                                $ cinematic = False
                                return

                            "Poke it.":
                                $ cinematic = True
                                Narrator "You poke the Snapjaw Orchid..."
                                Narrator "It's mouth hooks onto your finger, drawing blood."
                                Narrator "You pull your finger out... it doesn't seem satisfied."
                                $ cinematic = False
                                return
                            "Leave it be.":
                                return


                    if "Moon Melon" in planted_seeds:
                        $ cinematic = True
                        Narrator "You inspect your Moon Melon, a large, round plant that glows a deep blue."
                        Narrator "You're surprised how much it's already grown."
                        Narrator "There's something pleasing about it... a scent... the shape..."
                        Narrator "You can't put your finger on it, but you enjoy looking at it."
                        $ cinematic = False
                        menu:
                            "Water it.":
                                $ cinematic = True
                                Narrator "You carefully water the Moon Melon..."
                                play sound "audio/watering_can_pick_up.mp3"
                                play sound "audio/watering_can_water_soil.mp3"
                                play sound "audio/watering_can_put_down.mp3"
                                Narrator "It seems to squirm away from the liquid."
                                $ Quality_Flower -= 5
                                $ cinematic = False
                                return
                            "Poke it.":
                                $ cinematic = True
                                Narrator "You poke the Moon Melon... it seems to bob like a balloon."
                                Narrator "It clearly isn't doing much... yet you're enjoying yourself."
                                $ cinematic = False
                                return

                            "Sprinkle salt along the soil." if book_collected == "The Illustrated Botanical":
                                $ cinematic = True
                                Narrator "You collect the salt left by Alice on the table..."
                                Narrator "... and sprinkle it along the soil."
                                play sound "audio/fertilizer_add.mp3"
                                Narrator "The Moon Melon seems to react, eminating a soothing fragrance."
                                $ Quality_Flower += 10
                                $ cinematic = False
                                return
                            
                            "Leave it be.":
                                $ Quality_Flower += 5
                                return


                    if "Sanguine Lily" in planted_seeds:
                        $ cinematic = True
                        Narrator "You inspect your Sanguine Lily... it has already grown tremendously since you planted it."
                        Narrator "The flower itself is rather interesting... long, thin petals stretch out and curl like spindling fingers."
                        Narrator "And between the strands, like spiderwebs, are little red threads."
                        Narrator "You've never seen anything like it before."
                        $ cinematic = False 
                        menu:
                            "Water it.":
                                play sound "audio/watering_can_pick_up.mp3"
                                play sound "audio/watering_can_water_soil.mp3"
                                play sound "audio/watering_can_put_down.mp3"
                                $ cinematic = True
                                Narrator "You carefully water the Sanguine Lily... it doesn't seem to care for it."
                                $ cinematic = False
                                return

                            "Poke it.":
                                $ cinematic = True
                                Narrator "You poke the Sanguine Lily."
                                Narrator "As expected, it latches onto your finger, drawing blood."
                                Narrator "You feel drained as its teeth latch into your skin."
                                Narrator "Instinctivly, you pull away."
                                $ Quality_Flower += 5
                                $ cinematic = False
                                return

                            "Prick your finger and feed it." if book_collected == "Carnivorous Plants of Viordia and their Many Applications":
                                $ cinematic = True
                                Narrator "You take a thin needle and prick your skin, letting a few dozen drops of blood drop down onto the plant."
                                Narrator "It lifts its head up, as though to catch them as a dog catches a thrown treat."
                                Narrator "It seems to enjoy it."
                                $ cinematic = False
                                $ Quality_Flower += 10
                                return

                            "Leave it be.":
                                $ Quality_Flower -= 5
                                return
                        

                    else:
                        return

            "(Talk to Melody)":
                show melody sprite with dissolve
                $ cinematic = True
                Narrator "You approach Melody, who is tending to a small plant."
                $ cinematic = False
                Melody "Glad you turned up... I sort of needed someone to help with Aria."
                menu:
                    "You seem stressed about Xander's plants.":
                        Melody "I don't mean to be... well, mean."
                        Melody "I just don't want to risk everything over Xander not checking on his crops."
                        Melody "It's nothing personal, if anything, I'm just trying to stop Aria from getting implicated."
                        Melody "You understand, right?"
                        menu:
                            "I guess.":
                                Melody "Glad to hear it... I just don't think it's worth the risk."
                                Melody "Xander will be fine. I'm certain of that. If he wasn't, I'd stick my neck out for him."
                                Melody "But right now, he can recover. We're early enough on."
                                Melody "We have days to the potion exam. He can plant something else, I'm sure."
                                hide melody sprite
                                return
                            "Not really.":
                                Melody "Well, maybe when I'm {i}not{/i} around, you and Aria should restore them."
                                Melody "I really want to pass. I don't want to risk this."
                                $ cinematic = True
                                Narrator "You see that she's pleading."
                                Narrator "You should leave the topic alone."
                                $ cinematic = False
                                hide melody sprite
                                return
                                


                    "I have some questions...":
                        call melodyhub_main from _call_melodyhub_main_5
                        return

                    "(Leave)":
                        stop music
                        jump Morning2Greenhouse_Choices



            "(Talk to Aria)":
                show aria sprite with dissolve
                $ cinematic = True
                Narrator "Aria steps towards you as you approach. Her arms are twisted around her body like she's embracing herself."
                $ cinematic = False
                Aria "Hmm? Did you need to talk?"
                call Morning2Greenhouse_Aria from _call_Morning2Greenhouse_Aria
                hide aria sprite
                jump Morning2Greenhouse_Choices

                label Morning2Greenhouse_Aria:
                    menu:
                        "(Parting the Roots of the Mage Tree)" if Flag_GreenhouseTunnel and not Flag_GreenhouseTunnelUnlocked:
                            call AriaOpensGreenhouseTunnel from _call_AriaOpensGreenhouseTunnel
                            jump Morning2Greenhouse_Aria

                            label AriaOpensGreenhouseTunnel:
                                Aria "Is it in the way of something?"
                                menu:
                                    "A pipe leading out of the school.":
                                        Aria "Oh..."
                                        pass
                                Aria "I mean I can talk to him... He doesn't talk back but he reacts."
                                menu:
                                    "Can't you make him move?":
                                        Aria "Why would I? If someone shoved you aside you wouldn't like that."
                                        Aria "I'll ask."
                                        Aria "But I can't promise anything."
                                        Aria "I'll ask him later."
                                        $ Flag_GreenhouseTunnelUnlocked = True
                                        return 
                                    "Sure, please ask him.":
                                        Aria "I will later."
                                        $ Flag_GreenhouseTunnelUnlocked = True
                                        return

                        "(Xander's Plants)":
                            Aria "I found them like that."
                            Aria "When Melody got here she asked me if {i}I{/i} did it."
                            Aria "As if I'd ever do something like that."
                            Aria "Xander's going to be heartbroken. I'll break the news to him when he gets here."
                            menu:
                                "Are you going to fix them?":
                                    Aria "I want to."
                                    Aria "But Melody's right. If I interfere with them I'm going to sabotague all of us."
                                    Aria "Eileen's probably already seem it all. Either her or one of Alice's copies."
                                    pass
                            Aria "I hate it."
                            $ cinematic = True
                            Narrator "Aria looks back down at the flowers. You notice one begin to perk up, the soft dark frailness dissipating."
                            Narrator "A moment later, you see her turn from it, and the flower returns to it's former state."
                            $ cinematic = False
                            jump Morning2Greenhouse_Aria
                        
            
                        "(I have other questions)":
                            call ariahub_main from _call_ariahub_main
                            jump Morning2Greenhouse_Aria

                        "(Nothing to say.)":
                            hide aria sprite
                            return

            "(Leave the Greenhouse)":
                $ cinematic = True
                Narrator "You leave the {b}Greenhouse{/b}."
                $ cinematic = True
                stop music
                jump Morning2Choices





label Morning2Courtyard:
    scene courtyard morning
    play music "audio/project_w_concept_03_gmajor.mp3"
    $ cinematic = True
    Narrator "You enter the {b}Courtyard{/b}."
    Narrator "The morning dew hits you as you step through the grass."
    Narrator "The cold wind sends a chill down your spine but you stand still, staring out from the top of the mountain, along the green landscape."
    Narrator "Forests for as far as you can see. You wonder where your home is?"
    Narrator "You were too young to know the place on the map..."
    Narrator "You're sure you'll see it again, soon."
    $ cinematic = False
    $ Location = "Courtyard"
    jump Morning2Courtyard_Choices

    label Morning2Courtyard_Choices:
        $ cinematic = True
        Narrator "What do you want to do?"
        $ cinematic = False
        menu:
            "(Investigate outside the dorms)" if Flag_XanderWatched:
                $ cinematic = True
                Narrator "You remember what Xander told you... it sticks with you."
                $ cinematic = False
                call Morning2Courtyard_Dorms from _call_Morning2Courtyard_Dorms
                jump Morning2Courtyard_Choices

                label Morning2Courtyard_Dorms:
                    $ cinematic = True
                    Narrator "You walk over to the dormitory windows."
                    Narrator "You notice some handprints on the window, as though something has been outside, looking in."
                    Narrator "You look over your shoulder at the forest. There's a small parting, where something came through."
                    Narrator "Squinting, you make out a set of eyes."
                    Narrator "There's something in the forest." 
                    Narrator "Watching you."
                    $ cinematic = False
                    show alice sprite:
                        xalign 0.5 
                        yalign 0.3  
                    Alice "Pupil, you shouldn't be this far out of the courtyard."
                    $ cinematic = True
                    Narrator "The doll looks at you, seemingly oblivious to your fear."
                    $ cinematic = False
                    Alice "Move back to the courtyard, please."
                    $ cinematic = True
                    Narrator "You do as she says, following her closely." 
                    Narrator "As you get back to the Courtyard, you feel the eyes on you dissipate."
                    hide alice sprite
                    $ cinematic = False
                    $ Flag_TheWatcher = True
                    return

            "(Explore the Courtyard)":
                $ cinematic = True
                Narrator "You take a moment to explore the {b}Courtyard{/b}."
                Narrator "You notice a few flowers blooming in the cracks of the stone path."
                Narrator "Their colors are vibrant against the gray stones."
                Narrator "You can't help but feel a sense of calm wash over you."
                Narrator "As you look out over the mountain, you wonder how many mages have stood where you're stood."
                Narrator "Eileen... Alice... the council."
                Narrator "The older students who one day disappered from the Scholomance... {i}freed{/i}, you hoped."
                Narrator "You wonder what they're doing now. Where over the horizon they ended up."
                $ cinematic = False
                jump Morning2Courtyard_Choices

            "(Leave the {b}Courtyard{/b})":
                $ cinematic = True
                Narrator "You leave the {b}Courtyard{/b}."
                $ cinematic = True
                stop music
                jump Morning2Choices


### Afternoon 2 ###
label Afternoon2Choices:
    scene dormitory afternoon
    play music "audio/project_w_dorms.mp3"
    $ Day2Morning = False
    $ Day2Afternoon = True
    $ Location = "Dormitory"
    $ cinematic = True
    Narrator "You sit at the end of your bed. The afternoon sun streams through the window, casting a warm glow over the room."
    Narrator "You must've fallen asleep..."
    $ cinematic = False
    jump Afternoon2Choices_Menu

label Afternoon2Choices_Menu:
    $ cinematic = True
    Narrator "You wonder what you should do."
    $ cinematic = False
    menu:
        "(Go to the {b}Library{/b})":
            stop music
            jump Afternoon2Library

        "(Return to the {b}Dormitory{/b})" if Location != "Dormitory":
            stop music
            jump Afternoon2Dorms

        "(Go to the {b}Alchemy Lab{/b})" if Location != "Alchemy Lab":
            stop music
            jump Afternoon2AlchemyLab

        "(Go to the {b}Atrium{/b})" if Location != "Atrium":
            stop music
            jump Afternoon2Atrium

        "(Go to the {b}Artificing Lab{/b})" if Location != "Artificing Lab":
            stop music
            jump Afternoon2ArtificingLab

        "(Go to the {b}Greenhouse{/b})" if Location != "Greenhouse":
            stop music
            jump Afternoon2Greenhouse
        
        "(Go to the {b}Courtyard{/b})" if Location != "Courtyard":
            stop music
            jump Afternoon2Courtyard

        "({b}Explore{/b})":
            stop music
            $ result = renpy.random.randint(1, 7)
            if result == 1:
                $ cinematic = True
                Narrator "Your exploration takes you to the {b}Library{/b}."
                $ cinematic = False
                jump Afternoon2Library
            if result == 2:
                $ cinematic = True
                Narrator "You decide to stay in the dormitory..."
                $ cinematic = False
                jump Afternoon2Dorms
            if result == 3:
                $ cinematic = True
                Narrator "Your stroll leads you to the {b}Alchemy Lab{/b}."
                $ cinematic = False
                jump Afternoon2AlchemyLab
            if result == 4:
                $ cinematic = True
                Narrator "You find yourself in the {b}Atrium{/b}."
                $ cinematic = False
                jump Afternoon2Atrium
            if result == 5:
                $ cinematic = True
                Narrator "Perhaps you're feeling the urge to tinker as you've ended up in the {b}Artificing Lab{/b}."
                $ cinematic = False
                jump Afternoon2ArtificingLab
            if result == 6:
                $ cinematic = True
                Narrator "You breathe in the fresh air of the {b}Greenhouse{/b}."
                $ cinematic = False
                jump Afternoon2Greenhouse
            if result == 7:
                $ cinematic = True
                Narrator "You feel the wind cut to your bone as you stand in the {b}Courtyard{/b}, overlooking the forest."
                $ cinematic = False
                jump Afternoon2Courtyard

        "({b}Pass Time{/b})":
            $ Day1Morning = False
            $ cinematic = True
            Narrator "You go back to your dorm and take a nap."
            $ cinematic = False
            $ Location = "Dormitory"
            jump Night2DecisionMenu





label Afternoon2Library: #empty
    scene library afternoon
    play music "audio/project_w_concept_04_fminor.mp3"
    $ Location = "Library"
    $ cinematic = True
    Narrator "You enter the {b}Library{/b}. The scent of old books and tomes fills the air."
    Narrator "You don't hear anyone else here."
    $ cinematic = False
    if Flag_ArchivesDiscovered:
        $ cinematic = True
        Narrator "You look over at the archives... wondering whether there is a way of entering you aren't aware of."
        Narrator "In the afternoon light, this place takes on a new form -- one of maroon, stuffy academia. White, nearly transparent pages..."
        Narrator "...holding millions of words written for {b}you{/b}."
        $ cinematic = False
        pass
    else:
        $ cinematic = True
        Narrator "You look around, noticing a door you haven't seen before."
        Narrator "It's gated, a great padlock stopping you."
        Narrator "Yet you can't help but approach it. There's an aura to it, as though moving towards honey-scented wood." 
        Narrator "You can feel great magic, as though spectral fingers are luring you closer. Twisting and spiralling."
        Narrator "You breathe it in..."
        Narrator "Whatever is behind the door is old magic."
        Narrator "Those scents, dewdrops on grass, honey warmed up, feel intrinsic to you."
        Narrator "They feel intimate."
        Narrator "More a part of you than your beating heart."
        Narrator "You look up at the label above the door."
        Narrator "{b}The Archives{/b}."
        $ Flag_ArchivesDiscovered = True
        $ cinematic = False
        menu:
            "(Try the door.)":
                $ cinematic = True
                Narrator "The chains are strong. The lock seems unbreakable."
                Narrator "You need a key."
                $ cinematic = False
                pass
            "(Leave it be.)": 
                $ cinematic = True
                Narrator "You kill the urge to move closer. You don't know where you find the determination."
                Narrator "You know there is nothing for you here."
                Narrator "Nothing yet..."
                $ cinematic = False
                pass
        pass
    $ cinematic = True
    Narrator "You take a breath."
    $ cinematic = False
    jump Afternoon2Library_Choices

    label Afternoon2Library_Choices:
        $ cinematic = True
        Narrator "You wonder what you should do..."
        $ cinematic = False
        menu:
            "(Inspect the Archives Door)":
                $ cinematic = True
                Narrator "You inspect the archives door. Tugging on the gate -- it rattles, but holds firm."
                Narrator "You kneel to inspect the lock itself, as it doesn't seem to even have a keyhole."
                Narrator "As you touch it, you feel a spark as whatever enchantment is on the piece of artifice meets the latent magic on your skin."
                Narrator "You now know that it's artifice... and that there's an enchantment on it."
                Narrator "You wonder if there's some sort of spell you could use to break it."
                $ Flag_ArchivesArtifice = True
                $ cinematic = False
                jump Afternoon2Library_Choices

            "(Look for books on Botany)" if not book_collected:
                $ cinematic = True
                Narrator "You check for the books on botany, all of which seem somewhat tattered and dated."
                Narrator "Not by misuse, or a lack of care, but by age."
                Narrator "It seems as though every book in this library comes with it's own layer of dust."
                Narrator "It doesn't help that parts of the wooden floor seem to have warped over years, leaving some bookshelves angular."
                Narrator "Nevertheless, you poke around until -- trying not to disturb Tao, who seems very aware of your presence."
                Narrator "You find a few books that seem relevant to your needs."
                $ cinematic = False
                call Afternoon1Library_BotanyBooks from _call_Afternoon1Library_BotanyBooks_1
                return

            "(Leave the Library)":
                $ cinematic = True
                Narrator "You leave the {b}Library{/b}."
                stop music
                jump Afternoon2Choices_Menu




label Afternoon2Dorms:#Melody is in the dorms, she feels a bit under the weather so she's taking a break (she's sabotaging alarms) # talks to you about Flag_TeachersLoungeQuestioned
    scene dormitory afternoon

    $ cinematic = True
    if Location not "Dormitory":
        Narrator "You head back to the {b}Dormitory{/b}."
        pass
    else:
        Narrator "You stay in the {b}Dormitory{/b}."
        pass
    Narrator "The afternoon light, despite the cold, feels heavy through the windowpanes."
    Narrator "You feel the weight of exams melt as you sit at your bed."
    show melody sprite with dissolve
    Narrator "After a few moments, you see Melody emerge from behind her bed curtain."
    hide melody sprite
    $ Location = "Dormitory"
    $ cinematic = False
    jump Afternoon2Dorms_Choices
    
    label Afternoon2Dorms_Choices:
        $ cinematic = True
        Narrator "You wonder what you should do..."
        $ cinematic = False
        menu:
            "(Talk to Melody)":
                show melody sprite with dissolve
                $ cinematic = True
                Narrator "Melody looks upbeat as you approach. You can tell she's tired, but she still forces a smile."
                $ cinematic = False
                Melody "You feeling under the weather, too? I thought I'd let myself rest this afternoon..."
                jump Afternoon2Melody_Choices
                label Afternoon2Melody_Choices:
                    menu:
                        "How are you?":
                            Melody "I {i}said{/i} 'under the weather' but I guess it's more like... lethargic."
                            Melody "I guess I've not had a break... I can afford it."
                            Melody "You should do the same. I've seen you running around all day... have a sit down."
                            jump Afternoon2Melody_Choices
                        "Where do Alice & Eileen stay?" if Flag_TeachersLoungeQuestioned:
                            Melody "The teachers lounge... I'm pretty sure. It's up the stairs in the upstairs corridor Directly across from the dorms."
                            Melody "It's always locked."
                            $ Flag_DiscoveredTeachersLounge = True
                            Melody "I didn't check.."
                            Melody "But I saw them go up there yesterday."
                            Melody "You know... It's odd to have teachers with us so often..."
                            Melody "Back at the Scholomance they sort of left us to our own devices..." 
                            Melody "I suppose they didn't want to risk spending time with a bunch of unstable mages."
                            Melody "It sort of feels as though we're under a microscope. Especially with Alice's dolls around the place."
                            menu:
                                "...":
                                    jump Afternoon2Melody_Choices
                                "What do you think is in there?":
                                    Melody "The teacher's lounge? Probably a kitchen... a few beds..."
                                    Melody "It's a room for {i}people{/i} so at the end of the day it's most like something boring."
                                    jump Afternoon2Melody_Choices
                        "(Leave)":
                            hide melody sprite
                            jump Afternoon2Dorms_Choices


            "(Look out the window)" if Flag_TheWatcher:
                $ cinematic = True
                Narrator "Remembering whatever you saw in the forest, you decide to part the curtain behind your bed and peer through the window..."
                Narrator "From the safety of your dormitory, you stare out into the forest... the damp grass gleaming as wind ripples through it."
                Narrator "You see nothing watching you."
                Narrator "Yet, as you peer into the forest, you still feel like something is looking back at you."
                $ cinematic = False
                jump Afternoon2Dorms_Choices

            "(Take a nap)":
                $ cinematic = True
                Narrator "You pull the blanket over your head... the closed curtains around you forming a sanctuary."
                Narrator "You drift off..."
                $ cinematic = False
                jump Night2Choices
            
            "(Leave the {b}Dormitory{/b})":
                stop music
                jump Afternoon2Choices_Menu




label Afternoon2AlchemyLab: #Tao is trying to perfect a potion for the exam -- it's going badly. They are stressed.
    scene alchemy lab afternoon
    play music "audio/Potion_Theme.mp3"
    $ Location = "Alchemy Lab"
    $ cinematic = True
    Narrator "You enter the {b}Alchemy Lab{/b}."
    Narrator "The scent of herbs and chemicals fills the air, mingling with the faint hum of magical energy."
    Narrator "In the dim light, you notice how the potions and chemicals glow, casting soft shadows along the walls."
    show tao sprite with dissolve
    Narrator "At one of the stations, you see Tao, deep in thought. Hand aimlessly stirring a potion as the other hold a recipe tome."
    hide tao sprite
    $ cinematic = False
    if not potion_stolen or not Flag_PotionNotStolen or Flag_LockBreakerNeeded:
        $ cinematic = True
        Narrator "You notice a glass cupboard, filled to the brim with potions."
        $ cinematic = False
        menu:
            "(Investigate)":
                call Night1AlchemyLab_Potions from _call_Night1AlchemyLab_Potions_2
                jump Afternoon2AlchemyLab_Choices
    else:
        $ cinematic = True
        Narrator "You notice the missing potions."
        Narrator "There's a twinge of guilt that seems to sit with you..."
        Narrator "You ignore it."
        $ cinematic = False
        jump Afternoon2AlchemyLab_Choices
    
    label Afternoon2AlchemyLab_Choices:
        $ cinematic = True
        Narrator "You wonder what you should do..."
        $ cinematic = False
        menu:
            "(Talk to Tao)":
                show tao sprite
                if Flag_Afternoon2Tao == False:
                    $ cinematic = True
                    Narrator "You approach Tao, who doesn't look up from their work."
                    Narrator "As you step closer, you see the pot bubble up."
                    Narrator "It splashes, catching Tao's sleeve."
                    $ cinematic = False
                $ Flag_Afternoon2Tao = True
                Tao "Crap!"
                Tao "Damn it, damn it, damn it!"
                menu:
                    "Are you okay?":
                        Tao "No! No, it is {i}not{/i} going well."
                        Tao "Every blasted potion just..."
                        Tao "I could've sworn this one worked."
                        Tao "It's simple. I don't understand what I'm doing incorrectly!"
                        Tao "It's a simple recipe. I've dissolved the ember-cherries in the brine, I've added moon melon skin..."
                        $ cinematic = True
                        Narrator "Tao looks over their book again, checking whether they've missed a step."
                        $ cinematic = False
                        Tao "The only reason this {i}isn't{/i} working is if they've been tampered with."
                        Tao "Screw it. I'll wash the skins, then create a purifying alkaline solution..."
                        Tao "Say, did you need something? You're just sort of... hovering."
                        menu:
                            "Wanted to see if you needed help.":
                                Tao "Unless you can actually help, I don't need you hovering."
                                Tao "Either this book is incorrect, {i}and{/i} I'm having amnesia, or there's something wrong with my plants."
                                Tao "Tell me, did you tamper with my plants? I won't be mad."
                                Tao "Ok, I will be mad, but tell me, I'm losing my mind."
                                menu:
                                    "I haven't touched anything.":
                                        Tao "Then... something is up with the materials..."
                                        Tao "I'll try another recipe. Perhaps one from another book."
                                        Tao "Perhaps whatever Xander did to his plants impacted mine."
                                        Tao "His plot was the one next to mine... yes... I bet that's it."
                                        Tao "What an idiot."
                                        $ cinematic = True
                                        Narrator "You're sure if you stay all you'll hear is rambling..."
                                        menu:
                                            "(Leave)":
                                                hide tao sprite
                                                jump Afternoon2AlchemyLab_Choices
                                    "Yes, I'm an evil mastermind who... tampers with plants.":
                                        Tao "Ha-ha. Very funny."
                                        Tao "It's interesting that you believe that's someone here wouldn't do that."
                                        Tao "So not only are you not particularly intelligent, you're also too trusting."
                                        Tao "That's all. You can go."
                                        hide tao sprite
                                        jump Afternoon2AlchemyLab_Choices

                            "Good point... (Leave)":
                                hide tao sprite
                                jump Afternoon2AlchemyLab_Choices
                

            "(Investigate Potions)" if not potion_stolen or not Flag_PotionNotStolen or Flag_LockBreakerNeeded:
                call Night1AlchemyLab_Potions from _call_Night1AlchemyLab_Potions_3
                jump Afternoon2AlchemyLab_Choices

            "(Leave the {b}Alchemy Lab{/b})":
                stop music
                jump Afternoon2Choices_Menu





label Afternoon2Atrium:
    play music "audio/project_w_class.mp3"
    scene atrium afternoon with fade
    $ Day2Afternoon = True
    $ Location = "Atrium"
    $ cinematic = True
    Narrator "You enter the Atrium. You can hear the sound of the moons as they rotate..."
    Narrator "...Magical masses made from heavy stone, twisting and turning around one another."
    if not Quest_XanderProgress:
        Narrator "As you step towards the centre, you see Xander, his head deep in his hands."
        Narrator "Whatever book he was reading is discarded. Turned upside down, pages frayed along the marble."
        pass
    else:
        Narrator "Xander stares up at the moons... you can see the stress on his face."
        Narrator "As you look at him, he smiles."
    $ cinematic = False
    jump Afternoon2Atrium_Choices

    label Afternoon2Atrium_Choices:
    menu:
        "(Talk to Xander)":
            if not Quest_XanderProgress:
                call XanderQuestStartDialogue from _call_XanderQuestStartDialogue
                jump Afternoon2Atrium_Choices

            else:
                call Afternoon2Atrium_Xander from _call_Afternoon2Atrium_Xander
                jump Afternoon2Atrium_Choices

        "(Explore the Atrium)":
            $ cinematic = True
            Narrator "You look around the atrium..."
            Narrator "Nothing seems out of place."
            if Flag_NotAliceMet:
                Narrator "You check the sewer grate and see nothing."
                pass
            else:
                Narrator "You look up at the moons, feeling a sense of calm."
                pass
            Narrator "You wonder whether you should be studying."
            Narrator "You haven't seen Alice or Eileen in a while."
            Narrator "You wonder where they're staying..."
            $ Flag_TeachersLoungeQuestioned = True
            jump Afternoon2Atrium_Choices

        "(Leave the Atrium)":
            stop music
            jump Afternoon2Choices_Menu

    label XanderQuestStartDialogue:
        show xander sprite with dissolve
        $ cinematic = true
        Narrator "You walk over. Xander doesn't even look up at you."
        Narrator "He's muttering something to himself as holds his head in his hands."
        Narrator "He's shaking, you notice little magical bolts of electricity spewing from his nails, fizzling into the air around him."
        $ cinematic = False
        Xander "...fire... water... air... or... water... then stone... then... fire-water-air... or... water? then stone...then..."
        menu:
            "Xander, are you okay?":
                Xander "Uhhh... my head's pounding. I feel like I'm gonna puke. Or I'm gonna run. Or puke."
                Xander "I can't think straight. I can't focus. I can't... I can't..."
                $ cinematic = True
                Narrator "He takes a breath. Still shaking."
                $ cinematic = False
                Xander "My crops died. All of them. I must've messed up."
                Xander "I'm such an idiot. I'm screwed. I've never been good at exams. I don't even know what we're trying to do half the time. No matter how much I study, I don't even get the basics right!"
                Xander "It's growing a plant, something I've done a hundred times and I {i}still{/i} fucked it up!"
                menu:
                    "You're being too hard on yourself.":
                        Xander "I'll be stuck at the Scholomance forever..."
                        Xander "I'll probably die there!"
                        pass
                    "You need to calm down...":
                        Xander "Easy for you to say! You didn't fuck everything up!"
                        pass
                Xander "Everyone here just studies all the time. It's real lonely." 
                Xander "I'm used to having a ton of brothers around. I miss home so bad..."
                menu:
                    "I can help you study.":
                        $ cinematic = True
                        Narrator "Xander perks up, a small smile forming on his face."
                        Narrator "You can see the relief hit him as he internalises what you said."
                        $ cinematic = False
                        Xander "Really? I hate that I have to ask for help. You know, if I could just get a few more hours in the Archives, I could catch up to the others." 
                        Xander "But it's locked up. I'm guessing whatever is in there will help me pass."
                        Xander "I've seen Tao in the Library... there's no way they'd be studying there if not to investigate it." 
                        Xander "Can you break into the Archives with me?"
                        menu:
                            "Yes, I'll help you.":
                                $ Quest_XanderProgress = True
                                Xander "Really? Thank you. I know it's risky but I need the help."
                                Xander "I'll do anything you need."
                                menu:
                                    "Just pass, Xander. You don't owe me.":
                                        Xander "Saint's I could just hug you. I'm not gonna... unless you want me to?"
                                        menu:
                                            "Sure.":
                                                Xander "C'mere..."
                                                $ cinematic = True
                                                Narrator "Xander pulls you close, wrapping his arms around you."
                                                Narrator "He stays there for a bit longer than you thought he would..."
                                                Narrator "You awkwardly tap his back... he releases you."
                                                Xander "Guess I needed that..."
                                                $ Affinity_Xander += 10
                                                pass
                                            "I'm not a hugging person...":
                                                Xander "I get that..."
                                                $ Affinity_Xander += 5
                                                pass
                                    "I might call you up on that.":
                                        Xander "'Course. You know me."
                                        pass
                                Xander "Right... I'm going to try to break the lock tonight... maybe you can figure out ways to break it?"
                                if Flag_ArchivesArtifice_Xander:
                                    menu:
                                        "(Tell him Rex already told you how)": 
                                            Xander "He called me a twerp..."
                                            Xander "Good to know we can just... break it."
                                            Xander "Rex is kinda mean... good guy overall, but mean."
                                            pass
                                else:
                                    menu:
                                        "Will do.":
                                            pass
                                Xander "If you're a hundred percent in... just meet me in the library tonight after curfew."
                                Xander "I'll wait for you."
                                menu:
                                    "Tonight in the Library... got it.":
                                        hide xander sprite
                                        return

                            "That's against the rules... sorry.":
                                Xander "Great... thanks for nothing!"
                                Xander "I'm gonna get shipped back to the Scholomance. Enjoy your hard earned freedom."
                                $ Affinity_Xander -= 10
                                hide xander sprite
                                return
                    
                    "Have you talked to Alice or Eileen about it?":
                        Xander "I might be a farmboy, but that doesn't mean I'm dumb." 
                        Xander "They'll put me on discipline for making excuses to slack off."
                        Xander "Thanks but not really helping. Can you leave me be... please."
                        $ Affinity_Xander -= 10
                        hide xander sprite
                        return


            "(Don't get involved.)":
                hide xander sprite
                return

    label Afternoon2Atrium_Xander:
        show xander sprite
        $ cinematic = True
        Narrator "You find Xander sat at the bench."
        $ cinematic = False
        Xander "Hey... I'll see you tonight at the Library."
        Xander "Careful sneaking out. I don't want you getting in shit for me."
        Xander "Was there something you wanted to chat about?"
        menu:
            "Just a few general questions...":
                call xanderhub_main from _call_xanderhub_main_1
                hide xander sprite
                return

            "Just checking on you...":
                Xander "I'm stressed, but after tonight it should be better."
                Xander "I'm worried about getting caught by Eileen or Alice..."
                Xander "If I get caught I'm {i}definitely{/i} going back to the Scholomance... but if I don't..."
                Xander "I guess I'll be more likely to pass."
                Xander "Risk versus reward or whatever."
                hide xander sprite
                return

            "Nothing at all.":
                hide xander sprite
                return


label Afternoon2ArtificingLab:#Rex is being berated by Eileen about poisoning Xander's crops. He says he didn't do it. She says she'll catch him.
    scene artificing lab afternoon
    play music "audio/Marigold District_MASTER2_LOOPED.mp3"
    $ Location = "Artificing Lab"
    if Afternoon2ArtificingLabVisited:
        $ cinematic = True
        Narrator "You enter the {b}Artificing Lab{b}."
        $ cinematic = False
        jump Afternoon2ArtificingLab_Choices
    else:
        $ cinematic = True
        Narrator "As you enter the {b}Artificing Lab{/b} you hear Rex, his voice raised."
        $ cinematic = False
        show rex sprite at left
        Rex "I'm telling you. I didn't do anything."
        show eileen sprite at right
        Eileen "You believe that you didn't leave evidence... Are you that arrogant."
        Eileen "You believe you can concoct a potion like that and leave no remnants?"
        Rex "As you said, I'm a D+ student at my best, how would I have made something that could poison Xander's plants?"
        Eileen "It's an impressive potion."
        Rex "I didn't do it."
        Eileen "{i}I{/i} don't believe you."
        Rex "Then prove I did it. Innocent until proven guilty."
        Eileen "I prefer the opposite approach."
        Eileen "I've got my eye on you, Rex. Sabotage isn't something I can allow in the Summit."
        $ Afternoon2ArtificingLabVisited = True
        Rex "..."
        Narrator "You hear heavy footsteps as Eileen leaves the Artificing Lab, passing you with a stern glance."
        Eileen "Shouldn't you be studying?"
        menu:
            "Yes...":
                Eileen "Very good."
                pass
            "Probably...":
                Eileen "I detest non-committal pupils. Hurry on."
                pass
            "No...":
                Eileen "Hmm. It's your future, I suppose."
                pass
        hide rex sprite
        hide eileen sprite
        with dissolve
        jump Afternoon2ArtificingLab_Choices


    
    label Afternoon2ArtificingLab_Choices:
        $ cinematic = True
        Narrator "You wonder what you should do."
        menu:
            "(Talk to Rex)" if not Flag_XanderPoisoned:
                show rex sprite
                Rex "Oh... you're here."
                Rex "Did you hear that old witch? Thinks I poisoned Xander's crops."
                menu:
                    "Did you?":
                        Rex "No. What's the point? I don't care if he passes or not."
                        pass
                    "She seemed angry.":
                        Rex "That? That was nothing. I remember when--"
                        Rex "Know what, nevermind."
                        pass
                Rex "Still... I guess now we know someone poisoned Xander's plants. I'm betting it was Tao, those two are always at eachothers throats."
                play sound "audio/dialogue_information_default.mp3"
                $ Flag_XanderPoisoned = True
                Rex "Didn't think that sorta thing would still be going on."
                menu:
                    "Shame.":
                        Rex "The only shame is that I'm catching flack for it."
                        Rex "Either way... I'm gonna put my head down and finish this crap."
                        Rex "If Eileen's investigating me, I don't have long before she throws me in isolation."
                        menu:
                            "(Leave)":
                                hide rex sprite
                                jump Afternoon2ArtificingLab_Choices
                

            "(Investigate the Artificing Lab)":
                if not artifice_options:
                    call Afternoon1ArtificingLab_Explore from _call_Afternoon1ArtificingLab_Explore_1
                    jump Afternoon2ArtificingLab_Choices
                else:
                    $ cinematic = True
                    Narrator "You take a closer look around the lab."
                    Narrator "The locked cupboards are tattered by age."
                    Narrator "As you peer through one of the holes you see it's filled with dusty scraps of metal and a few empty bulbs."
                    Narrator "You wonder whether there's anything else in there..."
                    $ cinematic = False
                    menu:
                        "(Break lock)" if Flag_HammerAcquired:
                            Narrator "You pull the hammer out from your bag and bring it down on the lock."
                            Narrator "With a loud {i}clunk{/i} it unbolts, the metal feeling loose."
                            Narrator "Inside you find a blueprint of some sort of Artifice..."
                            Narrator "{b}Delivery Bird{/b}"
                            menu:
                                "(Take it with you)":
                                    play sound "audio/clue_found_item_alert.mp3"
                                    $ artifice_options.append("Delivery Bird")
                                    $ cinematic = True
                                    Narrator "You stash it in your bag."
                                    $ cinematic = False
                                    jump Afternoon2ArtificingLab_Choices

                                "(Leave it)":
                                    jump Afternoon2ArtificingLab_Choices

                        "(Magic: Unlock the cupboard)" if Spell_Unlocking:
                            play sound "audio/reveal_magic_spell.mp3"
                            Narrator "You focus on the lock, feeling the magic within you stir."
                            Narrator "With a few whispered words, the cabinet unlocks with a loud {b}{i}clunk{i}{b}. It's clearly not been touched in a while."
                            menu:
                                "(Take it with you)":
                                    $ artifice_options.append("Delivery Bird")
                                    $ cinematic = True
                                    Narrator "You stash it in your bag."
                                    $ cinematic = False
                                    jump Afternoon2ArtificingLab_Choices

                                "(Leave it)":
                                    jump Afternoon2ArtificingLab_Choices
                        
                        "(Leave it alone)":
                            jump Afternoon2ArtificingLab_Choices
            
            "(Leave the Artificing Lab)":
                Narrator "You decide to leave the {b}Artificing Lab{/b}"
                stop music
                jump Afternoon2Choices_Menu





label Afternoon2Greenhouse: #You can check on the passage -- which Aria has unveiled if Flag_GreenhouseTunnelUnlocked = True
    scene greenhouse afternoon
    play music "audio/project_w_concept_03_gmajor.mp3"
    $ Location = "Greenhouse"
    $ cinematic = True
    Narrator "As you enter the {b}Greenhouse{/b}, the scent of damp earth and blooming flowers fills the air."
    Narrator "You notice your crops have grown... whatever magic this soil brings working busily."
    $ cinematic = False
    jump Afternoon2Greenhouse_Choices
    label Afternoon2Greenhouse_Choices:
        menu:
            "(Check on the passageway)" if Flag_GreenhouseTunnelUnlocked:
                $ cinematic = True
                Narrator "You approach the passageway Rex told you about..."
                Narrator "A grate once covered by roots now has nearly enough room for you to fit in."
                Narrator "You know the tree is moving them... though, slowly."
                Narrator "You're sure if you come back tonight you'll be able to fit through."
                Narrator "As you look down, you see little reflections in the water, the strong Greenhouse light filtering down to reveal icy blue water."
                Narrator "Perhaps a spring fuels the running water."
                $ cinematic = False
                jump Afternoon2Greenhouse_Choices

            "(Tend to your Crops)" if not Flag_Day2PlantsWatered:
                call Morning1Greenhouse_Plants from _call_Morning1Greenhouse_Plants_1
                $ Flag_Day2PlantsWatered = True
                jump Afternoon2Greenhouse_Choices

            "(Leave {b}Greenhouse{/b})":
                $ cinematic = True
                Narrator "You decide to leave the {b}Greenhouse{/b}..."
                $ cinematic = False
                stop music
                jump Afternoon2Choices_Menu



label Afternoon2Courtyard: 
    scene courtyard afternoon
    play music "audio/project_w_concept_03_gmajor.mp3"
    $ Location = "Courtyard"
    "You enter the {b}Courtyard{/b}."
    if not Afternoon2CourtyardVisited:#Alice and Aria are talking about the exams
        $ cinematic = True
        show aria sprite at left
        show alice sprite at right
        Narrator "You notice Alice and Aria both sitting in the grass."
        Narrator "You can't help but eavesdrop..."
        $ cinematic = False
        $ Afternoon2CourtyardVisited = True
        Alice "But you {i}have{/i} been studying, correct?"
        Aria "A little bit... I dunno, I've had other things on my mind."
        Alice "What sort of things..."
        Aria "It gets worse when I'm stressed, Alice. I don't want something to happen."
        Alice "It won't... and if it does, I'll deal with it."
        Aria "I just get the feeling that Eileen is waiting for me to mess up."
        Alice "Hmm... I can see why you might believe that."
        Aria "I can't control my magic... Though... when I'm in the Greenhouse that changes. It's like the Great Mage Tree is holding me."
        Alice "It's an odd enchantment, isn't it. It almost seems to care."
        Aria "I think it does."
        Alice "Then spend more time with it. If it helps you to be around it, study under it."
        Aria "What happens after? You know, when I leave? I won't have something like that around and it'llo all start again."
        Alice "I can't answer... But know that I understand."
        Alice "Anyway, my dress is getting dirty sat here. I'll leave you to st-... well, whatever it is you're doing."
        $ cinematic = True
        Narrator "You watch Alice get up and walk towards the Atrium. She looks over at you with a smile."
        hide alice sprite with dissolve
        Narrator "The Courtyard looks as it always does, though since the rain ceased this morning you still notice the leaves of trees slick with droplets."
        $ cinematic = False
        hide aria sprite
        pass

    else:
        $ cinematic = True
        Narrator "The Courtyard looks as it always does, though since the rain ceased this morning you still notice the leaves of trees slick with droplets."
        Narrator "You step into the grass and feel the wind on your skin."
        $ cinematic = False
        pass
    $ cinematic = True
    Narrator "You wonder what you should do."
    $ cinematic = False
    jump Afternoon2Courtyard_Choices


    label Afternoon2Courtyard_Choices:
        menu:
            "(Talk to Aria)":
                show aria sprite
                if Afternoon2Aria == False:
                    $ cinematic = True
                    Narrator "You approach Aria, who seems lost in thought."
                    $ cinematic = False
                    Aria "Hello. Did you want to take a seat? I'm just... well, I guess I'm just watching the clouds move."
                    Aria "It's been so long since we last saw them... well, real clouds."
                    menu:
                        "Are you okay?":
                            Aria "Last night I had a nightmare that felt real. It's one I'm sure you've had, too."
                            Aria "It was the one where you're back at the Scholomance."
                            Aria "You hear the sound of water overhead because somewhere on the surface of the lake something has whipped up a storm."
                            Aria "The water above you is thrashing... you feel the walls, they're wet and slick."
                            Aria "The whole lake above the Scholomance is angry, and it's trying to get in..."
                            menu:
                                "Can't say I've had that one.":
                                    Aria "One day you will. You've been through what every mage has."
                                    pass
                                "I've had a similar one.":
                                    Aria "That whole place is built on nightmares."
                                    pass
                    Aria "Sorry if I seem melancholic. I've been trying to study but can't seem to focus."
                    Aria "I just... I don't think I'll be placed anywhere, even if I pass."
                    menu:
                        "Is that why you aren't trying to study?":
                            Aria "That's probably it."
                            Aria "I just don't see the point. Alice wants to console me but in truth there's nothing to say." 
                            Aria "This isn't a feeling to be resolved, it's one I have to live in until the situation changes."
                            Aria "Hmm..."
                            Aria "If it's alright with you, I'd like to be alone."
                            $ Affinity_Aria += 10
                            $ Afternoon2Aria = True
                            menu:
                                "Sure.":
                                    hide aria sprite
                                    jump Afternoon2Courtyard_Choices
                else: 
                    $ cinematic = True
                    Narrator "Aria looks lost in thought. You should leave her be."
                    hide aria sprite
                    jump Afternoon2Courtyard_Choices

            "(Talk to Alice)":
                jump Afternoon2Alice
                label Afternoon2Alice:
                    show alice sprite:
                        xalign 0.5 
                        yalign 0.3  
                    Alice "Good afternoon, pupil. Did you need something?"
                    menu:
                        "Is Aria alright?":
                            Alice "She'll be okay. Like you, she's stressed about her exams."
                            Alice "Many pupils find themselves in this state."
                            jump Afternoon2Alice

                        "Where are you and Eileen staying?" if Flag_TeachersLoungeQuestioned:
                            Alice "Up the hall in the corridor... there's a teachers lounge."
                            Alice "It's not my favourite place, but it's only a week."
                            $ Flag_DiscoveredTeachersLounge = True
                            jump Afternoon2Alice

                        "I have other questions...":
                            call alicehub_main from _call_alicehub_main
                            jump Afternoon2Alice
                        
                        "(Leave)":
                            hide alice sprite
                            jump Afternoon2Courtyard_Choices


            "(Explore)":#with alice there you can't leave the courtyard
                $ cinematic = True
                Narrator "You look toward the forest, taking in the sights and sounds."
                Narrator "The trees sway gently in the breeze, their leaves rustling softly."
                Narrator "As you step away from the Courtyard, towards the forest, you hear Alice yell loudly in your direction."
                $ cinematic = False
                show alice sprite:
                    xalign 0.5 
                    yalign 0.3  
                Alice "Absolutely not. Come back."
                hide alice sprite
                menu:
                    "(Return)":
                        jump Afternoon2Courtyard_Choices

            "(Leave {b}Courtyard{/b})":
                stop music
                $ cinematic = True
                Narrator "You decide to leave the {b}Courtyard{/b}."
                $ cinematic = False
                jump Afternoon2Choices_Menu



### Night 2 ###

label Night2Choices:
    $ Day2Afternoon = False
    $ Day2Night = True
    scene dormitory night with fade
    play music "audio/project_w_dorms.mp3"
    $ Location = "Dormitory"
    $ cinematic = True
    Narrator "As people begin to settle down for the night, you find yourself back in the dormitory."
    Narrator "It's just past curfew, but you feel uneasy."
    Narrator "You feel a chill in the air, as though something strange will happen."
    Narrator "You sit at the end of your bed, listening to pages turn and the occasional ambience of your fellow pupils..."
    $ cinematic = False
    if not Spell_Light:
        $ cinematic = True
        Narrator "As you take a breath, you see Melody emerge from her sleeping area. She doesn't seem tired."
        Narrator "She looks at you, and something in her eye glows for a moment, as though she has an idea."
        $ cinematic = False
        show melody sprite
        Melody "Hey, I know it's late..."
        Melody "I noticed you don't read at night. You don't know the Light Spell, do you?"
        menu:
            "Light spell?":
                Melody "I'm glad I get to teach you it. Basically, it makes a little light orb that follows you. It's great for reading at night."
                Melody "Here, take this..."
                $ cinematic = True
                Narrator "She hands you a ripped piece of paper -- it looks like it might have been pulled out of a journal."
                Narrator "There's a spell on it. It's easy, almost nursery rhyme in it's simplicity."
                $ Spell_Light = True
                play sound "audio/learn_spell.mp3"
                $ cinematic = False
                Melody "It's simple, but effective."
                menu:
                    "Thank you.":
                        Melody "Don't mention it."
                        hide melody sprite
                        jump Night2Choices_Menu
                    "Why are you giving me this?":
                        Melody "We're friends. Do I need a reason?"
                        Melody "Anyway, I'll be in my bed if you need me."
                        hide melody sprite
                        jump Night2Choices_Menu
    else:
        jump Night2Choices_Menu

    label Night2Choices_Menu:
        if not Night2Explored:
            $ cinematic = True
            Narrator "You wonder what you should do with your night..."
            $ cinematic = False
            menu:
                "(Talk to Tao)": #Tao is stressed about the exam - they are reading a book and making notes
                    show tao sprite with dissolve
                    $ cinematic = True
                    Narrator "Tao's curtain is open as they study at their desk, scratching furiously along a tattered notebook. As you approach, they look at you over their shoulder."
                    $ cinematic = False
                    Tao "Hmm? I'm a bit busy... what do you want?"
                    menu:
                        "I have a few questions...":
                            Tao "I can afford a small break..."
                            call taohub_main from _call_taohub_main_1
                            Tao "Right... can you leave me be now?"
                            menu:
                                "Sure...":
                                    hide tao sprite
                                    jump Night2Choices_Menu
                        "Nothing...":
                            hide tao sprite
                            jump Night2Choices_Menu



                "(Talk to Aria)": #Aria is having an early night after feeling a bit melancholic - talks from behind a curtain
                    show aria sprite with dissolve
                    $ cinematic = True
                    Narrator "You approach Aria's curtain, and her voice comes softly from behind it."
                    Aria "Hey... is someone there?"
                    $ cinematic = False
                    menu:
                        "(Ask if she's okay)":
                            Aria "I'm okay. Just sleepy."
                            Aria "We'll talk tomorrow."
                            hide aria sprite
                            jump Night2Choices_Menu

                        "(Leave her be)":
                            hide aria sprite
                            jump Night2Choices_Menu


                "(Talk to Rex)" if not Quest_RexPlanRejected and not Quest_RexProgress: #Rex pulls you into his area, closing the curtains behind you to ask whether you want to do his plan (blowing up Eileen's half built statue in the Atrium)
                    if Affinity_Rex >= 50:
                        show rex sprite with dissolve
                        $ cinematic = True
                        Narrator "You walk over to Rex's curtain... he says nothing but you hear the sound of metal scraping."
                        $ cinematic = False
                        menu:
                            "Rex?":
                                Rex "Hey, just a sec."
                                pass
                            "(Leave)":
                                hide rex sprite
                                jump Night2Choices_Menu
                        $ cinematic = True
                        Narrator "You hear him tinker some more. After a moment, he opens the curtains and looks around the room with a look in his eye."
                        Narrator "He looks like he's looking out for someone. He pulls you in by your shirt, closing the curtain behind you."
                        $ cinematic = False
                        Rex "You got a minute? I wanted to run something by you..."
                        menu:
                            "Sure I do.":
                                pass
                        Rex "Listen. You're different from the others. I can tell you're not scared of me. So I'll let you in on something." 
                        Rex "I got a plan for graduation day. A big event."
                        menu:
                            "A party?":
                                pass
                            "Something tells me you aren't throwing us a party...":
                                pass
                        Rex "You know that the Council's building a statue of Eileen, right? Can't imagine why. But I bet she's loving it." 
                        Rex "All that glory for being the Council's pet. Well, I can't just let that happen. I'm going to blow it up before our graduation ceremony."
                        menu:
                            "You can't be serious...":
                                Rex "I'm always serious."
                                pass
                            "You're building a {i}bomb{/i}?":
                                Rex "Not a bomb... I'm not some psychopath wanting to hurt people. Well, most people."
                                pass
                        Rex "Eileen is everything I hate about mages. When I think about how miserable I was at the Scholomance, it always goes back to how much they controlled me." 
                        Rex "Think about it: we'll be the mages that stood up to them. Are you in?"
                        menu:
                            "Yes, I'll help you.":
                                Rex "I knew I liked you."
                                $ Affinity_Rex += 10
                                Rex "Right, I've been building a few devices... One of them is a nifty bit of artifice I'm calling the Stonecutter."
                                Rex "It's basically a big hammer... with blades..."
                                Rex "I need to finish it, and to do that I need materials... which is why I've been trying to find a way out of the Summit."
                                Rex "I can't leave. Eileen's watching me like a hawk... but she seems to barely notice you."
                                Rex "Think you could run a few errands for me over the next few days? I'll tell you what I need in the mornings..."
                                menu:
                                    "I can do that.":
                                        Rex "That's great."
                                        pass
                                    "It might be hard...":
                                        Rex "Just whatever you can spare. It'll be worth it."
                                        pass
                                Rex "For this to work... I'll need the materials in three days."
                                Rex "On graduation day, I'll cast the spell, activate the Artifice, and everyone will watch Eileen's legacy crumble." 
                                Rex "One more thing. I'm trusting you not to rat me out to Eileen and Alice."
                                $ Quest_RexProgress = True
                                $ cinematic = True
                                Narrator "You nod, feeling a mix of excitement and apprehension."
                                $ cinematic = False
                                Rex "I need to finish this up... mind if we chat more tomorrow? I've got a few things to run by you."
                                menu:
                                    "Sure.":
                                        $ cinematic = True
                                        Narrator "Rex smiles. You don't think you've seen him smile before."
                                        Narrator "You leave him alone."
                                        hide rex sprite
                                        $ cinematic = False
                                        jump Night2Choices_Menu

                            "No, I don't agree with you.":
                                Rex "I overestimated you. This conversation never happened."
                                $ Quest_RexPlanRejected = True
                                $ cinematic = True
                                Narrator "He looks pissed. You leave him be."
                                $ cinematic = False
                                hide rex sprite
                                jump Night2Choices_Menu


                    else:#Rex is busy.
                        $ cinematic = True
                        Narrator "You walk over to Rex's curtain... he says nothing but you hear the sound of metal scraping."
                        $ cinematic = False
                        menu:
                            "Rex?":
                                Rex "Kinda busy. Come back tomorrow."
                                jump Night2Choices_Menu
                            "(Leave)":
                                jump Night2Choices_Menu



                "(Talk to Melody)": #Melody is studying
                    show melody sprite with dissolve
                    $ cinematic = True
                    Narrator "Melody sits at the desk by her bed, surrounded by books and notes."
                    $ cinematic = False
                    menu:
                        "(Ask what she's studying)":
                            Melody "Oh, just some advanced spell theory. It's dry."
                            Melody "Very, very dry. Five days to go..."
                            Melody "That's how I stay motivated... counting days."
                            Melody "I'm guessing you're not tired."
                            menu:
                                "Not particularly.":
                                    Melody "Curfew is always a bit early... if you're anything like Rex or Xander... you can just sneak out, I suppose."
                                    Melody "Must be scary, being out there at night."
                                    Melody "Certainly not something I'll be doing. Plus, if Eileen catches them, they're good as dead."
                                    Melody "..."
                                    Melody "Okay, maybe not {i}dead{/i}..."
                                    Melody "I'm rambling. Did you need something?"
                                    menu:
                                        "I have a few questions...":
                                            call melodyhub_main from _call_melodyhub_main_6
                                            hide melody sprite
                                            jump Night2Choices_Menu
                                        "No. I'll head to bed now.":
                                            hide melody sprite
                                            jump Night2Choices_Menu
                                "I'll be going to bed soon.":
                                    Melody "Same here."
                                    hide melody sprite
                                    jump Night2Choices_Menu
                        "(Leave)":
                            hide melody sprite
                            jump Night2Choices_Menu

                "(Talk to Xander)" if not Quest_XanderProgress:
                    $ cinematic = True
                    Narrator "You see that Xander's curtain is drawn."
                    Narrator "You don't hear anything behind it."
                    $ cinematic = False
                    menu:
                        "Xander?":
                            $ cinematic = True
                            Narrator "You call out to Xander, but there's no response."
                            Narrator "You wait a moment, but still nothing."
                            Narrator "You part the curtain. He's gone. You wonder where."
                            $ cinematic = False
                            jump Night2Choices_Menu

                        "(Leave)":
                            jump Night2Choices_Menu


                "(Sneak Out)":
                    stop music
                    $ cinematic = True
                    Narrator "You tiptoe your way into the corridor... hoping no one catches you."
                    $ cinematic = False
                    jump Night2SneakDecision
                
                "(Go to Sleep)":
                    stop music
                    $ cinematic = True
                    Narrator "You pull the covers over you, looking up at the ceiling as it lulls you to sleep."
                    Narrator "Moments after your eyes are closed, you fall asleep."
                    $ Day2Night = False
                    jump EndOfDemo
        else:
            scene dormitory night
            $ Location = "Dormitory"
            $ cinematic = True
            Narrator "You make it back to the dormitory unscathed."
            Narrator "Everyone else seems to be sleeping."
            Narrator "The only thing you can do without waking someone, or getting caught, is going to sleep."
            Narrator "You close the curtain and pull the covers over you..."
            Narrator "And drift off to sleep..."
            $ cinematic = False
            stop music
            jump EndOfDemo


label Night2SneakDecision:
    if Spell_Light:
        scene corridor night with fade
        play music "audio/project_w_main_theme_concept_02_fade.mp3"
        $ Location = "Corridor"
        $ cinematic = True
        Narrator "You ignite a white orb of light in your hand, casting stark shadows along the walls."
        Narrator "You're thrilled, you realise. Your heart's racing."
        Narrator "You wonder where you should explore..."
        $ cinematic = False
        menu:
            "(Go to the {b}Library{/b})" if not Quest_XanderComplete and Location != "Library":
                stop music
                jump Night2Library

            "(Go to the {b}Alchemy Lab{/b})" if Location != "Alchemy Lab":
                stop music
                jump Night2AlchemyLab

            "(Go to the {b}Atrium{/b})" if not Night2AtriumVisited and Location != "Atrium":
                if Flag_NotAliceMet:
                    stop music
                    jump Night2Atrium

                else:
                    stop music
                    jump Night2Atrium2

            "(Go to the {b}Artificing Lab{/b})" if Location != "Artificing Lab":
                stop music
                jump Night2ArtificingLab

            "(Go to the {b}Greenhouse{/b})" if Location != "Greenhouse":
                stop music
                jump Night2Greenhouse

            "(Search for the Teachers Lounge)" if Flag_DiscoveredTeachersLounge and Location != "Teachers Lounge":
                stop music
                jump Night2TeachersLounge

            "(Return to the {b}Dormitory{/b})" if Location != "Dormitory":
                stop music
                $ cinematic = True
                Narrator "You decide to return to your room..."
                $ cinematic = False
                jump Night2Choices_Menu

    else:
        $ cinematic = True
        Narrator "You can't see anything. It's too dangerous to go ahead without light."
        Narrator "You turn around."
        $ cinematic = False
        jump Night2DecisionMenu






label Night2Atrium: #the thing isn't there. The moons are wacky. You find a shattered porcelain hand by the moons.
    scene atrium night with fade
    play music "audio/Oratory_MASTER_LOOPED.mp3"
    $ Location = "Atrium"
    $ cinematic = True
    Narrator "The atrium is eerily quiet, the usual sounds of water replaced by an unsettling stillness."
    Narrator "You glance up at the moons, their shapes distorted and swirling in the air..."
    Narrator "As you look around, you notice something glinting on the ground near the base of the moons."
    Narrator "You step closer, keeping an eye on the grate to make sure that nothing is below it."
    Narrator "You lean over and see a shattered porcelain hand lying on the ground. Little splinters scattered and broken."
    Narrator "It's clear the doll reached through the grate... and something cut it off."
    Narrator "You feel unsettled..."
    Narrator "You decide to leave the Atrium."
    $ cinematic = False
    $ Night2AtriumVisited = True
    jump Night2SneakDecision
    

label Night2Atrium2: #same as before except this time you don't look under the grates. You find a shattered porcelain hand by the moons.
    scene atrium night with fade
    play music "audio/Oratory_MASTER_LOOPED.mp3"
    $ Location = "Atrium"
    $ cinematic = True
    Narrator "The atrium is eerily quiet, the usual sounds of water replaced by an unsettling stillness."
    Narrator "You glance up at the moons, their shapes distorted and swirling in the air..."
    Narrator "As you look around, you notice something glinting on the ground near the base of the moons."
    Narrator "You step closer."
    Narrator "You lean over and see a fragments of some sort lying on the ground. Little pale splinters scattered and broken, as though a vase has dropped.."
    Narrator "You feel unsettled..."
    Narrator "You decide to leave the Atrium."
    $ cinematic = False
    $ Night2AtriumVisited = True
    jump Night2SneakDecision
    

label Night2Library: #Quest_XanderProgress Xander is waiting for you to break into the Archives. Eileen is in the Archives waiting for him.
    scene library night with fade
    $ Location = "Library"
    play music "audio/project_w_concept_04_fminor.mp3"
    $ cinematic = True
    Narrator "You arrive at the Library... a heavy light filters beneath the doorway. As you open it, you see Xander."
    show xander sprite with dissolve
    $ cinematic = False
    if Quest_XanderProgress:
        Xander "You came! Hey!"
        menu:
            "You sound surprised.":
                pass
        Xander "I'm... I'm a little surprised. I thought you might chicken out. It kinda dawned on me that I'm asking for a {i}lot{/i}."
        Xander "But... I'm glad you came. I really need the help."
        $ cinematic = True
        Narrator "He moves over to the Archives door. Even in the darkness you can make out the great lock."
        $ cinematic = False
        Xander "Any ideas on how to get it open?"
        menu:
            "I know how to open it.." if Flag_ArchivesArtifice_Xander:
                $ cinematic = True
                Narrator "You tell Xander that you already asked Rex how to break this piece of artifice."
                Narrator "Xander looks oddly annoyed as you explain it."
                $ cinematic = False
                Xander "He called me a twerp... that sucks. But it's good to know I can just... break it."
                Xander "Guess I'll try that."
                $ cinematic = True
                Narrator "Xander places his hands together and closes his eyes. Without even a whisper of a spell, static forms between his fingertips."
                Narrator "You can smell his hair beginning to singe as electricity crackles between his palms, growing and growing into a flurry of chaotic bolts."
                Narrator "He reaches forward and grasps the lock... it bursts open, unraveling like a tightrope cut loose. The chain fractures and falls to the ground with a heavy thud."
                Narrator "After a long moment, Xander takes a breath, letting his magic dissipate. His eyes are bright blue, as though the heat is still captured in his irises."
                $ cinematic = False
                Xander "Okay. Let's go in."
                menu:
                    "(Enter the Archive)":
                        hide xander sprite
                        stop music
                        jump Night2Archive

            "Have you tried hitting it?":
                Xander "I've tried hitting it... That's usually the first thing I do. First I hit it then I shock it. Do you think that'd work?"
                menu:
                    "It might.":
                        Xander "Alright, I guess... I'll give it a shot."
                        $ cinematic = True
                        Narrator "Xander places his hands together and closes his eyes. Without even a whisper of a spell, static forms between his fingertips."
                        Narrator "You can smell his hair beginning to singe as electricity crackles between his palms, growing and growing into a flurry of chaotic bolts."
                        Narrator "He reaches forward and grasps the lock... it bursts open, unraveling like a tightrope cut loose. The chain fractures and falls to the ground with a heavy thud."
                        Narrator "After a long moment, Xander takes a breath, letting his magic dissipate. His eyes are bright blue, as though the heat is still captured in his irises."
                        $ cinematic = False
                        Xander "Okay. Let's go in."
                        menu:
                            "(Enter the Archive)":
                                hide xander sprite
                                stop music
                                jump Night2Archive
            
            "There's probably some spell we don't know...":
                Xander "I doubt it. If that was so, Tao or Melody or, well, someone would've already gotten in."
                Xander "I was thinking of just brute forcing it. It's not refined, and Eileen will launch her own investigation and I'll definitely get caught... but what other options do I have?"
                menu:
                    "Just hit it.":
                        Xander "Don't need to tell me twice."
                        $ cinematic = True
                        Narrator "Xander places his hands together and closes his eyes. Without even a whisper of a spell, static forms between his fingertips."
                        Narrator "You can smell his hair beginning to singe as electricity crackles between his palms, growing and growing into a flurry of chaotic bolts."
                        Narrator "He reaches forward and grasps the lock... it bursts open, unraveling like a tightrope cut loose. The chain fractures and falls to the ground with a heavy thud."
                        Narrator "After a long moment, Xander takes a breath, letting his magic dissipate. His eyes are bright blue, as though the heat is still captured in his irises."
                        $ cinematic = False
                        Xander "Okay. Let's go in."
                        menu:
                            "(Enter the Archive)":
                                hide xander sprite
                                stop music
                                jump Night2Archive

    else:
        Xander "What are you doing here?"
        menu:
            "Exploring...":
                Xander "Well... unless you want to be dragged into something, I'd suggest exploring somewhere else."
                menu:
                    "What are you doing?":
                        Xander "Breaking into the Archives... if I want to salvage my grade after I messed up my crops this is the only way."
                        menu:
                            "Need help?":
                                Xander "Really? You'd help? That's a relief. I have no clue how to break this lock."
                                $ cinematic = True
                                Narrator "Xander moves over to the lock on the Archive door."
                                $ cinematic = False
                                menu:
                                    "I do." if Flag_ArchivesArtifice_Xander:
                                        $ cinematic = True
                                        Narrator "You tell Xander that by some miracle, you already asked Rex how to break this piece of artifice."
                                        Narrator "Xander looks oddly annoyed as you explain it."
                                        $ cinematic = False
                                        Xander "He called me a twerp... that sucks. But it's good to know I can just... break it."
                                        Xander "Guess I'll try that."
                                        $ cinematic = True
                                        Narrator "Xander places his hands together and closes his eyes. Without even a whisper of a spell, static forms between his fingertips."
                                        Narrator "You can smell his hair beginning to singe as electricity crackles between his palms, growing and growing into a flurry of chaotic bolts."
                                        Narrator "He reaches forward and grasps the lock... it bursts open, unraveling like a tightrope cut loose. The chain fractures and falls to the ground with a heavy thud."
                                        Narrator "After a long moment, Xander takes a breath, letting his magic dissipate. His eyes are bright blue, as though the heat is still captured in his irises."
                                        $ cinematic = False
                                        Xander "Okay. Let's go in."
                                        menu:
                                            "(Enter the Archive)":
                                                hide xander sprite
                                                stop music
                                                jump Night2Archive

                                    "Have you tried hitting it?":
                                        Xander "I've tried hitting it... That's usually the first thing I do. First I hit then I shock it. Do you think that'd work?"
                                        menu:
                                            "It might.":
                                                Xander "Alright, I guess... I'll give it a shot."
                                                $ cinematic = True
                                                Narrator "Xander places his hands together and closes his eyes. Without even a whisper of a spell, static forms between his fingertips."
                                                Narrator "You can smell his hair beginning to singe as electricity crackles between his palms, growing and growing into a flurry of chaotic bolts."
                                                Narrator "He reaches forward and grasps the lock... it bursts open, unraveling like a tightrope cut loose. The chain fractures and falls to the ground with a heavy thud."
                                                Narrator "After a long moment, Xander takes a breath, letting his magic dissipate. His eyes are bright blue, as though the heat is still captured in his irises."
                                                $ cinematic = False
                                                Xander "Okay. Let's go in."
                                                menu:
                                                    "(Enter the Archive)":
                                                        hide xander sprite
                                                        stop music
                                                        jump Night2Archive
                                    
                                    "There's probably some spell we don't know...":
                                        Xander "I doubt it. If that was so, Tao or Melody or, well, someone would've already gotten in."
                                        Xander "I was thinking of just brute forcing it. It's not refined, and Eileen will launch her own investigation and I'll definitely get caught... but what other options do I have?"
                                        menu:
                                            "Just hit it.":
                                                Xander "Don't need to tell me twice."
                                                $ cinematic = True
                                                Narrator "Xander places his hands together and closes his eyes. Without even a whisper of a spell, static forms between his fingertips."
                                                Narrator "You can smell his hair beginning to singe as electricity crackles between his palms, growing and growing into a flurry of chaotic bolts."
                                                Narrator "He reaches forward and grasps the lock... it bursts open, unraveling like a tightrope cut loose. The chain fractures and falls to the ground with a heavy thud."
                                                Narrator "After a long moment, Xander takes a breath, letting his magic dissipate. His eyes are bright blue, as though the heat is still captured in his irises."
                                                $ cinematic = False
                                                Xander "Okay. Let's go in."
                                                menu:
                                                    "(Enter the Archive)":
                                                        hide xander sprite
                                                        stop music
                                                        jump Night2Archive


                            "You're going to get shipped off to the Scholomance. Good luck.":
                                Xander "I know! I know. Maybe I'll see you there."
                                menu:
                                    "I'd hope not.":
                                        $ cinematic = True
                                        Narrator "You turn around and leave. It's probaby best to avoid... whatever it is he's doing."
                                        $ cinematic = False
                                        hide xander sprite
                                        stop music
                                        jump Night2SneakDecision
                                    "...":
                                        $ cinematic = True
                                        Narrator "You turn around and leave. It's probaby best to avoid... whatever it is he's doing."
                                        $ cinematic = False
                                        hide xander sprite
                                        stop music
                                        jump Night2SneakDecision
                    
                    "I'd rather not get dragged into something...":
                        $ cinematic = True
                        Narrator "You turn around and leave. It's probaby best to avoid... whatever it is he's doing."
                        $ cinematic = False
                        hide xander sprite
                        stop music
                        jump Night2SneakDecision


label Night2Archive: #Xander quest.
    scene archive night with fade
    play music "audio/project_w_combat_01.mp3"
    $ Location = "Archive"
    $ ArchiveOpened = True
    $ cinematic = True
    show xander sprite at left
    Narrator "As you pass through the threshold, your lights extinguish."
    Narrator "You remember a spell in the Scholomance which did that -- a whole room sealed from mana such that no one could cast spells inside."
    Narrator "You feel the overwhelming pressence of it. Or more so a lack of it. As though you're in a perfectly silent room where even your voice is muted."
    Narrator "With no residual light, you struggle to move, your footsteps colliding with eachother as you move through the darkness."
    $ cinematic = False
    Xander "I can't believe we did it... I need to find a light, I can't see my feet in here."
    $ cinematic = True
    Narrator "You trip on something, but regain your balance before you hit the ground by hanging on to a shelf. As you stand, you feel a switch."
    $ cinematic = False
    Eileen "Allow me to help you with that."
    show eileen sprite at right
    $ cinematic = True
    Narrator "A dim light switches on, revealing the makeup of the room, along with Eileen, who is seated, rather sternly, on a velvet red chaise lounge with a half-read book on her lap."
    Narrator "You notice the blanket, tossed hastily aside beneath a tall wall of books. It's clear she was sleeping."
    $ cinematic = False
    Xander "Fuck."
    menu:
        "Language...":
            $ cinematic = True
            Narrator "Eileen sighs, rubbing the bridge betweewn her eyes with her finger and thumb."
            $ cinematic = False
            pass
        "Fuck.":
            Eileen "Indeed."
            pass
    $ cinematic = True
    Narrator "As your eyes adjust to the light... you see her compose herself, standing up straight and placing the book she was reading on the coffee-table before her."
    $ cinematic = False
    Eileen "You both know that nobody is supposed to be in here. Just, you know, cards on the table."
    Eileen "Not only is it past curfew, but you've managed to break a perfectly good lock."
    Eileen "..."
    Eileen "It {i}was{/i} locked, wasn't it?"
    Xander "It's not locked... right now..."
    Xander "Are you supposed to be in here?"
    Eileen "None of your business. The reason I'm here is--"
    Eileen "Oh, sod it. I needed some peace and quiet from you lot. What are you doing in here?"
    Xander "Honestly? Cards on the table... I needed some extra time. My crops died, you see, and--"
    Eileen "Right, right... you do realise they got poisoned, don't you?"
    Xander "I... did not."
    Xander "I thought if I got in here, I'd find a way to salvage my grade. I can't get my head around the exam material. I really need it."
    Xander "You're failing me on the spot, aren't you. Just... please don't punish my friend, I dragged them into it. They didn't even want to be here I just needed--"
    Eileen "Please be quiet, I've got quite the headache."
    Xander "Sorry, ma'am."
    Eileen "Do not call me that."
    Xander "Sorry..."
    $ cinematic = True
    Narrator "Eileen takes a long breath."
    $ cinematic = False
    Eileen "The academic side of Magecraft is never as straightforward as you'd like. Not like combat, at least."
    Eileen "You know. The place where a hit is a hit and a miss is a miss. You get bloody or you bloody someone up. Simple things. Win or lose."
    Eileen "That's more your world, isn't it."
    Xander "I-- yes. That's exactly how I feel. Enchantments don't work how I want. I can barely brew a potion. And my last Artifice tried to kill me. I'm horrible."
    Xander "I'm completely useless at being a Mage. If I'm honest, I don't even know how to read runes, I just sound them out and hope it goes well."
    Eileen "Mages can't choose their gifts." 
    Eileen "For example, if one were to break into a locked room at night, one that had the potential to utterly ruin a thousand year old Artifice must be quite gifted in breaking things."
    menu:
        "Uhh...":
            pass
    Eileen "Xander, your path begins when you understand your strength. I must admit that potion craft and artifice were never things I excelled in..." 
    Eileen "... I killed my crops on purpose out of boredom. Combat is what I excelled in, and that's brought me to where I am today."
    Xander "Really? Did you fail all of your final exams?"
    Eileen "Don't pry... what I'm saying is there is far more to being a Mage than getting top marks. The council needs pupils with combat talent..."
    Eileen "Nevertheless... you two have the opportunity to turn around, head back to your dormitory and I will forget what transpired here."
    Xander "Thank you."
    menu:
        "How did you get in here? The lock was bolted.":
            Eileen "I thought I told you not to pry."
            pass
        "Thank you.":
            pass
    $ cinematic = True
    Narrator "Eileen flicks her hand, as though you were servants she was dispatching."
    Narrator "Xander drags you by the arm, and pulls you back into the library."
    Narrator "Before you close the door, you hear her words:" 
    $ cinematic = False
    Eileen "Not a word that either of us were in here to Alice."
    hide eileen sprite
    show xander sprite at center
    $ cinematic = True
    Narrator "The door closes. Xander summons a cold blue light to illuminate both of your faces."
    stop music
    play music "audio/Underground_Ambience.mp3"
    Narrator "He's pale. You are too."
    $ cinematic = False
    Xander "That was..."
    Xander "That was intense."
    Xander "Thanks for helping me out. I owe you one."
    $ Affinity_Xander += 20
    $ Quest_XanderComplete = True
    $ Quest_XanderProgress = False
    Xander "I think I'm going to head back to the dorm... I need some sleep. Are you coming with?"
    menu:
        "Yes.":
            $ cinematic = True
            Narrator "Xander leads you back. The whole time you can feel your heart beating."
            Narrator "He's silent, as though deep in thought."
            Narrator "Despite not getting any studying done, he seems happier. As though he's finally seen some light at the end of a dark tunnel."
            $ cinematic = False
            stop music
            hide xander sprite
            jump Night2Choices_Menu

        "I have other stuff to do.":
            Xander "Well, take care."
            $ cinematic = True
            Narrator "Xander leads you to the corridor, where you go your seperate ways."
            $ cinematic = False
            stop music
            hide xander sprite
            jump Night2SneakDecision

 




label Night2AlchemyLab: #Locked
    scene alchemy lab night with fade
    play music "audio/potions_classroom_ambience.mp3"
    $ cinematic = True
    $ Location = "Corridor"
    Narrator "You approach the Alchemy Lab and twist the handle."
    Narrator "It's locked."
    if Spell_Unlocking:
        play sound "audio/reveal_magic_spell.mp3"
        Narrator "You try to unlock it with a spell... it doesn't seem to do anything. The door unlocks but doesn't move... perhaps something is blocking it."
        pass
    else:
        pass
    Narrator "You decide to leave it alone."
    stop music
    $ cinematic = False
    jump Night2SneakDecision



label Night2ArtificingLab:
    scene artificing lab night with fade
    play music "audio/Marigold_Ambience.mp3"
    $ Location = "Artificing Lab"
    $ cinematic = True
    Narrator "You sneak into the {b}Artificing Lab{/b}. Dusty workstations and half-finished projects litter the room."
    Narrator "It smells like solder and smoke. The thin windows overlook a forest that is oddly bright under moonlight. You can't help but look out."
    Narrator "You look at the tools littered about, left by whoever was last here."
    $ cinematic = False
    jump Night2ArtificingLab_Choices

    label Night2ArtificingLab_Choices:
        $ cinematic = True
        Narrator "You wonder what you should do."
        $ cinematic = False
        menu:
            "(Search the Lab)":
                if Flag_LockBreakerNeeded == True:
                    call Night1ArtificingLab_SearchLock from _call_Night1ArtificingLab_SearchLock_1
                    jump Night2ArtificingLab_Choices

                else:
                    call Night1ArtificingLab_Search from _call_Night1ArtificingLab_Search_1
                    jump Night2ArtificingLab_Choices
                
            "(Look for Machine Parts)" if artifice_options:
                call Night2ArtificingLab_MachinePart from _call_Night2ArtificingLab_MachinePart
                jump Night2ArtificingLab_Choices

                label Night2ArtificingLab_MachinePart:
                    $ cinematic = True
                    Narrator "You search through the lab for any machine parts. Your [artifice_options] creation doesn't need much, but it doens't help to look."
                    Narrator "You find a small hammer beside some refined, malleable metal."
                    play sound "audio/clue_found_item_alert.mp3"
                    Narrator "You pick them both up and place them in your bag."
                    Narrator "You also find a few scraps of wire and a small gear."
                    Narrator "You add those to your bag as well."
                    play sound "audio/clue_found_item_alert.mp3"
                    $ cinematic = False
                    $ Flag_ArtificeParts = True
                    $ Flag_HammerAcquired = True
                    return

            "(Leave the {b}Artificing Lab{/b})":
                stop music
                jump Night2SneakDecision




label Night2Greenhouse: #You can escape into the forest. (Flag_GreenhouseTunnelUnlocked)
    scene greenhouse night
    play music "audio/project_w_concept_03_gmajor.mp3"
    $ Location = "Greenhouse"
    $ cinematic = True
    Narrator "You enter the {b}Greenhouse{/b}, moonlight filtering through the painted skylight, revealing the unshaded nooks in a dreamlike view."
    Narrator "You see the crops, some turning to your light as you approach. It flickers the closer you get to the tree, as though the magic in the room belongs only to him."
    $ cinematic = False
    jump Night2Greenhouse_Choices

    label Night2Greenhouse_Choices:
        Narrator "You wonder what you should do..."
        menu:
            "(Inspect the Tunnel)" if Flag_GreenhouseTunnelUnlocked:
                $ cinematic = True
                Narrator "You peer into the hole... the roots moving just enough for a person to descend through."
                Narrator "Other than running water, there's only silence below it."
                if Flag_NotAliceMet:
                    Narrator "You hope you don't see the doll down here."
                else:
                    pass
                Narrator "Do you want to enter?"
                $ cinematic = False
                menu:
                    "(Yes.)":
                        stop music
                        scene tunnel night with fade
                        play music "audio/Underground_Ambience.mp3"
                        $ cinematic = True
                        Narrator "You step into the tunnel, the air growing cooler and damper as you proceed."
                        Narrator "The faint sound of dripping water echoes around you."
                        Narrator "As your light ignites fully, you can see the tunnel around you... Stone slabs jutted at odd angles to make up a circular tunnel."
                        Narrator "Along the floor, you notice running water -- clean and clear... but also slightly warm."
                        Narrator "Whatever spring they emerge from must be close... you follow the flow of the water and let it lead you."
                        Narrator "After a few minutes of walking, you look up to see moonlight. The faux moons in the Atrium spin and rotate above you through a small, head-sized, grate."
                        Narrator "You know the courtyard is ahead of you. You follow the water for a long while until you see collapsed stone."
                        Narrator "The tunnel is split, to your right there's a small area that seems to descend down the mountain, and to your right, moonlight pouring through the rubble at a climable angle."
                        $ cinematic = False
                        menu:
                            "(Left)":
                                $ cinematic = True
                                Narrator "You look at the hole... it seems to tight for you to squeeze through."
                                $ cinematic = False
                                menu:
                                    "(Go Right)":
                                        $ cinematic = True
                                        Narrator "You approach the rubble, the moonlight illuminating the way."
                                        Narrator "You clamber up the rubble, your hands dirty with dust."
                                        $ cinematic = False
                                        stop music
                                        jump Night2Courtyard

                            "(Right)":
                                $ cinematic = True
                                Narrator "You approach the rubble, the moonlight illuminating the way."
                                Narrator "You clamber up the rubble, your hands dirty with dust."
                                $ cinematic = False
                                stop music
                                jump Night2Courtyard

                    "(No.)":
                        $ cinematic = True
                        Narrator "You step away from the hole. Maybe you'll come back later."
                        $ cinematic = False
                        jump Night2Greenhouse_Choices

            "(Inspect the Crops)" if planted_seeds: #You can sabotague other crops
                $ cinematic = True
                Narrator "You look over the crops, a few small plots of herbs and vegetables, all thriving under the magical light."
                Narrator "All, but Xander's, who have been dug up and binned."
                Narrator "You know you can't tend to your crops in the night. Someone will check them in the morning... so insted you just look over at them, watching them grow."
                $ cinematic = False
                menu:
                    "(Inspect your Crops)":
                        if "Winged Jasmine" in planted_seeds:
                            $ cinematic = True
                            Narrator "You inspect your Winged Jasmine."
                            $ cinematic = False
                            if quality => 50:
                                $ cinematic = True
                                Narrator "It's thriving, it's blue and white colours seemingly silky smooth and untainted."
                                $ cinematic = False
                                jump Night2Greenhouse_Choices
                            else:
                                $ cinematic = True
                                Narrator "It seems to be wilting... You wonder why."
                                $ cinematic = False                                
                                jump Night2Greenhouse_Choices

                        if "Snapjaw Orchid" in planted_seeds:
                            $ cinematic = True
                            Narrator "You inspect your Snapjaw Orchid."
                            $ cinematic = False
                            if quality => 50:
                                $ cinematic = True
                                Narrator "The pink, fleshy bits of it's {i}mouth{/i} seem to be developing well. You can tell it's healthy."
                                $ cinematic = False
                                jump Night2Greenhouse_Choices
                            else:
                                $ cinematic = True
                                Narrator "As you reach close to look at it, you notice it turn to try and grab your finger. That can't be a good sign."
                                $ cinematic = False
                                jump Night2Greenhouse_Choices

                        if "Moon Melon" in planted_seeds:
                            $ cinematic = True
                            Narrator "You inspect your Moon Melon."
                            $ cinematic = False
                            if quality => 50:
                                $ cinematic = True
                                Narrator "You're suprised at how much it's grown... it's positively glowing and fragrant. You're sure it's healthy."
                                $ cinematic = False 
                                jump Night2Greenhouse_Choices
                            else:
                                $ cinematic = True
                                Narrator "It seems to be wilting... You wonder why."
                                $ cinematic = False                                
                                jump Night2Greenhouse_Choices

                        if "Sanguine Lily" in planted_seeds:
                            $ cinematic = True
                            Narrator "You inspect your Sanguine Lily."
                            $ cinematic = False
                            if quality => 50:
                                $ cinematic = True
                                Narrator "It's long tendrils have grown even more. As you look at it, it seems to glisten. You can tell it's healthy."
                                $ cinematic = False
                                jump Night2Greenhouse_Choices
                            else:
                                $ cinematic = True
                                Narrator "The ends of it's long tendrils are blackened... you know that's not a good sign."
                                $ cinematic = False
                                jump Night2Greenhouse_Choices   
                        else:
                            jump Night2Greenhouse_Choices


                    "(Leave)":
                        if sabotaged_potions == False:
                            Narrator "As you step away from the crops, a thought seems to manifest in your mind -- fully formed."
                            Narrator "If there are only limited slots... why not play dirty?"
                            Narrator "If your whole future is riding on this one week... you might as well..."      
                            menu:
                                "(Sabotage someone's crops)":
                                    Narrator "Who should you sabotage?"
                                    menu:
                                        "(Melody)":
                                            $ sabotaged_plants.append("Melody")
                                            $ Flag_MelodyPlantSabotaged = True
                                            $ cinematic = True
                                            Narrator "You sneak over to Melody's plants, digging in the soil to cut the roots."
                                            play sound "audio/uproot_plant.mp3"
                                            Narrator "You don't feel good about it... but sabotaging Melody feels like your best shot at scoring higher than her."
                                            $ cinematic = False
                                            jump Night2Greenhouse_Choices

                                        "(Xander)":
                                            $ sabotaged_plants.append("Xander")
                                            $ Flag_XanderPlantSabotaged = True
                                            Narrator "You sneak over to Xander's plants, digging in the soil to cut the roots."
                                            play sound "audio/uproot_plant.mp3"
                                            Narrator "You don't really know why you did it... they're already dead."
                                            jump Night2Greenhouse_Choices

                                        "(Aria)":
                                            $ sabotaged_plants.append("Aria")
                                            $ Flag_AriaPlantSabotaged = True
                                            $ cinematic = True
                                            Narrator "You sneak over to Aria's plants, digging in the soil to cut the roots."
                                            play sound "audio/uproot_plant.mp3"
                                            Narrator "You get the feeling they'll grow back."
                                            $ cinematic = False
                                            jump Night2Greenhouse_Choices

                                        "(Rex)":
                                            $ sabotaged_plants.append("Rex")
                                            $ Flag_RexPlantSabotaged = True
                                            $ cinematic = True
                                            Narrator "You sneak over to Rex's plants, digging in the soil to cut the roots."
                                            play sound "audio/uproot_plant.mp3"
                                            Narrator "Rex isn't much of a threat, but sabotaging him will ensure he has better things on his mind."
                                            $ cinematic = False
                                            jump Night2Greenhouse_Choices

                                        "(Tao)":
                                            $ sabotaged_plants.append("Tao")
                                            $ Flag_TaoPlantSabotaged = True
                                            $ cinematic = True
                                            Narrator "You sneak over to Tao's plants, digging in the soil to cut the roots."
                                            play sound "audio/uproot_plant.mp3"
                                            Narrator "You don't feel good about it, but sabotaging Tao's feels like your best option."
                                            $ cinematic = False
                                            jump Night2Greenhouse_Choices

                                        "(Nevermind)":
                                            $ cinematic = True
                                            Narrator "Almost as quickly as the thought materialised in your mind, it vanishes."
                                            Narrator "What were you thinking?"
                                            $ cinematic = False
                                            jump Night2Greenhouse_Choices
                                
                        else:
                            $ cinematic = True
                            Narrator "You leave your plants be."
                            $ cinematic = False
                            jump Night2Greenhouse_Choices

            "(Investigate the {b}Greenhouse{/b})":
                $ cinematic = True
                Narrator "You inspect the greenhouse, the smells sticking out more here than they do anywhere else in the Summit."
                Narrator "You move up to the tree, feeling a surge of magic around it. You know that the tree is sentient, but it doesn't speak to you."
                Narrator "It barely seems to acknowldge you."
                play sound "audio/dialogue_information_default.mp3"
                Narrator "The rest of the greenhouse is tall flowers, wild grass, and carefully segmented crop areas, with bags of seeds stored away in cupboards dotting the edge of the room."
                Narrator "There was nothing this complex in the Scholomance. You learned botany with imported plants, teleported in by stern looking mages in strict uniforms, who seemed to look at you with distain."
                Narrator "What was there would grow under an artificial sun, something akin to the moons, but far less elegant. Like the harsh bulbs imported from the neighbouring country of Cerulia, where magic is outlawed."
                Narrator "You feel the magic in your body resonating with that of the tree, with that of the flowers and crops... Everything smells like honey, but you can't remember the last time you saw bees."
                Narrator "You realise, with a pang, that you're longing for something that you're sure no longer exists."
                Narrator "You should distract yourself with something else."
                $ cinematic = False
                jump Night2Greenhouse_Choices

            "(Leave the {b}Greenhouse{/b})":
                $ cinematic = True
                Narrator "You decide to leave the Greenhouse, the smell of flowers and dew evaporating as you close the door behind you."
                $ cinematic = False
                stop music
                jump Night2SneakDecision




label Night2Courtyard: #accessed through Greenhouse (Flag_GreenhouseTunnelUnlocked)
    scene courtyard night with fade
    $ Location = "Courtyard"
    play music "audio/project_w_concept_02_eminor.mp3"
    $ cinematic = True
    $ Night2Explored = True
    Narrator "You emerge from the tunnel, batting away the branches that were concealing it. You stand a few steps into the forest, from here you can look out and see the full scale of the summit."
    Narrator "It seems so bright, even in the dark. You can see lights in the window of the dormitory. From here you can even make out the faux moons in the Atrium."
    Narrator "As you walk into the Courtyard you find yourself looking out through the clearing, over the mountain. The sky is filled with a million stars, all twinkling for you."
    Narrator "You haven't been outside in the night, looking up at the stars since your magic first manifested. You feel freedom."
    Narrator "You feel small. A whole universe above you but here you are, stuck on a mountain..."
    $ cinematic = False
    jump Night2Courtyard_Choices

    label Night2Courtyard_Choices:
        scene courtyard night with fade
        play music "audio/project_w_concept_02_eminor.mp3"
        $ Location = "Courtyard"
        Narrator "You wonder what you should do..."
        menu:
            "(Enter the Forest)":
                $ cinematic = True
                Narrator "With no one to stop you, you enter the forest..."
                $ cinematic = False
                stop music
                jump Night2Forest
            
            "(Go back inside through the tunnel)":
                $ cinematic = True
                Narrator "You've seen enough... time to head back."
                scene corridor night
                Narrator "As you make your way to your room, you see Eileen in the hallway... she doens't see you."
                Narrator "It's too risky to stay out."
                Narrator "You go back to your room."
                $ cinematic = False
                stop music
                jump Night2Choices_Menu




label Night2Forest: #accessed through Courtyard (Flag_ForestDiscovered) #You can find the Doll and agree to sacrifice a classmate.
    scene forest night with fade
    $ Location = "Forest"
    $ cinematic = True
    Narrator "You step into the forest, the trees towering above you, their leaves whispering secrets in the night breeze. You ignite a light in your hand and let it hover above your shoulder."
    Narrator "The ground is thick with folliage, you watch your step as you move through it." 
    Narrator "As you do, you notice that something else has already made a path -- with crushed branches and disturbed bushes making your progress easier."
    Narrator "A trail for you to follow."
    $ cinematic = False
    jump Night2Forest_Choices

    label Night2Forest_Choices:
        scene forest night with fade
        play music "audio/project_w_main_theme_concept_02.mp3"
        $ Location = "Forest"
        $ cinematic = True
        Narrator "You wonder what you should do..."
        $ cinematic = False
        menu:
            "(Follow the Trail)": #leads to the ent place Aria ends up. Nice clearning, big sleeping trees.
                $ cinematic = True
                Narrator "You follow the trail lit by moonlight. The stones feel soft under your shoes --  crisp, icy grass crackles like glass shards"
                Narrator "The trees seem to part for you, their branches reaching out like arms, guiding you deeper into the forest."
                Narrator "It's odd, you feel like you're being led somewhere... but you can't see anyone."
                Narrator "After a few minutes of walking, the plants seem to part and make room for long grass."
                Narrator "You come to a clearing. The trees here forming it are enormous, their trunks wide and gnarled, their leaves forming a dense canopy overhead."
                $ cinematic = False
                menu:
                    "(Enter the clearing)":
                        stop music
                        jump Night2Forest_Trail

                label Night2Forest_Trail:
                    scene forest clearing
                    $ Location = "Clearing"
                    $ cinematic = True
                    Narrator "Looking around, you notice small trees, their branches drooping as though they were asleep."
                    Narrator "They're short, and rather than having thick trunks, you notice that they have many, slender branches that lithely catch the moonlight."
                    Narrator "The grass around them clings like clothing."
                    Narrator "You step closer to the centre of the clearing, and as you do, you notice on of the branches moving. Twisting, turning, as if to look at you."
                    Narrator "It's at that moment that you realise it is not a tree you are looking at... it's something alive and moving."
                    Narrator "You take careful steps backward, noticing a few other trees beginning to move..."
                    Narrator "You hear move movement in the trees in the forest. They sway and move aside, as if making room for something bigger."
                    $ cinematic = False
                    menu:
                        "(Run)":
                            $ cinematic = True
                            Narrator "You feel adrenaline rush through you as you sprint through the forest, following the trail until you reach the courtyard. The soft glow of the Summit's lights a sanctuary..."
                            $ cinematic = False
                            stop music
                            jump Night2Courtyard_Choices

                    
            "(Go off the beaten path)": #leads to the doll, hiding in a small grotto. one armed. something poking out.
                if Quest_NotAliceProgress:
                    $ cinematic = True
                    Narrator "You descend through the shrubbery, following your intuition and the slow descent of the mountain."
                    Narrator "It feels almost natural to you, as if you're following an invisible thread."
                    Narrator "It leads you down. Lower and lower through the forest, until you stumble across a small grotto, with a dull light eminating within."
                    $ cinematic = False
                    menu:
                        "(Enter the Grotto)":
                            play music "audio/project_w_concept_02_eminor.mp3"
                            $ cinematic = True
                            Narrator "You step into the grotto, wind at your back. As you step through the threshold, the world falls silent."
                            Narrator "You hadn't realised how loud the forest was in the night. Birds, insects, all forming a cacophony of nature."
                            Narrator "Here, there is only silence."
                            Narrator "The light within flickers and blurs, while yours remains strong."
                            Narrator "You step closer, and your light shifts, bouncing off the walls of the cave to reveal..."
                            Narrator "A small doll, sitting in the centre of the grotto."
                            show notalice sprite with dissolve
                            Narrator "It's Alice's doll, missing a forearm, eye cracked, something crawling within it."
                            Narrator "It looks at you. If it could smile, you're sure it would."
                            Narrator "You notice that the flickering light is coming from within the Doll an ambient yellow that dulls into reds."
                            Narrator "It turns its remaining hand over, signalling for you to sit on the rock opposite it."
                            $ cinematic = False
                            menu:
                                "(Take a seat)":
                                    $ cinematic = True
                                    Narrator "You sit across from the doll. The rock is uncomfortable, but you bare it."
                                    $ cinematic = False
                                    jump Night2Forest_Grotto
                                    
                                "(Remain standing)":
                                    $ cinematic = True
                                    Narrator "You stand your ground."
                                    $ cinematic = False
                                    jump Night2Forest_Grotto
                                    
                                "(Turn around and leave)":
                                    $ cinematic = True
                                    Narrator "You shouldn't be here. You step backwards until you're out of the grotto, then sprint back to the Courtyard."
                                    $ cinematic = False
                                    stop music
                                    hide notalice sprite
                                    jump Night2Courtyard_Choices

                        "(Turn Back)":
                            $ cinematic = True
                            Narrator "You follow the path back the way you came, until you come to the crossroads once again."
                            $ cinematic = False
                            stop music
                            jump Night2Forest_Choices

                    label Night2Forest_Grotto: #NotAlice only speaks using words Alice has spoken
                        scene forest grotto with fade
                        $ cinematic = True
                        Narrator "After a few moments of silence, the Doll speaks. It's voice is still a mimicry of Alice's... but there's something different about it."
                        $ cinematic = False
                        NotAlice "Good evening, pupil."
                        NotAlice "You took your time, but you did as I asked... You found me."
                        NotAlice "We aren't in the Scholomance anymore, pupil."
                        NotAlice "Instead... we are in an ancient place."
                        NotAlice "I ask again... as part of the test."
                        NotAlice "What is it you desire..."
                        NotAlice "... from this place?"
                        menu:
                            "I want to pass":
                                NotAlice "Ha... ha."
                                pass

                            "I want to escape":
                                NotAlice "Escape?"
                                pass

                        NotAlice "Very well."
                        NotAlice "I can offer you a choice."
                        NotAlice "A sacrifice..."
                        NotAlice "One of your classmates... and in exchange..."
                        NotAlice "In five days, you will have your wish."
                        jump Night2Forest_Grotto_Choices




                        label Night2Forest_Grotto_Choices:
                            menu:
                                "(Sacrifice?)":
                                    NotAlice "A classmate. Gone... forever."
                                    NotAlice "A body... to feed me."
                                    jump Night2Forest_Grotto_Choices

                                "What are you?":
                                    NotAlice "Something... else."
                                    menu:
                                        "You grant wishes. Like a genie?":
                                            NotAlice "Not a genie."
                                            jump Night2Forest_Grotto_Choices

                                        "What's inside the doll?":
                                            NotAlice "You'll see..."
                                            NotAlice "As I grow..."
                                            jump Night2Forest_Grotto_Choices
                                
                                "What happened to you?":
                                    NotAlice "The moons... crushed me."
                                    NotAlice "Inconvenient..."
                                    jump Night2Forest_Grotto_Choices

                                "({b}Make your Choice{/b})":
                                    $ cinematic = True
                                    Narrator "The doll looks at you with a stillness you've only ever seen in stone statues."
                                    Narrator "You feel a chill run down your spine."
                                    Narrator "You've come this far. You need to make a choice."
                                    $ cinematic = False
                                    menu:
                                        "Xander":
                                            $ cinematic = True
                                            Narrator "The dolls eye flashes. You feel your magic surge, your light flickers as you lack the mana to produce it."
                                            $ cinematic = False
                                            NotAlice "As you wish."
                                            $ sacrificed_character.append("Xander")
                                            pass
                                        "Aria":
                                            $ cinematic = True
                                            Narrator "The dolls eye flashes. You feel your magic surge, your light flickers as you lack the mana to produce it."
                                            $ cinematic = False
                                            NotAlice "As you wish."
                                            $ sacrificed_character.append("Aria")
                                            pass
                                        "Tao":
                                            $ cinematic = True
                                            Narrator "The dolls eye flashes. You feel your magic surge, your light flickers as you lack the mana to produce it."
                                            $ cinematic = False
                                            NotAlice "As you wish."
                                            $ sacrificed_character.append("Tao")
                                            pass
                                        "Rex":
                                            $ cinematic = True
                                            Narrator "The dolls eye flashes. You feel your magic surge, your light flickers as you lack the mana to produce it."
                                            $ cinematic = False
                                            NotAlice "As you wish."
                                            $ sacrificed_character.append("Rex")
                                            pass
                                        "Melody":
                                            $ cinematic = True
                                            Narrator "The dolls eye flashes. You feel your magic surge, your light flickers as you lack the mana to produce it."
                                            $ cinematic = False
                                            NotAlice "As you wish."
                                            $ sacrificed_character.append("Melody")
                                            pass
                                    $ cinematic = True
                                    Narrator "You feel drained. As though you've been dragged, kicking and screaming through freezing water."
                                    Narrator "Your spell-light is too dim to reveal anything around you."
                                    Narrator "But you can still see the dolls eyes, watching."
                                    $ cinematic = False
                                    NotAlice "You're dismissed."
                                    NotAlice "I'll see you soon."
                                    $ cinematic = True
                                    hide notalice sprite with dissolve
                                    Narrator "You step away from the doll, feeling your hands along the grotto walls until you find yourself back in the moonlit forest."
                                    Narrator "You know you need to get back to the Summit. Without your magic you're defenseless."
                                    Narrator "You look back at the grotto once more. The light in there still flickers, though now, much stronger."
                                    scene forest night with fade
                                    Narrator "Clambering and stumbling, you find your way back to the crossroads, and follow the trail to the Summit."
                                    scene courtyard night with fade
                                    Narrator "In the dark, you manage to navigate through the tunnel, through the Greenhouse and back to the dorms."
                                    scene dormitory night with fade
                                    $ Location = "Dormitory"
                                    queue music "audio/Oratory_Ambience.mp3"
                                    Narrator "You sit at the edge of your bed, catching your breath."
                                    Narrator "The silence of the dorms is interrupted only by the beating of your heart."
                                    $ cinematic = False
                                    if "Xander" in sacrificed_character:
                                        show xander sprite with dissolve
                                        Xander "Hey, are you okay?"
                                        $ cinematic = True
                                        Narrator "You look up to see Xander. He parts his curtains to look over at you, a soft yellow light illuminating him."
                                        Narrator "He looks as though he's just woken up from a bad dream."
                                        Narrator "Before you can respond... you notice something..."
                                        Narrator "You notice something under his bed."
                                        Narrator "A hand reaching out from underneath."
                                        $ cinematic = False
                                        Xander "What's up--"
                                        $ cinematic = True
                                        Narrator "Before he can finish his sentence, the hands pull him under with a quickness you thought impossible."
                                        Narrator "His body seems to bend and morph, kicking as whatever has a hold of him drags him into the shadows."
                                        Narrator "And then, there's nothing. Just a soft yellow light illuminating an empty bed quarters."
                                        hide xander sprite
                                        $ cinematic = False
                                        jump PostSacrificeSleep

                                    elif "Aria" in sacrificed_character:
                                        show aria sprite with dissolve
                                        Aria "Are you okay?"
                                        Aria "You look exhausted. I can make you some tea if you need."
                                        $ cinematic = True
                                        Narrator "You're surprised to see Aria, parting her curtains to look at you."
                                        Narrator "She seems restless, as though she's just woken from a bad dream."
                                        Narrator "She switches on her lamp and stands up."
                                        Narrator "You notice something under her bed."
                                        Narrator "A hand reaching out from underneath."
                                        $ cinematic = False
                                        Aria "I'll just make you some tea... one mo--"
                                        $ cinematic = True
                                        Narrator "Before she can finish her sentence, the hands pull her under with a quickness you thought impossible."
                                        Narrator "Her body seems to bend and morph, kicking as whatever has a hold of her drags her into the shadows."
                                        Narrator "And then, there's nothing. Just a soft yellow light illuminating an empty bed quarters."
                                        $ cinematic = False
                                        hide aria sprite
                                        jump PostSacrificeSleep

                                    elif "Tao" in sacrificed_character:
                                        show tao sprite with dissolve
                                        Tao "Do you mind? Some of us are trying to sleep."
                                        $ cinematic = True
                                        Narrator "You look over to see Tao, lit by their nightlight."
                                        Narrator "A book is closed over their lap as they sit at the end of their bed. They clearly woke up before you entered."
                                        Narrator "You notice something under the bed."
                                        Narrator "A hand reaching out from underneath."
                                        $ cinematic = False
                                        Tao "The least you could do is keep qui--"
                                        $ cinematic = True
                                        Narrator "Before they can finish, the hands reaches up and pulls them under with a quickness you thought impossible."
                                        Narrator "Tao's body seems to bend and morph, kicking as whatever has a hold of them drags them into the shadows."
                                        Narrator "And then, there's nothing. Just a soft yellow light illuminating an empty bed quarters."
                                        $ cinematic = False
                                        hide tao sprite
                                        jump PostSacrificeSleep

                                    elif "Rex" in sacrificed_character:
                                        show rex sprite with dissolve
                                        Rex "You're up, too?"
                                        Rex "Saints... You look horrible."
                                        $ cinematic = True
                                        Narrator "You look over to see Rex, lit by his nightlight. He's half-dressed. You can tell he's been up a while."
                                        Narrator "He sits at the edge of his bed, like you."
                                        Narrator "You notice something under the bed."
                                        Narrator "A hand reaching out from underneath."
                                        $ cinematic = False
                                        Rex "What happened to you--"
                                        $ cinematic = True
                                        Narrator "Before he can finish his sentence, the hands pull him under with a quickness you thought impossible."
                                        Narrator "Rex's body seems to bend and morph, kicking as whatever has a hold of him drags him into the shadows."
                                        Narrator "And then, there's nothing. Just a soft yellow light illuminating an empty bed quarters."
                                        $ cinematic = False
                                        hide rex sprite
                                        jump PostSacrificeSleep
                                    
                                    elif "Melody" in sacrificed_character:
                                        show melody sprite with dissolve
                                        Melody "Saints... it's you." 
                                        Melody "I had the worst nightmare."
                                        $ cinematic = True
                                        Narrator "You look over to see Melody. She's parted her curtain so that she can better see you. Her light is on."
                                        Narrator "As she stirs to look over at you..."
                                        Narrator "... you notice something under the bed."
                                        Narrator "A hand reaching out from underneath."
                                        $ cinematic = False
                                        Melody "Say... you don't look too good."
                                        Melody "Did something--"
                                        $ cinematic = True
                                        Narrator "Before she can finish her sentence, the hands pull her under with a quickness you thought impossible."
                                        Narrator "Melody's body seems to bend and morph, kicking as whatever has a hold of her drags her into the shadows."
                                        Narrator "And then, there's nothing. Just a soft yellow light illuminating an empty bed quarters."
                                        $ cinematic = False
                                        hide melody sprite
                                        jump PostSacrificeSleep

                                    else:
                                        stop music
                                        return
                                    
                            label PostSacrificeSleep:
                                $ cinematic = True
                                Narrator "You stare at where you once saw your classmate."
                                Narrator "An empty, unmade bed."
                                Narrator "You hope it's worth it."
                                Narrator "Your body seems to force you to lay down... you draw the curtains around you and hide underneath the blanket."
                                Narrator "You wait for sleep. Hoping it comes quickly."
                                $ cinematic = False
                                stop music
                                jump EndOfDemo




                else:
                    $ cinematic = True
                    Narrator "You descend through the shrubbery, feeling lost."
                    Narrator "It feels as though the darkness is too imposing to work through."
                    Narrator "You find yourself back at the crossroads."
                    $ cinematic = False
                    stop music
                    jump Night2Forest_Choices

            "(Go back)":
                $ cinematic = True
                Narrator "You decide to go back. The forest doesn't seem too safe to explore..."
                $ cinematic = False
                stop music
                jump Night2Courtyard_Choices






label Night2TeachersLounge: #player cannot enter because it's locked and has teachers in it, but it's now an option in future.
    scene corridor night
    $ Location = "Corridor"
    $ cinematic = True
    Narrator "Beside the Library, you see a small staircase. At the top, is an old, blue door."
    Narrator "The {b}Teachers Lounge{/b}."
    Narrator "You shouldn't knock. Whoever is in there would surely catch you."
    Narrator "Taking note of it, you decide to leave it be."
    $ cinematic = False
    $ TeachersLounge = True
    jump Night2SneakDecision




label EndOfDemo:
    scene black with fade
    play music "audio/Title_Theme_MASTER.mp3"
    "You have now completed Episode 1!"
    "We hope you enjoyed your time at The Summit!"
    "Thank you, so much, for playing!"
    "If you want to support us as we create Episode 2, 3, and other games, we have a Patreon!"
    "While you wait, we have also created a Podcast, set inside the world of the Summit."
    play sound "audio/dialogue_information_default.mp3"
    return




###########################
#    Night 0 Dormitory    #
###########################

label BTAO20: #Tao Dormitory Night 0
    ###################################
    ## Do not remove this portion
    show border onlayer UI
    ###################################
    show tao sprite
    Tao "{i}Shared{/i} dorms? Do they not have the budget for individual rooms?" 
    Tao "I've gotten all my studying done but some idiots leave it til the last moment and I'm sensitive enough to light without people being up and about."
    menu: 
        "Did you want to talk?":
            if Flag_PlayerMoonInspect:

                Tao "Usually not. However, I saw you inspecting the moons. Did you learn anything?"
                menu: 
                    "No. Not really.":
                        Tao "If it makes you feel better, I didn't either."
                        Tao "If you don't mind, I'm heading to bed."
                        menu:
                            "(Leave Tao be.)":
                                hide tao sprite
                                return
                            "I just have a few questions...":
                                Tao "{i}Sigh{/i}. Fine. What is it?"
                                call taohub_main from _call_taohub_main_2
                                hide tao sprite
                                return
            else:
                Tao "What in the Saints would give you that impression? I'm about to sleep. Shoo."
                $ cinematic = True
                Narrator "Tao sits back in their chair, clearly unwilling to talk."
                Narrator "They flip open a book, blocking your view of them."
                hide tao sprite
                return

        "(Leave Tao be.)":
            hide tao sprite
            return





label BXAN12: #Xander Dormitory Night 0
    ###################################
    ## Do not remove this portion
    show border onlayer UI
    ###################################
    show xander sprite
    Xander "Oh, it's you again. Are you about to pull an all-night study session, too?" 
    Xander "I got no choice with all these exams coming up. And anyway, you can't really leave the dorms after hours, because, you know..."
    menu:
        "Why?":
            pass
    Xander "Hmm, I thought Alice warned everyone. It's that huge magic tree. It's manic, or crazy, or something. I don't exactly remember, but it'll whack you."
    Xander "Did you wanna talk about somethin'? I'm gonna be up a while."
    menu:
        "(Continue) Sure, we can chat.":
            call xanderhub_main from _call_xanderhub_main_2
            return
        "(Exit Conversation) I'll pass for now.":
            hide xander sprite
            return


label BARI28: #Aria Dormitory Night 0
    ###################################
    ## Do not remove this portion
    show border onlayer UI
    ###################################
    show aria sprite
    Aria "Oh, hello. I saw you come in before me." 
    Aria "There's so much space... have you seen the ceiling? I'm sure you have."
    Aria "It's cold in here. Aren't you cold?"
    menu: 
        "Not particularly":
            Aria "I'm used to warmth, I guess. Maybe the blankets will warm me up."
            pass
        "A little.":
            Aria "They should really put a fire in here."
            pass
    Aria "I'm a bit nervous if I'm honest. As much as the Scholomance had a bite to it, I was {i}used{/i} to it."
    Aria "Tia's taking care of my plants..."
    $ cinematic = True
    Narrator "Aria looks down at her hands again."
    $ cinematic = False
    Aria "Okay, now I'm getting more nervous."
    Aria "Did you want to talk about something? Talking might help."
    menu: 
        "(Continue) Sure.":
            $ Affinity_Aria+= 10
            call ariahub_main from _call_ariahub_main_1
        "(Exit Conversation) I'm a little tired.":
            show aria sprite sad 
            Aria "Okay. Goodnight then. Big day tomorrow."
            hide aria sprite
            return


label BREX22: #Rex Dormitory Night 0
    ###################################
    ## Do not remove this portion
    show border onlayer UI
    ###################################
    show rex sprite
    Rex "Why are you up so late? Aren't you a good student like the rest of them?"
    menu: 
        "I'm a night owl.":
            Rex "Hm. Well then I might be seeing you around more than I thought."
            $ Affinity_Rex+= 10
            menu: 
                "(Continue) I was wondering...":
                    call rexhub_main from _call_rexhub_main_1
                "(End Conversation) Bye for now.":
                    Rex "Alright... see ya."
                    hide rex sprite
                    return
        "Can't sleep. I'm a bit anxious.":
            Rex "Don't come crying to me. I've got my own problems. Try Aria, she's all soppy like you."
            $ Affinity_Rex-= 10
            hide rex sprite
            return





        
        







        































        










###########################
# Character Introductions #
###########################
# I've put all the intros here.

####################
# Tao Introduction #
####################
label BTAO01:

    ###################################
    ## Do not remove this portion
    show border onlayer UI 
    ###################################

    $ cinematic = True
    Narrator "You notice a familiar face glimpsing up at the moons. While you didn't speak to Tao in the Scholomance, you'd heard of them, in fact, their name was usually mentioned when exam results were posted -- Tao, like Melody, was always at the top."
    $ cinematic = False
    show tao sprite
    Tao "Oh, you're here too."
    menu: 
        "I am...":
            pass
        "...":
            pass
    Tao "We didn't speak much, did we? We should try and keep it cordial, we're both here to pass, so let's not step on one another's toes."
    play sound "audio/moon_sparkle.mp3"
    menu:
        "How have you been?":
            Tao "I'd rather not do small talk. We both have better things to be doing."
            menu: 
                "Why are you staring up at the moons?":
                    pass
                "Like stare up at the moons?":
                    pass
        "Why are you looking up at the moons?":
            Tao "I'd rather not do small talk. We both have better things to be doing."
            menu:
                "Like stare up at the moons?":
                    pass

    Tao "Is that what it looks like to you? You're not the type to work out how things work, are you? It shows."
    $ Flag_TaoMet = True
    $ journal__bio_tao.isUnlocked = Flag_TaoMet
    menu: 
        "That's not very nice of you":
            Tao "You're right. Sorry."
            pass

        "Can you answer a basic question without being demeaning?":
            Tao "Apparently not... apologies."
            menu:
                "(Exit Conversation)":
                    hide tao sprite
                    return
                "...":
                    pass
    Tao "Do you have to keep hovering around me? I'm certain your time would be better spent studying."
    Tao "If you're so incessant on chatting we can do so later."
    menu:
        "(Keep Hovering)":
            Tao "Ugh. Really?"
            pass
        "(Exit Conversation)":
            hide tao sprite
            return 
    $ cinematic = True
    Narrator "Tao rolls their eyes. You're not going to get much else from them."
    $ cinematic = False
    menu: 
        "Look up at the moons with them.":
            play sound "audio/main_hall_ambience.mp3"
            $ cinematic = True
            Narrator "You look up at a miniturised replica of the night sky. Two lunar bodies orbitting one another."
            Narrator "They produce a faint, magical light that feels warm on your skin. Tao seems to smile as you inspect it."
            $ Affinity_Tao+= 5
            Narrator "Part of you wonders how magic like this is crafted." 
            Narrator "You feel something in you the resonates with it, as though when you reach out you can touch it. It's like touching a pond with your mind."
            Narrator "Every ripple seems to shift the density of magic in the room. The more you try and notice it, the harder it gets to decipher."
            Narrator "You pull away. Tao doesn't shift. They clearly see more of what is going on than you do."
            Narrator "It's like they're looking into each individual thread of a complex blanket, while all you can see is the zig-zagging pattern it forms."
            Narrator "You could be here all day. It's best you move."
            $ Flag_PlayerMoonInspect = True
            hide tao sprite
            menu:
                "Move on.":
                    return
        "Move on.":
            hide tao sprite
            return
    return

        
#####################
# Aria Introduction #
#####################
label BARI01:
    ###################################
    ## Do not remove this portion
    show border onlayer UI 
    ###################################
    show aria sprite
    $ cinematic = True
    Narrator "You tap the womans shoulder, her attention seems drawn toward the stained glass at the far end of the room." 
    Narrator "Through it, lit by only moonlight, you notice the branch of a tree."
    Narrator "You can't help but notice her smell. Lavender. Quite strong, too. It reminds you of the fields outside the city."
    
    $ cinematic = False

    # Removed at quarter_size from below
    show aria sprite with dissolve 
    Aria "Oh, it's you! Maybe you don't remember me from the Scholomance. I'm Aria."
    $ cinematic = True
    Narrator "She extends her hand for you to shake it."
    $ cinematic = False
    menu:
        "I remember you. Everyone called you a tree hugger.":
            Aria "Why would you hug a tree? They don't really like that..."
            "You're strange, even for a mage."
            pass
        "No, sorry, I was buried in my studies over there.":
            Aria "It'll be more of the same this week, I'm afraid."
            "We've made it this far. What's one more week?"
            pass
    Aria "Odd... Why didn't our paths cross at the Scholomance?"
    menu: 
        "I'm the solitary sort.":
            Aria "Oh no, I'm not. I hate being alone."
            "I know what you mean."
            pass
            
        "I was busy. Got to impress the Mage Council somehow.":
            Aria "I can't imagine being like them. Stuck inside stone walls, in meetings all the time... sounds frustrating."
            menu: 
                "Makes you I wonder how they all felt during {i}their{/i} final exams.":
                    pass
                "Could be.":
                    pass

        "Unlucky, I guess.":
            Aria "At least we've got however long these exams last."
            "Sure."
            pass

    Aria "Hm, you're not like the other students here. I'll leave you to it. Good luck on the exams. Let me know if you need help."
    $ Flag_AriaMet = True
    $ journal__bio_aria.isUnlocked = Flag_AriaMet
    hide aria sprite
    return


#######################
# Xander Introduction #
#######################
label BXAN01:
    ###################################
    ## Do not remove this portion
    show border onlayer UI 
    ###################################
    show xander sprite
    $ cinematic = True
    Narrator "You'd seen the man approaching you before. Though, usually, his hair was burned or half-alight whenever he drew your attention." 
    Narrator "Now, he looks oddly put together, even his uniform is somewhat crisp, even if he's not wearing it correctly."
    $ cinematic = False
    show xander sprite

    Xander "You look kinda familiar..."
    Xander "I'm Xander. Did we meet at the Scholomance?"
    menu: 
        "We met a few times.":
            Xander "Uh, I must've been busy trying to keep up with studying." 
            Xander "That's why I don't really remember you. Anyway, we both made it to the Summit in the end. This place makes me feel like I ate a big old goat, horns and all, and it's not settling well."
            pass
        "I don't think we met.":
            Xander "Thank the Saints... I was worried because I couldn't place you. We have a lot on our minds this week, heh?"
            pass
    Xander "Anywho... glad we're finally in the graduation group."
    Xander "I'll see ya around, I guess." 
    hide xander sprite
    $ Flag_XanderMet = True
    $ journal__bio_xander.isUnlocked = Flag_XanderMet
    return



#######################
# Melody Introduction #
####################### 
label BMEL01:
    ###################################
    ## Do not remove this portion
    show border onlayer UI 
    ###################################
    $ cinematic = True

    Narrator "A familiar face approaches you. Her bright eyes and warm smile seem almost contagious." 

    $ cinematic = False
    show melody sprite
    Melody "So good to meet you! I think we met a few times back at the Scholomance. Melody, like a song, that sort of melody."
    Melody "It's so nice to see you again, when I heard who the graduating class were this time, I wanted to chat to you but everything got so busy, you know?" 
    Melody "If you need anything, like a chat, some gossip, a cup of tea, come talk to me. I've done a {i}lot{/i} of studying so I can help you with whatever you need."
    menu:
        "Will do!":
            Melody "Good! Good. I wish I'd talked to you back at the Scholomance, but that place was such a mess of Mages and mayhem so I just never found the time. Really sorry."
            pass
        "...":
            Melody "Oh you're nervous? I'm nervous, too. I'm sort of a nervous chatterer - just ask my old dorm mates. Sorry, I guess I'll leave you be."
            pass
    Melody "Anyway, I'll let you chat with everyone else. We're gonna be stuck together for a week, might as well get friendly."
    $ cinematic = True
    Narrator "With a quick, but earnest wave, she steps away."
    $ Flag_MelodyMet = True
    $ journal__bio_melody.isUnlocked = Flag_MelodyMet
    hide melody sprite

    return




#######################
#  Rex Introduction   #
####################### 
label BREX01: 
    ###################################
    ## Do not remove this portion
    show border onlayer UI 
    ###################################
    show rex sprite
    $ cinematic = True
    Narrator "You bump into a tall figure. He's broad-shouldered with tattered clothes. He doesn't seem to wear his uniform correctly. He looks down at you with disarming look in his eye."
    $ cinematic = False
    Rex "What do you want?"
    menu: 
        "Who are you?":
            Rex "Didn't see you at the Scholomance... then again, I guess I kept to myself most of the time. Just try and stay outta my way, alright?"
            pass
        "Nothing right now.":
            Rex "Alright. Buzz off then."
            pass
    $ cinematic = True
    Narrator "You remember him... or at least remember hearing about him. Cairyx... though most people just called him Rex."
    Narrator "He doesn't seem interested in talking."
    $ cinematic = False
    hide rex sprite
    $ Flag_RexMet = True
    $ journal__bio_rex.isUnlocked = Flag_RexMet
    return



#######################
# Eileen Introduction #
####################### 
label BEIL01: 
    ###################################
    ## Do not remove this portion
    show border onlayer UI 
    ###################################
    return





######################
# Alice Introduction #
###################### 
label BALI01:
    ###################################
    ## Do not remove this portion
    show border onlayer UI 
    ###################################
    return


#######################
#NotAlice Introduction#
####################### 
label BNAL01:
    ###################################
    ## Do not remove this portion
    show border onlayer UI 
    ###################################
    return

















##############################################################################################
## CHARACTER MAIN HUBS // CHARACTER MAIN HUBS // CHARACTER MAIN HUBS // CHARACTER MAIN HUBS ##
##############################################################################################

#######################
#   Melody Main Hub   #
####################### 
label melodyhub_main:
    Melody "What's the matter?"
    menu:
        "About that light spell..." if Flag_LightSpellNotLearned:
            call HMEL01 from _call_HMEL01
            return

        "About the Potion Exam..." if not Day0Night:
            call HMEL02 from _call_HMEL02
            return

        "What do you think of Tao?" if Flag_TaoMet:
            call HMEL03 from _call_HMEL03
            return

        "What do you think of Aria?" if Flag_AriaMet:
            call HMEL04 from _call_HMEL04
            return

        "What do you think of Rex?" if Flag_RexMet:
            call HMEL05 from _call_HMEL05
            return

        "What do you think of Xander?" if Flag_XanderMet:
            call HMEL06 from _call_HMEL06
            return

        "What do you think about Inquisitor Eileen?":
            call HMEL07 from _call_HMEL07
            return

        "What do you think about Alice?":
            call HMEL08 from _call_HMEL08
            return

        "I saw 'Alice' in the forest..." if Flag_NotAliceMet:
            call HMEL09 from _call_HMEL09
            return

        "Do you have dreams? What do you want to do after Graduation?":
            call HMEL10 from _call_HMEL10
            return

        "I'm worried about the exams.":
            call HMEL11 from _call_HMEL11
            return

        "Do you know anything about the graduation placements?":
            call HMEL12 from _call_HMEL12
            return

        "(Combat Exam)":
            if Flag_CombatExamCompleted:
                call HMEL13 from _call_HMEL13
            else:
                call HMEL14 from _call_HMEL14
            return

        "(Exit Conversation)":
            $ result = renpy.random.randint(1, 4)
            if result == 1:
                Melody "See you."
                return
            if result == 2:
                Melody "Bye!"
                return
            if result == 3:
                Melody "Let me know if you need anything."
                return
            if result == 4:
                Melody "I guess we'll talk another time."
                return

        "(Potion Exam)":
            if Flag_PotionExamCompleted:
                call HMEL15 from _call_HMEL15
            else:
                call HMEL16 from _call_HMEL16
            return

        "(Artificing Exam)":
            call HMEL17 from _call_HMEL17
            return

        "(Magic) How did your magic manifest?":
            call HMEL18 from _call_HMEL18
            return

        "Would you say we're friends?":
            if Day0Afternoon or Day0Night or Day1Afternoon or Day1Morning or Day1Night or Day2Morning or Day2Afternoon or Day2Night:
                call HMEL19a from _call_HMEL19a
            elif Day3Morning or Day3Afternoon or Day3Night or Day4Morning or Day4Afternoon or Day4Night:
                call HMEL19b from _call_HMEL19b
            elif Day5Morning or Day5Afternoon or Day5Night or Day6Morning or Day6Afternoon or Day6Night:
                call HMEL19c from _call_HMEL19c
            else:
                call HMEL19d from _call_HMEL19d
            return

        "(Mage Society) What do you know about Mage Society?":
            call HMEL20 from _call_HMEL20
            return

    return


    


    

    
    
    label HMEL01:

        Melody "Oh, you wanna know about the light spell? Sure... here." 
        Melody "It's simple enough, then again lights something I've always been good at so I picked it up pretty quick."
        $ cinematic = True
        Narrator "She hands you a page torn from an old book. You take a moment to read it. You wonder whether she was allowed to remove it, but stash it anyway."
        $ Spell_Light = True
        $ cinematic = False
        menu: 
            "Thank you.":
                jump melodyhub_main
        Melody "If you end up roaming around at night, make sure you use it. I don't want you getting lost or something. Ha ha."
        menu: 
            "Got it.":
                return
            "I don't plan on roaming.":
                Melody "Probably wise. Inquisitor Eileen seems strict. I doubt either of us would want her shouting at us."
                jump melodyhub_main
        jump melodyhub_main

    label HMEL02:
        #HMEL02
        show melody sprite happy
        Melody "Of course I'll help you with potions. It's like, the thing I know best." 
        Melody "The book they give you, it's not always right, or well, it's often really incomplete." 
        Melody "If I were you, I'd just try new stuff and see if it works, as long as you're following the rules regarding energy and colour you'll be fine."
        Melody "I like matching reds, you know, like ember cherries, it means I ended up with a powerful potion." 
        Melody "It all sounds a bit too simple but potions are often just a balancing act in order to bring out the magical or medicinal properties within them." 
        Melody "Give it a shot."
        hide melody sprite happy
        menu: 
            "Sure, I'll give that a shot.":
                show melody sprite happy
                Melody "Hope I helped! Let me know how it goes, yeah?"
                hide melody sprite happy
                pass
            "So… just do whatever and match colours.":
                show melody sprite happy
                Melody "Exactly. That's how I do it, and I always do well on my potion mixing."
                hide melody sprite happy
                pass
        menu:
            "(Exit Conversation)":
                jump melodyhub_main
        jump melodyhub_main

    

    label HMEL03:
        #HMEL03
        Melody "Tao... right. Look, I'm going to be honest here. I don't like Tao -- don't tell them, obviously, it's probably just me being a bit antsy, but one time Tao ratted me out to Eileen."
        Melody "I just don't trust them. They screwed me over and I'm pretty sure they screwed Aria over at one point too -- at least that's what I've heard."
        show melody worried
        Melody "This stays between us, right?"
        menu: 
            "Sure,":
                pass
            "Of course,":
                pass
        hide melody worried
        Melody "Great. Sorry, I really don't want to be mean, I just don't trust them."
        $ cinematic = True
        Narrator "She looks relieved."
        $ cinematic = False
        menu: 
            "(End Conversation)":
                jump melodyhub_main
        jump melodyhub_main


    label HMEL04:
        #HMEL04
        Melody "Aria? We never really started talking. I should change that. Just {i}so{/i} busy, you know?"
        menu: 
            "Busy?":
                Melody "Maybe busy isn't the right way of putting it." 
                Melody "I mean, back at the Scholomance I really didn't make new friends unless they approached me… not because I didn't want to but because I just felt like I didn't want to intrude." 
                Melody "From what I understand, Aria is very 'go with the flow.' It's like, parallel lines, you know? We're not gonna meet without external influence."
                menu: 
                    "Should I introduce you?":
                        Melody "I'll get round to it before graduation… She doesn't seem to be doing so well and I don't wanna stress her out right now."
                        menu: 
                            "Well, don't take too long.":
                                Melody "Trust me, I won't."
                                pass
                    "Right":
                        pass
            "You should talk to her":
                Melody "I'll get round to it before graduation… She doesn't seem to be doing so well and I don't wanna stress her out right now."
                menu: 
                    "Well, don't take too long":
                        Melody "Trust me, I won't."
                        jump melodyhub_main
        jump melodyhub_main
            
    label HMEL05:
        #HMEL05
        show melody sprite intense
        Melody "Rex is a bit troubled… I'd stay out of his way. I think deep down he's sweet, but you have to get past the exterior, and there's not enough time for that and exams."
        Melody "If I'm honest, I only really know Rex by persona alone. I was in the cafeteria when he set Lionel Robyn's cloak on fire." 
        Melody "He's memorable..."
        hide melody sprite intense
        menu: 
            "He set someone on {b}fire{/b}?":
                Melody "Their cloak. Lionel was a bit of a bully so no one really cared." 
                Melody "From my perspective, it was two troublemakers getting into a spat. Very much a spectator sport for the rest of us."
                pass
            "Have you ever talked to Rex?":
                Melody "A couple of times, not about anything important though." 
                Melody "He's not the studious type so our chances of meeting randomly in the library or study hall was low."
                pass
        menu: 
            "Right...":
                jump melodyhub_main
    

    label HMEL06:
        #HMEL06
        show melody sprite happy
        Melody "Uhh, Xander's a mixed bag. He's really good at fighting." 
        Melody "I used to watch him zip around in the courtyard but, well, he's not the best at remembering things." 
        Melody "I think he gets in his head. If I had time to tutor him, he'd probably do good. "
        menu: 
            "Do you tutor pepole often?":
                Melody "I used to, when I had more time for it." 
                Melody "Either way, Xander will probably do fine, as long as he doesn't let himself collapse under the pressure of passing."
                menu: 
                    "Right.":
                        hide melody sprite happy
                        jump melodyhub_main
    
    label HMEL07:
        #HMEL07
        show melody sprite intense
        Melody "I don't know what I can say about Eileen without sounding a bit mean…" 
        Melody "Watching her makes me wonder what went so wrong in her life that she ended up so mean and spiteful."
        Melody "She's scary, but deep down I think she does care." 
        Melody "Even though she's certainly the most brutal of the instructors, I get the feeling she wants what's best for us, but best for her means something very different."
        hide melody sprite happy
        menu: 
            "Right.":
                hide melody sprite happy
                jump melodyhub_main
    
    label HMEL08:
        #HMEL08
        show melody sprite happy
        Melody "Oh, I like Alice. She's... helpful, it sure is nice to have a teacher who cares." 
        Melody "I'm pretty sure without Alice, Aria would've been kicked out with all the mess she ends up in."
        menu: 
            "Right.":
                jump melodyhub_main
            "Trouble?":
                Melody "Yeah, she can be quite destructive with her spells. I've seen her pull up the flooring a few times when working with her magic."
                Melody "Property damage doesn't sit well with the council, but she never really got punished for it. I think Alice is very on her side."
                menu: 
                    "...":
                        hide melody sprite happy
                        jump melodyhub_main
        
    label HMEL09:
        #HMEL09
        Melody "You saw Alice in the forest? It was probably just one of her dolls." 
        Melody "I don't know what you mean by 'like Alice', but you should probably ask her." 
        Melody "Maybe she messed up a ritual or something -- Geomancy isn't exactly something I'm comfortable with."
        jump melodyhub_main

    
    label HMEL10:
        #HMEL10
        show melody sprite happy
        Melody "You want to know about my dreams? I feel like we're at a sleepover or something..."
        $ cinematic = True
        Narrator "She purses her lips in thought, which seems out of character for someone usually so put together."
        Melody "For now? Graduating. This place has been great but I think we're all over it. Wherever we end up I'm sure we'll all be a lot happier."
        Melody "Maybe they'll put you and me somewhere close so we can visit… Wait, where do you want to end up?"
        menu:
            "Somewhere in the city.":
                Melody "Oh, me too. Maybe they'll take both of us. With that many people around I'm sure we'd never get bored!"
                $ Flag_MelodySabotage = True
                pass
            "Somewhere out in the country.":
                Melody "You're the isolated type, I guess I can see that about you." 
                Melody "The countryside sounds lovely, I know a lot of old people retire out there. Not sure what there's to do for a mage though." 
                Melody "If you want to be out in the country, you're definitely the perfect candidate for it. Not my cup of tea, but you might be happy there."
                pass
            "Somewhere by the sea.":
                Melody "Oh, I had enough of that growing up. Sea air's nice but it starts to get oppressive after a while… Then again, I'm pretty picky." 
                Melody "I used to get called fussy as a kid -- seems like they called me that because I was a bit more meticulous than my parents." 
                Melody "I can see the heat and salt water doing you well though, it has a way of mellowing everything over." 
                Melody "Plus, the community is tight-knit. If you're looking to make friends, I'm sure you'd be good at it."
                pass
            
            "Somewhere in the mountains.":
                Melody "To each their own. This place is cold enough, maybe it's the altitude. I can't imagine having to deal with snow or worse, climbing." 
                Melody "You're probably more adventurous than me though. My version of a good time is a nice book and chat with a friend." 
                Melody "Sledding around and taking care of animals is… not for me."
                pass
        Melody "Still, wherever we end up, if you're close by, I'll visit. Imagine having the support of a fellow graduate. Who knows what our lives will look like next week."
        menu: 
            "Hopefully, a bit less stressful.":
                Melody "You and me both."
                hide melody sprite happy
                jump melodyhub_main
            "I'd rather not speculate.":
                Melody "Good point, I shouldn't jinx it."
                hide melody sprite happy
                jump melodyhub_main

    label HMEL11:
        #HMEL11
        Melody "Getting anxious about exams is completely normal. Try and not worry too much though." 
        Melody "If it helps, most people around here are focusing so much on their studies that they aren't being competitive about it." 
        Melody "We all just want to pass. People fail, but you're far more likely to pass if you're in a good mental state. We're all going to pass… well maybe not Xander..." 
        Melody "I'm kidding! Obviously, I hope he passes."
        menu: 
            "Thanks.":
                Melody "Of course!"
                jump melodyhub_main
            "What if I fail?":
                Melody "Friend! Trust me, you won't! And if you do, you know what the worst situation is, I mean, we were just living it."
                Melody "You go back to the Scholomance until you get put through this place again. It's a setback but you've already been through it. I pinky swear that you'll be fine."
                menu: 
                    "That's very kind.":
                        jump melodyhub_main
                

    label HMEL12:
        #HMEL12
        Melody "I haven't looked into it -- but I heard the mayor of Ilara City is going to attend our graduation event." 
        Melody "I've heard about him from a book I read, so I'm imagining that's an option for us. I hope all the spots are close together!"
        menu: 
            "I'm sure they will be.":
                Melody "Crossing my fingers!"
                jump melodyhub_main
            "Then we'll have to write letters.":
                jump melodyhub_main

    ###DIFFERENT BRANCHES OF SAME DIALOGUE###
    label HMEL13:
        #HMEL13
        Melody "It got pretty difficult, for a minute I thought I was going to lose." 
        Melody "I've probably scraped a pass. Thankfully, it's a collation of all our exam scores that we're marked on." 
        Melody "How did you do?"
        menu: 
            "It could've gone better.":
                Melody "Hmm. I'm sure you did better than you think..."
                jump melodyhub_main
            "Pretty good.":
                Melody "Glad to hear it."
        Melody "At least we can relax now."
        jump melodyhub_main
        #HMEL14


    label HMEL14:
            Melody "I'm not used to fighting, I think the combat exam might be the one I'm least prepared for." 
            Melody "What can I do except try my best. If you're looking for advice, I'm probably not the best for it. I heard Xander is good at this sorta stuff."
            menu: 
                "Right.":
                    Melody "Sorry I'm not much help here."
                    jump melodyhub_main
                
    ###END###
    ###DIFFERENT BRANCHES OF SAME DIALOGUE###
    label HMEL15:
        #HMEL15
        Melody "How'd your exam go?"
        menu:
            "Horrible. It blew up in my face.":
                show melody sprite intense
                Melody "Huh, it went that badly? I made the same potion as you and mine was fine." 
                Melody "It should've worked!" 
                Melody "Maybe Rex messed with your plants or something? I'm so angry for you!"
                menu: 
                    "You think Rex sabotaged me?":
                        Melody "Maybe I shouldn't have said that without proof. I just know he's one to tamper with things."
                        hide melody sprite intense
                        call potionfail from _call_potionfail
                        jump melodyhub_main
                    "Maybe I messed it up.":
                        hide melody sprite intense
                        show melody sprite sad
                        Melody "Hmm. It's not a complex potion and it certainly shouldn't have backfired in any way."
                        hide melody sprite sad
                        show melody sprite
                        call potionfail from _call_potionfail_1
                        jump melodyhub_main
                    
                    "I'm confused":
                        Melody "I am too."
                        hide melody sprite intense
                        call potionfail from _call_potionfail_2
                        jump melodyhub_main

            "Could've been better.":
                Melody "Aww, I'm sure you did fine!"
                jump melodyhub_main
            "It went well.":
                Melody "Oh, that's so good. We're past the halfway point. Not long until we're graduating."
                jump melodyhub_main

        label potionfail: 
            if Flag_PotionSubmitted == True:
                Melody "Hopefully, you'll still get a pass or maybe a retake option. Sorry you went through that."
                jump melodyhub_main
            elif Flag_PotionSubmitted == False:
                Melody "Did you make sure to submit everything? If you don't submit it might not be marked."
                jump melodyhub_main

            
    
    label HMEL16:
        Melody "Everyone's so nervous for the Potion Exam. I guess I've studied enough that I'm feeling pretty calm. I already know the recipe I'll be using -- it'll get me top marks, for sure."
        menu: 
            "Recipe?":
                Melody "I've always been the type to plan out things -- I'm not going to go into the exam with no recipe in mind."
                pass
            "Good for you, I guess.":
                Melody "We all have our strengths!"
                pass
        
        Melody "If you're worried, I don't mind giving you one of my other recipes, you know, as a guide. If you're interested."
        menu:
            "That would really help.":
                Melody "Oh, well here you go. Happy to help."
                play sound "audio/dialogue_information_default.mp3"
                $ cinematic = True
                Narrator "She hands you a handwritten recipe."
                Narrator "{i}Potion of Night Vision{/i}"
                Narrator "You suppose it's to help you see in the dark."
                Narrator "The instructions look rather clear, though Melody's handwriting isn't the clearest -- embellished with little stars and moons."
                $ cinematic = False
                Melody "Don't be too worried about the exam. I think if you overthink it you'll just end up anxious and unfocused."
                $ Flag_MelodySabotagedPotion = True
                jump melodyhub_main
            "Thanks, but I should be fine.":
                Melody "As long as you turn {i}something{/i} in I'm sure you'll pass."
                Melody "Anyway, don't be too worried about the exam. I think if you overthink it you'll just end up anxious and unfocused. "
                jump melodyhub_main
    ###END###

    label HMEL17:
        #HMEL17
        Melody "I'm not versed in artificing." 
        Melody "I know enough to get through the exam -- I mean, that's what most of my studying was for -- but I don't think any advice I could give you would help since I barely get it myself." 
        Melody "Maybe ask Alice, she might slide you a book or something that might help. Oh, you could check the Library."
        menu: 
            "Makes sense.":
                "Sorry..."
                jump melodyhub_main
                
            
            "Are you sure you can't help?":
                Melody "If I could, I would. I really don't want to give you bad advice -- I'd feel so guilty if something I did screwed you over."
                jump melodyhub_main
                
    

    label HMEL18:
        #HMEL18
        Melody "Oh, I think I'm like everyone else here. My magic manifesting was not pleasant." 
        Melody "I was pretty young and the town I lived in was getting a really heavy storm."
        Melody "Thunder, lightning, strong winds -- usually it wouldn't freak me out but this time I was just feeling so unsettled that I worked myself into an anxious state..."
        $ cinematic = True
        Narrator "Melody brushes her hair with the back of her hand rhythmically -- you can tell she doesn't know she's doing it. The brightness in her eyes seems dulled."
        $ cinematic = False
        Melody "I don't actually remember doing anything myself..."
        Melody "Like I remember one of my friends at the Scholomance mentioned that they felt the magic, sort of like how I do spellcasting now, but looking back there wasn't any of that." 
        Melody "I went to my room and hid under my covers and read my book. A few hours later, I emerged from my room to find that all the mirrors and windows were fogged over." 
        Melody "At first I didn't think too much of it, I just thought the storm had done something weird but when I wiped them nothing happened." 
        Melody "Every single glass object in my house was opaque, reflecting nothing. Letting nothing through -- even light."
        show melody sprite happy
        Melody "Obviously, that scared me even more and I ended up hiding under my covers again."
        Melody "My parents brought in a few mages to interview me, as they had a suspicion that I had done it inadvertently."
        hide melody sprite happy
        Melody "None of them could replicate what I did or fix it. It was quite costly to repair but I didn't get to see the new ones, I had already gone to the Scholomance by that point."
        Melody "Looking back... it wasn't the worst manifestation I've heard of. I read one instance where a mage inadvertently warped her parents across the country to a holiday spot they'd once visited." 
        Melody "When the parents got back they found most of their close friends and family had gone missing, too."
        Melody "This girl had essentially teleported her parents across the country and then done the same again when she went to get help -- over and over. Horrific, right?"
        menu:
            "Yours seems rather scary, too.":
                Melody "It really wasn't. It was expensive, though. I'm sure my mother will tell me the story until she retires. "
                pass
            "Why mirrors?":
                Melody "I have an affinity for light -- that's what the mages told me, anyway." 
                Melody "It would've been far more boring if I just manifested a little floating light like the spell I use to read -- it would be a bit more in line with my current uses for magic, though..."
                pass
        Melody "You know, magic is great to have -- but the daily applications are honestly a little boring. At least with us graduating we'll be capable of applying it in more ways." 
        Melody "Light magic's great for agriculture. I saw Tao water their plants with a water spell. Obviously, we're strong enough to protect others too -- well, maybe I'm not but I'm sure you are, same with Xander." 
        Melody "Imagine what a mage outside of the Society would look like -- what would we even get up to?"
        Melody "Probably nothing." 
        Melody "Either way, I think every mage here has an interesting story around their manifestation." 
        Melody "I'm quite curious to see whether anyone can get Eileen to tell hers. I have this fear that she'll toss me across the room like a ball if I broach the question."
        jump melodyhub_main

    label HMEL19a: 
        #HMEL19
        Melody "What a cute question!" 
        Melody "Of {i}course{/i} we're friends. Like, I can already see you and me getting super close, you know? I warm up quick."
        jump melodyhub_main


    label HMEL19b:
        Melody "We've been here like, a few days and I already feel like we've been friends forever. These little chats we have are always so fun."
        jump melodyhub_main


    label HMEL19c:
        Melody "You're certainly my closest friend here. That might not be saying much but it means a lot to me. I trust you, you know. I hope you trust me, too." 
        jump melodyhub_main



    label HMEL19d:
        Melody "Ha ha ha haha. {i}I'm in stitches.{/i} You cannot be asking me that right now."
        jump melodyhub_main

    label HMEL20:
        #HMEL20
        Melody "The idea of a bunch of faceless people managing me for the rest of my life sure isn't nice..."
        Melody "Then again, it seems like it's working out for Alice and Eileen. I'm not big on playing politics -- even if I'm smart enough to get by in that sort of world it seems the opposite of glamorous." 
        Melody "It also makes the idea of blowing stuff up seem appealing." 
        Melody "Imagine being a mage, capable of what we can all do, and you decide to sit in a boardroom all day making decisions for people you don't care about and who do not care about you."
        $ cinematic = True
        Narrator "Almost as though she's let a facade slip, she puts a smile on her face and looks you in the eye."
        $ cinematic = False
        Melody "Wait, that was a bit of a rant, sorry. I'm always optimistic, but bureaucrats, even in the mage world, seem pointless and annoying." 
        Melody "They should get real jobs, honestly."
        menu:
            "I thought you'd be interested in politics.":
                Melody "Surely not. I think authority is important, but authority should benefit everyone. I didn't mind getting sent off to the Scholomance when I was a kid but I would've liked a choice in it." 
                Melody "It seems silly that they can't devise another option for training future mages." 
                Melody "If the mages in those seats cared about what us students had to say about it then we'd be given an alternative."
                menu:
                    "Hmm.":
                        jump melodyhub_main
            "Fair point.":
                jump melodyhub_main

        #Exit









#######################
#   Xander Main Hub   #
####################### 
label xanderhub_main:
    ###################################
    ## Do not remove this portion
    show border onlayer UI 
    ###################################
    Xander "Everything alright, pal?"
    menu:
        "Tell me about where you came from.":
            call HXAN01 from _call_HXAN01
            return

        "What was it like on the farm?" if Flag_XanderFarmer == True:
            call HXAN02 from _call_HXAN02
            return

        "What happened the first time your magic manifested?":
            call HXAN03 from _call_HXAN03
            return

        "What do you think of me?":
            if Affinity_Xander < 30:
                call HXAN04a from _call_HXAN04a
                return
            else:
                call HXAN04b from _call_HXAN04b
                return

        "Heard you're the best fighter among us.":
            call HXAN05 from _call_HXAN05
            return

        "What do you think of Melody?" if Flag_MelodyMet:
            call HXAN06 from _call_HXAN06
            return
        
        "What do you think of Tao?" if Flag_TaoMet:
            call HXAN07 from _call_HXAN07
            return

        "What do you think of Aria?" if Flag_AriaMet:
            call HXAN08 from _call_HXAN08
            return

        "What do you think of Rex?" if Flag_RexMet:
            call HXAN09 from _call_HXAN09
            return

        "What do you think about the authorities we're under as mages?" if Flag_MageAuthority:
            call HXAN10 from _call_HXAN10
            return

        "What do you think of Eileen?" if not Flag_XanderEileenOpinion:
            call HXAN11 from _call_HXAN11
            return

        "What do you think of Alice?" if not Flag_XanderAliceOpinion:
            call HXAN12 from _call_HXAN12
            return

        "Are we friends?":
            if Affinity_Xander < 40:
                call HXAN13a from _call_HXAN13a
                return

            else:
                call HXAN13b from _call_HXAN13b
                return

        "What do you think of the Mage Council?":
            call HXAN14 from _call_HXAN14
            return

        "What's the Adventurer's Guild?" if Flag_AdventureGuild:
            call HXAN15 from _call_HXAN15
            return

        "Ok, so how do I find the key to the Archives?" if Quest_XanderProgress:
            call HXAN16 from _call_HXAN16
            return

        "(Exit Conversation)":
            $ result = renpy.random.randint(1, 4)
            if result == 1:
                Xander "See ya!"
                return
            if result == 2:
                Xander "Later."
                return
            if result == 3:
                Xander "Bye."
                return
            if result == 4:
                Xander "Ok, chat later."
                return

    return



    label HXAN01:
        #HXAN01
        Xander "Huh -- my past? Like where I grew up and that? Why'd you wanna know?"
        menu:
            "Because we're more than just students at the Scholomance.":
                if Affinity_Xander > 50:
                    Xander "Uh, well, we're farmers. Mom and pops have a farm down in a valley. We're not rich, but it's great soil and the winters aren't too bad." 
                    Xander "I was doing chores from when I could walk. Cows, chickens, sheep -- you name it, I was feeding it."
                    Xander "Farming's not easy. A few bad harvests and your family starves."
                    $ Flag_XanderFarmer = True
                    play sound "audio/dialogue_information_default.mp3"
                    Xander "But I loved it. Out every day, working with my hands, talking to the animals." 
                    Xander "Lots of space and fresh air. Lots of friends too -- although they were all my brothers." 
                    Xander "We're six boys and I'm... let's see…um…the fifth one. One of us was always up for a game, or a scrap. How do you think I got so good at fighting?"
                    jump xanderhub_main

                else:
                    Xander "Uh, well, I grew up on a little farm with my parents down in the valley. I have a bunch of brothers." 
                    Xander "We're tough boys. Lots of digging holes and building walls. It was pretty good. Animals like me, and I like lifting heavy stuff so… yeah."
                    play sound "audio/dialogue_information_default.mp3"
                    $ Flag_XanderFarmer = True
                    jump xanderhub_main

    label HXAN02:
        Xander "Our farm's known for its beef and milk. I'm proud of that. Cows are smart, you know." 
        Xander "We're far from the big towns. Pops has to go into town for supplies every other month. Wouldn't see him for almost a week."
        Xander "But it was never lonely in the valley. Kids from the other farms came by." 
        Xander "My brothers -- there's five of them -- always had some chore or shenanigan in mind for me. I miss the lot of them." 
        Xander "When I get back, I'll help them out again. They're probably hurting for hands."
        jump xanderhub_main


    label HXAN03:
        Xander "My manifestation? Heh -- it was actually pretty funny. Me and my brothers were building a fence for the sheep. Real hard work." 
        Xander "But we chose that day for it, because we could tell it'd be sunny and dry. There I was, sweat pouring down my face… stinging my eyes..." 
        Xander "and I just wished the fence would build itself. Really, really, wished it... and pop pop, just like that, lightning came out of the sky and destroyed the fence." 
        Xander "Ha! I couldn't believe it. Six hours of work, gone. All the sheep panicked and ran for it."

    label HXAN04a:
        Xander "I reckon you'd do well in the Mage Council. You seem to be the type they want."
        jump xanderhub_main



    label HXAN04b:
        Xander "You seem like a good person. You helped me when I really needed it... sorry I was such a mess about it all. I panicked a little bit, right?" 
        Xander "I was so focused on how bad I was at things that I didn't stop and think that my talents might not be like Melody's or Tao's. Weird, right, before I got sent to the Scholomance, I never really compared myself to others..." 
        Xander "I guess I didn't need to."
        jump xanderhub_main

    label HXAN05:
        Xander "Ha! Wanna have a scrap for fun?"
        menu:
            "What's wrong with you?":
                Xander "Oh c'mon, don't be a wimp."
                menu:
                    "I'm not a wimp.":
                        Xander "Yea, right." 
                        Xander "Remember back at the Scholomance, when we used to have those interhouse fighting tournaments? I won a few, you know. Could've gone all the way to the top, but they kicked me out because I couldn't keep my grades up."
                        pass

            "No way, because you'd beat me for sure.":
                Xander "Ha! You can hold your own. I can tell." 
                Xander "I could've been a Scholomance champion, you know? I competed in the interhouse fighting tournaments." 
                Xander "Eileen told me I had what it takes to go all the way. But they kicked me out because I couldn't keep my grades up."
                pass
        Xander "I was so bummed. I never cared about the titles… It was about the thrill."
        Xander "I'm all intuition. I don't do well when I have to think about everything. Neither does my magic. I just wanna go -- {i}pop, pop, pop{/i} -- and see what happens."
        Xander "You ever feel like that? All cooped up. All this spark but nothing to ignite?"
        menu: 
            "I like to keep a level head.":
                Xander "Guess not..."
                jump xanderhub_main
            "Sometimes. I guess I'll have to hold out until graduation.":
                if Affinity_Xander > 50:
                    Xander "Or find other ways to get the energy out."
                    menu:
                        "Pretty direct.":
                            show xander sprite shy
                            Xander "I didn't mean for it to come out like that..."
                            hide xander sprite shy
                            Xander "Anywho lets talk about somethin' else."
                            jump xanderhub_main
                        "If only it was that easy.":
                            Xander "I know, right?"
                            jump xanderhub_main
                else:
                    Xander "You'll make it."
                    jump xanderhub_main
    
    label HXAN06:
        Xander "Mel?"
        if Day0Afternoon or Day0Night or Day1Afternoon or Day1Morning or Day1Night or Day2Morning or Day2Afternoon or Day2Night or Day3Morning or Day3Afternoon or Day3Night or Day4Morning or Day4Afternoon or Day4Night or Day5Morning or Day5Afternoon or Day5Night or Day6Morning or Day6Afternoon or Day6Night:
            Xander "She's always nice when I ask her stuff. Seems like a genuine person. I think anyone who's nice should do great in life."
            jump xanderhub_main
        else: 
            Xander "I like her. She tried to help me with the potions exam. I didn't do too well, but she still tried."
            jump xanderhub_main
            
    label HXAN07:
        Xander "Tao is a whiny, spoiled rich kid. Wouldn't last a minute on a farm." 
        Xander "I don't hang out with them. One time -- just that one time -- I cheated on a test and Tao ratted me out. Until then I liked them..." 
        Xander "Friends should stick together, you know? I'm not gonna trust someone like that again."
        menu:
            "That bad?":
                Xander "Well, it sure wasn't good."
                jump xanderhub_main
            "Sounds like a tough situation.":
                Xander "Damn right."
                jump xanderhub_main

    label HXAN08:
        Xander "Aria? Euh, she's from the country, like me. Do you think she'd like an Owlcat if I caught her one?"
        menu: 
            "You'd go out of your way like that?":
                if Affinity_Xander < 40:
                    Xander "She's the only one who loves animals as much as I do. She'd take care of it."
                    jump xanderhub_main
                else: 
                    Xander "I wanna see the look on her face. She'd love it. Aria's so… sweet and kind. She doesn't put on airs." 
                    Xander "And she's smart."
                    $ cinematic = True
                    Narrator "He looks you dead on. You realise for once, he's serious."
                    $ cinematic = False
                    Xander "She is. The others don't think so, I heard them talking shit. But one time, I saw her grow a tree through a stone wall. Ha!" 
                    Xander "The wall broke right in half like stale bread. How'd she do that? I haven't been able to talk to her since. She makes me too nervous."
                    jump xanderhub_main

    label HXAN09:
        Xander "Rex? I don't mind him, but I avoid him. Trouble has a way of finding him. Rex has a bad reputation here." 
        Xander "He's not a bad guy, he just can't get along with anyone, especially the teachers. I just don't get how he survives without any friends." 
        Xander "Anyway -- I got to focus on graduating. Rex'll be nothing but a distraction with his antics."
        $ Flag_MageAuthority = True
        jump xanderhub_main

    label HXAN10:
        Xander "Um, authority's not a bad thing, because the mages need a leader." 
        Xander "Someone that tells them how to work together. Where I'm from, everyone has their role to play, and that's how we survive."
        "I don't mind following a leader with a good plan."
        jump xanderhub_main

    label HXAN11:
        Xander "You wanna know what {i}I{/i} think of Eileen?"
        if Quest_XanderComplete:
            Xander "She scares me. Someone told me she's not just a teacher. Her real job is to handle mages for the Council." 
            Xander "Mages that are strong enough to wreak havoc but don't follow the rules. The Council hates that." 
            Xander "Eileen's job is to sort them out if they're the destructive kind. If we ever step out of line like that, she'll be sent to take care of us."
            menu: 
                "What do you mean, “take care”...":
                    Xander "Yea, I mean kill. Don't be a baby. Why else would they be making her that huge statue?" 
                    Xander "If I needed a powerful mage to keep other powerful mages in line, I'd try to stay on her good side, right?" 
                    Xander "Give her rewards and stuff. That's the story behind her statue. Or so I heard."
                    jump xanderhub_main

            
        elif Day0Night or Day0Afternoon or Day1Afternoon or Day1Morning or Day1Night:
            Xander "She watched me do a combat test back at the Scholomance." 
            Xander "Just sat there staring the whole time. I'm pretty sure she doesn't like me."
            jump xanderhub_main

        
        else:
            $ Flag_XanderEileenOpinion = True
            Xander "I never expected Eileen to give me advice. She's real intimidating." 
            Xander "And you know what the weirdest part is? I think she's right. I'm not good at anything other than fighting." 
            Xander "Neither is she when you get down to the heart of it. I wonder if she'd take on an apprentice? There's no way I'm passing all my exams, so maybe another path is out there."
            menu: 
                "You'd want that?":
                    Xander "I dunno. I just know I'm not cut out for this place."
                    jump xanderhub_main
                
                "Probably not. She seems the lonely type.":
                    Xander "Everyone needs someone. Learned that one the hard way."
                    jump xanderhub_main

    label HXAN12:
        Xander "Heh… Alice reminds me of a hen we have on the farm. Runs around clucking at everyone about everything, but never laid one egg." 
        Xander "I dunno how much help she's been. She keeps telling me to study, but never tells me what I'm doing wrong."
        $ Flag_XanderAliceOpinion = True
        jump xanderhub_main 

    label HXAN13a:
        Xander "I'd say we're friends, right?" 
        Xander "We're all at the Summit together, same with Melody and Aria. It's not a competition if we're all trying to pass, right?"
        Xander "Right?"
        menu: 
            "Of course.":
                jump xanderhub_main


    label HXAN13b:
        Xander "Yea, you're my buddy. You never held my freak outs against me." 
        Xander "And anyone who went through what the Scholomance put us through is my friend. Well, almost everyone."
        jump xanderhub_main

    label HXAN14:
        Xander "The Mage Council? My plan is to lay low after Scholomance, and hope they won't notice me. The last thing I wanna do is have to show up to all those functions." 
        Xander "To be honest, my dream since I was a kid was to join an Adventure Guild. I wonder if I can still do that after graduation..."
        $ Flag_AdventureGuild = True
        menu:
            "I'd hope so. Seems like a waste otherwise.":
                Xander "Damn right."
                $ Affinity_Xander += 5
                jump xanderhub_main

    label HXAN15:
            Xander "When I was a kid, adventurers from the Guild travelled through the valley all the time. Sometimes, pops put them up in our barn."
            menu: 
                "What does the Adventure Guild do?":
                    Xander "If a town or village is dealing with an unusual problem, like a great beast or something, they call the Guild."
                    Xander "The Guild sends Adventurers to deal with the situation. Pays them well and gives them special privileges, too! Well, while they're on the job."
                    menu:
                        "Why do you want to join so badly?":
                            Xander "It's hard to explain. Like, I don't think about it every day, but I also never forget it." 
                            Xander "When I daydream, it's usually about the Guild. I respect how they fight to protect others, not just for themselves."
                            $ Affinity_Xander += 5
                            menu: 
                                "Sounds like a hard life.":
                                    Xander "Maybe. Let me tell you something really weird. I've had my fortune read, you know. An elder in the valley had the gift. She told me I'd die in combat one day." 
                                    Xander "My brother thought she probably meant in some village bar brawl. But after the Scholomance, I'm not so sure." 
                                    Xander "I figure, if I can get a job in combat, I could get better at it. Then, I might stand a chance of changing my fate when the day comes."
                                    jump xanderhub_main
                        "Sounds exclusive and hard to get in.":
                            Xander "You got a nose for these things, heh? You're not wrong." 
                            Xander "I've only ever seen one or two adventurers that could do magic, but they were never human, usually elves or horned." 
                            Xander "But I figure, I'm a mage that can fight. There's a first time for everything, right?"
                            jump xanderhub_main
    
    label HXAN16:
        Xander "Glad you're helping me. The spell I used to hide it split it into several pieces that are scattered around the room." 
        Xander "No matter what I do, I just can't get the key to reappear whole."
        Xander "Can you try, if you got enough mana? Cast the finder spell to locate the pieces of the key." 
        Xander "Once you've found all the pieces, they should just combine magically."
        Xander "Saints... who came up with this crap. I get we're in a magic castle but... c'mon."
        jump xanderhub_main


            











        
                    



        



            







#######################
#   Aria Main Hub     #
####################### 
label ariahub_main:
    ###################################
    ## Do not remove this portion
    show border onlayer UI 
    ###################################
    Aria "Did you want to discuss something?"
    menu:

        "Tell me about where you came from...":
            if Affinity_Aria < 30:
                call HARI01a from _call_HARI01a
                return
            else: 
                call HARI01b from _call_HARI01b

        "What happened the first time your magic manifested?" if not Day0Night or Day1Morning or Day1Afternoon or Day1Night:
            call HARI02 from _call_HARI02
            return

        "What do you think of me?":
            if Quest_AriaComplete:
                call HARI03a from _call_HARI03a
                return

            else:
                call HARI03b from _call_HARI03b
                return

        "Are we friends?" if not Day0Night:
            if Day2Morning or Day2Afternoon or Day2Night or Day3Morning or Day3Afternoon or Day3Night:
                call HARI11a from _call_HARI11a
                return

            elif Day4Morning or Day4Afternoon or Day4Night or Day5Afternoon or Day5Night or Day6Morning or Day6Afternoon or Day6Night:
                call HARI11b from _call_HARI11b
                return
            
            else: 
                call HARI11c from _call_HARI11c
                return

        "What do you think of the Mage Council?" if Location == "Greenhouse":
            call HARI12 from _call_HARI12
            return

        "What do you think of Melody?" if Flag_MelodyMet:
            call HARI05 from _call_HARI05
            return

        "What do you think of Tao?" if Flag_TaoMet:
            call HARI06 from _call_HARI06
            return

        "What do you think of Xander?" if Flag_XanderMet:
            call HARI07 from _call_HARI07
            return

        "What do you think of Rex?" if Flag_RexMet:
            call HARI08 from _call_HARI08
            return
            

        "Tell me more about the Ents" if Quest_AriaComplete:
            call HARI04 from _call_HARI04
            return

        "What do you think of Eileen?" if not Flag_AriaEileenOpinion:
            call HARI09 from _call_HARI09
            return

        "What do you think of Alice?" if not Flag_AriaAliceOpinion:
            call HARI10 from _call_HARI10
            return

        "Tell me more of what happened in the forest." if Quest_AriaComplete:
            call HARI14 from _call_HARI14
            return

        "What's the deal with the Great Mage Tree?" if not Day0Afternoon and not Day0Night and not Day1Morning and not Day1Afternoon and not Day1Night:
            call HARI17 from _call_HARI17
            return

        "What's with you and the forest?" if Quest_AriaProgress or Quest_AriaComplete:
            call HARI16 from _call_HARI16
            return

        "Do you want to be a powerful mage?" if not Day0Night:
            call HARI15 from _call_HARI15
            return

        "How do you see your life after Scholomance?" if Day4Morning or Day4Afternoon or Day4Night or Day5Afternoon or Day5Night or Day6Morning or Day6Afternoon or Day6Night:
            if Quest_AriaComplete:
                call HARI18a from _call_HARI18a
                return
            else:
                call HARI18b from _call_HARI18b
                return

        "(Exit Conversation)":
            $ result = renpy.random.randint(1, 4)
            if result == 1:
                Aria "Bye for now."
                return
            if result == 2:
                Aria "Ok, talk later."
                return
            if result == 3:
                Aria "Goodbye."
                return
            if result == 4:
                Aria "Ok, see you later."
                return


    return
    
    



    label HARI01a:
        Aria "My childhood? Um, well, I'm from a pretty small town up in the mountains, far from here. Not sure you'd relate."
        menu:
            "I still want to hear about it.":
                pass
            "I relate.":
                pass
        Aria "Back home, I guess you'd say we're old fashioned. We know we have to depend on each other to get by. We only get supplies in the spring and summer. Mountain paths get blocked up quick in the winter."
        Aria "Pops sells herbal potions and mum hunts. We live a bit outside the town, higher up than anyone else. Not by choice, you know." 
        Aria "My parents married in secret when my brother was born."
        Aria "Some people in the town didn't think they should've married at all, so they went off on their own." 
        Aria "I reckon they did alright for a while. But when I came along, the elders said I came into the world under dark signs." 
        $ cinematic = True
        Narrator "You notice Aria looking down, her expression troubled. Her fingers play with the seams of her skirt, picking and picking. When she notices you watching her, she forces a smile."
        $ cinematic = False
        Aria "The day I was born the town had its first earthquake. It shook the town so bad. An elder's home was destroyed." 
        Aria "They were all scared of me after that."
        Aria "It was so unfair." 
        Aria "I spent a lot of time looking down on my town, questioning what made them so different from me." 
        Aria "I found my answer the day my magic manifested. My parents didn't like the idea of the Scholomance, they thought it would change me. I thought I didn't have any choice but to go..." 
        show aria sprite sad
        Aria "Turns out I was right. Maybe they were, too."
        show aria sprite sad
        menu: 
            "You were just a child.":
                Aria "I know I caused that earthquake. The elder was right."
                $ Affinity_Aria += 5
                pass
            "Do you think you caused the earthquake?":
                Aria "I'm certain of it."
                pass
        menu: 
            "...":
                jump ariahub_main



    label HARI01b:
        Aria "We're from a mountain town, far from here. My family lived higher up than everyone else in town." 
        Aria "It was kind of like the four of us, against the world. It made me happy in a weird way." 
        Aria "My parents never told my brother and me what people said about us."
        Aria "My parents got married in secret when my brother was born." 
        show aria sprite sad
        Aria "Back home, we're very traditional and lots of people didn't think they should've married because they're from different religions." 
        Aria "They told mum and pops that their kids would be born weak and sick. It didn't help that when I was born, the town had its first earthquake." 
        Aria "It shook the town so bad. An elder's home was destroyed. They were all scared of me after that."
        hide aria sprite sad
        Aria "But still, I guess I'm lucky I had my pops. When my magic manifested, pops knew exactly what it was. He asked the schoolmistress what he should do." 
        Aria "She told him I had to go to Scholomance."
        Aria "I wasn't sure about it. It was a strange place, far from everything I knew. But I thought that if I became a mage, I could help the people I care about." 
        Aria "The school would teach me how." 
        Aria "But I must be doing it wrong, because my powers are getting more and more chaotic. It's like a wild animal that just does what it wants." 
        Aria "It's me, but it's not me."
        menu: 
            "You feel like you aren't in control?":
                Aria "I'm {i}not{/i} in control. It's like..."
                Aria "Imagine walking down a busy road and suddenly a tree falls."
                Aria "Except, it happens constantly. Every time you're on that busy street a tree falls."
                Aria "And these trees are old, thick, goliaths, they've stood for millenia, nothing could break them."
                Aria "And yet every time you're on that street, one falls."
                Aria "You're the problem. You can't figure out exactly how, but you know it's you."
                Aria "I know it's me. Everyone knows it's me."
                Aria "So while everyone hates the Scholomance... Saints, I hate the Scholomance..."
                Aria "It's bittersweet, you know? The reality is what's for the better isn't what I want."
                Aria "Is me graduating going to put more people in danger?"
                menu:
                    "Do you want me to answer that for you?":
                        Aria "I think I already know the answer."
                        pass

                    "I know it won't.":
                        Aria "You're sweet. I appreciate you saying that."
                        $ Affinity_Aria += 5
                        pass
                Aria "Thanks for listening... I get a bit sentimental when I think of home."
                Aria "I miss the mountains, the way the air feels up there. It's... peaceful."
                Aria "The Summit sort of reminds me of it all. Especially when I'm around the Mage Tree."
                Aria "I can't tell if it's trying to soothe me, or if it's just scared. But I keep going back to it... sort of messed up."
                Aria "I guess it's my way of coping. Finding comfort in the chaos."
                Aria "Anyway... I got off topic. Did you want to ask something else?"
                menu: 
                    "...":
                        jump ariahub_main



    label HARI02:
        Aria "Manifestation? Well, the first time my magic manifested, no one but pops saw." 
        Aria "I remember sitting in our garden, just a few patches of dry dirt where we grew food in the summer." 
        Aria "I just... I wished we had more food. That way mum wouldn't have to spend so much time hunting. I pictured it, you know?" 
        Aria "A garden overgrown with food. Desperate. Eyes closed shut. I almost jumped out of my skin when my pops started shouting." 
        Aria "The garden was spitting vegetables from the ground. Carrots and potatoes shooting up like popcorn from the dirt, soon I couldn't see any dirt at all."
        show aria sprite sad
        Aria "Pops just looked at me. I didn't know what he was thinking but I was terrified. I'd lived my whole life thinking an earthquake was my fault and now I was sure I was doing this." 
        Aria "He grabbed my shoulder gently but I felt like he was pulling me out of the air. He told me never to tell any outsiders I could do this." 
        Aria "The town would accuse us of stealing food. I heard the fear in his voice but I was grinning. I could finally help my family, I wasn't just another mouth to feed."
        menu: 
            "Your dad sounds scary.":
                Aria "You don't get what I'm trying to say."
                Aria "Even after all the potions and spells we learned, nobody ever told me I had a river inside me." 
                Aria "I know I'm just at the beginning of knowing what my new abilities mean, but I'm not afraid of them anymore." 
                Aria "I know it'll be a hard road but I reckon I can control it with the right help."
                pass

            "Wish I could have seen that.":
                if Quest_AriaComplete == True:
                    Aria "It's been a long way from the mountains to here. I never felt like I fit in at Scholomance." 
                    Aria "But after that night in the forest, I see it all different."
                    Aria "With the ent I felt another episode coming on, but I didn't panic. It was like..." 
                    Aria "this river. Fast. Warm. A river ran from me to him. My mind traveled the river. Then we talked. Not in words, in pictures."
                    Aria "Even after all the potions and spells we learned, nobody ever told me I had a river inside me." 
                    Aria "I know I'm just at the beginning of knowing what my new abilities mean, but I'm not afraid of them anymore." 
                    Aria "I know it'll be a hard road but I reckon I can control it with the right help."
                    pass

                else:
                    Aria "The Scholomance taught me magic can grow life. But I'm starting to see magic is somehow always more than you bargained for."
                    Aria "I want to help people, but I can't stop my magic from hurting them." 
                    Aria "I destroyed part of the Archive by just daydreaming -- what would've happened if someone was standing there?"
                    Aria "I hate it."
                    pass
        menu:
            "...":
                jump ariahub_main



    label HARI03a:
        Aria "I still can't believe you found me in the woods. No one has ever done that for me. Your energy is so positive, it'll come back to you, just watch!"
        $ Affinity_Aria += 5
        jump ariahub_main



    label HARI03b:
        Aria "You? Of course I think you're nice. You can be weird too, but that's what I like about you."
        Aria "Let's chat more often. Everyone else is so wrapped up in exams, it gets so lonely."
        jump ariahub_main



    label HARI11a:
        Aria "I'd hope so! I'd love to be friends with you. It'll be tough doing this week alone."
        menu: 
            "Guess we're friends.":
                show aria sprite happy
                Aria "I had a good feeling about you. Where I'm from, we rely on each other to get by." 
                Aria "Anytime you need help, I'll do what I can."
                hide aria sprite happy
                $ Affinity_Aria += 5
                jump ariahub_main
            "I'd rather just study.":
                show aria sprite sad
                Aria "Ah, no problem. But you don't have to be a stranger, you know."
                hide aria sprite sad
                jump ariahub_main           



    label HARI11b:
        Aria "I'm glad you asked... I've been building up to just talking to you about it." 
        Aria "I just... I want to let you know, you're a real friend. No one's really talking to me after some incidents my magic caused." 
        Aria "They think I'm bad luck or something. It's nice to have someone who enjoys chatting with me."
        menu: 
            "Don't listen to them.":
                pass

            "That's cruel.":
                pass

        Aria "I'm kind of used to it. In my hometown, some people really looked down on my family." 
        Aria "Got to keep your head up. Don't let them win. That's what mum says."
        menu: 
            "I agree with your mum.":
                Aria "I'm trying my best, I really am."
                jump ariahub_main

            "You'll find a way to fix it.":
                Aria "What I'm really worried about is my exams. What if I lose control and fail?"
                menu: 
                    "We're in the same boat. We could all fail and get shipped back to the Scholomance.":
                        Aria "You're just trying to make me feel better."
                        jump ariahub_main



    label HARI11c:
        Aria "Why wouldn't we be?"
        jump ariahub_main


    label HARI12:
        Aria "If you think life at the Scholomance is tough, what do you reckon is coming after?" 
        Aria "I imagine more rules, more Council meetings, reporting to a dozen mages like Eileen." 
        Aria "It's really not my cup of tea at all. Ties my stomach in knots just thinking on it."
        Aria "Want to hear another secret? What I want most in the whole world is to live alone, deep in the forest." 
        Aria "In a warm cabin, full of herbs and flowers." 
        Aria "Animals coming and going as they like." 
        Aria "I'm safe. I can't hurt anyone." 
        Aria "No one can hurt me."
        jump ariahub_main

    
    label HARI05:
        Aria "Oh, Melody? I don't know, I'm sure she doesn't like me much because I'm not from the city." 
        Aria "I think when she's more secure in herself, she'll let herself trust others."
        menu: 
            "That's... harsh.":
                pass
        Aria "Back at Scholomance we were in some of the same classes. Mel probably doesn't even remember I was there." 
        Aria "One time during an atelier, her practice wand broke and she started to cry. I was surprised because she's supposed to be so tough..."
        menu:
            "Surprised that her wand broke?":
                Aria "Yea, she had to start the enchantment all over again but there wasn't enough time." 
                Aria "That stuff happens to us all the time, but not to her."
                pass

            "Surprised that she cried?":
                Aria "A bit. We only got minor discipline for stuff like that. She had to use a simpler spell because there was no time left." 
                Aria "But it was like her life was crumbling before her eyes."
                pass
        menu:
            "Can you elaborate on why you think she can't trust others?":
                Aria "She's nice enough, but she's not a genuine person. She's always sizing you up, looking for your weakness." 
                Aria "Mel does it so often that she can't believe other people aren't doing it to her." 
                Aria "It makes her put up walls."
                pass
        menu:
            "But how do you know this?":
                Aria "I notice a lot of things." 
                Aria "People think I'm stupid because I wear pretty dresses and have bigger things to worry about than grades."
                Aria "Mel lets her facade down around me. She knows I'm not a threat."
                Aria "But I can see the cracks. I can see how hard she tries to keep it all together."
                Aria "It's like she's holding a fragile glass sculpture, and she's terrified of it shattering."
                jump ariahub_main
    
    label HARI06:
        Aria "Tao is a sweetheart under all that, I can feel it." 
        Aria "It's just that they never put anything above being the best at school."
        Aria "I know I'll never be the best mage here. But there's more to life than getting the best grades." 
        Aria "What about being a good friend that you can rely on?"
        Aria "If only they'd keep secrets. Instead, they'd try to use it against you." 
        Aria "I like Tao but I can't trust them, which makes me sad."
        jump ariahub_main

    label HARI07:
        Aria "Xander? I'd like to get to know him better but he's so quiet." 
        Aria "I tried to offer him some stew one time, but he all but ran from me!"
        Aria "He's moody during exams, I think he's really stressed." 
        Aria "If we were friends I'd tell him that it's not the end of the world if you can't memorize everything." 
        Aria "Sometimes you can work around it."
        jump ariahub_main

    label HARI08:
        Aria "Rex never seems happy." 
        Aria "I feel bad for him, he really seems to hate it here, and no matter how much he rebels they always deal with him." 
        Aria "I've tried to make friends with him a few times but he won't have it."
        Aria "He reminds me of a mountain goat. A headstrong loner that won't hesitate to charge at you when they're mad." 
        Aria "When I have time, I'll make him a fire flower or something. I'm sure he'd feel better."
        jump ariahub_main

    
    label HARI04:
        Aria "I'm as surprised as anyone the ents like me."
        menu: 
            "What was it like talking to an Ent?":
                Aria "It takes them forever to finish a thought. Really stubborn, the lot of them."
                menu: 
                    "Good thing you're patient.":
                        Aria "It's the other way around, more like. The ent that held me was 645 years old." 
                        Aria "To him we're just babies. We'll be gone in the blink of an eye. Got the feeling he was sorry for me."
                        pass

            "What did you think the Ent wanted?":
                Aria "He asked me who I was, chatting to him like that."
                menu: 
                    "What did you say?":
                        Aria "Erm, I said my name. Then I asked him his name." 
                        Aria "His name was very, very long, too long. I only remember how it started, so I call him Nert in my head."
                        pass
        menu: 
            "Do you realize how rare what you did was?":
                Aria "Hm, it felt natural to me. Living things always have something to say." 
                Aria "Something to ask Nert when I see him next."
                $ Affinity_Aria += 10
                jump ariahub_main
    
    label HARI09:
        Aria "I don't know why Eileen dislikes me so much." 
        Aria "She says I need to stop the daydreaming."
        Aria "It's not fair, I never set out to hurt anyone."
        Aria "Doesn't intention matter to her?"
        show aria sprite sad
        Aria "She told me that I was a weak mage and would get someone killed one day. I can feel her watching me and it makes me really anxious."
        hide aria sprite sad
        $ Flag_AriaEileenOpinion = True
        jump ariahub_main

    label HARI10:
        Aria "You know, Alice collected me from home and took me to the Scholomance." 
        Aria "I know mum and pops wanted to ask her if they'd ever see me again." 
        Aria "I don't remember what we talked about on our way to the school. She was chatting away, and I just nodded." 
        Aria "I was so scared." 
        Aria "First time away from home and all that. But she made me feel like magic was the biggest opportunity of my life." 
        Aria "She told me not to be ashamed." 
        Aria "I wouldn't have tried so hard to be a good mage if it wasn't for Alice."
        Aria "I don't know what makes her so kind but I'm grateful for it. I've always felt like she's been on my side."
        $ Flag_AriaAliceOpinion = True
        jump ariahub_main
    
    label HARI14:
        Aria "Before you found me, I just... wandered." 
        Aria "I wasn't using the light spell anymore. Stupid, maybe, but I wanted the dark." 
        Aria "I wasn't going back to the Summit so it didn't matter."
        Aria "I don't know how much time passed. A voice in my gut said the forest was watching me to see what I'd do." 
        Aria "Animal noises everywhere and..." 
        Aria "other sounds I didn't know. When I couldn't run any more, I sat down in a patch of brush."
        menu: 
            "That's when you met the Ent?":
                Aria "Not right away. I lay my head down and let myself drift." 
                Aria "My whole body was hot and the flowers started to bloom from my head down to my toes." 
                Aria "Ones I'd never seen before. That's when he started to grumble."
                pass
            "How scared were you?":
                Aria "Scared enough. I'd still rather be there than trapped at the Summit." 
                Aria "My heart was beating out of my chest, though."
                pass            

        Aria "The Ent lifted me up. I knew what his intentions were." 
        Aria "He just wanted to meet me. It was like he was holding my magic, and my magic was holding me." 
        Aria "I began to see what my power could be."
        jump ariahub_main

    label HARI17:
        Aria "He's the best part of this place. At first I was afraid of him, either he'd aggravate my... condition… or I'd hurt him somehow."
        Aria "But he makes me so calm. I feel almost like myself again." 
        Aria "He's a very special being. I feel he's been enchanted, but it's more than that."
        menu: 
            "You can sense that?":
                pass

        Aria "Oh yes. If I ever get out of this place, I'd love to learn spells that can make trees so... human."
        jump ariahub_main

    label HARI16:
        show aria sprite happy
        Aria "The others are scared of the forest, I can tell. It's nicer than anywhere in the Summit." 
        Aria "I grew up watching all kinds of animals in the woods." 
        Aria "The thing with animals is that they're never stressed, never in a hurry, they take their time..." 
        Aria "But if you threaten their territory, they are fierce protectors. I know it's a funny thing to say but I look up to them."
        Aria "Look at the trees." 
        Aria "The forest has never been touched as long as the Summit's been here." 
        Aria "You got to wonder what creatures live in woods as old as these."
        hide aria sprite happy
        jump ariahub_main


    label HARI15:
        Aria "Everyone here wants magical power more than anything. But if you can be blessed with magic, can't you be cursed too?" 
        Aria "The town elders told my mum I'd be born sick because my pops was a different religion than her."
        menu: 
            "What do the teachers say?":
                Aria "They tell me I'm not working hard enough. I'm doing everything I can." 
                Aria "Maybe I'm not mage material. But I can't go home like this, either."
                jump ariahub_main
            "That's your fear talking.":
                Aria "The day I was born, an earthquake leveled several houses in town and they said it was my fault." 
                Aria "And now, my magic is out of control. Aren't I sick after all?"
                menu: 
                    "Why do you think your powers are cursed?":
                        Aria "I know I needed to go to the Scholomance to learn how to handle my magic." 
                        Aria "I'm afraid my magic is stronger than me. It'll do something worse than an earthquake." 
                        Aria "Something really, really, bad."
                        jump ariahub_main

    label HARI18a:
        Aria "It's all different since the forest."
        Aria "I get now I'm just part of a big mystery that's happening around us all the time." 
        Aria "I'm not good or evil. It's my choices that make the world better or worse. If I deal with my fear, my magic will help me find my place." 
        Aria "I reckon I'm starting to get what it means to be a mage."
        jump ariahub_main
    
    label HARI18b:
        Aria "Scared and confused. I can't sort it out, if I'm honest." 
        Aria "I can't fix my magic. And I don't see what place a broken mage has in this world."
        jump ariahub_main



        











#######################
#   Tao Main Hub      #
####################### 
label taohub_main:
    ###################################
    ## Do not remove this portion
    show border onlayer UI 
    ###################################
    Tao "What did you want to discuss?"
    menu:
        "(Botany)":
            call HTAO014 from _call_HTAO014
            return

        "(Artificing)":
            call HTAO13 from _call_HTAO13
            return

        "(Potions)":
            if Quest_TaoComplete:
                call HTAO12a from _call_HTAO12a
                return

            else:
                call HTAO12b from _call_HTAO12b
                return

        "What was your childhood like?":
            if Quest_TaoComplete:
                call HTAO01a from _call_HTAO01a
                return

            else:
                call HTAO01b from _call_HTAO01b
                return

        "How did your magic first manifest?":
            call HTAO02 from _call_HTAO02
            return

        "What do you think of Melody?" if Flag_MelodyMet:
            if Quest_TaoComplete:
                call HTAO03a from _call_HTAO03a
                return
            else:
                call HTAO03b from _call_HTAO03b
                return

        "What do you think of Rex?" if Flag_RexMet:
            if Quest_TaoComplete:
                call HTAO04a from _call_HTAO04a
                return
            else:
                call HTAO04b from _call_HTAO04b
                return

        "What do you think of Aria?" if Flag_AriaMet:
            if Quest_TaoComplete:
                call HTAO05a from _call_HTAO05a
                return
            else:
                call HTAO05b from _call_HTAO05b
                return

        "What do you think of Alice?":
            if Quest_TaoFailed:
                call HTAO08a from _call_HTAO08a
                return
                        
            elif Quest_TaoComplete:
                call HTAO08b from _call_HTAO08b
                return

            else:
                call HTAO08c from _call_HTAO08c
                return
        
        "What do you think of Xander?" if Flag_XanderMet:
            if Quest_TaoComplete:
                call HTAO06a from _call_HTAO06a
                return
            
            else:
                call HTAO06b from _call_HTAO06b
                return
        
        "Can you tell me about your father?" if Flag_C3TaoFather:
            if Quest_TaoComplete:
                call HTAO11a from _call_HTAO11a
                return

            else:
                call HTAO11b from _call_HTAO11b
                return

        "What do you think of Eileen?" if not Flag_TaoEileenOpinion:
            call HTAO09 from _call_HTAO09
            return

        "(Mage Council)":
            call HTAO10 from _call_HTAO10
            return

        "What do you think of me?":
            if Quest_TaoComplete:
                call HTAO07a from _call_HTAO07a
                return
            else:
                call HTAO07b from _call_HTAO07b
                return
        
        "What happened with you and Xander?" if Flag_TaoXanderFriendship:
            if Quest_TaoComplete:
                call HTAO15a from _call_HTAO15a
                return

            else:
                call HTAO15b from _call_HTAO15b
                return

        "(Exit Conversation)":
            $ result = renpy.random.randint(1, 4)
            if result == 1:
                Tao "You're going? Hmm."
                return
            if result == 2:
                Tao "Go ahead."
                return
            if result == 3:
                Tao "Goodbye."
                return
            if result == 4:
                Tao "..."
                return            












        












    return

    label HTAO014:
        Tao "Botany? Just cut things up. It's all about being optimal."
        Tao "There should be a recipe book somewhere in your things that help you with that sort of thing. If not, perhaps check the archive."
        Tao "Either way, do you mind?"
        jump taohub_main

    
    label HTAO13: 
        Tao "Oh... I cannot help you there." 
        Tao "Artificing isn't really my forte, I just have a selection prepared and hope that'll get me the grade I need." 
        Tao "One of the others should know better... perhaps Rex -- as... ridiculous as he is, he has a knack for tinkering."
        jump taohub_main

    label HTAO12a:
        Tao "You should've learned how to do this years ago... that's what the Scholomance was for."
        Tao "But I suppose I'll help you. Here, this is a simple, but solid recipe. Just follow it." 
        Tao "I can't help you during the exam, though, you know? I don't want to fail due to misconduct or something dubious like that."
        jump taohub_main

    label HTAO12b:
        Tao "Why are you wasting my time? What, do you expect me to teach you so you can pass your exam?" 
        Tao "Find someone else, I have my own troubles to focus on."
        jump taohub_main
    
    label HTAO01a:
        Tao "You really want to know more about me?"
        Tao "Really? I've not had that interesting a life."
        menu:
            "I do.":
                pass
            "Yeah, maybe not.":
                jump taohub_main
        Tao "I grew up in the northern part of Viordia but my father moved us to the capital because he got a promotion at work."
        Tao "Before that he travelled around the continent similar to Eileen and Alice, making sure that all of us mages are in line and everything is 'up to standard'."
        Tao "Moving was an ordeal. I had a solid set of good friends I'll probably never see again, not the sort I competed with, just the sort who supported and knew me." 
        Tao "Settling in a large city wasn't the best and then just as soon as I made new friends I had to move again because my magic manifested."
        Tao "I couldn't sit down without causing a chill, nor could I touch anything I didn't want ice crystals to destroy."
        $ Flag_C3TaoFather = True
        Tao "I feel as though I'm ranting here but to sum it up my life was mostly boring, if anything I'm excited to get out and finally settle somewhere." 
        Tao "It'd be nice to end up somewhere close to my parents, though."
        menu: 
            "Yeah, that would be nice.":
                jump taohub_main


    label HTAO01b:
        Tao "My past? Why? What's the point of wasting time learning anything about me?"
        menu:
            "Because I'm {i}interested{/i}.":
                pass

            "Connecting with someone is never a 'waste' of time.":
                pass

            "You're right.":
                jump taohub_main
        Tao "Really?"
        menu:
            "Why else would I ask.":
                pass

            "I am.":
                pass
        $ Affinity_Tao += 10
        Tao "Fine... I had a boring upbringing, my father's also a mage, which was nice I suppose."
        Tao "It meant that when my magic manifested it wasn't as if I had no one to lean on."
        Tao "Nevertheless, why are you asking such personal questions? {i}Shoo{/i}. Surely, you have other things on your mind."
        menu:
            "({i}Shoo{/i}) ...":
                jump taohub_main

    label HTAO02:
        Tao "Why would you want to know about how my magic manifested? What do you get out of that?"
        Tao "Isn't it sort of an embarrassing ordeal for us? I'm sure more than a few mages caused a disturbance the first time their magic decided to materialise."
        menu:
            "I'm curious.":
                pass

            "You're right, it {i}is{/i} embarrassing.":
                Tao "Exactly, so why should I talk to you about it? {i}Shoo{/i}. Go away."
                menu:
                    "({i}Shoo{/i}) ...":
                        jump taohub_main

        Tao "Surprising. Uhh, I suppose when it manifested it was essentially just water magic." 
        Tao "I ruined my parents wallpaper by making it rain in our kitchen." 
        Tao "My mother was furious, she thought one of my father's enchantments was being odd but when she shooed me out so she could clean up the same thing happened in our dining room."
        Tao "After a few days of chaos the water started freezing, which caused a whole new set of problems I'm sure you understand."
        Tao "Not as embarrassing as most, but still a bit of a nuisance. I kept having blips of issues like that until I was funnelled into the Scholomance like the rest of you."
        if Quest_TaoComplete:
            Tao "Well... I suppose other's didn't have a mage father, as that part is rare."
            Tao "When my father got back he tried to keep me calm enough that he could handle my magic, teach me himself, that sort of thing." 
            Tao "Sadly, his magic is completely different from mine and hiding something like a mage in your family would almost certainly have gotten him arrested."
            Tao "So after a few horrid lessons of him trying to teach me how to use a type of magic completely opposite from his, he got Alice involved, who sent me to the Scholomance."
            Tao "I think about that very often." 
            Tao "My father didn't really seem to want me to go to the Scholomance, I suppose he was embarrassed that I wouldn't do as well as him but I suppose that shame was outweighed by his inability to help me." 
            Tao "By the time I'd left, half the living room needed skates to navigate and we hadn't had working water in a while as the pipes were frozen. My poor mother."
            menu: 
                "Sounds rough.":
                    Tao "Isn't it for everyone?"
                    jump taohub_main
        else:
            Tao "Sated, or do you also want to know what my first words were?"
            menu: 
                "{i}Sated.{/i}":
                    jump taohub_main
                "What were they?":
                    $ cinematic = True
                    Narrator "Tao shoots you a glare that reminds you, oddly enough, of Eileen's scowl. You should leave them be."
                    $ cinematic = False
                    jump taohub_main
    
    label HTAO03a:
        Tao "I don't like her, nor do I trust her. The temptation to do anything to be the best was intense in me, and it took its toll. It still does."
        Tao "I can say that behind that pretty face, there's probably something devious going on. You don't get to the top of the mountain without crushing a few ants."
        Tao "I know what it takes to get where she is, trust me, there's something amiss with her."
        jump taohub_main

    label HTAO03b:
        Tao "I can't say I detest Melody but I certainly don't like her." 
        Tao "We've been academic rivals since our first days in the Scholomance, and while I study, study, study and work for those top marks, she just seems to breeze through it all."
        Tao "There's always a cost to academic achievement and she's yet to pay it." 
        Tao "I was the top student in our first year, with her coming second, and she was top in the third year with me coming second, the trend kept fluctuating like that."
        Tao "I will beat her, cementing myself as the top student of our year. I don't care what stunts she pulls, I'm ready for it."
        jump taohub_main

    
    label HTAO04a:
        Tao "I feel rather guilty about Rex. He was friendly to me, especially after seeing I was isolated."
        Tao "I thought we could be friendly, so I taught him a somewhat..." 
        Tao "...complex spell I found in the restricted area of the Great Library in the Scholomance... he tried it, but it backfired." 
        Tao "He got in trouble with the tutors."
        Tao "They questioned where he learned that spell, obviously he said that I taught him it..." 
        Tao "I did, but I didn't want to get in trouble so I denied it and he got in more trouble for not only 'lying' but also accessing a restricted area of the library."
        menu: 
            "You accessed the restricted section of the library?":
                Tao "The more advanced the knowledge I possess, the higher the grade. That was my logic, I suppose."
                menu:
                    "I see. It makes sense that he'd hate you after that.":
                        pass

            "Makes sense he'd hate you after that.":
                pass
        Tao "He's justified to. In a... sort of odd way, it's a good thing, though." 
        Tao "The man seems on the path that'll end up with Eileen hunting him down. I've seen less volatile things in the alchemy lab." 
        Tao "He's one bad day away from blowing up the school. I don't think our friendship not blossoming caused that. "
        menu: 
            "Most likely not.":
                jump taohub_main
            "...":
                jump taohub_main



    label HTAO04b:
        Tao "Rex and I aren't on good terms, I don't have much to say about him so don't waste my time."
        menu: 
            "Why are you on bad terms?":
                Tao "He tried to sabotage one of my projects. When I saw that he would be in our graduation class I devised a spell to stop tampering specifically for him."
                Tao "it seems he didn't like that."
                menu:
                    "...":
                        jump taohub_main

            "Fine.":
                menu:
                    "...":
                        jump taohub_main
    

    label HTAO05a:
        Tao "Truly I don't mind Aria. I've never really spoken to her, but I've noticed her from afar." 
        Tao "She's powerful, I'm sure in terms of raw power she rivals some more mature mages like Eileen and Alice."
        Tao "I believe she's a little ditzy to really navigate that sort of power. I had similar issues when my power manifested."
        Tao "I've always been a little... well, not jealous exactly, perhaps a better word is envious... of how quickly people tend to like Aria." 
        Tao "She has this odd worldview about her, she's capable of seeing positives anywhere she goes... she seems uncomplicated, but I've seen when that facade breaks."
        Tao "It's hard to trust someone who is all about the bright side. You wonder if they're purposely ignoring discomforts or whether they're simply unphased by them." 
        Tao "Either way, I have nothing against Aria, but I think it's a bit too close to graduation to start any conversation."
        menu: 
            "...":
                jump taohub_main
        

    label HTAO05b:
        Tao "You want to know what I think of Aria… She's ditsy but powerful, I'll beat her in grades but if it came to a fight she'd mop the floor with everyone here other than Eileen, that much I'm sure of."
        menu:
            "Even Xander and Rex?":
                Tao "If either of them have a braincell between them, they'd agree with me. Aria is a once in a lifetime mage in raw power."
                Tao "Half of the instructors feared her at the Scholomance. I'd imagine Eileen is only here in order to have something to counteract her if she fell of the deep end."
                Tao "That's what I think of her. Can I go back to my work now?"
                menu: 
                    "...":
                        jump taohub_main
    

    label HTAO08a: 
        Tao "I don't want to talk about her." 
        Tao "What, did she send you here?"
        Tao "Leave me alone. Please."
        menu:
            "...":
                jump taohub_main

    label HTAO08b:
        Tao "With everything that went on, I think Alice has everyone's best interest at heart." 
        Tao "Despite my not liking it, I'm sure the advice she gave me is out of a place of experience."
        Tao "I was taking everything too far and close to breaking down. I still think she's overbearing, but I have a bit more respect for her."
        menu:
            "...":
                jump taohub_main

    label HTAO08c:
        Tao "Alice seems nice. I always found her dolls rather creepy, though." 
        Tao "It took me a long time to understand that she merged conjuration with Geomancy in order to create them." 
        Tao "I wonder why they're so specifically porcelain."
        Tao "Is it a wealth statement? Or a magical restriction..."
        menu:
            "...":
                jump taohub_main

    label HTAO06a:
        Tao "I'd rather not get into what happened between Xander and I. It's not relevant. Let's just say we fell out and leave it there."
        menu: 
            "...":
                jump taohub_main


    label HTAO06b:
        Tao "I'd rather not talk about Xander. Everyone knows we were friends at one point, but friends drift, especially when the difference between us is so vast." 
        Tao "There comes a point where you have to cut yourself off from the slackers in order to focus on your own work."
        Tao "It was probably for the best, people like him are intellect pits, anything smart around them catches the dumbness curse they're clearly afflicted with..."
        $ Flag_TaoXanderFriendship = True
        menu: 
            "...":
                jump taohub_main

    label HTAO11a:
        Tao "If I'm being candid with you, I don't enjoy talking about my father."
        Tao "In most cases, the first thing anyone notable talks about with me is my father. It instils a lot of pressure on me."
        Tao "I don't know of any mages who have mage children, it being a seemingly random trait means that I had a very unique experience as a teen, but it also means I never really got to define my own path."
        Tao "I don't have an excuse to not be as competent as him, after all, he's my blood so I should be able to be equal if not better than him."
        Tao "Plus, and please don't tell anyone this, I don't really know my father all too well, his job has always meant he's far from me." 
        Tao "When I was a child I lived only with my mother as his job meant he travelled around the country similar to what Eileen and Alice do."
        Tao "He'd be back every few months, but it's not like I really connected with him during that time." 
        Tao "I had my own worries, school, grades, friends... all things I never relied on him for."
        Tao "When my father got promoted I initially believed we were being blessed, he felt more like a myth than a man." 
        Tao "I wanted to actually understand where I came from. My mother and I have this complicated..." 
        Tao "....attitude." 
        Tao "She expects the best of me, both because she's a recognized academic, but also because of who my father is."
        Tao "Thus, I spent a lot of my time trying to impress this man who I never really saw, and I always managed it." 
        Tao "He'd come back, see my grades, tell my mother how well I was doing, and we'd celebrate."
        Tao "So, when he got promoted it meant he'd be spending far more time with us. We had to move, which was horrible, but at least he'd be home in the evenings."
        Tao "I barely got to spend any time with him though because a few weeks after we moved into this big new house my magic started to manifest itself." 
        Tao "I think I was in denial at first. My drinking glass froze and I fully believed that perhaps a chill did it."
        Tao "I kept hiding it, not really understanding what was happening to me because it felt like an impossibility. But sadly, no, I was a mage."
        Tao "Of course, I didn't know what would happen." 
        Tao "My father got home to wet walls and a frozen kitchen floor and instead of yelling or exclaiming or having any sort of reaction he just calmly tried to fix it."
        Tao "I expected to be shuttled off to the Scholomance, which I imagined to be this prestigious school where I'd excel, but instead he..." 
        Tao "...please don't tell anyone this, but he tried to hide it, bury it, help me control any power I had so that it wouldn't see the light of day."
        Tao "I thought it was because I was such a disappointment. I'd ruined this beautiful house, I'd ruined his reputation, and I was presenting myself as an obstacle to his career." 
        Tao "It was unfathomable, really." 
        Tao "He never left my side, he took what time he could off work so he could watch me to make sure I wasn't destroying anything."
        Tao "Eventually, the inconvenience got too much and he brought Alice into my room, who explained what was going to happen for the next seven years of my life." 
        Tao "I can still remember her sitting next to me on a perpetually cold chair and telling me that I {i}had{/i} to go to the Scholomance, {i}all mages{/i} do."
        Tao "I was happy to. School was something I was good at, school was something I could adapt to." 
        Tao "Obviously, getting there was horrid, and being there for seven years was also horrid, but at least I wasn't living in a house of people who I knew would be disappointed in me."
        Tao "However, that's also where I changed." 
        Tao "I had this idea in my mind that if I immerged from the depths of that school without being as prestigious and as successful as my father, I would've been a failure."
        Tao "I still feel that pressure. Perhaps it's because we're almost at graduation, but I still have this gut feeling that the moment I see my father something is going to happen."
        Tao "I want nothing more than to make him proud, but I don't know if I'm even a person, forget mage, he'd be proud of." 
        Tao "I'm immerging from the Scholomance with no friends, potentially no top grades, and enough mental breakdowns to put an asylum to shame."
        menu:
            "(Friends) You have me, Tao.":
                Tao "Oh."
                Narrator "Tao looks at you, and for a brief moment, smiles a wide, grateful smile."
                Tao "That means the world to me, really. Thank you."
                pass
            "(Say nothing.)":
                Tao "What will be, will be."
                Tao "It's a new start. A fresh start. I'm just glad I learned something from those seven years."
        Tao "..."
        Tao "Ah, that got a bit dark, didn't it? I'm sure you have your own pressures, but those are mine." 
        Tao "After we're out of this place, perhaps we'll have a few moments of solace to make all this seem inconsequential."
        show tao sprite happy
        Tao "Nevertheless, don't let me keep you. I'm certain you have some last minute revision or planning you want to do."
        hide tao sprite happy
        menu:
            "I will.":
                jump taohub_main


    label HTAO11b:
        Tao "What's there to know? My father works as something akin to a diplomat for Mages." 
        Tao "He's above Eileen and Alice in authority, and known well enough among mages."
        Tao "We get along, I suppose."
        menu: 
            "Makes sense...":
                jump taohub_main


    label HTAO09:
        $ Flag_TaoEileenOpinion = True
        Tao "My father told me he grew up scared of Eileen, she's sort of legendary among mages. I didn't expect her to be as... mean, as she is." 
        Tao "There is really nothing that pleases her."
        menu: 
            "...":
                jump taohub_main

    label HTAO10:
        Tao "I suppose other than the proctors, I'm the most knowledgeable about that sort of thing... My father does work in that sector."
        $ Flag_C3TaoFather = True
        Tao "From what I understand, the Mage Council dictates the jurisdiction and justification of mages." 
        Tao "All mages must be registered, all mages must act within specific parameters."
        Tao "Mages like Eileen and Alice have guiding roles, my father is in a more political position."
        Tao "We're not exactly allowed to be normal people... I suppose if they did we'd be hunted down." 
        Tao "Despite us being more powerful than a regular person, we don't exactly have numbers on our side and having supernatural abilities doesn't always mean we're accepted."
        Tao "I suppose having a body of mages watching over us is better than a regular government."
        Tao "I'd imagine a government that feared us would use us as cannon fodder in some random war. Not particularly fun..."
        Tao "I've heard that's what happens in Dawn. You know, the capital of Cerulia. They execute mages over there."
        menu: 
            "That's horrible.":
                Tao "It's not exactly pleasant to think about."
                jump taohub_main

    label HTAO07a:
        Tao "What do I think of you? Hmmn. You're... good. You stuck your neck out to help me when I needed it." 
        Tao "It would've been nice to be friends for longer, but I've come to understand that I never really treated my friends properly." 
        Tao "Perhaps we can make a change to that going forward. We'll stay in touch after the exams, surely."

    label HTAO07b:
        Tao "Why are you wasting my time? Can't you see that I'm busy, some people here are actually trying to pass their exams." 
        Tao "I barely know you, you barely know me, why do you want me to give you some half-baked assessment?"
        Tao "Actually. Here is your assessment..."
        Tao "You annoy me. F for Fail."
        jump taohub_main


    label HTAO15a:
        Tao "Ah. Xander... yes. Honestly, I have a lot of regrets when it comes to my friendship with him."
        Tao "I wouldn't say I was a very good friend, lets leave it at that. Perhaps I won't repeat the same mistake." 
        Tao "If you want to hear about how bad I was, I imagine he'll tell you."
        jump taohub_main



    label HTAO15b:
        Tao "Hmm. It's not a surprise you know that Xander and I were once friends. We were in the Scholomance for seven years, at some point you have to chat..."
        menu: 
            "We've not really met.":
                pass

            "Why'd you fall out?":
                pass
        
        Tao "All my brief friendship with Xander taught me was that students shouldn't be friends. We're competitors, through and through."
        Tao "The more time I spend wasted on other students the less time I study for myself. Why help the competition get ahead?" 
        Tao "I don't want to be stuck in some backwater village as the town mage..."
        Tao "That includes you."
        menu:
            "Likewise.":
                $ Affinity_Tao -= 10
                jump taohub_main
            "...":
                jump taohub_main



















#######################
#   Rex Main Hub      #
####################### 

label rexhub_main:
    ###################################
    ## Do not remove this portion
    show border onlayer UI 
    ###################################
    Rex "What's up?"
    menu:

        "What's your family like back home?":
            if Affinity_Rex < 40:
                call HREX02a from _call_HREX02a
                return

            else: 

                call HREX02b from _call_HREX02b
                return

        "Can you help me with artificing?":
            call HREX01 from _call_HREX01
            return

        "What happened the first time your magic manifested?":
            call HREX03 from _call_HREX03
            return

        "Why do the others say you don't want friends?" if not Flag_HREX12:
            call HREX12 from _call_HREX12
            return

        "Where did you get the idea to mess with statues?" if Quest_RexProgress:
            call HREX14 from _call_HREX14
            return

        "What do you think of Melody?" if Flag_MelodyMet:
            call HREX05 from _call_HREX05
            return

        "What do you think of Tao?" if Flag_TaoMet:
            call HREX06 from _call_HREX06
            return

        "What do you think of Aria?" if Flag_AriaMet:
            call HREX08 from _call_HREX08
            return

        "What do you think of Xander?" if Flag_XanderMet:
            call HREX07 from _call_HREX07
            return

        "What did you think of the Scholomance?":
            call HREX15 from _call_HREX15
            return

        "What do you think of Eileen?":
            if Affinity_Rex > 50:
                call HREX11a from _call_HREX11a
                return

            else:
                call HREX11b from _call_HREX11b
                return

        "What do you think of Alice?":
            call HREX10 from _call_HREX10
            return
        
        "Are we friends?":
            if Affinity_Rex < 50 and not Quest_RexProgress and not Quest_RexComplete and not Quest_RexProgress:
                call HREX09a from _call_HREX09a
                return
            elif Affinity_Rex > 50 and Quest_RexProgress:
                call HREX09b from _call_HREX09b
                return

            elif Quest_RexComplete and not Flag_PlayerSnitchesRex:
                call HREX09c from _call_HREX09c
                return

            
            elif Flag_PlayerSnitchesRex:
                call HREX09d from _call_HREX09d
                return

            else:
                call HREX09e from _call_HREX09e
                return

        "What do you think of the Mage Council?":
            call HREX13 from _call_HREX13
            return

        "Heard you were an anarchist or something?":
            call HREX04 from _call_HREX04
            return

        "Why do you dislike Eileen so much?":
            if Affinity_Rex < 50:
                call HREX16a from _call_HREX16a

            else:
                call HREX16b from _call_HREX16b

        "(Quest) Remind me, what do you need me to do?" if Quest_RexProgress:
            call HREX17 from _call_HREX17
            return

        "(Quest) Are you sure blowing up Eileen's statue is what you really want?" if Quest_RexProgress:
            call HREX18 from _call_HREX18
            return

        "(Archives) Have you seen the Archive Door Lock?" if Flag_ArchivesArtifice:
            call HREX28 from _call_HREX28
            return

        "(Exit Conversation)":
            $ result = renpy.random.randint(1, 4)
            if result == 1:
                Rex "Later."
                return
            if result == 2:
                Rex "..."
                return
            if result == 3:
                Rex "Hmm."
                return
            if result == 4:
                Rex "Bye."
                return       


        









    return





    label HREX02a:
        Rex "All family is, is trouble and baggage. Do yourself a favour and don't pry."
        menu:
            "Got it...":
                jump rexhub_main


    label HREX02b:
        Rex "My family, heh? Let's see… dad didn't do shit for me. My ma shipped me off to Scholomance as soon as she could."
        menu: 
            "What was your mom like?":
                Rex "She was a clockmaker. Pendulum clocks. Ran the shop herself and never really had time for me, so I was on my own a lot. Sometimes I wish she had taught me clockmaking."
                menu: 
                    "Why didn't she?":
                        Rex "She probably wanted to. But when I was old enough to learn, my magic manifested. Ma never looked at me the same after that." 
                        Rex "She was scared of me, of what I'd do. Next thing I knew… Scholomance. I swear everything's just been a blur since. Anyway, let's move on."
                        menu: 
                            "...":
                                jump rexhub_main
            
            "What was your dad like?":
                Rex "Not much to say. He fancied himself some sort of scholar, but whatever talent he had, he drank away. Taught me to fight by smacking me around." 
                Rex "That's the only thing he taught me."
                Rex "What does he think of your magic?"
                Rex "I don't know and don't care."
                menu: 
                    "...":
                        jump rexhub_main

    label HREX01:
        Rex "Course I can."
        menu: 
            "Oh.":
                pass
            "Really?":
                pass
        
        Rex "You thought I wouldn't share tips? I'm not like Melody or Tao, who will do anything for top marks." 
        Rex "They're nothing but a couple of drudges for the school, and they don't even know it. Pathetic."
        Rex "What do you wanna know?"
        menu: 
            "How do I get a good grade?":
                Rex "Most of it's just the materials. You can't build one of those big city towers with stone alone, you've gotta use reinforced metal..."
                Rex "You've gotta figure out how to make your materials better."
                Rex "Other than that, just make something not shitty."
                pass
        Rex "It's not that complicated."
        Rex "Anyway... since I did you a favor. You owe me. All good?"
        menu:
            "Sure.":
                Rex "Good."
                $ Flag_RexArtificing = True
                jump rexhub_main

    label HREX03:
        Rex "My manifestation? Every mage seems to have some sob story around their manifestation. I'm not that kind of guy."
        menu: 
            "Indulge me.":
                pass
            "What happened?":
                pass
        if Affinity_Rex < 50:
            Rex "Let's just say, when it happened, it was pointed at the right people. I have no regrets."
            Rex "That's all you're getting."
            jump rexhub_main

        else:
            Rex "My ma was always busy running the clock shop, so I took care of myself most of the time. I did whatever I wanted." 
            Rex "I know it sounds like every kid's dream. But the truth is, when people see you're a little kid, alone, they see a target."
            Rex "The boys that ran the street chased me for money from time to time. When they realized I had none, they chased me for fun." 
            Rex "That one time, I ran into the shop and they followed me in. They threw things around. Demanded cash from ma."
            Rex "Every bone in my body was screaming at them to stop. From head to toe, my body felt hot, prickly. My fingers became flames, the flames ripped up my arms." 
            Rex "I smelt my hair burning. A firestorm swallowed me up. It was still me at the centre." 
            Rex "I could still think, still feel. That's why I wasn't scared. My gut told me not to fight it."
            Rex "I don't remember much after that. Ma told me they ran out of the shop, begging the neighbours for water to put out their clothes." 
            Rex "I won't pretend I'm sorry." 
            Rex "They deserved it."
            menu:
                "Sounds like they had it coming.":
                    Rex "Damn right. Knew you'd get it."
                    Rex "Sometimes violence is the answer."
                    Rex "If my magic wasn't twinged with some demon bullshit, Eileen wouldn't have an issue."
                    Rex "She uses violence all the time to get what she wants."
                    Rex "Hypocrite."
                    $ Affinity_Rex += 10
                    jump rexhub_main
                
                "You {i}burned{/i} them?":
                    Rex "Yeah. I did."
                    Rex "And I'd do it again."
                    $ Affinity_Rex <= 5
                    jump rexhub_main

    label HREX12:
        $ Flag_HREX12 = True
        Rex "I don't need friends, unless youre willing to help me with my plan. Actions over words, as they say. Friends take risks for each other, right?"
        menu: 
            "What's the plan?":
                Rex "If you have to ask, you ain't someone I'd be friends with." 
                Rex "Piss off."
                $ Affinity_Rex -= 5
                jump rexhub_main

            "Sure, I'll help you.":
                "I knew you weren't like the others. We'll be thick as thieves, you and me."
                $ Affinity_Rex += 10
                jump rexhub_main
                #####DOLATERJOSH I need to figure out how to tie this into his quest. Coming back to it.
            
            "I won't help you.":
                "Thought so. Don't bother me, then. And don't you dare go running to Eileen and Alice."
                $ Affinity_Rex -= 5
                jump rexhub_main

    label HREX14:
        Rex "Statues are a symbol of the Mage Council. They're too high and mighty for something as corrupt as your average mage."
        Rex "You know who gets a statue? Hypocrites, liars, and authoritarians. Mages who'll do anything to get to the top." 
        Rex "You'll probably see Melody's statue one day, ha!"
        menu:
            "Right.":
                jump rexhub_main

    label HREX05:
        Rex "Melody is evil. I know you won't believe me, no one believes that that uptight nerd could be anything but a model mage, but I've seen it." 
        Rex "She puts her ambition first."
        Rex "You all think I'm untrustworthy, well, the face of evil is right over there."
        menu:
            "...":
                jump rexhub_main

    label HREX06:
        Rex "You might feel sorry for Tao, but don't turn your back on them. They're dangerous…obsessed about grades and will throw you under the carriage for a high mark."
        Rex "Mark my words, they'll brown nose all the right people and the doors will open for them. People like that aren't worth my time."
        menu:
            "...":
                jump rexhub_main 

    label HREX08:
        Rex "Honestly, I'm surprised Aria's made it this far. The look in her eyes sometimes. A deer in a forest of wolves."
        Rex "It's kind of her fault. She's such a pushover. I think she hopes they'll come around to her." 
        Rex "Her magic is something else, though. I've seen her do some wild shit."
        menu:
            "...":
                jump rexhub_main 

    label HREX07:
        Rex "Xander? Barely know him. I mean we've chatted but he's..."
        Rex "...too much. He's short, quick, and too in your face."
        Rex "I think, underneath it all, he's terrified. I almost feel sorry for the guy, but he's just {i}so{/i} annoying."
        menu:
            "...":
                jump rexhub_main 

    label HREX15:
        Rex "I'm going to burn it place down -- it wasn't a university, it was a prison. I shouldn't have been put here just because I got magic."
        Rex "If the Scholomance disappeared tomorrow the world would be a better place."
        menu:
            "No it wouldn't. Mages wouldn't have a school.":
                Rex "Mages will learn magic in other ways. We don't need the Council or that school, believe me."
                jump rexhub_main 
            "At least we wouldn't have to take exams.":
                Rex "No exams, no ateliers, no punishments. You're finally seeing what things could be like."
                $ Affinity_Rex += 10
                jump rexhub_main 

    label HREX11a:
        Rex "Erm, ok, I've never told anyone this before, but I did some portal magic. I know it's forbidden for students." 
        Rex "We'd done some magic theory on it in class - I just started playing around after hours." 
        Rex "No bad intentions, honest."
        Rex "Then, once, only for a few moments, a small portal opened up in my room." 
        Rex "I just about pissed myself." 
        Rex "But a voice in my head said, look at what you can do."
        Rex "An imp crawled out." 
        Rex "A squirmy, nasty thing. Only a baby." 
        Rex "I kept it in my room for a couple of days and fed it from the mess hall." 
        Rex "What was I supposed to do, let it go? Anyway, the imp got out one night. Everyone panicked." 
        Rex "Eileen caught and killed the poor wretch." 
        Rex "Then she went ballistic on me. The witch looked twice her normal size, screaming that portals were forbidden and I was either dumb or evil for opening one."
        Rex "You know what?" 
        Rex "That damn imp was the one and only time I ever came close to understanding my magic at Scholomance." 
        Rex "It meant something, that I was responsible for it, even if it was an accident." 
        Rex "Eileen ruined it. She deprived me of something big. Something that I can't even explain."
        Rex "So, yea, I hold a grudge. Everyone who gave me shit for it can be swallowed by the ground."
        jump rexhub_main


    label HREX11b:
        Rex "Eileen is a cruel witch. Period. I'd never trust her. I'd never help her."
        jump rexhub_main

    label HREX10:
        Rex "She's weak. Always going on about everyone's feelings. Trying to be friendly. Maybe she puts it on to get close to us."
        Rex "One thing I can't square -- what's someone so nice doing with all those enchanted Dolls? I don't think I want to know why she made them."
        jump rexhub_main

    label HREX09a:
        Rex "You're just another keener trying to climb the ranks. So nah, we're not friends."
        jump rexhub_main
    
    label HREX09b:
        Rex "Heh, well, do you want to be? I know it's hard for me to open up. Not used to relying on other people for anything." 
        Rex "But it's not so bad, is it? Having someone to plan with, to talk things over with."
        $ Affinity_Rex += 5
        menu: 
            "Do you have friends?":
                Rex "Nah, I don't think so. All conformists in the end. I do feel more sorry for Aria and Xander." 
                Rex "They're probably like me, going about their lives, and then -- bam -- they end up in the Scholomance." 
                Rex "Melody and Tao think the school will make their dreams come true. They'll see..."
                menu:
                    "You think?":
                        Rex "They're smart. They'll know one day they got conned."
                        Rex "Sure they'll have power and authority, but they'll never be free."
                        Rex "Not like us."
                        menu: 
                            "Sounds sad.":
                                jump rexhub_main

            "What are your thoughts on your plan?":
                Rex "There's a lot of magic the Council won't teach us, you know. They have the knowledge, but they keep it for themselves." 
                Rex "That's why the broken statues will piss them off -- not because we disrupted some ceremony."
                jump rexhub_main


    label HREX09c:
        Rex "Course. You had my back. I'm glad I met you."
        Rex "Shame we're not gonna see each other much wherever you end up."
        jump rexhub_main

    
    label HREX09d:
        Rex "I know it was you who snitched to Eileen and Alice. And to think, for a minute, I thought we could be friends. Get out of my sight."
        $ Affinity_Rex -= 50
        jump rexhub_main


    label HREX09e:
        Rex "I don't really know you. What an weird question."
        jump rexhub_main



    label HREX13:
        Rex "No chance I'll be let into the Mage Council's inner network. Eileen probably thinks I'll try to burn the place down. Maybe I will."
        Rex "There's nothing for me in there. After the Scholomance, I'll make it on my own terms." 
        Rex "I'll think of something. I always do. I don't care if I have to sleep in a ditch, as long as I'm free."
        jump rexhub_main

    label HREX04:
        Rex "Heh, I'm not an anarchist. And I don't hate society. What I do hate is the Mage Council. Just because we manifested magic, they're allowed to run our lives." 
        Rex "They tell us how to do magic, where to do it, and why."
        Rex "Going to Scholomance ruined my life. I'm stuck in the mousetrap they built. All they've ever done for me is threaten me with punishment if I didn't act right." 
        Rex "I'd rather die than be under their thumb forever."
        menu: 
            "I agree with you.":
                Rex "I'm glad. But you'll have to prove it some day."
                pass

            "A bit dramatic.":
                Rex "You'll see what I'm talking about one day."
                pass
        jump rexhub_main





    label HREX16a:
        Rex "She's everything that's wrong with the Mage Council. Authoritarian, controlling, obsessed with power." 
        Rex "You'll never reach your full potential under her." 
        Rex "All she wants is to rule you, magic be damned."
        menu:
            "She's just doing her job.":
                Rex "Her job is killing people who don't agree with the Mage Council."
                Rex "Come up with a better argument, you bootlicker."
                $ Affinity_Rex -= 10
                jump rexhub_main

            "I don't think so.":
                Rex "Who cares what you think?"
                jump rexhub_main



    label HREX16b:
        Rex "I have a bad history with Eileen. I experimented with some portal magic and summoned an imp. I was just curious, I swear it was an accident!" 
        Rex "It was also the only time I thought having magic might be some sort of gift. Eileen cut me down to size pretty quick." 
        Rex "Made me sick, what she did to that imp. I've never forgiven her."
        Rex "I didn't ask to be a mage. Magic took me away from my ma, from my home. Ma wasn't perfect but I still miss her."
        menu: 
            "I understand.":
                Rex "You know? I think you do."
                Rex "You probably got taken from something you loved, too. Maybe you don't have fire magic tied to demons, but you still got stuck in that prison."
                $ Affinity_Rex += 5
                jump rexhub_main

            "She's just doing her job.":
                Rex "Her job is killing people who don't agree with the Mage Council."
                Rex "Come up with a better argument, you bootlicker."
                $ Affinity_Rex -= 10
                jump rexhub_main

    label HREX17:
        Rex "This is the plan: you work on the potion we need for the ritual that'll destroy Eileen's statue. I was never good at that. I have the stone cutter spell." 
        Rex "Go to the Atrium after curfew. Douse the statue with your potion. For my plan to work, you have to douse the statue before the end of the thursday, otherwise my ritual won't work."
        Rex "It needs time to take effect."
        Rex "On graduation day, I'll cast the spell, and everyone will watch Eileen's legacy crumble."
        Rex "Are you ready for this?"
        menu: 
            "I am.":
                Rex "Good."
                jump rexhub_main


    label HREX18:
        Rex "What do you mean? Getting cold feet on me?"
        menu: 
            "I'm just wondering. Don't be so suspicious all the time.":
                Rex "Have you met me?"
                menu: 
                    "Yea, and you should probably spend more time studying for exams.":
                        Rex "Ha. I'm gonna be the mage Eileen and the Council never forget. You're free to study with the others if you want." 
                        menu: 
                            "Our plan seems a lot more fun to me.":
                                Rex "Happy to hear it."
                                jump rexhub_main
                    "Maybe I will.":
                        Rex "So you are getting cold feet. Gonna run to the proctors?"
                        menu: 
                            "No. But I'm out.":
                                "Good. Don't."
                                $ Quest_RexFailed = True
                                $ Quest_RexProgress = False
                                jump rexhub_main

                            "Haven't decided yet.":
                                Rex "Make up your mind."
                                jump rexhub_main


            "If I'm being honest, it seems extreme.":
                Rex "You only think that because the Scholomance taught us that."
                menu: 
                    "If the Scholomance is wrong about everything, what do you believe is true?":
                        Rex "I dunno what I believe. All I know is that there's something more out there." 
                        Rex "But they want to distract us from it by building statues to each other."
                        menu: 
                            "Not worth making new enemies. We'll be out of here in a few days.":
                                Rex "Ha. Eileen and the Council already think I'm the villain. I've got nothing to lose. "

                            "Statues are the least of our problems. You're focused on the wrong thing.":
                                Rex "Alright. I'm listening. How do you figure?"
                                menu: 
                                    "Even if we blow up Eileen's statue, the Council will just build another one. The real question is what we're going to do after graduation.":
                                        menu: 
                                            "How we're going to be responsible for whatever village we're assigned to.":
                                                Rex "I don't feel responsible for a bunch of people I've never met."
                                                menu: 
                                                    "I think you want to blow up this statue to show other mages they don't have to toe the line.":
                                                        Rex "Well, they don't."
                                                        menu: 
                                                            "So show them that.":
                                                                menu: 
                                                                    "I know you want to get one over on Eileen. But a clean break from this place is a better plan.":
                                                                        Rex "A clean break. Ya. I think I like that. That way, they'll never be able to hold it over my head." 
                                                                        Rex "And I'll never have to think about the Summit again." 
                                                                        Rex "..."
                                                                        Rex "I'm calling off the plan. We can still, erm, hang out though. A bit later."
                                                                        $ Quest_RexPlanStopped = True
                                                                        $ Quest_RexProgress = False
                                                                        jump rexhub_main
        
        label HREX28:
            Rex "Oh that old piece of crap?"
            Rex "Yeah, it's artifice alright... older than anything I've seen before though."
            Rex "I don't know how to break something like that... weirdly enough though, Xander might."
            Rex "His affinity is electricity... which is useful for breaking artifice. Does something to the magnetism of it."
            menu:
                "Really?":
                    Rex "Yeah... really. You think I wanna give that twerp props for anything?"
                    Rex "You want it broken, ask him."
                    $ Flag_ArchivesArtifice_Xander
                    return


#######################
#  Melody 2 Main Hub  #
####################### 

label melody2hub_main:
    ###################################
    ## Do not remove this portion
    show border onlayer UI 
    ###################################
    Melody2 "Hmm?"
    menu:

        "(Friendship) Are we {i}actually{/i} friends?":
            call HMEL27 from _call_HMEL27
            return

        "(Dreams) Do you have a dream?":
            call HMEL21 from _call_HMEL21
            return

        "(Past) Tell me about your past.":
            call HMEL22 from _call_HMEL22
            return

        "(Tao) What do you really think of Tao?":
            if Quest_MelodyComplete:
                call HMEL24a from _call_HMEL24a
                return

            else:
                call HMEL24b from _call_HMEL24b
                return

        "(Aria) What do you really think of Aria?":
            call HMEL25 from _call_HMEL25
            return

        "(Rex) What do you really think of Rex?":
            call HMEL28 from _call_HMEL28
            return

        "(Graduation Spot) Tell me about the graduation spots.":
            call HMEL29 from _call_HMEL29
            return

        "(Exams) Got anything on the exams?":
            call HMEL30 from _call_HMEL30
            return

        "(Combat Exam)":
            if Flag_CombatExamCompleted:
                call HMEL31a from _call_HMEL31a
                return
            else:
                call HMEL31b from _call_HMEL31b
                return

        "(Potion Exam)":
            if Flag_PotionExamCompleted:
                call HMEL33a from _call_HMEL33a
                return

            else:
                call HMEL33b from _call_HMEL33b
                return

        "(Artificing Exam)":
            if Flag_ArtificingExamCompleted:
                call HMEL35a from _call_HMEL35a
                return

            else:
                call HMEL35b from _call_HMEL35b
                return

        "I met something that looked like Alice but clearly wasn't... 'Alice'":
            call HMEL37 from _call_HMEL37
            return

        "(Magic) How did your magic manifest?":
            call HMEL38 from _call_HMEL38
            return

        "(Mage Society)":
            call HMEL39 from _call_HMEL39
            return

        "(Exit Conversation)":
            $ result = renpy.random.randint(1, 4)
            if result == 1:
                Melody2 "Don't be a stranger."
                return
            if result == 2:
                Melody2 "Bye."
                return
            if result == 3:
                Melody2 "Hmm, you're going? Bye."
                return
            if result == 4:
                Melody2 "We'll talk."
                return       






    label HMEL27:
        Melody2 "You want to know whether we're friends?"
        Melody2 "Ha. That's the sort of question the ditzy overly nice girl I pretend to be would ask."
        menu: 
            "That's not an answer.":
                Melody2 "Wait, you're serious?"
                menu:
                    "...":
                        Melody2 "Sure. We're friends. I mean what's the phrase -- {i}honour among thieves.{/i} For us, I guess we have a kinship." 
                        "{i}Mages of a feather, or whatever.{/i} If what we're doing now isn't considered friendship, I don't know what is."
                        menu: 
                            "Have you ever had a friend before?":
                                Melody2 "None in the Scholomance, that's for sure." 
                                Melody2 "I don't think I ever trusted anyone there. Who would? If you're not the best you'll get screwed over."
                                Melody2 "That's probably why we're being open about it now. I know you'll screw other people over to get ahead."
                                Melody2 "You know I'll do the same -- there's no backstabbing there."
                                menu:
                                    "I guess.":
                                        Melody2 "Plus, it's exhausting to keep the facade up."
                                        jump melody2hub_main
                                    "I'm not going to backstab you.":
                                        Melody2 "We'll see."
                                        jump melody2hub_main

    label HMEL21:
        Melody2 "I've always dreamed of going to the city -- the Scholomance was always a route to that. I like having magic, who wouldn't?" 
        Melody2 "But I'm going to love my time in the city so much more. So much to do."
        Melody2 "I won't be sequestered off to a backwater town where the most interesting thing that can happen is a travelling band or someone dying." 
        Melody2 "I won't be put through that again. "
        jump melody2hub_main

    label HMEL22:
        Melody2 "The village I'm from had, max, fifty people in it. All of them old, all of them obstinate. The only thing to do there was count flowers in the fields and swim in a freezing ocean. I hated it, it was the sort of place people like me are imprisoned in."
        Melody2 "The second my magic manifested I knew it was my ticket out. Wish come true, really. I'm never going back there."
        menu:
            "What about your parents?":
                Melody2 "There wasn't anything my parents did wrong. They were simply happy living a simple life in a quiet place." 
                Melody2 "The village might as well have been at the end of the world -- isolated on a small island with nothing going in and out."
                Melody2 "It's the sort of place you go to die."
                jump melody2hub_main

            "What about your friends?":
                Melody2 "Everyone was older than twenty when I was {i}born{/i}. There was no one my age to talk to so I spent most of my time with birds and make-believe friends."
                menu: 
                    "That's all you had?":
                        Melody2 "Again, what other option did I have? This isn't me telling you some sob story -- if anything, I'm being open with you."
                        jump melody2hub_main

                    "Sounds hard.":
                        Melody2 "I made do."
                        jump melody2hub_main


            "(Say nothing.)":
                Melody2 "If that's all, you can stop prying. After graduation we probably won't ever see each other again..." 
                Melody2 "...but still, I'd rather not make friendship bracelets and fairy chains right now."
                menu: 
                    "Got it.":
                        jump melody2hub_main


    label HMEL24a:
        Melody2 "You know, messing with Tao's potion was more fun than I thought it'd be."
        menu:
            "Do you enjoy messing with people's grades?":
                Melody2 "Sometimes. It depends on the person."
                Melody2 "Messing with Xander's grade is like pushing over a toddler -- not {i}that{/i} fun. But with Tao I know there's stakes."
                jump melody2hub_main


    label HMEL24b:
        Melody2 "Tao is insufferable."
        Melody2 "If {i}I{/i} was the child of an accomplished mage I simply {i}wouldn't{/i} be an insufferable nutjob with no personality, charm, or ability to make a single friend in their seven years of studying." 
        Melody2 "As much as I like being alone, I'm smart enough to know how to play nice."
        Melody2 "Fake it til you make it… or end up alone behind a desk at the back of a building filing papers because no one else wants to deal with you." 
        Melody2 "Like it or not, being sociable and {i}*scoff*{/i} personable, is as important as being smart and reliable nowadays."
        Melody2 "It doesn't matter what level of nepotism Tao was born into, they'll be a failure if they can't grasp the basics of being nice to talk to."
        Melody2 "And this isn't me being {i}biassed{/i} because they're probably the biggest roadblock I have to the city spot -- they just aren't nice to be around."
        menu: 
            "Seems like a grudge.":
                Melody2 "If that's how it reads I doubt you've had to talk to Tao in any meaningful way."
                pass
            "That's a bit harsh.":
                Melody2 "Shame."
                pass
            "You think Tao won't be successful because they're not nice to be around?":
                Melody2 "Absolutely. If you haven't noticed, the average person is not smart." 
                Melody2 "Dumb people are loud, confidence is convincing, and being capable of putting the right words in a row usually means people perceive you as smarter than you actually are."
                Melody2 "What this means for Tao is that no one will listen to anything they have to say because they won't say it eloquently, nicely, or with enough charisma to be convincing." 
                Melody2 "A small number of people in the room will actually internalise what someone is telling them and think it through..." 
                Melody2 "...if I sounded reasonable and intelligent enough I could easily have gotten half the people in the Scholomance to inadvertently kill themselves by suggesting they create potions that {i}sounded{/i} right but were actually noxious gas."
                Melody2 " I wouldn't, obviously. But that's not the point -- Tao is smarter than me." 
                Melody2 "They study harder, learn quicker, think better -- in athletic terms, they're a track star, but the sad truth is that no one gives a crap what the smart person has to say -- they care what the charismatic one does."
                Melody2 "If people don't like you, they will not listen to you, and Tao is allergic to being likeable."
                pass
        Melody2 "It's a good lesson to us though -- watching someone with everything going for them self-sabotage does remind you of what's important." 
        Melody2 "Maybe they'll improve... maybe not." 
        Melody2 "The way I see it is we shouldn't let a good spot go to waste on someone who will not have the power to utilise it."
        menu: 
            "I like Tao. I hope they improve." if Quest_TaoComplete:
                Melody2 "You must see something I don't then."
                pass
            "So in a way, we should sabotage Tao so the spot is used by someone who can do something with it?":
                Melody2 "If that motivates you, sure. Why not?"
                pass
            "We can hope":
                Melody2 "You can. I don't really care all that much."
                pass

        Melody2 "Just remember, they're still the main contender to sabotage. Don't get attached to a bear cub. It might be cute, but it'll kill you one day."
        jump melody2hub_main


    label HMEL25:
        Melody2 "Aria's... fine. She's annoying, but her being here is more often helpful than not." 
        Melody2 "On one hand, Aria can be a threat, academically, when she puts her mind to it." 
        Melody2 "On the other hand, she usually causes some hijinx or issue due to how unstable her magic can be..." 
        Melody2 "...meaning a lot of Eileen and Alice's attention is on her, which is helpful when we're trying to not get caught."
        Melody2 "Still not being able to control your powers into your twenties is embarrassing -- most of us had ourselves under control in our teens..." 
        Melody2 "...she's too old for this sort of problem. I don't even know why they put her up for graduation." 
        Melody2 "Maybe they just want to get rid of her."
        Melody2 "It's a shame, right? The girl can grow a garden by daydreaming but can't be bothered to be normal for five minutes."
        Melody2 "She's born lucky to have that sort of power, but she's also lucky they haven't put her in some mage prison or something -- her power is probably making the council pensive."
        menu:
            "I'm sure they wouldn't lock her up.":
                Melody2 "What else do you do with someone capable of that sort of destruction? I wouldn't feel safe being alone with her if she had a bad day..." 
                Melody2 "...half of us would end up being collateral. Locking that sort of person up is much better than the {i}obvious{/i} alternative."
                menu: 
                    "Which is?":
                        Melody2 "'Subduing' her, permanently." 
                        Melody2 "We all know Eileen's done it before -- at least, if we're reading between the lines of those history books." 
                        Melody2 "I'm sure those problematic rogue mages didn't just decide to concede."
                        Melody2 "It's not the nicest thought. In a way I really like Aria, I just wish she could manage herself better. It's annoying to watch someone born so lucky have such basic, solvable problems." 
                        Melody2 "Make you wish you'd been born that lucky yourself."
                        Melody2 "I'm sure she'll figure it out eventually at whatever backwater town she ends up in."
                        jump melody2hub_main

    label HMEL28:
        Melody2 "Rex is about as bright as a cave. He puts on a show, 'oh look at me I'm edgy, I hate authority,' but anyone who really hated authority wouldn't be here, they'd have burned the school down." 
        Melody2 "Anarchists are only as useful as their ability to commit to it. He needs to learn to play the long game."
        jump melody2hub_main




    label HMEL29:
        Melody2 "Alice told me the slots when I arrived -- she mentioned one of the spots is near my hometown." 
        Melody2 "I will not be going to that one. I read up on each of them in the library… the five are:"
        Melody2 "{i}Lyra Plains{/i}, a desert town to the south. It's small, set up around an oasis called the Lyranic Oasis. I don't do well in heat."
        Melody2 "{i}Jubilee Grove{/i} was another one. I've not actually read too much on it other than it's super rural and surrounded by farmland..." 
        Melody2 "...sounds like the sort of place that would drive me insane."
        Melody2 "{i}Willow Peaks{/i} was in the mountains somewhere. Looks boring."
        Melody2 "<i>Tomis Village</i> was like… a few hours away from my hometown. It's a small town on the coast -- I remember we used to get produce from there sometimes." 
        Melody2 "I'd rather not have to be that close to my parents, and a small fishing town does not sound like the sort of place I want to spend my time."
        Melody2 "Finally, {i}Ilara City{/i} is where I want to go. The regional capital. It's a big, sprawling city with tens of thousands of people living there." 
        Melody2 "It's not a crappy little town, it's a city -- that spot is mine."
        Melody2 "There could be more spots, but those are the ones Alice mentioned. Four rocks and one diamond. I doubt it's a coincidence there are only five of us graduating from this set." 
        Melody2 "Maybe these are the towns that either didn't have a town mage, for whatever reason. "
        jump melody2hub_main



    label HMEL30:
        Melody2 "I doubt you need to study that hard for these exams. You're not an idiot like the rest of them."
        jump melody2hub_main

    label HMEL31a:
        Melody2 "It went fine. I've never been great in combat -- it's not something I particularly enjoy. I doubt I'll need that skill in the city -- surely there will be other mages for that."
        Melody2 "I'm guessing you did well?"
        menu:
            "It could've gone better.":
                "As long as your average grade was fine, it shouldn't matter. That's why it's graded on a curve, I guess."
                jump melody2hub_main

            "I think I did fine.":
                Melody2 "Hmm."
                jump melody2hub_main



    label HMEL31b:
        Melody2 "I have a few tricks up my sleeve for the combat exam. I'm not going to do as well as someone like Xander, but I know I'll pass."
        jump melody2hub_main




    label HMEL33a:
        Melody2 "Well, that was easy. Why does everyone else look so pale?"
        menu: 
            "It did not go well.":
                "Hmm. Shame."
                pass

            "It went fine.":
                "Never doubted you…"
                pass

        Melody2 "I think everyone else did not enjoy that. Rex looks like he's gonna blow something up."
        jump melody2hub_main


    label HMEL33b:
        Melody2 "Potions are my strong suit. I'll be fine."
        menu: 
            "Why are you so confident with potions?":
                pass
        Melody2 "Potions are needed by everyone. If you're good at it, you basically end up being a pseudo authority."
        Melody2 "They sell for a lot, they're easy to make once you know the recipe, but still, somehow, people mess it up."
        Melody2 "I've heard about mages who retired by writing one or two potion recipe books -- everyone wants them."
        Melody2 "When I figured all that out, it was just a point of studying a lot and making sure I practised regularly."
        jump melody2hub_main

    label HMEL35a:
        Melody2 "That went better than expected. I thought the artificing exam would be the hardest one but..." 
        Melody2 "...well, that was fine. Much easier than the written exam's we had at the Scholomance. How did you do?"
        menu:
            "It did not go well.":
                Melody2 "Well… let's hope you did well on your other tests…"
                jump melody2hub_main

            "It went fine.":
                Melody2 "Never doubted you..."
                jump melody2hub_main



    label HMEL35b:
        Melody2 "Artificing shouldn't be too hard. I've probably spent the most time studying for it." 
        Melody2 "As long as we make it out of the exam alive I think we'll pass."
        menu: 
            "Alive?":
                "We're in a room with Rex. He could just blow us up. You never know. Intentionally or not, some artificing is dangerous."
                menu: 
                    "Exciting...":
                        jump melody2hub_main


    label HMEL37:
        Melody2 "I don't know what you mean by 'not Alice'... you sound a little crazy so I'm gonna recommend you don't trust whatever it was you saw."
        Melody2 "This is me being very firm but very friendly, be careful." 
        Melody2 "I've read that some creatures can take on human form... trusting it enough to get close will probably get you killed."
        Melody2 "It could have been one of Alice's dolls, but I trust you're smart enough to tell the difference."
        menu:
            "Can you come see it with me?":
                "Are you insane? No. Whatever is in that forest will hopefully stay there. I'd rather not see it in the flesh -- or... porcelain, whatever it has."
                jump melody2hub_main
    
            "I'll avoid it.":
                Melody2 "Good… Even if you're somewhat a rival, I don't want you dead."
                jump melody2hub_main


    label HMEL38:
        Melody2 "Did I lie to you about my first manifestation… I probably did. Disregard a lot of it." 
        Melody2 "It's easier for someone like Aria or Xander to relate to the idea that it manifested when I was scared -- because that's most mages, right?"
        Melody2 "The first time my magic manifested I was very angry. My parents had promised me a dog if I did well on a test."
        Melody2 "I studied every day and had to travel a few hours to the nearby town to take the test."
        Melody2 "I was so excited that I got the teacher to mark it before I left so I could bring it back home with me."
        Melody2 "When I got home my parents told me they weren't going to get me a dog -- we didn't have the space and they didn't want to deal with the cleaning associated with it..." 
        Melody2 "...despite me saying I would clean it."
        Melody2 "I got so angry. I just felt this haze travelling over me, then through me. I could barely breathe, I just wanted to scream."
        Melody2 "When I opened my eyes, the entire house was dark. I'd turned every single window and piece of glass in our house completely opaque."
        Melody2 "My parents were worried… I think they knew before I did what I'd done."
        Melody2 "I remember my mother scolding me, seemingly out of instinct, and when she did I screamed again..." 
        Melody2 "...but this time instead of turning the glass opaque or fixing it, the windows shattered one by one." 
        Melody2 "I wasn't even screaming when the kitchen window burst, I was mystified." 
        Melody2 "I must've scared them a lot because a few days later they shipped me off to the Scholomance."
        menu: 
            "Did you do it on purpose?":
                Melody2 "Smash the glass? A little. I wanted the glass to smash and it did so on that level I'm culpable."
                Melody2 "Whatever that means."
                pass

            "Your parents kind of suck.":
                Melody2 "They're fine. If my daughter was suddenly intensely angry and powerful I would probably send her off somewhere far away from me."
                Melody2 "It's not like I was going to hurt them, but then again, who knows what I was and was not in control of at that point."
                pass

        Melody2 "I didn't want to go to the Scholomance, but I didn't want to stay at home. That small town always felt too small. My parents had me trade out one prison for another." 
        Melody2 "Perhaps prison's a bit intense to describe the Scholomance but, really, would any of us wanted to attend that place."
        Melody2 "I think manifesting magic was worth a childhood cut short. It's a price we all paid."
        Melody2 "But that price is too much if I get sent back to a small little town old people die in."
        jump melody2hub_main

    label HMEL39:
        Melody2 "You want to know my thoughts on Mage Society… I guess it's a big club, when you think about it." 
        Melody2 "Then again, all things are when they're insular and what's more isolating than being a mage." 
        Melody2 "We're a tiny minority of the population and the governance we have is essentially a bunch of people who know each other and were lucky to be there first."
        Melody2 "I'm guessing the Mage Council and Association is full of nepotism -- how could it not be." 
        Melody2 "Who's going to trust some random mage they've never met to sort things out with other people."
        Melody2 "It seems to me like it's all about power and pleasing those with it. How can any mage tell Eileen what to do?" 
        Melody2 "She's essentially capable of killing them with a flick of her wrist. She doesn't, why? Because they appease her." 
        Melody2 "She wants a statue, they build a statue, she wants to hunt rogue mages, she's allowed to."
        Melody2 "Then, with Eileen on their side, what opposing mage faction could function?" 
        Melody2 "It's like two people hitting each other with sticks -- the one with the longer stick's going to have an advantage."
        Melody2 "Mage Society seems like something you have to really be invited into..." 
        Melody2 "I have a few ideas on who I could use to get in but getting the city spot is step one. The city, after all, is the best place to network"
        Melody2 "..."
        Melody2 "What a rant..."
        jump melody2hub_main



#######################
#    Alice Main Hub   #
####################### 

label alicehub_main:
    ###################################
    ## Do not remove this portion
    show border onlayer UI 
    ###################################
    Alice "What do you need??"
    menu:
        "(Past)":
            call HALI01 from _call_HALI01
            return

        "(Sewer Doll)" if Flag_NotAliceMet:
            call HALI02 from _call_HALI02
            return

        "I think Tao needs help." if Flag_TaoNonVerbal:
            call HALI03 from _call_HALI03
            return
        
        "(Great Mage Tree)" if Location == "Greenhouse":
            call HALI04 from _call_HALI04
            return

        "(Xander)" if Flag_XanderMet:
            call HALI06 from _call_HALI06
            return

        "(Melody)" if Flag_MelodyMet:
            call HALI07 from _call_HALI07
            return

        "(Tao)" if Flag_TaoMet:
            call HALI08 from _call_HALI08
            return

        "(Aria)":
            if Quest_AriaProgress:
                call HALI10a from _call_HALI10a
                return

            else:
                call HALI10b from _call_HALI10b
                return
        
        "(The Summit)":
            call HALI11 from _call_HALI11
            return

        "(Rex Statues)":
            call HALI12 from _call_HALI12
            return

        "(Mage Society)":
            call HALI13 from _call_HALI13
            return

        "(Your Job)" if Flag_DemoAliceJob:
            call HALI14 from _call_HALI14
            return

        "(Exit Conversation)":
            $ result = renpy.random.randint(1, 4)
            if result == 1:
                Alice "See you."
                return
            if result == 2:
                Alice "See you soon!"
                return
            if result == 3:
                Alice "Let me know if you need anything."
                return
            if result == 4:
                Alice "Come back if you need anything."
                return














    label HALI01:
        Alice "Hmm... I always get questions about my personal life."
        if Quest_TaoComplete or Quest_AriaComplete or Quest_XanderComplete:
            Alice "I suppose the summary is that I was raised by an artisan family. I'd say I'm still more artisan than mage." 
            Alice "The dolls are an extension of that -- my family worked with porcelain. I've not seen them in a while, but I'd imagine they still do."
            Alice "My magic manifested rather late, late enough into my teens that I'd already devised a life I wanted -- magic was a curveball to that..." 
            Alice "...as I imagine it was to you and your classmates. While in the Scholomance I dreaded what my life would look like..." 
            Alice "but after a few bad nights crying I realised I could combine magic with what I wanted." 
            Alice "Geomancy has some domain over clay and the tools I'd used back home..." 
            Alice "...the only thing stopping me was the looming dread of graduation and a lack of motivation I now realise was probably some sort of depression, which is natural." 
            Alice "I was dealing with the grief of losing my old life, it's hard to do much with that looming over you."
            Alice "What I hope you can take from this, is that graduation should be a fresh start. You should be shattering the old and figuring out who you are and what you can bring to other people's lives." 
            Alice "I know your classmates see magic as a curse -- but if you overlook the hardship it comes with, it is really quite the blessing."
            Alice "I know you're a person who likes to help others, so perhaps that perspective is something that comes more naturally to you than it did for Eileen or I."
            menu:
                "...":
                    jump alicehub_main



    label HALI02:
        Alice "None of my dolls leave the grounds. That's too many things to keep track of. Are you sure that you saw one? It just seems… unlikely."
        menu: 
            "I'm sure.":
                Alice "I'll talk to Eileen. I recommend you don't leave the grounds."
                jump alicehub_main
            "Maybe I didn't.":
                Alice "Hmm. Alright then..."
                jump alicehub_main


    label HALI03:
        Alice "The teachers noticed, I don't think I've seen this sort of breakdown from them before. We are worried and we're doing what we can to support them." 
        Alice "We're afraid of what might happen if they get pulled from the exams -- I sent a dove to Tao's father yesterday, he is on the way." 
        Alice "We're going to let Tao do the exams in that state, and I'll try and we will take what is happening into account when judging the grades."
        Alice "Thank you for looking out for Tao, I know they don't have any friends here, so it's good that you're keeping your eye on them."
        Alice "You're a good person."
        jump alicehub_main

        
    label HALI04:
        Alice "Ah! The mage tree… We have a good friendship -- if you believe people and trees can be friends." 
        Alice "It's unspoken, of course. The Summit was built around the tree. No one knows whether it's just some living enchantment like the Watching Moons are, or whether it's sentient." 
        Alice "Either way, it reacts, and acts, and seems to have things it likes. It likes Aria, it likes me... I think Eileen and him are on bad terms, if I'm honest." 
        Alice "I watched it recede a branch away from her when she got close once."
        jump alicehub_main

    label HALI06:
        Alice "I like Xander. He has a good heart. I wish he would put less pressure on himself. Same goes to all of you!"
        jump alicehub_main

    label HALI07:
        Alice "Ah! Melody. Melody reminds me of myself. Eager. Excited to learn. Often nervous. I think great things are coming to that girl."
        jump alicehub_main

    label HALI08:
        Alice "Hmm. Tao seems to be struggling. I understand why… this must be the most stressful time of your lives. The weight of your future is on your shoulders." 
        Alice "But Tao's level of anxiety seems unbearable. I just wish I could take it away from them. Worry less... live more... but look out for one another." 
        Alice "No matter how talented and hardworking Tao is, they are still just a young adult who deserves some level of peace through all this."
        jump alicehub_main

    label HALI10a:
        Alice "It's best not to talk about Aria right now. I'd rather not get heated." 
        Alice "I adore and sympathise with that girl, but she had me worried sick."
        jump alicehub_main

    label HALI10b:
        Alice "I'm hopeful for Aria's future. Given the right direction she could do anything. The only thing holding her back is control." 
        Alice "All that power in a woman so sweet and unstructured leads to its own set of issues." 
        Alice "The nicest people struggle making hard decisions and when you're someone with that level of power, organisation is more so about safety." 
        Alice "The Mage Council will not like the level of power they have to allow Aria to have, it'll take a lot of control from her part to convince them."
        jump alicehub_main

    label HALI11:
        Alice "Oh the Summit is just lovely when you have the chance to explore it. Only in the day, of course." 
        Alice "It's a very odd place to be on -- this mountain is a centre of magical occurrences so you often get to see some peculiar events." 
        Alice "When I first arrived here, the first thing I did was try and figure out how the Watching Moons worked." 
        Alice "Spells like that are often too complex for most students, but I figured it out." 
        Alice "In fact, that sort of charm is what I used for my dolls."
        menu:
            "And what charm would {i}that{/i} be?":
                Alice "You'll work it out eventually."
                jump alicehub_main
            "...":
                jump alicehub_main

    label HALI12:
        Alice "Those poor statues. All that hard work. At least restoring them shouldn't be too arduous. Still, very selfish of Rex to pull that sort of prank…"
        jump alicehub_main

    label HALI13:
        Alice "You aren't the first to ask me about Mage Society. I get that you're all very curious." 
        Alice "My experiences were... normal." 
        Alice "The Scholomance prepared me for what I was entering into, I felt ready."
        Alice "I didn't dislike studying but after the amount I did during my education, Mage Society was a breath of fresh air."
        Alice "I entered and did a job that was assigned to me. After people saw what my talents were in, they moved me towards my current role." 
        Alice "I'm good with people, so helping other mages who are graduating, in school, out in the workforce, or even just first finding their power, is very aligned with who I am." 
        Alice "Try not to feel pensive about what comes next. You will be okay."
        $ Flag_DemoAliceJob = True
        menu:
            "Isn't it odd that we don't get a choice?":
                Alice "In a world where everyone heralds freedom, we have to play by other rulesets."
                Alice "It must seem odd to you. I mean, the lot of you are in your twenties."
                Alice "When I was in my twenties... the world was a different place."
                Alice "War was always on the horizon... our kin were being hunted down one at a time..."
                Alice "Mages are a distruptive force in the world, so we must enforce any structure we can onto them."
                Alice "It keeps allof us safe."
                Alice "As unpopular as the Mage Council are... they exist for a reason. It wasn't as though there was some power vaccum and they happened to seize it."
                Alice "They were forced to."
                Alice "As was I. As are you. As are those hundred students in the Scholomance."
                Alice "As dreary as it seems. It's {i}this{/i} or it's something much worse."
                menu:
                    "...":
                        jump alicehub_main
            "Is your life fun?":
                Alice "I try not to ask myself that."
                Alice "I find it tends to ruin my mood."
                Alice "Life can't be fun forever."
                Alice "You're alive to experience fleeting happiness, not everlasting."
                Alice "Horrible to say, but it's true."
                Alice "Everything you do will be measured, just like this exam."
                Alice "The step of every Mage is held to a higher standard because of the gifts we were born with."
                Alice "We aren't allowed a bad day. We aren't allowed to have a drunken row in a pub..."
                Alice "A strong disagreement with a coworker..."
                Alice "We're not even allowed to seem outwardly hostile."
                Alice "If we live on whims and do as we please all it takes is one bad egg to ruin a peaceful life we have fought hard to attain."
                Alice "I don't want to enter a war. I'm sure none of you do either."
                Alice "I have fun, sometimes."
                Alice "But I like to live in reality, where we sculpt our lives from the clay we're given. You know?"
                menu:
                    "I know...":
                        jump alicehub_main

                    "That's a long way of saying 'no'.":
                        Alice "Haha..."
                        Alice "Don't you have studying to do?"
                        jump alicehub_main

        label HALI14:
            Alice "Ha. I've had many jobs after I graduated. Like most of you will be, I was assigned a city position in Estului." 
            Alice "It was… interesting, but unfulfilling." 
            Alice "Luckily, the Mage Society understood my actual desires and saw talent in me for other things so I was assigned a new role -- an invigilator role." 
            Alice "My job was to essentially check up on and help other mages who were in my former position." 
            Alice "That ended up going well and I was promoted so that I could spread more guidance, and eventually that also meant helping students too." 
            Alice "It's very rare for people to be able to visit the Scholomance again after they graduate, but I was given that blessing. I found it all fulfilling." 
            Alice "I get to travel -- I love travelling -- and I get to spend time on my hobbies while doing so." 
            Alice "Eileen and I have a very privileged job. The only thing it lacks is companionship -- it's very rare that the two of us are in the same place." 
            Alice "I've been asking the Council to assign me an apprentice, but I have doubts they'll allow that until they find the right fit."
            jump alicehub_main

            

                


    return


    


        


