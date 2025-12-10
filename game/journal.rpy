####################################################################
#
# Classes setup
#
####################################################################

init python:
    class Spell:
        def __init__(self, name, icon, category, difficulty, description):
            self.name = name
            self.icon = icon
            self.category = category
            self.difficulty = difficulty
            self.description = description

    class CharacterBio:
        def __init__(self, name, image, description, specialty='???', short_description='???', isUnlocked=False):
            self.name = name
            self.image = image
            self.description = description
            self.specialty = specialty
            self.short_description = short_description
            self.isUnlocked = isUnlocked

    class ExamInfo:
        def __init__(self, name, scheduled, description):
            self.name = name
            self.scheduled = scheduled
            self.description = description

    def getNextItemInArray(item, array):
        arrayLength = (len(array) - 1)

        try:
            currentIndex = array.index(item)

            if currentIndex == arrayLength:
                return array[0]
            elif currentIndex < arrayLength:
                return array[currentIndex + 1]
            
        except:
            print("An exception occurred.")
            item = array[0]
            return item

    def resetCurrentCharacter():
        return journal__bio_default

####################################################################
#
# Create spells, bios, and exams
#
####################################################################

# Spells
define journal__spell_light = Spell("Light Spell", "images/icon_spell_light.png", "Light", "Easy", "Creates light.")
define journal__spell_unlocking = Spell("Unlocking Spell", "images/icon_spell_unlocking.png", "Unlocking", "Easy", "Unlocks doors and so on.")
define journal__spell_telekinesis = Spell("Telekinesis Spell", "images/icon_spell_telekinesis.png", "Telekinesis", "Medium", "Throws things about the room.")

define journal__spells_list = [journal__spell_light, journal__spell_unlocking, journal__spell_telekinesis]


# Characters
default journal__bio_aria = CharacterBio("Aria", "images/aria/aria sprite.png", "Aria's a daydreamer, but she's one of the nicer people in the exams. While she doesn't ever really try with her studies, she's sort of closely watched over by the proctors because of her natural talent as a mage. I've heard that she daydreamed a tree to grow through the ceiling, and for the dorms to flood. She'll help anyone but always seems to forget to do her own work.", isUnlocked=Flag_AriaMet)
default journal__bio_xander = CharacterBio("Xander", "images/xander/xander sprite.png", "Xander's hot headed but friendly. He lets his emotions get in the way of his studying, but will still try and help anyone who needs it -- especially with combat. I'm not sure if he's studying enough to pass the exams, but everyone is sure he'll at least try.", isUnlocked=Flag_XanderMet)
default journal__bio_rex = CharacterBio("Rex", "images/rex/rex sprite.png", "Rex seems like the kind of man to start a fight over very little. We're all mages here, but he's not too interested in camaraderie, it's all aggression from him. He doesn't seem to have many friends, I suppose there's not much time to fix that before gradutation.", isUnlocked=Flag_RexMet)
default journal__bio_tao = CharacterBio("Tao", "images/tao/tao sprite.png", "Tao is the child of a renowned mage, and I think they take that too seriously. They spend their days studying, working, and generally hanging out on their own. It's a little sad, I wonder why they haven't managed to make a friend in the Scholomance?", isUnlocked=Flag_TaoMet)
default journal__bio_alice = CharacterBio("Alice", "images/alice/alice sprite.png", "An Inquisitor... the more supportive of the two. She seems to keep a close eye on all of us -- who knows why she wants to help us so much, I think most students here throw it back in her face.", isUnlocked=Flag_AliceMet)
default journal__bio_eileen = CharacterBio("Eileen", "images/eileen/eileen sprite.png", "Every mage has heard whispers of Eileen, she's legendary. Theres a lot of literature on her in the libraries, and I'm pretty sure they're trying to build a statue of her. It seems weird that she's here, looking over our exams. It certainly adds to the pressure.", isUnlocked=Flag_EileenMet)
default journal__bio_melody = CharacterBio("Melody", "images/melody/melody sprite.png", "A mage who's dream is to become a great Alchemist.", isUnlocked=Flag_MelodyMet)
default journal__bio_default = CharacterBio("???", 'gui/none.png', "???", isUnlocked=True)

default journal__characterBio_list = [journal__bio_alice, journal__bio_aria, journal__bio_eileen, journal__bio_melody, journal__bio_rex, journal__bio_tao, journal__bio_xander]


# Exams
define journal__exam_combat = ExamInfo("Combat", "Day 6", "Combat usually involves fighting off magical beings... it's not very pleasant.")
define journal__exam_artificing = ExamInfo("Artificing", "Day 3", "Tinkering with metals and magic in order to build automatons and magical mechanisms.")
define journal__exam_potion = ExamInfo("Potions", "Day 5", "Brewing potions is the cornerstone of being a town mage, it is of the utmost importance to succeed at it.")

define journal__exam_list = [journal__exam_artificing, journal__exam_combat, journal__exam_potion]


####################################################################
#
# Journal screen
#
####################################################################

default current_character = journal__bio_default

screen journal(tab):

    tag menu
    use game_menu(_("Journal"))

    default current_tab = tab

    frame:
        xoffset -50
        ypos 150
        style 'game_menu_content_frame'
        has hbox
        spacing 250
        vbox:
            spacing 10
            style_prefix 'journal'

            textbutton _("Spells"): 
                selected False
                if current_tab == 'spells':
                    selected True
                action ShowMenu("journal", "spells")
            textbutton _("Exams"): 
                selected False
                if current_tab == 'exams':
                        selected True
                action ShowMenu("journal", "exams")
            textbutton _("Characters"): 
                selected False
                if current_tab == 'characters':
                        selected True
                action ShowMenu("journal", "characters")

            if current_tab == 'characters':
                #list of characters to choose from
                frame:
                    background Frame('gui/corner_bottom_left.png', 50, 1, 1, 50)
                    padding (10, 25)
                    xoffset 65
                    has vbox
                    spacing 0
                    for character in journal__characterBio_list:
                        if character.isUnlocked == True:
                            textbutton _(character.name): 
                                style "charlist_button"
                                selected False
                                if character == current_character:
                                    selected True
                                action [SetVariable("current_character", character),
                                ShowMenu("journal", "characters")]
                        else:
                            textbutton _(journal__bio_default.name): 
                                style "charlist_button"
                                selected False
                                if character == current_character:
                                    selected True
                                action [SetVariable("current_character", journal__bio_default),
                                ShowMenu("journal", "characters")]

        vbox:
            #xsize 900
            xalign 0.5
            yalign 0.0

            if current_tab == "exams":
                vbox:
                    spacing 35
                    for exam in journal__exam_list:
                        
                        frame:
                            background Frame('gui/frame_corners_faded.png', left=49, top=50)
                            padding (45,45)
                            has vbox
                            xfill True
                            spacing 5
                            hbox:
                                xfill True
                                spacing 60
                                text exam.name size 36
                                text exam.scheduled italic True xalign 1.0
                            add Frame('gui/divider_horizontal.png', 1, 1) ysize 2
                            null height 10
                            text exam.description
                        
            if current_tab == "spells":
                vbox:
                    spacing 35
                    for spell in journal__spells_list:
                        frame:
                            background Frame('gui/frame_corners_faded.png', left=49, top=50)
                            padding (45,45)
                            has vbox
                            xfill True
                            spacing 5
                            hbox:
                                xfill True
                                spacing 60
                                text spell.name size 36
                                text spell.difficulty italic True xalign 1.0
                            add Frame('gui/divider_horizontal.png', 1, 1) ysize 2
                            hbox:
                                spacing 10
                                add spell.icon yalign 0.5
                                text spell.category italic True
                            null height 10
                            text spell.description

            if current_tab == "characters":
                hbox:
                    ysize 776
                    xsize 1645
                    spacing 300
                    
                    #character information
                    vbox:
                        ysize 776
                        spacing 30
                        if current_character:
                            frame:
                                background Frame('gui/corner_bottom_left.png', 50, 1, 1, 50)
                                padding (30,30)
                                has hbox
                                spacing 10

                                # image
                                frame:
                                    background Frame('gui/frame_lightTsp.png', 32, 32)
                                    ysize 700
                                    xsize 390
                                    if current_character != journal__bio_default:
                                        image current_character.image:
                                            ysize 706
                                            ypos 10
                                            if current_character == journal__bio_xander:
                                                xsize -992
                                                xcenter 150
                                                
                                            if current_character == journal__bio_aria:
                                                xcenter 250
                                                xsize -549

                                            if current_character == journal__bio_melody:
                                                xsize 637
                                                xcenter 245
                                            
                                            if current_character == journal__bio_rex:
                                                xsize -636
                                                xcenter 250

                                            if current_character == journal__bio_tao:
                                                xsize -544
                                                xcenter 200
                                                
                                            if current_character == journal__bio_eileen:
                                                xsize 635
                                                xcenter 225
                                                ypos 6

                                            if current_character == journal__bio_alice:
                                                ysize 788
                                                xsize -865
                                                xcenter 120
                                                ypos 0

                                        add 'gui/corner_bottom_left.png' yalign 1.0 xalign 0.0 xoffset -36 yoffset 40
                                # text
                                vbox:
                                    xsize 667
                                    hbox:
                                        spacing 30
                                        yalign 1.0
                                        text current_character.name size 72 italic True yalign 0.5
                                        image 'gui/divider_vertical.png'
                                        vbox:
                                            yalign 0.5
                                            text 'Specialty: [current_character.specialty]'
                                            text current_character.short_description
                                    frame:
                                        background Frame('gui/frame_corners_faded.png', left=49, top=50)
                                        ysize 595
                                        xfill True
                                        padding (45,45)
                                        text current_character.description
                                    hbox: 
                                        xfill True
                                        yoffset 10
                                        # if(current_character != journal__bio_default):

                                        #     textbutton _("Next >"):
                                        #         style "journal_next"
                                        #         selected False
                                        #         text_size 24
                                                
                                        #         xalign 1.0
                                        #         action [SetVariable('current_character', getNextItemInArray(current_character, journal__characterBio_list)), ShowMenu("journal", "characters")]

style journal_button_text is navigation_button_text:
    yoffset -1

style journal_next is button:
    ysize None
    xsize None
    xpadding 25
    hover_background Frame('gui/quick_hover.png', 14, 0)

style journal_next_text:
    italic True
    hover_color yellow

style charlist_button is button:
    xpadding 50
    xoffset 10
    hover_background Frame('gui/charlist_hover_bg.png', 42, 68)
    selected_idle_background Frame('gui/charlist_hover2_bg.png', 42, 68)
    selected_hover_background Frame('gui/charlist_hover2_bg.png', 42, 68)

style charlist_button_text is journal_button_text