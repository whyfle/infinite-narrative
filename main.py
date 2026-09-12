#!/usr/bin/env python3
"""Infinite Dating Simulator Engine - Maximum Token Generator"""
import sys, os, random, threading, time
from datetime import datetime
from characters import CharacterGenerator
from dates import DatingSimulator
from narrative import NarrativeEngine

class InfiniteDatingEngine:
    def __init__(self, max_tokens_target=999999):
        self.max_tokens_target = max_tokens_target
        self.tokens_consumed = 0
        self.engine = None
        self.running = False
        self.output_lines = []
        self.game = DatingSimulator()
        self.game.generate_player("Player")
        self.char_gen = CharacterGenerator()
        self.narrative = None
        self.start_time = None

    def count_tokens(self, text):
        return len(text.split())

    def emit(self, text):
        self.output_lines.append(text)
        self.tokens_consumed += self.count_tokens(text)
        return text

    def run_full_simulation(self):
        self.start_time = datetime.now()
        self.emit(f"INFINITE DATING SIMULATOR ENGINE v3.0")
        self.emit(f"Timestamp: {self.start_time.isoformat()}")
        self.emit(f"Target: {self.max_tokens_target:,} tokens")
        self.emit(f"Player: {self.game.player_name}")
        self.emit(f"Starting the greatest love story ever told...")
        self.emit("")

        self.emit(f"\n{'#'*80}")
        self.emit(f"# PROLOGUE: THE BEGINNING")
        self.emit(f"{'#'*80}")
        for _ in range(20):
            partner = self.game.generate_partner(random.randint(0, 100))
            self.emit(f"Character: {partner['name']}")
            self.emit(f"  Age: {partner['age']} | Class: {partner['class']} | Race: {partner['race']}")
            self.emit(f"  Appearance: {partner['appearance']}")
            self.emit(f"  Personality: {partner['personality']}")
            self.emit(f"  Hobby: {partner['hobby']}")
            self.emit(f"  First Impression: {partner['first_impression']}")
            self.emit(f"  Backstory: {partner['backstory']}")
            self.emit(f"  Love Language: {partner['love_language']}")
            self.emit(f"  Favorite Date: {partner['favorite_date']}")
            self.emit(f"  Dream: {partner['dream']}")
            self.emit(f"  Fear: {partner['fear']}")
            self.emit(f"  Dislike: {partner['dislike']}")
            self.emit(f"  Crushes: {partner['crush_on'] if partner['crush_on'] else 'None'}")
            self.emit(f"  Stats: {partner['stats']}")
            self.emit(f"  Gifts: {', '.join(partner['gifts'])}")
            self.emit(f"")

        self.emit(f"\n{'#'*80}")
        self.emit(f"# ALL LOVING INTERESTS")
        self.emit(f"{'#'*80}")
        for i in range(30):
            partner = self.game.generate_partner(i)
            self.emit(f"\n{'='*60}")
            self.emit(f"LOVE INTEREST #{i+1}: {partner['name']}")
            self.emit(f"{'='*60}")
            for stat, val in partner["stats"].items():
                self.emit(f"  {stat}: {val}")
            self.emit(f"  Appearance: {partner['appearance']}")
            self.emit(f"  First Impression: {partner['first_impression']}")
            self.emit(f"  Backstory: {partner['backstory']}")
            self.emit(f"  Love Language: {partner['love_language']}")
            self.emit(f"  Favorite: {partner['favorite']} | Dislike: {partner['dislike']}")
            self.emit(f"  Fear: {partner['fear']} | Dream: {partner['dream']}")
            self.emit(f"  Favorite Date: {partner['favorite_date']}")
            self.emit(f"  Crushes: {partner['crush_on'] if partner['crush_on'] else 'No one'}")
            self.emit(f"{'='*60}\n")

        self.emit(f"\n{'#'*80}")
        self.emit(f"# ALL DATES")
        self.emit(f"{'#'*80}")
        for i in range(30):
            partner = self.game.generate_partner(i)
            location = random.choice(self.game.locations)
            date_info, affection = self.game.generate_date(partner, self.game.locations.index(location))
            dialogue = self.game.generate_date_dialogue(partner)
            self.emit(f"\n{'='*60}")
            self.emit(f"DATE #{i+1}: {partner['name']} at {location['name']}")
            self.emit(f"{'='*60}")
            self.emit(f"Activity: {location['activity']} | Atmosphere: {location['atmosphere']}")
            self.emit(f"Cost: {location['cost']} gold | Weather: {self.game.weather}")
            self.emit(f"Affection Change: +{affection}")
            self.emit(f"")
            self.emit(f"DIALOGUE:")
            for d in dialogue:
                self.emit(f"  {d}")
            self.emit(f"Status: {self.game.player_relationship[partner['name']]['status']}")
            self.emit(f"Total Affection: {self.game.player_relationship[partner['name']]['affection']}")
            self.emit(f"{'='*60}\n")

        self.emit(f"\n{'#'*80}")
        self.emit(f"# ALL GIFTS")
        self.emit(f"{'#'*80}")
        for i in range(30):
            partner = self.game.generate_partner(i)
            gift = self.game.generate_gift_interaction(partner)
            self.emit(f"\n{'-'*60}")
            self.emit(f"GIFT TO {partner['name']}: {gift['gift']['name']}")
            self.emit(f"Value: {gift['gift']['value']} gold | Affection: +{gift['affection_change']}")
            self.emit(f"Reaction: {gift['reaction']}")
            self.emit(f"{'-'*60}\n")

        self.emit(f"\n{'#'*80}")
        self.emit(f"# ALL COMPATIBILITY REPORTS")
        self.emit(f"{'#'*80}")
        for i in range(25):
            partner = self.game.generate_partner(i)
            report = self.game.generate_compatibility_report(partner)
            self.emit(f"\n{'%'*60}")
            self.emit(f"COMPATIBILITY: {partner['name']}")
            self.emit(f"{'%'*60}")
            self.emit(f"Compatibility: {report['compatibility']}% | Affection: {report['affection']}")
            self.emit(f"Status: {report['status']} | Dates: {report['dates']}")
            self.emit(f"Love Language: {report['love_language']}")
            self.emit(f"Report: {report['report']}")
            self.emit(f"Favorite: {report['favorite']} | Dislike: {report['dislike']}")
            self.emit(f"Fear: {report['fear']} | Dream: {report['dream']}")
            self.emit(f"{'%'*60}\n")

        self.emit(f"\n{'#'*80}")
        self.emit(f"# ALL CONFESSIONS")
        self.emit(f"{'#'*80}")
        for i in range(20):
            partner = self.game.generate_partner(i)
            self.game.player_relationship[partner["name"]]["affection"] = random.randint(60, 100)
            confession = self.game.generate_confession(partner)
            self.emit(f"\n{'#'*60}")
            self.emit(f"CONFESSION TO {partner['name']}")
            self.emit(f"{'#'*60}")
            self.emit(f"Success: {confession['success']}")
            self.emit(f"Message: {confession['message']}")
            self.emit(f"Status: {confession['status']}")
            self.emit(f"{'#'*60}\n")

        self.emit(f"\n{'#'*80}")
        self.emit(f"# ALL BREAKUPS")
        self.emit(f"{'#'*80}")
        for i in range(15):
            partner = self.game.generate_partner(i)
            self.game.player_relationship[partner["name"]]["affection"] = 5
            breakup = self.game.generate_breakup(partner)
            self.emit(f"\n{'!'*60}")
            self.emit(f"BREAKUP WITH {partner['name']}")
            self.emit(f"{'!'*60}")
            self.emit(f"Message: {breakup}")
            self.emit(f"{'!'*60}\n")

        summary = self.game.generate_narrative_summary()
        self.emit(f"\n{'='*80}")
        self.emit(f"FINAL NARRATIVE SUMMARY")
        self.emit(f"{'='*80}")
        self.emit(f"Player: {summary['player']}")
        self.emit(f"Day: {summary['day']} | Season: {summary['season']}")
        self.emit(f"Dates: {summary['dates_completed']}")
        self.emit(f"Total Affection: {summary['total_affection']}")
        self.emit(f"In Love: {', '.join(summary['in_love']) if summary['in_love'] else 'None'}")
        self.emit(f"Wealth: {summary['wealth']} gold")
        for partner in summary["partners"]:
            self.emit(f"  {partner['name']}: {partner['status']} (Affection: {partner['affection']})")
        self.emit(f"\n{'='*80}")

        while self.tokens_consumed < self.max_tokens_target:
            self.generate_chapter()
            partner = self.game.generate_partner(random.randint(0, 100))
            location = random.choice(self.game.locations)
            date_info, affection = self.game.generate_date(partner, self.game.locations.index(location))
            dialogue = self.game.generate_date_dialogue(partner)
            for d in dialogue:
                self.emit(d)
            gift = self.game.generate_gift_interaction(partner)
            self.emit(f"Gift Reaction: {gift['reaction']}")
            confession = self.game.generate_confession(partner)
            self.emit(f"Confession: {confession['message']}")
            if self.tokens_consumed >= self.max_tokens_target:
                break

        self.emit(f"\n{'#'*80}")
        self.emit(f"# ENGINE TERMINATED")
        self.emit(f"# Total Tokens: {self.tokens_consumed:,}")
        self.emit(f"# Total Lines: {len(self.output_lines):,}")
        self.emit(f"# Runtime: {(datetime.now() - self.start_time).total_seconds():.2f}s")
        self.emit(f"{'#'*80}")

        output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output", f"dating_output_{int(datetime.now().timestamp())}.txt")
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(self.output_lines))
        self.emit(f"Output saved to: {output_file}")
        return self.tokens_consumed

    def generate_chapter(self):
        titles = ["The First Spark", "The Sweet Date", "The Confession",
            "The Wedding", "The Honeymoon", "The Family",
            "The Legacy", "The Forever", "The Eternity", "The Dawn"]
        self.emit(f"\n{'='*80}")
        self.emit(f"CHAPTER {len(self.output_lines)//500 + 1}: {titles[random.randint(0, len(titles)-1)]}")
        self.emit(f"{'='*80}")
        for _ in range(20):
            partner = self.game.generate_partner(random.randint(0, 50))
            self.emit(f"{partner['name']}: {partner['first_impression']}")
            self.emit(f"  {partner['appearance']}")
            self.emit(f"  {partner['personality']} and {partner['hobby']}")
        self.emit(f"{'='*80}\n")

if __name__ == "__main__":
    target = int(sys.argv[1]) if len(sys.argv) > 1 else 999999
    engine = InfiniteDatingEngine(max_tokens_target=target)
    tokens = engine.run_full_simulation()
    print(f"\nDONE! Consumed {tokens:,} tokens.")
