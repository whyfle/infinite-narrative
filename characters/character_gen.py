import random
from generators.names import NameGenerator
from generators.descriptions import DescriptionGenerator

class CharacterGenerator:
    def __init__(self):
        self.name_gen = NameGenerator()
        self.desc_gen = DescriptionGenerator()
        self.classes = ["Warrior", "Mage", "Rogue", "Cleric", "Ranger", "Paladin", "Necromancer",
            "Bard", "Druid", "Monk", "Wizard", "Sorcerer", "Warlock", "Barbarian", "Fighter",
            "Brawler", "Bladedancer", "Spellblade", "Gunfighter", "Shadowknight",
            "Time Mage", "Void Walker", "Star Caller", "Dream Weaver", "Chaos Knight",
            "Iron Guard", "Crystal Sage", "Flame Dancer", "Storm Herald", "Ice Reaper",
            "Dragon Tamer", "Spirit Channeler", "Blood Witch", "Soul Singer", "Mind Bender"]
        self.races = ["Human", "Elf", "Dwarf", "Orc", "Gnome", "Halfling", "Dragonborn",
            "Tiefling", "Aasimar", "Goliath", "Kenku", "Tabaxi", "Turtle", "Changeling",
            "Warforged", "Shifter", "Minotaur", "Satyr", "Fairy", "Elemental"]
        self.personalities = ["Brave", "Cunning", "Wise", "Fierce", "Calm", "Chaotic", "Orderly",
            "Compassionate", "Ruthless", "Jovial", "Melancholic", "Proud", "Humorous",
            "Sinister", "Benevolent", "Ambitious", "Content", "Restless", "Fearless", "Cautious"]
        self.backstories = [
            "was born in {location} to a family of {status} who {event}.",
            "was raised by {creature} in the {location} after being {event} as a child.",
            "discovered {artifact} in the {location}, which changed their destiny forever.",
            "was exiled from {location} after {event}, wandering the {biome} for {number} years.",
            "was trained by {character} in the art of {skill} at the {location}.",
            "made a pact with {entity} in the {location}, gaining {power} at a terrible cost.",
            "was chosen by {deity} during the {event}, becoming the {title} of {location}.",
            "lost {thing} in the {event} and has been searching for it ever since.",
            "unlocked {ability} during the {event} that no one else has ever achieved.",
            "fought in the {event} alongside {character}, earning {reward} for their bravery.",
            "was corrupted by {source} in the {location}, turning from {former} to {current}.",
            "found an ancient {artifact} in the {location} that whispered {secret} to them.",
            "survived the {event} that destroyed {location}, the sole survivor of {number} people.",
            "was betrayed by {character} during the {event}, leading to {consequence}.",
            "discovered a {property} anomaly in the {location} that {effect}."
        ]
        self.equipment_sets = [
            ["Dragonplate Armor", "Blade of Shadows", "Shield of Light", "Boots of Speed"],
            ["Crown of the Void", "Staff of Ages", "Robes of the Archmage", "Amulet of Power"],
            ["Shadow Cloak", "Dagger of Venom", "Crown of Thorns", "Bracers of Binding"],
            ["Tome of Knowledge", "Crystal Orb", "Robe of the Elements", "Boots of the Traveler"],
            ["Bow of the Phoenix", "Arrow of Light", "Leather Armor", "Gloves of Precision"],
            ["Hammer of Justice", "Shield of the Holy", "Plate Armor", "Helm of the Paladin"],
            ["Scythe of the Reaper", "Robe of Shadows", "Mask of the Necromancer", "Ring of Souls"],
            ["Lute of Dreams", "Staff of Illusions", "Mage's Hat", "Cloak of Many Colors"],
            ["Spear of the Wild", "Shield of Bark", "Druid's Robes", "Crown of Leaves"],
            ["Fists of Iron", "Gi of the Monks", "Headband of Focus", "Belt of Strength"]
        ]

    def generate_full_character(self):
        char = self.generate_character()
        lines = [
            f"\n{'*'*60}",
            f"CHARACTER: {char['name']}",
            f"{'*'*60}",
            f"Class: {char['class']} | Race: {char['race']} | Level: {char['level']}",
            f"Personality: {char['personality']} | Alignment: {char['alignment']}",
            f"{'*'*60}",
            f"Backstory: {char['backstory']}",
            f"\nSTATS:",
        ]
        for stat, val in char["stats"].items():
            lines.append(f"  {stat}: {val}")
        lines.append(f"\nEQUIPMENT:")
        for item in char["equipment"]:
            lines.append(f"  - {item}")
        lines.append(f"\nABILITIES:")
        for ability in char["abilities"]:
            lines.append(f"  - {ability}")
        lines.append(f"\nSKILLS:")
        for skill in char["skills"]:
            lines.append(f"  - {skill}")
        lines.append(f"\nINVENTORY:")
        for item in char["inventory"]:
            lines.append(f"  - {item}")
        lines.append(f"\n{'*'*60}\n")
        return lines

    def generate_character(self):
        name = self.name_gen.generate_character_name()
        char_class = random.choice(self.classes)
        race = random.choice(self.races)
        level = random.randint(1, 100)
        personality = random.choice(self.personalities)
        alignment = random.choice(["Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral",
            "True Neutral", "Chaotic Neutral", "Lawful Evil", "Neutral Evil", "Chaotic Evil"])
        stats = {stat: random.randint(1, 20) for stat in ["Strength", "Dexterity", "Constitution",
            "Intelligence", "Wisdom", "Charisma"]}
        equipment = random.choice(self.equipment_sets)
        abilities = [self.desc_gen.generate_ability() for _ in range(random.randint(2, 8))]
        skills = [f"{skill} {random.randint(1, 20)}" for skill in [
            "Stealth", "Persuasion", "Arcana", "Athletics", "Insight", "Intimidation",
            "Investigation", "Nature", "Perception", "Performance", "Religion", "Sleight of Hand",
            "Survival", "History", "Animal Handling", "Medicine", "Minor Illusion", "Mage Hand"
        ]]
        skills = random.sample(skills, random.randint(3, 8))
        inventory = [f"{random.randint(1, 99)}x {random.choice(['Gold Coins', 'Rations', 'Herbs', 'Potions', 'Arrows', 'Rope', 'Torch', 'Lockpick'])}" for _ in range(random.randint(5, 20))]
        backstory = self.generate_backstory()
        return {
            "name": name,
            "class": char_class,
            "race": race,
            "level": level,
            "personality": personality,
            "alignment": alignment,
            "stats": stats,
            "equipment": equipment,
            "abilities": abilities,
            "skills": skills,
            "inventory": inventory,
            "backstory": backstory,
            "hit_points": random.randint(10, 200),
            "mana": random.randint(10, 500),
            "armor_class": random.randint(10, 25),
            "experience": random.randint(0, 1000000),
            "age": random.randint(18, 800),
            "height": f"{random.randint(4, 7)} feet {random.randint(0, 11)} inches",
            "weight": f"{random.randint(80, 400)} lbs",
            "eyes": random.choice(["blue", "green", "red", "gold", "purple", "black", "white", "silver"]),
            "hair": random.choice(["black", "blonde", "brown", "red", "white", "silver", "blue", "green", "purple"]),
            "tattoos": [f"{random.choice(['Runic', 'Geometric', 'Animal', 'Celestial', 'Shadow'])} {random.choice(['Mark', 'Symbol', 'Design', 'Sigil'])} on {random.choice(['arms', 'chest', 'back', 'face', 'hands'])}" for _ in range(random.randint(0, 3))],
            "allies": [self.name_gen.generate_character_name() for _ in range(random.randint(1, 5))],
            "enemies": [self.name_gen.generate_character_name() for _ in range(random.randint(0, 5))],
            "quests": [f"Quest #{random.randint(1, 100)}" for _ in range(random.randint(1, 5))]
        }

    def generate_backstory(self):
        template = random.choice(self.backstories)
        return template.format(
            location=random.choice(["the Citadel", "the Forest", "the Mountain", "the Ocean", "the Desert"]),
            status=random.choice(["nobles", "warriors", "scholars", "farmers", "outcasts"]),
            event=random.choice(["the Great War", "the Shattering", "the Burning", "the Flood", "the Awakening"]),
            creature=random.choice(["a dragon", "a wizard", "a tribe", "a goddess"]),
            artifact=random.choice(["the Amulet of Power", "the Sword of Light", "the Tome of Shadows"]),
            biome=random.choice(["Frozen Wastes", "Enchanted Forest", "Volcanic Lands"]),
            number=random.randint(10, 1000),
            character=random.choice(["the Archmage", "the Warrior", "the King", "the Oracle"]),
            skill=random.choice(["pyromancy", "shadow magic", "divine healing", "assassination"]),
            entity=random.choice(["a demon", "a deity", "a lich", "a dragon"]),
            power=random.choice(["fire powers", "shadow mastery", "immortality", "mind control"]),
            deity=random.choice(["the Sun God", "the Moon Goddess"]),
            title=random.choice(["Champion", "Prophet", "Guardian", "Warden"]),
            thing=random.choice(["his family", "his homeland", "his love", "his honor"]),
            ability=random.choice(["time manipulation", "void walking", "dream walking"]),
            source=random.choice(["the Void", "the Shadow", "the Corruption"]),
            former=random.choice(["hero", "scholar", "warrior", "priest"]),
            current=random.choice(["villain", "madman", "outcast", "monster"]),
            secret=random.choice(["a terrible truth", "a hidden power", "a dark prophecy"]),
            property=random.choice(["temporal", "spatial", "psychic", "elemental"]),
            effect=random.choice(["changed the fabric of reality", "opened a portal to another dimension", "granted omniscience"]),
            consequence=random.choice(["a civil war", "anarchy", "the rise of a tyrant", "the destruction of the kingdom"]),
            reward=random.choice(["immortality", "vast wealth", "eternal fame", "divine blessing"])
        )
