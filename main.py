#!/usr/bin/env python3
"""Infinite Narrative Engine - Consume Maximum Tokens"""
import sys, random, itertools, json, os
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generators.names import NameGenerator
from generators.descriptions import DescriptionGenerator
from generators.quests import QuestGenerator
from generators.dialogue import DialogueGenerator
from generators.spells import SpellGenerator
from generators.loot import LootGenerator
from worlds.world_builder import WorldBuilder
from characters.character_gen import CharacterGenerator
from systems.combat import CombatSystem
from systems.inventory import InventorySystem
from systems.weather import WeatherSystem

class InfiniteNarrativeEngine:
    def __init__(self, max_tokens_target=999999):
        self.max_tokens_target = max_tokens_target
        self.tokens_consumed = 0
        self.name_gen = NameGenerator()
        self.desc_gen = DescriptionGenerator()
        self.quest_gen = QuestGenerator()
        self.dialogue_gen = DialogueGenerator()
        self.spell_gen = SpellGenerator()
        self.loot_gen = LootGenerator()
        self.world_builder = WorldBuilder()
        self.char_gen = CharacterGenerator()
        self.combat = CombatSystem()
        self.inventory = InventorySystem()
        self.weather = WeatherSystem()
        self.output_lines = []
        self.chapter = 0
        self.output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(self.output_dir, exist_ok=True)

    def count_tokens(self, text):
        return len(text.split())

    def emit(self, text):
        self.output_lines.append(text)
        self.tokens_consumed += self.count_tokens(text)
        if self.tokens_consumed % 5000 < 100:
            print(f"[TOKEN METER] Consumed: {self.tokens_consumed:,} tokens")
        return text

    def generate_chapter_header(self):
        self.chapter += 1
        titles = [
            "The Awakening", "The Descent", "The Revelation", "The Confrontation",
            "The Ascension", "The Collapse", "The Rebirth", "The Transcendence",
            "The Oblivion", "The Genesis", "The Eternal Return", "The Final Dawn",
            "The Shattered Veil", "The Infinite Loop", "The Cosmic Trial",
            "The Phantom Kingdom", "The Last Ember", "The Thousand Worlds",
            "The Nameless God", "The End of All Things"
        ]
        subtitle = self.desc_gen.generate_epic_phrase()
        return self.emit(f"\n{'='*80}\nCHAPTER {self.chapter}: {titles[(self.chapter-1) % len(titles)]}\n{subtitle}\n{'='*80}")

    def generate_world_introduction(self):
        world = self.world_builder.build_full_world()
        for line in world:
            self.emit(line)

    def generate_character_introductions(self, count=15):
        for i in range(count):
            char = self.char_gen.generate_full_character()
            for line in char:
                self.emit(line)
            self.emit("")

    def generate_quest_chain(self, count=20):
        for i in range(count):
            quest = self.quest_gen.generate_full_quest(i)
            for line in quest:
                self.emit(line)
            self.emit("")

    def generate_spell_catalog(self, count=30):
        for i in range(count):
            spell = self.spell_gen.generate_full_spell(i)
            for line in spell:
                self.emit(line)
            self.emit("")

    def generate_loot_treasure(self, count=25):
        for i in range(count):
            item = self.loot_gen.generate_full_item(i)
            for line in item:
                self.emit(line)
            self.emit("")

    def generate_discussion_scene(self, count=10):
        for i in range(count):
            scene = self.dialogue_gen.generate_full_scene(i)
            for line in scene:
                self.emit(line)
            self.emit("")

    def generate_combat_encounter(self, count=15):
        for i in range(count):
            encounter = self.combat.generate_full_encounter(i)
            for line in encounter:
                self.emit(line)
            self.emit("")

    def generate_weather_phenomena(self, count=20):
        for i in range(count):
            weather = self.weather.generate_full_weather(i)
            for line in weather:
                self.emit(line)
            self.emit("")

    def generate_procedural_names(self, count=50):
        self.emit(f"\n{'#'*80}")
        self.emit(f"# PROCEDURAL NAME REGISTRY - {count} ENTRIES")
        self.emit(f"{'#'*80}")
        for i in range(count):
            names = self.name_gen.generate_name_batch(5)
            self.emit(f"Batch {i+1}: {', '.join(names)}")
            self.emit(f"  - Kingdom: {self.name_gen.generate_kingdom_name()}")
            self.emit(f"  - City: {self.name_gen.generate_city_name()}")
            self.emit(f"  - River: {self.name_gen.generate_river_name()}")
            self.emit(f"  - Mountain: {self.name_gen.generate_mountain_name()}")
            self.emit(f"  - Artifact: {self.name_gen.generate_artifact_name()}")
            self.emit(f"  - Curse: {self.name_gen.generate_curse_name()}")
            self.emit("")

    def generate_recursive_story(self, depth=5):
        def recursive_tale(current_depth, max_depth, prefix=""):
            if current_depth > max_depth:
                return [f"{prefix}...and so it ended."]
            lines = []
            lines.append(f"{prefix}In the {self.desc_gen.generate_adjective()} realm of {self.name_gen.generate_kingdom_name()},")
            lines.append(f"{prefix}a {self.desc_gen.generate_noun()} {self.desc_gen.generate_adjective()} {self.desc_gen.generate_creature()}")
            lines.append(f"{prefix}encountered a {self.desc_gen.generate_noun()} of {self.desc_gen.generate_property()}.")
            lines.append(f"{prefix}{self.desc_gen.generate_sentence()}")
            lines.append(f"{prefix}{self.desc_gen.generate_sentence()}")
            lines.extend(recursive_tale(current_depth + 1, max_depth, prefix + "  "))
            lines.append(f"{prefix}Thus ended this tale, but {self.desc_gen.generate_another_tale()}")
            return lines

        self.emit(f"\n{'*'*80}")
        self.emit(f"* RECURSIVE NARRATIVE ENGINE - DEPTH {depth}")
        self.emit(f"{'*'*80}")
        for iteration in range(3):
            tale = recursive_tale(1, depth)
            for line in tale:
                self.emit(line)
            self.emit("")

    def generate_massive_artifact_list(self):
        self.emit(f"\n{'%'*80}")
        self.emit(f"% LEGENDARY ARTIFACT COMPENDIUM - ALL REALMS")
        self.emit(f"{'%'*80}")
        artifact_types = ["Weapon", "Armor", "Ring", "Amulet", "Staff", "Tome", "Crown", "Shield", "Dagger", "Potion", "Relic", "Gem", "Scroll", "Mirror", "Key"]
        material_types = ["Dragonbone", "Starmetal", "Voidite", "Crysthalis", "Obsidian", "Mithral", "Divine Gold", "Shadow Iron", "Celestial Silver", "Abyssal Bronze"]
        power_types = ["Supreme", "Eternal", "Catastrophic", "Mythic", "Transcendent", "Primordial", "Apocalyptic", "Infinity", "Omnipotent", "Boundless"]
        for i in range(100):
            artifact = {
                "id": f"ART-{i:04d}",
                "name": self.name_gen.generate_artifact_name(),
                "type": random.choice(artifact_types),
                "material": random.choice(material_types),
                "power": random.choice(power_types),
                "description": self.desc_gen.generate_detailed_description(),
                "history": self.desc_gen.generate_history(),
                "abilities": [self.desc_gen.generate_ability() for _ in range(random.randint(2, 5))],
                "curse": self.desc_gen.generate_curse(),
                "blessing": self.desc_gen.generate_blessing(),
                "origin": self.desc_gen.generate_origin(),
                "previous_wielders": [self.name_gen.generate_character_name() for _ in range(random.randint(1, 8))],
            }
            self.emit(f"[{artifact['id']}] {artifact['power']} {artifact['type']}: {artifact['name']}")
            self.emit(f"  Material: {artifact['material']} | Power Level: {artifact['power']}")
            self.emit(f"  {artifact['description']}")
            self.emit(f"  History: {artifact['history']}")
            self.emit(f"  Abilities: {', '.join(artifact['abilities'])}")
            self.emit(f"  Curse: {artifact['curse']}")
            self.emit(f"  Blessing: {artifact['blessing']}")
            self.emit(f"  Origin: {artifact['origin']}")
            self.emit(f"  Previous Wielders: {', '.join(artifact['previous_wielders'])}")
            self.emit("")

    def run(self):
        start = datetime.now()
        self.emit(f"INFINITE NARRATIVE ENGINE - Token Consumption Protocol Initiated")
        self.emit(f"Timestamp: {start.isoformat()}")
        self.emit(f"Target: {self.max_tokens_target:,} tokens")
        self.emit(f"Engine Version: ∞")
        self.emit("")

        self.generate_procedural_names(50)
        self.generate_world_introduction()
        self.generate_character_introductions(15)
        self.generate_massive_artifact_list()
        self.generate_spell_catalog(30)
        self.generate_loot_treasure(25)
        self.generate_quest_chain(20)
        self.generate_discussion_scene(10)
        self.generate_combat_encounter(15)
        self.generate_weather_phenomena(20)
        self.generate_recursive_story(depth=5)

        while self.tokens_consumed < self.max_tokens_target:
            self.generate_chapter_header()
            self.generate_world_introduction()
            self.generate_character_introductions(10)
            self.generate_spell_catalog(10)
            self.generate_loot_treasure(10)
            self.generate_quest_chain(5)
            self.generate_combat_encounter(5)
            self.generate_weather_phenomena(5)
            self.generate_recursive_story(depth=3)
            if self.tokens_consumed >= self.max_tokens_target:
                break

        self.emit(f"\n{'#'*80}")
        self.emit(f"# ENGINE TERMINATED")
        self.emit(f"# Total Tokens Consumed: {self.tokens_consumed:,}")
        self.emit(f"# Total Lines Generated: {len(self.output_lines):,}")
        self.emit(f"# Runtime: {(datetime.now() - start).total_seconds():.2f} seconds")
        self.emit(f"{'#'*80}")

        output_file = os.path.join(self.output_dir, f"narrative_output_{int(datetime.now().timestamp())}.txt")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(self.output_lines))
        self.emit(f"Output saved to: {output_file}")
        return self.tokens_consumed

if __name__ == "__main__":
    target = int(sys.argv[1]) if len(sys.argv) > 1 else 999999
    engine = InfiniteNarrativeEngine(max_tokens_target=target)
    tokens = engine.run()
    print(f"\nDONE! Consumed {tokens:,} tokens.")
