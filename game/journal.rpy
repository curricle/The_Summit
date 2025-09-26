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
        def __init__(self, name, image, description, specialty='???', short_description='???'):
            self.name = name
            self.image = image
            self.description = description
            self.specialty = specialty
            self.short_description = short_description

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
define journal__spell_light = Spell("Light Spell", "", "Light", "Easy", "Creates light.")
define journal__spell_unlocking = Spell("Unlocking Spell", "", "Unlocking", "Easy", "Unlocks doors and so on.")
define journal__spell_telekinesis = Spell("Telekinesis Spell", "", "Telekinesis", "Medium", "Throws things about the room.")

define journal__spells_list = [journal__spell_light, journal__spell_unlocking, journal__spell_telekinesis]


# Characters
define journal__bio_aria = CharacterBio("Aria", "images/aria/aria sprite.png", "A tree hugger.")
define journal__bio_xander = CharacterBio("Xander", "images/xander/xander sprite.png", "He's very energetic.")
define journal__bio_rex = CharacterBio("Rex", "images/rex/rex sprite.png", "He seems a bit rough around the edges.")
define journal__bio_tao = CharacterBio("Tao", "images/tao/tao sprite.png", "A rather studious sort.")
define journal__bio_alice = CharacterBio("Alice", "images/alice/alice sprite.png", "An Inquisitor... the more supportive of the two.")
define journal__bio_eileen = CharacterBio("Eileen", "images/eileen/eileen sprite.png", "An Inquisitor... best not get on her bad side.")
define journal__bio_melody = CharacterBio("Melody", "images/melody/melody sprite.png", "Put-together and friendly. Serious about her studies.")
define journal__bio_default = CharacterBio("???", '', "???")

define journal__characterBio_list = [journal__bio_alice, journal__bio_aria, journal__bio_eileen, journal__bio_melody, journal__bio_rex, journal__bio_tao, journal__bio_xander]


# Exams
define journal__exam_combat = ExamInfo("Combat", "Day 4", "Punching? Kicking?")
define journal__exam_artificing = ExamInfo("Artificing", "Day 3", "It's understood that artificing will be involved.")
define journal__exam_potion = ExamInfo("Potions", "Day 2", "Unexpected brews are sure to count against you.")

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

    vbox:
        xpos 100
        ypos 200
        spacing 30

        textbutton _("Spells") action ShowMenu("journal", "spells")
        textbutton _("Exams") action ShowMenu("journal", "exams")
        textbutton _("Characters") action ShowMenu("journal", "characters")

    vbox:
        xsize 900
        xalign 0.5
        yalign 0.5

        if current_tab == "exams":
            vbox:
                spacing 50
                for exam in journal__exam_list:
                    vbox:
                        spacing 5
                        hbox:
                            spacing 60
                            text exam.name
                            text exam.scheduled
                        text exam.description
                    
        if current_tab == "spells":
            vbox:
                spacing 50
                for spell in journal__spells_list:
                    vbox:
                        spacing 5
                        hbox:
                            spacing 60
                            text spell.name
                            text spell.difficulty
                        text spell.category
                        text spell.description

        if current_tab == "characters":
            hbox:
                ysize 776
                ypos 50
                xsize 1645
                spacing 300

                #list of characters to choose from
                frame:
                    background Frame('gui/frame_L.png', 32, 32, 32, 32)
                    padding (10, 25)
                    ypos 250
                    has vbox
                    spacing 20
                    for character in journal__characterBio_list:
                        textbutton _(character.name) action [SetVariable("current_character", character),
                            ShowMenu("journal", "characters")]
                
                #character information
                vbox:
                    ysize 776
                    spacing 30
                    if current_character:
                        frame:
                            background Frame('gui/frame_L.png', 32, 32)
                            padding (30,30)
                            has hbox
                            spacing 30

                            # image
                            frame:
                                background Frame('gui/frame_lightTsp.png', 32, 32)
                                ysize 700
                                xsize 390
                                if current_character != journal__bio_default:
                                    image current_character.image:
                                        ysize 706
                                        ypos 17
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
                                            
                                        if current_character == journal__bio_alice:
                                            ysize 788
                                            xsize -865
                                            xcenter 120
                                            ypos 0
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
                                    background Frame('gui/frame_darkBg.png', 32, 32)
                                    ysize 595
                                    xfill True
                                    padding (30, 30)
                                    text current_character.description
                        hbox: 
                            xfill True
                            textbutton _("Next >"):
                                text_size 24
                                xalign 1.0
                                action [SetVariable('current_character', getNextItemInArray(current_character, journal__characterBio_list)), ShowMenu("journal", "characters")]
                        

