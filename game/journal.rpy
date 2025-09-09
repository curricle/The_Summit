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
define journal__bio_aria = CharacterBio("Aria", "", "A tree hugger.")
define journal__bio_xander = CharacterBio("Xander", "", "He's very energetic.")
define journal__bio_rex = CharacterBio("Rex", "", "He seems a bit rough around the edges.")
define journal__bio_tao = CharacterBio("Tao", "", "A rather studious sort.")
define journal__bio_alice = CharacterBio("Alice", "", "An Inquisitor... the more supportive of the two.")
define journal__bio_eileen = CharacterBio("Eileen", "", "An Inquisitor... best not get on her bad side.")
define journal__bio_melody = CharacterBio("Melody", "", "Put-together and friendly. Serious about her studies.")

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

screen journal(tab):

    tag menu
    use game_menu(_("Journal"))

