import random
from datetime import datetime

class CharacterGenerator:
    def __init__(self):
        self.first_names = ["Aethon", "Zyrion", "Xanaris", "Morveth", "Kaelith", "Draven", "Vexara", "Nyxara", "Othara", "Thalric",
            "Pyra", "Luxina", "Sorath", "Eldric", "Valara", "Shadar", "Faelan", "Brielle", "Galen", "Haziel",
            "Ithil", "Jorun", "Kalith", "Lyralei", "Myrana", "Ravena", "Syntara", "Thalia", "Umbra", "Caelum",
            "Drakar", "Eryndor", "Falcon", "Ithil", "Jorun", "Kalith", "Nyx", "Othara", "Pyrath", "Qysara",
            "Ravena", "Syntara", "Thalia", "Umbra", "Vex", "Wyr", "Xyl", "Yth", "Zan", "Aur",
            "Celeste", "Diana", "Elara", "Freya", "Gemma", "Hana", "Iris", "Jade", "Kira", "Luna",
            "Maya", "Nora", "Olivia", "Priya", "Quinn", "Rosa", "Sage", "Tessa", "Vera", "Willa",
            "Yuki", "Zara", "Aiko", "Bianca", "Cleo", "Dahlia", "Esme", "Fiona", "Gina", "Hana",
            "Isla", "Juno", "Kaya", "Lilith", "Mika", "Nina", "Ora", "Poppy", "Rhea", "Sloane",
            "Trixie", "Vivian", "Wynne", "Xena", "Yvette", "Zelda", "Amara", "Brielle", "Chloe", "Daphne"]
        self.last_names = ["Stormweaver", "Shadowborn", "Starfall", "Ironfist", "Crimsonblade", "Frostheart", "Emberwing", "Voidwalker",
            "Dawnbringer", "Nightshade", "Lightbringer", "Darkclaw", "Earthshaker", "Windrider", "Stonesinger",
            "Moonspeaker", "Sunforger", "Starweaver", "Thundercall", "Mistwalker", "Rosewood", "Silverthorn",
            "Ashford", "Blackwell", "Cedarcrest", "Dunham", "Everhart", "Fairfax", "Greenfield", "Hawthorne",
            "Ironwood", "Jasper", "Kingsley", "Laurel", "Montclair", "Nettlesworth", "Oakley", "Pemberton",
            "Quincy", "Redmond", "Sternwood", "Tremaine", "Underwood", "Vale", "Whitmore", "Xavier",
            "Yates", "Zephyr", "Blackwood", "Carlisle", "Dawnbringer"]
        self.classes = ["Mage", "Warrior", "Rogue", "Cleric", "Ranger", "Paladin", "Bard", "Druid",
            "Monk", "Sorcerer", "Warlock", "Brawler", "Spellblade", "Time Mage", "Void Walker",
            "Star Caller", "Dream Weaver", "Chaos Knight", "Iron Guard", "Crystal Sage"]
        self.races = ["Human", "Elf", "Dwarf", "Dragonborn", "Tiefling", "Aasimar", "Goliath",
            "Kenku", "Tabaxi", "Shifter", "Warforged", "Fairy", "Satyr", "Minotaur", "Elemental"]
        self.personality_traits = ["Charismatic", "Mysterious", "Playful", "Serious", "Gentle",
            "Bold", "Shy", "Confident", "Whimsical", "Intense", "Caring", "Independent",
            "Affectionate", "Playful", "Intelligent", "Witty", "Passionate", "Reserved",
            "Adventurous", "Sweet"]
        self.hobbies = ["Reading ancient tomes", "Playing the lute", "Sword fighting", "Gardening",
            "Stargazing", "Cooking exotic meals", "Horseback riding", "Painting", "Dancing",
            "Fishing", "Crafting jewelry", "Exploring ruins", "Brewing potions", "Singing",
            "Horse racing", "Archery", "Meditation", "Hunting", "Writing poetry", "Collecting artifacts"]
        self.appearance = [
            "with {hair} hair and {eyes} eyes",
            "with {hair} flowing hair and a {build} figure",
            "with piercing {eyes} eyes and {skin} skin",
            "with {hair} hair that catches the light beautifully",
            "with {height} tall, {build} and {eyes} eyes",
            "with a delicate {height} frame and {hair} hair",
            "with an athletic {build} and {hair} hair",
            "with {height} and a graceful {build}",
            "with {eyes} eyes that sparkle like {light}",
            "with {hair} hair and a mysterious {build}"]
        self.hair_colors = ["silver", "golden", "jet black", "auburn", "platinum", "fire-red",
            "emerald green", "deep blue", "rose pink", "violet", "ice white", "bronze"]
        self.eye_colors = ["sapphire", "emerald", "ruby", "amber", "violet", "silver",
            "gold", "crimson", "jade", "midnight blue", "hazel", "storm gray"]
        self.build_types = ["slender", "athletic", "curvaceous", "petite", "tall", "muscular", "delicate"]
        self.skin_tones = ["porcelain", "sun-kissed", "olive", "fair", "warm bronze", "golden"]
        self.light_sources = ["starlight", "candlelight", "moonlight", "sunlight", "magic"]
        self.heights = ["5'2\"", "5'5\"", "5'7\"", "5'9\"", "5'11\"", "6'0\"", "6'2\"", "4'11\""]
        self.clothing_styles = ["elegant dress", "armor", "robes", "casual wear", "royal gown",
            "warrior garb", "flowing cloak", "formal suit", "fantasy outfit", "traditional attire"]
        self.smells = ["lavender", "jasmine", "woodsmoke", "amber", "vanilla", "cinnamon",
            "ocean breeze", "fresh rain", "rose petals", "musk"]

    def generate_dateable_char(self, index):
        name = random.choice(self.first_names) + " " + random.choice(self.last_names)
        char_class = random.choice(self.classes)
        race = random.choice(self.races)
        personality = random.choice(self.personality_traits)
        hobby = random.choice(self.hobbies)
        hair = random.choice(self.hair_colors)
        eyes = random.choice(self.eye_colors)
        build = random.choice(self.build_types)
        skin = random.choice(self.skin_tones)
        height = random.choice(self.heights)
        light = random.choice(self.light_sources)
        clothing = random.choice(self.clothing_styles)
        smell = random.choice(self.smells)
        age = random.randint(18, 35)
        affection = 0
        compatibility = random.randint(10, 100)
        attractiveness = random.randint(20, 100)
        intelligence = random.randint(20, 100)
        charm = random.randint(20, 100)
        humor = random.randint(20, 100)
        wealth = random.randint(1, 10)
        level = random.randint(1, 50)
        appearance_template = random.choice(self.appearance)
        appearance = appearance_template.format(
            hair=hair, eyes=eyes, build=build, skin=skin, height=height, light=light)
        stats = {
            "Attractiveness": attractiveness,
            "Charm": charm,
            "Intelligence": intelligence,
            "Humor": humor,
            "Wealth": wealth * 10,
            "Affection": affection,
            "Compatibility": compatibility,
            "Level": level,
            "Happiness": random.randint(50, 100),
            "Mood": random.choice(["Happy", "Playful", "Melancholic", "Excited", "Calm"]),
            "Status": random.choice(["Single", "Available", "Open", "Widowed"])
        }
        gifts = [f"{random.randint(1, 100)}x {random.choice(['Rose', 'Chocolate', 'Jewel', 'Poem', 'Perfume', 'Necklace', 'Flower', 'Ring'])}"]
        return {
            "index": index,
            "name": name,
            "class": char_class,
            "race": race,
            "age": age,
            "personality": personality,
            "hobby": hobby,
            "appearance": appearance,
            "clothing": clothing,
            "smell": smell,
            "stats": stats,
            "gifts": gifts,
            "first_impression": self.generate_first_impression(),
            "favorite": random.choice(["flowers", "jewelry", "books", "music", "adventure", "food", "art"]),
            "dislike": random.choice(["rudeness", "arrogance", "boredom", "mess", "silence"]),
            "fear": random.choice(["heights", "darkness", "spiders", "abandonment", "being alone"]),
            "dream": random.choice(["travel the world", "find true love", "master magic", "build a home", "become legendary"]),
            "favorite_date": random.choice(["stargazing", "dinner", "adventure", "dancing", "reading", "cooking", "walking"]),
            "gift_preference": random.choice(["flowers", "jewelry", "books", "chocolate", "perfume", "art", "music"]),
            "love_language": random.choice(["words of affirmation", "quality time", "receiving gifts", "acts of service", "physical touch"]),
            "backstory": self.generate_backstory(),
            "allies": [random.choice(self.first_names) + " " + random.choice(self.last_names) for _ in range(random.randint(1, 3))],
            "crush_on": random.choice(self.first_names) + " " + random.choice(self.last_names) if random.random() > 0.5 else None
        }

    def generate_first_impression(self):
        impressions = [
            "You are immediately captivated by {name}'s presence.",
            "{name} catches your eye from across the room.",
            "There is something magnetic about {name}.",
            "You feel an inexplicable connection to {name}.",
            "{name} radiates an aura that draws you in.",
            "Your heart skips a beat when you see {name}.",
            "{name} seems to be looking right at you.",
            "You feel a strange warmth in {name}'s presence.",
            "{name} is the most beautiful person in the room.",
            "Something about {name} makes your pulse race."
        ]
        return random.choice(impressions).format(name="{name}")

    def generate_backstory(self):
        stories = [
            "{name} grew up in a {location} and has always dreamed of {dream}.",
            "Born into a {status} family, {name} learned to {hobby} from a young age.",
            "{name} lost {thing} in the {event} and has been searching for purpose ever since.",
            "Raised by {creature} in the {location}, {name} developed a love for {hobby}.",
            "{name} discovered {artifact} during the {event}, which changed their destiny.",
            "After the {event}, {name} wandered the {biome} until finding {thing}.",
            "{name} was chosen by {deity} during the {event}, becoming {title}.",
            "The {event} left {name} with {scar}, but their spirit remains unbroken.",
            "{name} made a pact with {entity} to {goal}, at a great personal cost.",
            "Having survived the {event}, {name} now seeks {goal} with unwavering determination."
        ]
        story = random.choice(stories)
        return story.format(
            name="{name}",
            location=random.choice(["forest village", "coastal town", "mountain city", "desert oasis", "enchanted grove"]),
            dream=random.choice(["true love", "great adventure", "magical mastery", "eternal peace"]),
            status=random.choice(["noble", "humble", "mysterious", "royal"]),
            hobby=random.choice(["playing the lute", "sword fighting", "painting", "cooking", "dancing"]),
            thing=random.choice(["their family", "their homeland", "their love", "their honor"]),
            event=random.choice(["the Great War", "the Shattering", "the Burning", "the Flood"]),
            creature=random.choice(["a dragon", "a wizard", "a tribe of elves", "a mysterious spirit"]),
            artifact=random.choice(["the Amulet of Power", "the Sword of Light", "the Tome of Shadows"]),
            biome=random.choice(["Frozen Wastes", "Enchanted Forest", "Volcanic Lands"]),
            deity=random.choice(["the Sun God", "the Moon Goddess"]),
            title=random.choice(["Champion", "Prophet", "Guardian", "Warden"]),
            scar=random.choice(["a mark of power", "a scar of destiny", "a blessing of ages"]),
            entity=random.choice(["a demon", "a deity", "a lich"]),
            goal=random.choice(["save the world", "find true love", "master the elements"]))

    def generate_date_locations(self):
        return [
            {"name": "Crystal Terrace", "atmosphere": "romantic", "activity": "stargazing", "cost": 5, "bonus": "intimacy"},
            {"name": "Emerald Garden", "atmosphere": "serene", "activity": "walking", "cost": 3, "bonus": "comfort"},
            {"name": "Golden Tavern", "atmosphere": "lively", "activity": "dining", "cost": 10, "bonus": "fun"},
            {"name": "Ancient Library", "atmosphere": "intellectual", "activity": "reading", "cost": 2, "bonus": "intelligence"},
            {"name": "Moonlit Lake", "atmosphere": "magical", "activity": "boat ride", "cost": 8, "bonus": "wonder"},
            {"name": "Firelight Ballroom", "atmosphere": "elegant", "activity": "dancing", "cost": 15, "bonus": "romance"},
            {"name": "Shadow Market", "atmosphere": "mysterious", "activity": "browsing", "cost": 7, "bonus": "excitement"},
            {"name": "Sunrise Cliff", "atmosphere": "breathtaking", "activity": "picnic", "cost": 4, "bonus": "peace"},
            {"name": "Enchanted Forest", "atmosphere": "magical", "activity": "exploring", "cost": 6, "bonus": "adventure"},
            {"name": "Crystal Spa", "atmosphere": "relaxing", "activity": "massage", "cost": 20, "bonus": "luxury"},
            {"name": "Royal Observatory", "atmosphere": "scholarly", "activity": "stargazing", "cost": 12, "bonus": "wisdom"},
            {"name": "Bamboo Garden", "atmosphere": "tranquil", "activity": "meditation", "cost": 3, "bonus": "calm"},
            {"name": "Crimson Stage", "atmosphere": "artistic", "activity": "performance", "cost": 9, "bonus": "passion"},
            {"name": "Ocean Cliff", "atmosphere": "dramatic", "activity": "sunset watching", "cost": 8, "bonus": "beauty"},
            {"name": "Arcane Arena", "atmosphere": "thrill-seeking", "activity": "duel", "cost": 18, "bonus": "excitement"},
            {"name": "Starlight Chapel", "atmosphere": "sacred", "activity": "prayer", "cost": 1, "bonus": "blessing"},
            {"name": "Floating Island", "atmosphere": "dreamy", "activity": "flying", "cost": 25, "bonus": "euphoria"},
            {"name": "Cave of Echoes", "atmosphere": "mysterious", "activity": "exploring", "cost": 11, "bonus": "mystery"},
            {"name": "Winter Palace", "atmosphere": "regal", "activity": "feasting", "cost": 30, "bonus": "royalty"},
            {"name": "Desert Oasis", "atmosphere": "romantic", "activity": "drinking", "cost": 14, "bonus": "warmth"}
        ]

    def generate_gifts(self):
        return [
            {"name": "Red Roses", "value": 5, "affection_bonus": 15, "description": "Classic red roses symbolizing love"},
            {"name": "Diamond Necklace", "value": 50, "affection_bonus": 50, "description": "A stunning diamond pendant"},
            {"name": "Love Letter", "value": 2, "affection_bonus": 25, "description": "A heartfelt handwritten letter"},
            {"name": "Perfume", "value": 15, "affection_bonus": 20, "description": "An elegant fragrance"},
            {"name": "Chocolate Box", "value": 8, "affection_bonus": 12, "description": "Handcrafted artisanal chocolates"},
            {"name": "Magic Amulet", "value": 30, "affection_bonus": 35, "description": "A protective magical charm"},
            {"name": "Poetry Book", "value": 5, "affection_bonus": 18, "description": "A collection of love poems"},
            {"name": "Crystal Ring", "value": 25, "affection_bonus": 30, "description": "A shimmering crystal engagement ring"},
            {"name": "Stuffed Bear", "value": 3, "affection_bonus": 10, "description": "A soft and cuddly stuffed bear"},
            {"name": "Music Box", "value": 12, "affection_bonus": 22, "description": "A beautiful mechanical music box"},
            {"name": "Flower Crown", "value": 7, "affection_bonus": 16, "description": "A crown made of fresh flowers"},
            {"name": "Gold Bracelet", "value": 20, "affection_bonus": 28, "description": "An elegant gold bangle"},
            {"name": "Painting", "value": 18, "affection_bonus": 24, "description": "A beautiful portrait painting"},
            {"name": "Love Potion", "value": 100, "affection_bonus": 60, "description": "A mysterious glowing potion"},
            {"name": "Star Map", "value": 14, "affection_bonus": 20, "description": "A map of the night sky"},
            {"name": "Silk Scarf", "value": 9, "affection_bonus": 14, "description": "A luxurious silk scarf"},
            {"name": "Pocket Watch", "value": 22, "affection_bonus": 26, "description": "An ornate silver pocket watch"},
            {"name": "Gemstone Earrings", "value": 35, "affection_bonus": 42, "description": "Sparkling gemstone earrings"},
            {"name": "Birthday Cake", "value": 6, "affection_bonus": 15, "description": "A delicious cake with candles"},
            {"name": "Love Token", "value": 3, "affection_bonus": 50, "description": "A symbolic token of affection"}
        ]
