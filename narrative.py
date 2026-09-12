import random
from characters import CharacterGenerator
from dates import DatingSimulator

class NarrativeEngine:
    def __init__(self):
        self.char_gen = CharacterGenerator()
        self.dating = DatingSimulator()
        self.lines = []
        self.tokens = 0
        self.chapter = 0
        self.generate_massive_narrative()

    def emit(self, text):
        self.lines.append(text)
        self.tokens += len(text.split())

    def generate_chapter(self):
        self.chapter += 1
        titles = [
            "The First Meeting", "The Spark of Attraction", "The First Date",
            "Whispers of Love", "The Confession", "A Bond Forged",
            "The Wedding", "The Honeymoon", "The Family",
            "The Legacy", "The Golden Years", "The Eternal Promise"
        ]
        subtitle = self.char_gen.generate_dateable_char(0)["first_impression"]
        self.emit(f"\n{'='*80}")
        self.emit(f"CHAPTER {self.chapter}: {titles[(self.chapter-1) % len(titles)]}")
        self.emit(f"{subtitle}")
        self.emit(f"{'='*80}")

    def generate_player_introduction(self):
        self.emit(f"\n{'#'*80}")
        self.emit(f"# THE STORY OF {self.dating.player_name}")
        self.emit(f"# A Dating Simulator Epic")
        self.emit(f"{'#'*80}")
        self.emit(f"Day 1, {self.dating.season}. {self.dating.weather}.")
        self.emit(f"{self.dating.player_name} is a level {random.randint(1,20)} adventurer with")
        self.emit(f"{self.dating.player_charm} charm, {self.dating.player_intelligence} intelligence,")
        self.emit(f"and {self.dating.player_humor} humor. The journey begins...")
        self.emit(f"")
        for _ in range(random.randint(5, 15)):
            self.emit(self.dating.dating_scenes[0]["dialogue"][random.randint(0, len(self.dating.dating_scenes[0]["dialogue"])-1)] if self.dating.dating_scenes else f"{self.dating.player_name} walked into the {random.choice(['tavern', 'forest', 'city', 'castle'])}.")

    def generate_all_partners(self, count=20):
        for i in range(count):
            partner = self.dating.generate_partner(i)
            self.emit(f"\n{'*'*60}")
            self.emit(f"POTENTIAL LOVE INTEREST #{i+1}: {partner['name']}")
            self.emit(f"{'*'*60}")
            self.emit(f"Class: {partner['class']} | Race: {partner['race']} | Age: {partner['age']}")
            self.emit(f"Personality: {partner['personality']} | {partner['appearance']}")
            self.emit(f"Hobby: {partner['hobby']} | Favorite: {partner['favorite']}")
            self.emit(f"Smell: {partner['smell']} | Clothing: {partner['clothing']}")
            self.emit(f"Status: {partner['stats']['Status']}")
            self.emit(f"")
            self.emit(f"Stats:")
            for stat, val in partner["stats"].items():
                self.emit(f"  {stat}: {val}")
            self.emit(f"")
            self.emit(f"Backstory:")
            self.emit(f"  {partner['backstory']}")
            self.emit(f"")
            self.emit(f"First Impression:")
            self.emit(f"  {partner['first_impression']}")
            self.emit(f"")
            self.emit(f"Love Language: {partner['love_language']}")
            self.emit(f"Favorite Date: {partner['favorite_date']}")
            self.emit(f"Dream: {partner['dream']}")
            self.emit(f"Fear: {partner['fear']}")
            self.emit(f"Dislike: {partner['dislike']}")
            self.emit(f"Crush On: {partner['crush_on'] if partner['crush_on'] else 'No one'}")
            self.emit(f"")
            self.emit(f"Gifts:")
            for g in partner["gifts"]:
                self.emit(f"  - {g}")
            self.emit(f"")
            self.emit(f"{'*'*60}\n")

    def generate_all_dates(self, partner_count=15):
        for i in range(partner_count):
            partner = self.dating.generate_partner(i)
            location = random.choice(self.dating.locations)
            date, affection = self.dating.generate_date(partner, self.dating.locations.index(location))
            dialogue = self.dating.generate_date_dialogue(partner)
            self.emit(f"\n{'='*60}")
            self.emit(f"DATE #{i+1} with {partner['name']}")
            self.emit(f"{'='*60}")
            self.emit(f"Location: {location['name']} ({location['atmosphere']})")
            self.emit(f"Activity: {location['activity']}")
            self.emit(f"Cost: {location['cost']} gold | Weather: {self.dating.weather}")
            self.emit(f"Affection Change: +{affection}")
            self.emit(f"")
            self.emit(f"DIALOGUE:")
            for d in dialogue:
                self.emit(f"  {d}")
            self.emit(f"")
            self.emit(f"OUTCOME:")
            self.emit(f"  Status: {self.dating.player_relationship[partner['name']]['status']}")
            self.emit(f"  Total Dates: {self.dating.player_relationship[partner['name']]['dates']}")
            self.emit(f"  Total Affection: {self.dating.player_relationship[partner['name']]['affection']}")
            self.emit(f"{'='*60}\n")

    def generate_all_gifts(self, partner_count=15):
        for i in range(partner_count):
            partner = self.dating.generate_partner(i)
            gift = self.dating.generate_gift_interaction(partner)
            self.emit(f"\n{'-'*60}")
            self.emit(f"GIFT TO {partner['name']}")
            self.emit(f"{'-'*60}")
            self.emit(f"Gift: {gift['gift']['name']} ({gift['gift']['description']})")
            self.emit(f"Value: {gift['gift']['value']} gold | Affection: +{gift['affection_change']}")
            self.emit(f"")
            self.emit(f"Reaction:")
            self.emit(f"  {gift['reaction']}")
            self.emit(f"{'-'*60}\n")

    def generate_all_compatibility(self, partner_count=15):
        for i in range(partner_count):
            partner = self.dating.generate_partner(i)
            report = self.dating.generate_compatibility_report(partner)
            self.emit(f"\n{'%'*60}")
            self.emit(f"COMPATIBILITY REPORT: {partner['name']}")
            self.emit(f"{'%'*60}")
            self.emit(f"Compatibility: {report['compatibility']}%")
            self.emit(f"Affection: {report['affection']}")
            self.emit(f"Dates: {report['dates']}")
            self.emit(f"Status: {report['status']}")
            self.emit(f"Love Language: {report['love_language']}")
            self.emit(f"")
            self.emit(f"Report: {report['report']}")
            self.emit(f"")
            self.emit(f"Favorite: {report['favorite']}")
            self.emit(f"Dislike: {report['dislike']}")
            self.emit(f"Fear: {report['fear']}")
            self.emit(f"Dream: {report['dream']}")
            self.emit(f"")
            self.emit(f"{'%'*60}\n")

    def generate_all_confessions(self, partner_count=10):
        for i in range(partner_count):
            partner = self.dating.generate_partner(i)
            # Boost affection for confession
            self.dating.player_relationship[partner["name"]]["affection"] = random.randint(60, 100)
            confession = self.dating.generate_confession(partner)
            self.emit(f"\n{'#'*60}")
            self.emit(f"CONFESSION #{i+1} to {partner['name']}")
            self.emit(f"{'#'*60}")
            self.emit(f"Affection Level: {self.dating.player_relationship[partner['name']]['affection']}")
            self.emit(f"Success: {confession['success']}")
            self.emit(f"Message: {confession['message']}")
            self.emit(f"Status: {confession['status']}")
            self.emit(f"{'#'*60}\n")

    def generate_all_breakups(self, partner_count=10):
        for i in range(partner_count):
            partner = self.dating.generate_partner(i)
            self.dating.player_relationship[partner["name"]]["affection"] = 5
            breakup = self.dating.generate_breakup(partner)
            self.emit(f"\n{'!'*60}")
            self.emit(f"BREAKUP WITH {partner['name']}")
            self.emit(f"{'!'*60}")
            self.emit(f"Message: {breakup}")
            self.emit(f"Status: Broken")
            self.emit(f"{'!'*60}\n")

    def generate_massive_narrative(self):
        self.emit(f"INFINITE DATING SIMULATOR NARRATIVE ENGINE")
        self.emit(f"Generated: {datetime.now().isoformat()}")
        self.emit(f"Player: {self.dating.player_name}")
        self.emit(f"")
        self.generate_player_introduction()
        self.generate_all_partners(20)
        self.generate_all_dates(20)
        self.generate_all_gifts(20)
        self.generate_all_compatibility(20)
        self.generate_all_confessions(15)
        self.generate_all_breakups(10)
        summary = self.dating.generate_narrative_summary()
        self.emit(f"\n{'='*80}")
        self.emit(f"FINAL NARRATIVE SUMMARY")
        self.emit(f"{'='*80}")
        self.emit(f"Player: {summary['player']}")
        self.emit(f"Day: {summary['day']} | Season: {summary['season']}")
        self.emit(f"Dates Completed: {summary['dates_completed']}")
        self.emit(f"Total Affection: {summary['total_affection']}")
        self.emit(f"In Love: {', '.join(summary['in_love']) if summary['in_love'] else 'None'}")
        self.emit(f"Wealth: {summary['wealth']} gold")
        self.emit(f"Partners: {summary['partner_count']}")
        for partner in summary["partners"]:
            self.emit(f"  - {partner['name']}: {partner['status']} (Affection: {partner['affection']}, Dates: {partner['dates']})")
            self.emit(f"    First Meeting: {partner['first_meeting']}")
        self.emit(f"\n{'='*80}")

    def get_output(self):
        return self.lines

    def get_tokens(self):
        return self.tokens
