import random
from generators.descriptions import DescriptionGenerator

class SpellGenerator:
    def __init__(self):
        self.desc_gen = DescriptionGenerator()
        self.schools = ["Necromancy", "Pyromancy", "Cryomancy", "Electromancy", "Hydromancy",
            "Aeromancy", "Geomancy", "Umbramancy", "Photomancy", "Chronomancy",
            "Psychomancy", "Elementalism", "Conjuration", "Transmutation", "Divination",
            "Enchantment", "Illusion", "Abjuration", "Evocation", "Invocation",
            "Celestial", "Infernal", "Void", "Storm", "Nature", "Shadow",
            "Light", "Dark", "Chaos", "Order", "Life", "Death", "Mind", "Soul"]
        self.spell_names = [
            "Arcane Annihilation", "Void Cascade", "Starfall Surge", "Ember Eruption",
            "Frostbite Oblivion", "Thunderous Rebirth", "Shadow Weave", "Lightbringer's Wrath",
            "Abyssal Maw", "Temporal Stutter", "Psychic Devastation", "Elemental Convergence",
            "Soul Harvest", "Necrotic Bloom", "Celestial Judgment", "Infernal Pact",
            "Storm of Ages", "Dreamwalker's Path", "Chrono Freeze", "Mind Shatter",
            "Phoenix Rebirth", "Dragon's Breath", "Leviathan's Maw", "Titan's Fall",
            "Golem's Fury", "Wraith's Lament", "Demon's Call", "Angel's Descent",
            "Beast's Roar", "Hydra's Embrace", "Chimera's Maw", "Cerberus's Gate",
            "Minotaur's Charge", "Centaur's Volley", "Manticore's Sting", "Sphinx's Riddle",
            "Basilisk's Gaze", "Wyvern's Dive", "Pegasus's Grace", "Troll's Smash",
            "Ogre's Crush", "Giant's Stomp", "Elemental Mastery", "Spirit Walker",
            "Phantom Strike", "Specter's Cloak", "Revenant's Curse", "Lich's Dominion",
            "Vampire's Kiss"
        ]
        self.effects = [
            "deals {damage} points of {damage_type} damage to all enemies in a {radius} foot radius",
            "creates a {duration} field that {effect} all who enter",
            "summons a {creature} to fight for {duration} rounds",
            "transforms the caster into a {form} for {duration} minutes",
            "freezes all enemies in place for {duration} seconds",
            "restores {amount} health to all allies within {radius} feet",
            "deals {damage} damage and {secondary_effect}",
            "creates an impenetrable barrier that lasts {duration} rounds",
            "teleports the caster and up to {number} allies to {location}",
            "erases all {property} from the target, {effect}",
            "increases all attributes by {amount} for {duration} minutes",
            "summons a {weather} that lasts {duration} rounds",
            "grants the caster {ability} for {duration} minutes",
            "destroys all {object} within {radius} feet",
            "creates a {number} foot tall {object} that {effect}",
            "binds all enemies in a {radius} foot radius for {duration} seconds",
            "drains {amount} mana from all enemies and transfers it to allies",
            "opens a portal to {location} that lasts {duration} minutes",
            "causes all {object} in {radius} feet to {effect}",
            "conjures {number} {object}s that {effect} for {duration}"
        ]
        self.damage_types = ["fire", "ice", "lightning", "shadow", "void", "light", "necrotic",
            "arcane", "psychic", "physical", "poison", "radiant", "corrupt", "elemental", "primal"]
        self.secondary_effects = ["slowing them by 50%", "burning them for {amount} additional damage",
            "causing them to flee in terror", "paralyzing them", "confusing their senses",
            "draining their life force", "cursing them with {curse}", "reducing their defenses by 75%"]
        self.casters = ["Archmage", "Warlock", "Wizard", "Sorcerer", "Druid", "Shaman",
            "Necromancer", "Priest", "Oracle", "Seer", "Mystic", "Enchanter",
            "Illusionist", "Conjurer", "Transmuter", "Diviner", "Abjurer", "Invoker"]
        self.costs = ["100 mana", "500 mana", "1000 mana", "5000 mana", "10000 mana",
            "50000 mana", "100000 mana", "half of your life force", "your memory",
            "a year of your life", "your sight", "your voice", "your sanity"]
        self.rarities = ["Common", "Uncommon", "Rare", "Epic", "Legendary", "Mythic", "Transcendent", "Divine"]
        self.components = [
            "a {material} focus", "a {material} wand", "a {material} orb", "a {material} crystal",
            "an incantation in {language}", "a blood sacrifice", "a {material} sigil",
            "a {material} amulet", "a {material} staff", "a {material} ring"
        ]

    def generate_spell(self, index):
        school = random.choice(self.schools)
        name = random.choice(self.spell_names) + f" #{index}"
        level = random.randint(1, 25)
        damage = random.randint(10, 10000)
        damage_type = random.choice(self.damage_types)
        radius = random.randint(5, 1000)
        duration = random.randint(1, 1000)
        effect = random.choice(self.effects).format(
            damage=damage, damage_type=damage_type, radius=radius, duration=duration,
            effect=random.choice(self.secondary_effects), creature=random.choice(["fire elemental", "shadow creature", "light construct"]),
            form=random.choice(["dragon", "phoenix", "titan", "golem"]), amount=random.randint(10, 10000),
            secondary_effect=random.choice(self.secondary_effects), number=random.randint(1, 100),
            location=random.choice(["the Abyss", "the Heavens", "the Void", "the Elemental Plane"]),
            property=random.choice(["Time", "Space", "Reality", "Existence"]),
            weather=random.choice(["eternal storm", "blizzard", "thunderstorm", "fire rain"]),
            ability=random.choice(["fly", "shapeshift", "control minds", "read thoughts"]),
            object=random.choice(["enemies", "allies", "structures", "creatures", "artifacts"]),
            curse=random.choice(["the Curse of Ages", "the Mark of the Void", "the Shackles of Shadow"])
        )
        caster = random.choice(self.casters)
        cost = random.choice(self.costs)
        rarity = random.choice(self.rarities)
        component_template = random.choice(self.components)
        component = component_template.format(
            material=random.choice(["dragonbone", "starsteel", "voidite", "crysthalis"]),
            language=random.choice(["Ancient Draconic", "Celestial", "Abyssal", "Elder Tongue"])
        )
        cast_time = random.choice(["instant", "1 round", "3 rounds", "1 minute", "1 hour"])
        return {
            "index": index,
            "name": name,
            "school": school,
            "level": level,
            "caster": caster,
            "effect": effect,
            "cost": cost,
            "rarity": rarity,
            "component": component,
            "cast_time": cast_time,
            "cooldown": f"{random.randint(1, 100)} rounds",
            "range": f"{random.randint(10, 5000)} feet",
            "duration": f"{duration} seconds",
            "description": self.desc_gen.generate_detailed_description(),
            "history": self.desc_gen.generate_history(),
            "known_users": [f"{random.choice(self.casters)} {random.choice(['the Red', 'the Dark', 'the Ancient', 'the Lost'])}" for _ in range(random.randint(1, 5))],
            "variants": [f"{name} Variant {i}" for i in range(random.randint(1, 5))]
        }

    def generate_full_spell(self, index):
        spell = self.generate_spell(index)
        lines = [
            f"\n{'-'*60}",
            f"SPELL #{spell['index']}: {spell['name']}",
            f"School: {spell['school']} | Level: {spell['level']} | Rarity: {spell['rarity']}",
            f"{'-'*60}",
            f"Caster Class: {spell['caster']}",
            f"Cast Time: {spell['cast_time']} | Cooldown: {spell['cooldown']} | Range: {spell['range']}",
            f"Cost: {spell['cost']}",
            f"Component: {spell['component']}",
            f"Duration: {spell['duration']}",
            f"\nEFFECT:",
            f"  {spell['effect']}",
            f"\nDESCRIPTION:",
            f"  {spell['description']}",
            f"\nHISTORY:",
            f"  {spell['history']}",
            f"\nKNOWN USERS: {', '.join(spell['known_users'])}",
            f"\nVARIANTS: {', '.join(spell['variants'])}",
            f"{'-'*60}\n"
        ]
        return lines

    def generate_spell_catalog(self, count=10):
        catalog = []
        for i in range(count):
            spell = self.generate_spell(i)
            catalog.append(f"Spell #{spell['index']}: {spell['name']} ({spell['school']}, {spell['rarity']}, Level {spell['level']})")
        return catalog
