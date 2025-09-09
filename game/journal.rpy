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
        def __init__(self, name, image, description):
            self.name = name
            self.image = image
            self.description = description

    class ExamInfo:
        def __init__(self, name, scheduled, description):
            self.name = name
            self.scheduled = scheduled
            self.description = description


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

default current_character = ""

screen journal(tab):

    tag menu
    use game_menu(_("Journal"))

    default current_tab = tab

    hbox:
        ypos 200
        xalign 0.5
        spacing 150

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
                ysize 900
                ypos 300
                spacing 100

                #list of characters to choose from
                vbox:
                    spacing 20
                    for character in journal__characterBio_list:
                        textbutton _(character.name) action [SetVariable("current_character", character),
                            ShowMenu("journal", "characters")]
                
                #character information
                vbox:
                    hbox:
                        spacing 20
                        if current_character:
                            image current_character.image:
                                ysize 500
                                xsize 300
                            vbox:
                                spacing 60
                                text current_character.name
                                text current_character.description
                        

