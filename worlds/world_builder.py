import random
from generators.names import NameGenerator
from generators.descriptions import DescriptionGenerator

class WorldBuilder:
    def __init__(self):
        self.name_gen = NameGenerator()
        self.desc_gen = DescriptionGenerator()
        self.biomes = ["Frozen Tundra", "Volcanic Wastes", "Enchanted Forest", "Crystal Desert",
            "Abyssal Ocean", "Sky Islands", "Shadow Realm", "Celestial Plains",
            "Void Caverns", "Ember Mountains", "Frostfire Valley", "Dreaming Meadows",
            "Storm Coast", "Mystic Jungle", "Iron Desert", "Obsidian Plains",
            "Luminara Forest", "Shadowmere Lake", "Starfall Peaks", "Void Blossom Fields"]
        self.nations = ["Verdania", "Thalmora", "Drakhaven", "Solmist", "Umbraxis", "Frostveil",
            "Pyrestan", "Shadovar", "Crystalreach", "Emberhold", "Nightvale", "Starfall",
            "Ironpeak", "Shadowmere", "Dawnspire", "Eternalia", "Voidmere", "Luminara",
            "Stormhaven", "Wyndmoor"]
        self.civilizations = ["The Arcane Society", "The Iron Dominion", "The Crystal Pact",
            "The Void Collective", "The Ember Society", "The Frost Legion", "The Starfall Alliance",
            "The Abyssal Court", "The Celestial Guild", "The Dreaming Cult", "The Storm Riders",
            "The Dark Brotherhood", "The Holy Crusade", "The Wandering Tribes", "The Ancient Order"]
        self.natural_features = [
            "The Great Rift Valley", "The Endless Ocean", "The Crystal Mountain Range",
            "The Shadow Forest", "The Ember Falls", "The Frostspire Peaks", "The Void Lake",
            "The Celestial River", "The Dreaming Swamp", "The Storm Caldera",
            "The Luminara Caves", "The Ironwood Forest", "The Obsidian Plains",
            "The Starfall Desert", "The Abyssal Chasm", "The Sky Pillars",
            "The Crystal Caverns", "The Ember Wastes", "The Shadow Gate", "The Holy Spring"
        ]
        self.magic_systems = ["Elemental Magic", "Void Magic", "Celestial Magic", "Shadow Magic",
            "Chrono Magic", "Psychic Magic", "Nature Magic", "Blood Magic",
            "Arcane Magic", "Divine Magic", "Infernal Magic", "Chaos Magic",
            "Order Magic", "Life Magic", "Death Magic", "Soul Magic"]
        self.history_events = [
            "The Great Convergence", "The Age of Ruin", "The Eternal Dawn", "The Shattering",
            "The War of the Gods", "The Fall of the First Empire", "The Binding of the Void",
            "The Awakening of the Titans", "The Purification of the Realm", "The Forgotten Exodus",
            "The Rise of the Shadow", "The Golden Age", "The Dark Age", "The Rebirth",
            "The Final Battle", "The Age of Heroes", "The Era of Silence", "The Great Expansion"
        ]
        self.population_info = [
            "populated primarily by {race} who {activity}",
            "home to {race} and {race} who {activity}",
            "inhabited by {race} who {activity} and {race} who {activity}",
            "a melting pot of {race}, {race}, and {race} all {activity}",
            "populated by {race} who {activity} alongside {creature} who {activity}"
        ]
        self.races = ["humans", "elves", "dwarves", "orcs", "gnomes", "halflings", "dragonborn",
            "tieflings", "aasimar", "goliaths", "kenku", "tabaxi", "tortles", "changelings",
            "warforged", "shifters", "minotaurs", "satyrs", "fairies", "elementals"]
        self.activities = ["farm the {resource}", "trade {resource} with neighboring realms",
            "hunt {creature} for sport", "mine {resource} from the {feature}",
            "worship {deity} in grand temples", "practice {magic} as a way of life",
            "craft {resource} into magnificent works of art", "train warriors to defend against {threat}",
            "study {resource} at the great academies", "navigate the {feature} in great fleets"]

    def build_full_world(self):
        lines = []
        world_name = f"{random.choice(self.nations)} and the {random.choice(self.biomes)}"
        lines.append(f"\n{'#'*80}")
        lines.append(f"# THE WORLD OF {world_name.upper()}")
        lines.append(f"{'#'*80}")
        lines.append(f"")
        lines.append(f"Overview:")
        lines.append(f"  This realm encompasses {random.randint(10, 1000)} million square miles of {random.choice(['diverse', 'treacherous', 'beautiful', 'dangerous', 'mysterious'])} terrain.")
        lines.append(f"  The dominant magical force is {random.choice(self.magic_systems)}.")
        lines.append(f"  The world was shaped by {random.choice(self.history_events)} {random.randint(1000, 1000000)} years ago.")
        lines.append(f"")

        for nation_idx in range(random.randint(5, 15)):
            nation = self.build_nation(nation_idx)
            lines.extend(nation)
            lines.append("")

        for feature_idx in range(random.randint(3, 8)):
            feature = self.build_feature(feature_idx)
            lines.extend(feature)
            lines.append("")

        lines.append(f"\n{'#'*80}")
        lines.append(f"# WORLD SUMMARY")
        lines.append(f"{'#'*80}")
        lines.append(f"  Total Nations: {len(self.nations)}")
        lines.append(f"  Total Biomes: {len(self.biomes)}")
        lines.append(f"  Total Natural Features: {len(self.natural_features)}")
        lines.append(f"  Magic Systems: {len(self.magic_systems)}")
        lines.append(f"  History Events: {len(self.history_events)}")
        lines.append(f"  Current Age: {random.choice(self.history_events)}")
        lines.append(f"{'#'*80}")
        return lines

    def build_nation(self, index):
        name = self.nations[index % len(self.nations)]
        capital = self.name_gen.generate_city_name()
        population = random.randint(10000, 100000000)
        race = random.choice(self.races)
        activity = random.choice(self.activities).format(
            resource=random.choice(["gold", "crystal", "magic", "food", "steel", "knowledge"]),
            creature=random.choice(["dragons", "giants", "beasts", "elementals"]),
            feature=random.choice(["mountains", "forests", "oceans", "caves"]),
            deity=random.choice(["the Sun God", "the Moon Goddess", "the Shadow Lord"]),
            magic=random.choice(["Elemental Magic", "Void Magic", "Celestial Magic"]),
            threat=random.choice(["the Void", "the Shadow", "the Corruption"])
        )
        lines = [
            f"--- NATION {index+1}: {name} ---",
            f"  Capital: {capital}",
            f"  Population: {population:,} {race}",
            f"  Government: {random.choice(['Monarchy', 'Republic', 'Theocracy', 'Oligarchy', 'Anarchy', 'Magocracy'])}",
            f"  Activity: {activity}",
            f"  Military: {random.randint(1000, 1000000)} soldiers",
            f"  Magic Level: {random.choice(['Low', 'Medium', 'High', 'Supreme', 'Transcendent'])}",
            f"  Relations: {random.choice(['Allied', 'Hostile', 'Neutral', 'Trade Partner', 'At War'])} with {random.choice(self.nations)}",
            f"  Founded: {random.randint(1, 10000)} years ago",
            f"  Leader: {self.name_gen.generate_character_name()}",
            f"  Major Exports: {random.choice(['crystals', 'weapons', 'knowledge', 'magic', 'food', 'ore'])}",
            f"  Major Imports: {random.choice(['technology', 'magic', 'food', 'ore', 'luxuries', 'artifacts'])}",
            f"  National Trait: {self.desc_gen.generate_sentence()}",
            f"  National Animal: {self.name_gen.generate_creature()}"
        ]
        return lines

    def build_feature(self, index):
        name = self.natural_features[index % len(self.natural_features)]
        biome = random.choice(self.biomes)
        lines = [
            f"--- FEATURE {index+1}: {name} ---",
            f"  Biome: {biome}",
            f"  Size: {random.randint(10, 10000)} square miles",
            f"  Danger Level: {random.choice(['Low', 'Medium', 'High', 'Extreme', 'Fatal'])}",
            f"  Inhabitants: {random.choice(self.races)} and {self.name_gen.generate_creature()}",
            f"  Resources: {', '.join([random.choice(['gold', 'crystals', 'magic', 'food', 'ore', 'gems']) for _ in range(random.randint(2, 5))])}",
            f"  {self.desc_gen.generate_sentence()}",
            f"  {self.desc_gen.generate_sentence()}",
            f"  Exploration Level: {random.choice(['Explored', 'Partially Explored', 'Uncharted', 'Forbidden'])}",
            f"  Guardian: {self.name_gen.generate_creature()}"
        ]
        return lines
