import random
from generators.names import NameGenerator
from generators.descriptions import DescriptionGenerator
from characters.character_gen import CharacterGenerator

class CombatSystem:
    def __init__(self):
        self.name_gen = NameGenerator()
        self.desc_gen = DescriptionGenerator()
        self.char_gen = CharacterGenerator()
        self.attacks = ["Slash", "Strike", "Pierce", "Crush", "Burn", "Freeze", "Shock", "Corrode",
            "Disintegrate", "Rend", "Tear", "Pummel", "Hammer", "Impale", "Scorch",
            "Frostbite", "Electrocute", "Poison", "Vampirize", "Drain", "Absorb",
            "Reflect", "Deflect", "Redirect", "Bash", "Bludgeon", "Pierce", "Stab", "Cut",
            "Slice", "Dice", "Mangle", "Wrestle", "Grapple", "Pin", "Squeeze", "Crush"]
        self.moves = ["Attack", "Defend", "Cast Spell", "Use Item", "Flee", "Taunt", "Wait",
            "Dodge", "Block", "Counter", "Charge", "Overpower", "Feint", "Steal", "Heal",
            "Buff", "Debuff", "Summon", "Transform", "Ultimate"]
        self.creatures = [self.name_gen.generate_creature() for _ in range(20)]
        self.effects = ["poisoned", "slowed", "burned", "frozen", "stunned", "confused", "feared",
            "charmed", "cursed", "blinded", "deafened", "paralyzed", "silenced", "weakened",
            "strengthened", "empowered", "enraged", "shielded", "healed", "buffed"]
        self.areas = ["the Arena of Shadows", "the Battlefield of Echoes", "the Colosseum of Fire",
            "the Abyssal Pits", "the Storm Circle", "the Frostbound Field", "the Crystal Court",
            "the Void Throne Room", "the Ember Arena", "the Dreaming Battlefield"]
        self.los = ["You strike the enemy for {damage} points of {type} damage.",
            "The enemy counterattacks, dealing {damage} points of {type} damage to you.",
            "A critical hit! You deal {damage} additional damage!",
            "The enemy dodges your attack completely!",
            "Your spell lands perfectly, dealing {damage} {type} damage over {duration} rounds.",
            "The enemy is now {effect}!",
            "Your defensive stance absorbs {amount} points of damage.",
            "The battle rages on as both combatants trade blows.",
            "An elemental surge boosts your next attack by {amount}%!",
            "The enemy stumbles, giving you an opening for a free attack."]
        self.weathers = ["Clear", "Rain", "Storm", "Fog", "Snow", "Hail", "Wind", "Dust Storm",
            "Lightning Storm", "Fire Storm", "Shadow Storm", "Void Storm"]

    def generate_full_encounter(self, index):
        fighters = [self.name_gen.generate_character_name() for _ in range(random.randint(2, 5))]
        monsters = [random.choice(self.creatures) for _ in range(random.randint(1, 4))]
        area = random.choice(self.areas)
        weather = random.choice(self.weathers)
        rounds = random.randint(5, 50)
        rules = [f"{random.choice(self.moves)}: {random.choice(['Standard', 'Aggressive', 'Defensive', 'Ultimate'])}"] * random.randint(1, 3)
        lines = [
            f"\n{'='*60}",
            f"COMBAT ENCOUNTER #{index}",
            f"{'='*60}",
            f"Location: {area}",
            f"Weather: {weather}",
            f"Estimated Rounds: {rounds}",
            f"Fighters: {', '.join(fighters)}",
            f"Monsters: {', '.join(monsters)}",
            f"\nRules:",
        ]
        for rule in rules:
            lines.append(f"  {rule}")
        lines.append(f"\nCOMBAT LOG:")
        for round_num in range(rounds):
            fighter = random.choice(fighters)
            monster = random.choice(monsters)
            attack = random.choice(self.attacks)
            move = random.choice(self.moves)
            damage = random.randint(1, 9999)
            damage_type = random.choice(["fire", "ice", "lightning", "shadow", "physical", "arcane"])
            effect = random.choice(self.effects)
            los = random.choice(self.los).format(
                damage=damage, type=damage_type, duration=random.randint(1, 10),
                amount=random.randint(10, 200), effect=effect,
                creature=random.choice(self.creatures)
            )
            lines.append(f"  Round {round_num+1}: {fighter} {move} against {monster} with {attack}! {los}")
        lines.append(f"\nRESULTS:")
        for fighter in fighters:
            lines.append(f"  {fighter}: HP remaining {random.randint(0, 1000)}, Status: {random.choice(['Alive', 'Unconscious', 'Dead'])}")
        for monster in monsters:
            lines.append(f"  {monster}: HP remaining {random.randint(0, 500)}, Status: {random.choice(['Alive', 'Fleeing', 'Defeated'])}")
        lines.append(f"\n{'='*60}\n")
        return lines
