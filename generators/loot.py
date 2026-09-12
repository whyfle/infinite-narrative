import random
from generators.descriptions import DescriptionGenerator
from generators.names import NameGenerator

class LootGenerator:
    def __init__(self):
        self.desc_gen = DescriptionGenerator()
        self.name_gen = NameGenerator()
        self.rarities = ["Common", "Uncommon", "Rare", "Epic", "Legendary", "Mythic", "Transcendent", "Divine", "Cosmic", "Infinite"]
        self.rarity_colors = {"Common": "White", "Uncommon": "Green", "Rare": "Blue", "Epic": "Purple",
            "Legendary": "Orange", "Mythic": "Red", "Transcendent": "Gold", "Divine": "Rainbow",
            "Cosmic": "Silver", "Infinite": "Black"}
        self.item_types = ["Weapon", "Armor", "Accessory", "Consumable", "Material", "Quest Item",
            "Key", "Scroll", "Relic", "Mount", "Pet", "Tool", "Ring", "Amulet", "Helm",
            "Chestplate", "Boots", "Gloves", "Belt", "Cloak", "Shield", "Bow", "Wand",
            "Staff", "Dagger", "Sword", "Axe", "Mace", "Spear", "Crossbow", "Orb"]
        self.prefixes = ["The", "Ancient", "Forgotten", "Cursed", "Blessed", "Eternal", "Mythic",
            "Divine", "Shadow", "Void", "Star", "Celestial", "Abyssal", "Primordial",
            "Apocalyptic", "Infinity", "Boundless", "Omnipotent", "Transcendent", "Supreme"]
        self.materials = ["Dragon Scale", "Starsteel", "Void Essence", "Crystal Shard", "Obsidian",
            "Mithral", "Divine Gold", "Shadow Iron", "Celestial Silver", "Abyssal Bronze",
            "Phoenix Feather", "Griffin Leather", "Titan Stone", "Moon Diamond", "Sun Ruby"]
        self.enchantments = ["Fire I", "Fire II", "Fire III", "Ice I", "Ice II", "Ice III",
            "Lightning I", "Lightning II", "Lightning III", "Shadow I", "Shadow II", "Shadow III",
            "Holy I", "Holy II", "Holy III", "Void I", "Void II", "Void III",
            "Poison I", "Poison II", "Poison III", "Critical I", "Critical II", "Critical III",
            "Life Steal I", "Life Steal II", "Life Steal III", "Speed I", "Speed II", "Speed III",
            "Strength I", "Strength II", "Strength III", "Wisdom I", "Wisdom II", "Wisdom III",
            "Agility I", "Agility II", "Agility III", "Luck I", "Luck II", "Luck III",
            "Resistance I", "Resistance II", "Resistance III", "Absorb I", "Absorb II", "Absorb III",
            "Regeneration I", "Regeneration II", "Regeneration III", "Swift I", "Swift II", "Swift III"]
        self.sources = ["Defeated {creature}", "Found in {location}", "Crafted by {craftsman}",
            "Dropped by {boss}", "Purchased from {merchant}", "Reward for {quest}",
            "Discovered in {dungeon}", "Gifted by {npc}", "Found in {chest}",
            "Obtained from {event}", "Mined from {resource}", "Harvested from {plant}"]
        self.stats = ["Attack", "Defense", "Magic Power", "Speed", "Vitality", "Mana",
            "Critical Hit", "Dodge", "Health", "Mana Regen", "Resistance", "Luck",
            "Strength", "Dexterity", "Intelligence", "Charisma", "Constitution", "Wisdom"]

    def generate_item(self, index):
        rarity = random.choice(self.rarities)
        item_type = random.choice(self.item_types)
        prefix = random.choice(self.prefixes)
        name = f"{prefix} {self.name_gen.generate_noun()} of {random.choice(self.stats)}"
        material = random.choice(self.materials)
        level = random.randint(1, 100)
        base_stats = {stat: random.randint(1, 1000) for stat in random.sample(self.stats, random.randint(2, 5))}
        enchantments = random.sample(self.enchantments, random.randint(1, 4))
        source = random.choice(self.sources).format(
            creature=random.choice(["Dragon", "Golem", "Wraith", "Hydra", "Beast"]),
            location=random.choice(["the Abyss", "the Crystal Spire", "the Void Library"]),
            craftsman=random.choice(["Elminster", "Gandalf", "Merlin", "Zarlan"]),
            boss=random.choice(["Shadow Dragon", "Ancient Golem", "Void Wraith"]),
            merchant=random.choice(["The Shadow Merchant", "The Wandering Trader"]),
            quest=random.choice(["The Dragon's Trial", "The Void Expedition"]),
            dungeon=random.choice(["the Forgotten Crypt", "the Ancient Tomb", "the Dark Tower"]),
            npc=random.choice(["the Oracle", "the Sage", "the Mystic"]),
            chest=random.choice(["the Golden Chest", "the Iron Chest", "the Crystal Chest"]),
            event=random.choice(["the Festival of Stars", "the Eclipse", "the Convergence"]),
            resource=random.choice(["Void Ore", "Star Crystals", "Dragon Essence"]),
            plant=random.choice(["Everbloom", "Shadow Vine", "Crystal Flower"])
        )
        weight = round(random.uniform(0.1, 50.0), 1)
        value = rarity_to_value(rarity) * random.randint(1, 100)
        return {
            "index": index,
            "name": name,
            "type": item_type,
            "rarity": rarity,
            "color": self.rarity_colors[rarity],
            "level": level,
            "material": material,
            "base_stats": base_stats,
            "enchantments": enchantments,
            "source": source,
            "weight": weight,
            "value": value,
            "description": self.desc_gen.generate_detailed_description(),
            "flavor_text": self.desc_gen.generate_history(),
            "set_bonus": f"Set with {random.choice(self.item_types)}: {random.choice(self.stats)} +{random.randint(10, 500)}" if random.random() > 0.5 else None,
            "requirements": f"Level {level * 2} {random.choice(['Strength', 'Dexterity', 'Intelligence', 'Any'])}",
            "durability": random.randint(1, 1000),
            "sell_value": value // 2,
            "identify_required": rarity in ["Rare", "Epic", "Legendary", "Mythic", "Transcendent", "Divine", "Cosmic", "Infinite"],
            "unique": random.random() > 0.9,
            "crafted": random.random() > 0.7,
            "crafting_materials": [random.choice(self.materials) for _ in range(random.randint(1, 5))]
        }

    def generate_full_item(self, index):
        item = self.generate_item(index)
        lines = [
            f"\n{'='*60}",
            f"ITEM #{item['index']}: [{item['color']}] {item['name']}",
            f"Type: {item['type']} | Rarity: {item['rarity']} | Level: {item['level']}",
            f"{'='*60}",
            f"Material: {item['material']} | Weight: {item['weight']} lbs | Value: {item['value']} gold",
            f"Durability: {item['durability']} | Source: {item['source']}",
            f"Requirements: {item['requirements']}",
            f"Unique: {item['unique']} | Identifiable: {item['identify_required']}",
            f"\nBASE STATS:",
        ]
        for stat, val in item["base_stats"].items():
            lines.append(f"  {stat}: +{val}")
        if item["enchantments"]:
            lines.append(f"\nENCHANTMENTS: {', '.join(item['enchantments'])}")
        lines.append(f"\nDESCRIPTION: {item['description']}")
        lines.append(f"FLAVOR: {item['flavor_text']}")
        if item["set_bonus"]:
            lines.append(f"SET BONUS: {item['set_bonus']}")
        if item["crafted"]:
            lines.append(f"CRAFTING MATERIALS: {', '.join(item['crafting_materials'])}")
        lines.append(f"\n{'='*60}\n")
        return lines

def rarity_to_value(rarity):
    values = {"Common": 10, "Uncommon": 50, "Rare": 200, "Epic": 1000, "Legendary": 5000,
        "Mythic": 25000, "Transcendent": 100000, "Divine": 500000, "Cosmic": 1000000, "Infinite": 999999999}
    return values.get(rarity, 10)
