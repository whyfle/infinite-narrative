import random

class NameGenerator:
    def __init__(self):
        self.prefixes = ["Aeth", "Zyr", "Xan", "Mor", "Kael", "Dra", "Vex", "Nyx", "Oth", "Thal",
            "Pyra", "Grim", "Lux", "Sor", "Nyx", "Eld", "Val", "Shad", "Fae", "Ron",
            "Bri", "Cael", "Dra", "Ery", "Fal", "Gal", "Haz", "Ith", "Jor", "Kal",
            "Lyr", "Myr", "Nyx", "Oth", "Pyr", "Qys", "Rav", "Syn", "Tha", "Umb",
            "Vir", "Wyr", "Xyl", "Yth", "Zan", "Aur", "Bri", "Cri", "Dor", "Eld"]
        self.suffixes = ["ion", "aris", "mund", "beth", "rath", "mor", "vel", "nax", "dris", "korn",
            "lium", "aris", "beth", "cord", "nis", "thar", "vorn", "wick", "zor", "lan",
            "mir", "dris", "korn", "lium", "aris", "beth", "cord", "nis", "thar", "vorn"]
        self.kingdom_words = ["Verdania", "Thalmora", "Drakhaven", "Solmist", "Umbraxis", "Frostveil", "Pyrestan", "Shadovar", "Crystalreach", "Emberhold",
            "Nightvale", "Starfall", "Ironpeak", "Shadowmere", "Dawnspire", "Eternalia", "Voidmere", "Luminara", "Stormhaven", "Wyndmoor",
            "Ashenmoor", "Blightvale", "Crimsonwatch", "Darkholme", "Eboncrest", "Falcontower", "Grimstone", "Hollowfort", "Ivorykeep", "Jade Sanctum",
            "Kingsfall", "Lakeshore", "Mistmeadow", "Netherhold", "Oakhollow", "Palehall", "Quicksilver", "Redwater", "Silverdawn", "Thornwall"]
        self.city_words = ["Ashport", "Brimwick", "Cinderfall", "Duskhollow", "Embergate", "Frostpoint", "Gloomhaven", "Holloway", "Ironmaw", "Jade's Rest",
            "Kingscross", "Lanternmere", "Mistfield", "Netherwick", "Oakhaven", "Palehollow", "Quartzvale", "Redcliff", "Silverfall", "Thornbury",
            "Ashenvale", "Blackmere", "Cragmere", "Duskwall", "Emberstone", "Flamehollow", "Gloommere", "Hollowmere", "Ironvale", "Jadehaven",
            "Kingsmere", "Lakehollow", "Mistvale", "Nethervale", "Oakhollow", "Palevale", "Quicksilver", "Redvale", "Silverholm", "Thornvale"]
        self.river_words = ["River of Whispers", "Silverthread", "Voidflow", "Ashenmere", "Crystalmere", "Emberwash", "Frostflow", "Gloomwater", "Hollowstream",
            "Ironspine River", "Jadescale", "Kingsflow", "Luminflow", "Mistwater", "Netherflow", "Obsidianmere", "Paleflow", "Quicksilver Run",
            "Redmere", "Stormflow", "Thornwater", "Umbraflow", "Verdantmere", "Whitewater", "Xanadu River", "Ythmere", "Zephyrflow",
            "Aethonmere", "Brielle", "Crimsonmere", "Drakewater", "Embermere"]
        self.mountain_words = ["Mount Aether", "Peak of Whispers", "Shadowspire", "Voidpeak", "Crystalthorn", "Ember Mountain", "Frostspire", "Gloompeak",
            "Ironhorn", "Jade Mountain", "Kingspeak", "Luminpeak", "Mistspire", "Netherpeak", "Obsidianhorn", "Palehorn", "Quartzspire",
            "Redhorn", "Stonepeak", "Thornspire", "Umbrahorn", "Verdantspire", "Whithorn", "Xanaduspire", "Ythspire", "Zephyrpeak",
            "Aethspire", "Briarspire", "Crimsonspire", "Drakespire"]
        self.artifact_words = ["The", "Ancient", "Forgotten", "Cursed", "Blessed", "Eternal", "Mythic", "Divine", "Shadow", "Void",
            "Star", "Celestial", "Abyssal", "Primordial", "Apocalyptic", "Infinity", "Boundless", "Omnipotent", "Transcendent", "Supreme"]
        self.creature_prefixes = ["Shadow", "Void", "Star", "Crystal", "Fire", "Ice", "Storm", "Dark", "Light", "Ancient",
            "Fallen", "Holy", "Hell", "Moon", "Sun", "Celestial", "Abyssal", "Ethereal", "Elemental", "Primal"]
        self.creature_types = ["Dragon", "Griffin", "Phoenix", "Leviathan", "Titans", "Golem", "Wraith", "Demon", "Angel", "Beast",
            "Hydra", "Chimera", "Cerberus", "Minotaur", "Centaur", "Manticore", "Sphinx", "Basilisk", "Wyvern", "Pegasus"]
        self.character_first = ["Aethon", "Zyrion", "Xanaris", "Morveth", "Kaelith", "Draven", "Vexara", "Nyxara", "Othara", "Thalric",
            "Pyra", "Grimjaw", "Luxina", "Sorath", "Nyx", "Eldric", "Valara", "Shadar", "Faelan", "Ronin",
            "Brielle", "Caelum", "Drakar", "Eryndor", "Falcon", "Galen", "Haziel", "Ithil", "Jorun", "Kalith",
            "Lyralei", "Myrana", "Nyxara", "Othara", "Pyrath", "Qysara", "Ravena", "Syntara", "Thalia", "Umbra"]
        self.character_last = ["Stormweaver", "Shadowborn", "Starfall", "Ironfist", "Crimsonblade", "Frostheart", "Emberwing", "Voidwalker",
            "Dawnbringer", "Nightshade", "Lightbringer", "Darkclaw", "Earthshaker", "Windrider", "Stonesinger",
            "Moonspeaker", "Sunforger", "Starweaver", "Thundercall", "Mistwalker"]

    def generate_name(self):
        prefix = random.choice(self.prefixes)
        suffix = random.choice(self.suffixes)
        return prefix + suffix

    def generate_character_name(self):
        return f"{random.choice(self.character_first)} {random.choice(self.character_last)}"

    def generate_kingdom_name(self):
        return random.choice(self.kingdom_words)

    def generate_city_name(self):
        return random.choice(self.city_words)

    def generate_river_name(self):
        return random.choice(self.river_words)

    def generate_mountain_name(self):
        return random.choice(self.mountain_words)

    def generate_artifact_name(self):
        article = random.choice(self.artifact_words)
        noun = self.generate_noun()
        return f"{article} {noun}"

    def generate_curse_name(self):
        return f"Curse of the {random.choice(self.generate_artifact_name().split()[1:])} {random.choice(self.creature_types).lower()}"

    def generate_name_batch(self, count=5):
        return [self.generate_name() for _ in range(count)]

    def generate_noun(self):
        nouns = ["Sword", "Shield", "Crown", "Throne", "Realm", "Citadel", "Sanctum", "Tower", "Vault", "Grove",
            "Abyss", "Peak", "Valley", "River", "Ocean", "Forest", "Desert", "Mountain", "Island", "Continent",
            "Empire", "Dynasty", "Legacy", "Prophecy", "Tome", "Codex", "Scroll", "Relic", "Grail", "Chalice",
            "Mirror", "Lantern", "Key", "Door", "Gate", "Wall", "Bridge", "Road", "Path", "Trail",
            "Compass", "Astrolabe", "Crystal", "Gem", "Orb", "Sphere", "Pyramid", "Ziggurat", "Monolith"]
        return random.choice(nouns)

    def generate_creature(self):
        return f"{random.choice(self.creature_prefixes)} {random.choice(self.creature_types)}"

    def generate_property(self):
        props = ["Infinite", "Eternal", "Boundless", "Primordial", "Apocalyptic", "Mythic", "Divine", "Shadow", "Void", "Celestial"]
        return random.choice(props)
