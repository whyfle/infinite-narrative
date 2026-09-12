import random
from generators.names import NameGenerator
from generators.descriptions import DescriptionGenerator

class QuestGenerator:
    def __init__(self):
        self.name_gen = NameGenerator()
        self.desc_gen = DescriptionGenerator()
        self.quest_types = ["Main", "Side", "Epic", "Legendary", "Mythic", "Hidden", "Secret", "World", "Dimension", "Cosmic"]
        self.quest_givers = ["The Archmage", "The Warlord", "The Prophet", "The Ancient", "The Dragon",
            "The Spirit", "The Oracle", "The King", "The Thief", "The Monk", "The Sage",
            "The Hermit", "The Merchant", "The Ranger", "The Priest", "The Necromancer",
            "The Paladin", "The Bard", "The Alchemist", "The Druid", "The Ranger",
            "The Seer", "The Wanderer", "The Commander", "The Captain", "The Baron"]
        self.quest_locations = ["The Citadel of Shadows", "The Temple of Echoes", "The Abyssal Chasm",
            "The Crystal Spire", "The Void Library", "The Ember Court", "The Frost Throne",
            "The Dreaming Forest", "The Storm Gate", "The Ancient Library", "The Dragon's Peak",
            "The Shadow Realm", "The Celestial Garden", "The Nightmare Tower", "The Eternal Gate"]
        self.quest_objectives = [
            "Retrieve the {item} from the {location}",
            "Slay the {creature} that has been terrorizing the {location}",
            "Rescue the {character} who has been imprisoned by the {creature}",
            "Recover the {artifact} stolen by the {faction}",
            "Solve the riddle of the {location} to unlock the {secret}",
            "Gather {number} components for the {ritual} ritual",
            "Escort the {character} through the {dangerous} {location}",
            "Destroy the {curse} that has been corrupting the {location}",
            "Defeat the {boss} in combat to end their {threat}",
            "Negotiate peace between {faction1} and {faction2}",
            "Uncover the {secret} hidden within the {location}",
            "Collect the {number} fragments of the {artifact} scattered across {realm}",
            "Prove your worth by completing the {trial} of the {faction}",
            "Deliver the {message} to the {character} at the {location}",
            "Purify the {location} of the {corruption}"
        ]
        self.items = ["Sword of Light", "Amulet of Power", "Crown of Shadows", "Tome of Knowledge",
            "Dragon Egg", "Phoenix Feather", "Void Crystal", "Star Metal", "Ancient Relic",
            "Elixir of Life", "Phoenix Stone", "Shadow Orb", "Celestial Crown", "Abyssal Blade",
            "Stormcaller's Staff", "Frostfire Shield", "Emberheart Amulet", "Voidwalker's Cloak"]
        self.creatures_quest = ["Shadow Dragon", "Ancient Golem", "Void Wraith", "Storm Hydra",
            "Abyssal Leviathan", "Ember Phoenix", "Frost Giant", "Dark Chimera", "Star Serpent",
            "Corrupted Angel", "Nightmare Beast", "Eldritch Horror", "Temporal Drake",
            "Plague Demon", "Cosmic Horror"]
        self.characters_quest = ["Princess Elara", "King Aldric", "Sage Mirren", "Warrior Kael",
            "Mage Nyx", "Ranger Thalia", "Priest Othara", "Thief Zyrion", "Oracle Luxina",
            "Paladin Draven", "Bard Faelan", "Alchemist Brielle", "Druid Galen", "Necromancer Eryndor",
            "Hermit Ithil", "Merchant Jorun"]
        self.factions = ["The Shadow Covenant", "The Order of Light", "The Void Collective",
            "The Ember Society", "The Frost Legion", "The Starfall Alliance", "The Abyssal Court",
            "The Celestial Guild", "The Dreaming Cult", "The Storm Riders", "The Iron Dominion",
            "The Crystal Pact", "The Dark Brotherhood", "The Holy Crusade", "The Wandering Tribes"]
        self.rewards = [
            "The blessing of the {faction}, granting {power} abilities",
            "A sum of {amount} gold and the title of {title}",
            "The {artifact}, a legendary weapon of {power}",
            "Membership in the {faction} with full privileges",
            "Knowledge of the {secret} that has been hidden for {number} years",
            "The location of a {artifact} of {power} {level}",
            "A magical companion in the form of a {creature}",
            "The ability to {ability} at will",
            "The {title} of {realm}, ruling over all within",
            "Immortality through the {blessing} of the {faction}"
        ]

    def generate_quest(self, index):
        q_type = random.choice(self.quest_types)
        objective_template = random.choice(self.quest_objectives)
        objective = objective_template.format(
            item=random.choice(self.items),
            location=random.choice(self.quest_locations),
            creature=random.choice(self.creatures_quest),
            character=random.choice(self.characters_quest),
            artifact=random.choice(self.items),
            faction=random.choice(self.factions),
            secret=random.choice(["the hidden treasure", "the ancient prophecy", "the lost knowledge", "the sealed prison"]),
            ritual=random.choice(["summoning", "resurrection", "transformation", "warding"]),
            number=random.randint(1, 100),
            dangerous=random.choice(["treacherous", "enchanted", "cursed", "forbidden"]),
            curse=random.choice(["Blight of the Void", "Plague of Shadows", "Curse of Ages", "Witching Curse"]),
            boss=random.choice(self.creatures_quest),
            threat=random.choice(["tyranny", "corruption", "destruction", "enslavement"]),
            faction1=random.choice(self.factions),
            faction2=random.choice(self.factions),
            message=random.choice(["the warning", "the decree", "the invitation", "the ultimatum"]),
            corruption=random.choice(["Void Taint", "Shadow Rot", "Ember Plague", "Frost Decay"]),
            trial=random.choice(["Trial of Steel", "Trial of Wisdom", "Trial of Spirit", "Trial of Sacrifice"]),
            level=random.choice(["Supreme", "Mythic", "Eternal", "Transcendent"]),
            ability=random.choice(["fly", "shapeshift", "control time", "read minds"]),
            title=random.choice(["Champion", "Hero", "Lord", "Warden", "Guardian", "Protector"]),
            realm=random.choice(["the North", "the South", "the East", "the West", "the center of the world"])
        )
        giver = random.choice(self.quest_givers)
        location = random.choice(self.quest_locations)
        reward_template = random.choice(self.rewards)
        reward = reward_template.format(
            faction=random.choice(self.factions),
            power=random.choice(["legendary", "mythic", "divine", "transcendent"]),
            amount=random.randint(1000, 1000000),
            title=random.choice(["Lord of the Realm", "Champion of the Sun", "Warden of the Void"]),
            artifact=random.choice(self.items),
            secret=random.choice(["the hidden temple", "the ancient spell"]),
            number=random.randint(100, 10000),
            creature=random.choice(self.creatures_quest),
            blessing=random.choice(["Immortality", "Omniscience", "Infinite Power", "Eternal Youth"]),
            realm=random.choice(["the mortal plane", "the celestial realm"]),
            ability=random.choice(["fly", "shapeshift", "control time", "read minds"]),
            level=random.choice(["Supreme", "Mythic", "Eternal", "Transcendent"]),
            item=random.choice(self.items)
        )
        difficulty = random.choice(["Easy", "Medium", "Hard", "Extreme", "Impossible"])
        prestige = random.choice(["Bronze", "Silver", "Gold", "Platinum", "Diamond", "Mythic"])
        return {
            "index": index,
            "type": q_type,
            "title": f"{q_type} Quest of the {random.choice(self.quest_locations)}",
            "giver": giver,
            "location": location,
            "objective": objective,
            "reward": reward,
            "difficulty": difficulty,
            "prestige": prestige,
            "description": self.desc_gen.generate_sentence(),
            "prerequisites": [f"Complete {random.choice(self.quest_types)} Quest #{random.randint(1, 50)}" for _ in range(random.randint(0, 3))],
            "related_quests": [f"Quest #{random.randint(1, 100)}" for _ in range(random.randint(1, 5))]
        }

    def generate_full_quest(self, index):
        quest = self.generate_quest(index)
        lines = [
            f"\n{'='*60}",
            f"QUEST #{quest['index']}: {quest['title']}",
            f"Type: {quest['type']} | Difficulty: {quest['difficulty']} | Prestige: {quest['prestige']}",
            f"{'='*60}",
            f"Giver: {quest['giver']}",
            f"Location: {quest['location']}",
            f"Prerequisites: {', '.join(quest['prerequisites']) if quest['prerequisites'] else 'None'}",
            f"Related Quests: {', '.join(quest['related_quests'])}",
            f"Description: {quest['description']}",
            f"\nOBJECTIVE:",
            f"  {quest['objective']}",
            f"\nREWARD:",
            f"  {quest['reward']}",
            f"\n{'='*60}\n"
        ]
        return lines

    def generate_quest_chain(self, count=5):
        chains = []
        for i in range(count):
            chain = []
            chain_name = f"The {random.choice(['Chain of', 'Bloodline of', 'Legacy of', 'Cycle of'])} {random.choice(self.quest_locations)}"
            chain.append(f"\nQUEST CHAIN: {chain_name}")
            chain.append(f"Total Quests: {random.randint(3, 10)}")
            for j in range(random.randint(3, 10)):
                quest = self.generate_quest(j)
                chain.append(f"  Stage {j+1}: {quest['title']} - {quest['objective']}")
            chains.append("\n".join(chain))
        return chains
