import random
from characters import CharacterGenerator
from datetime import datetime

class DatingSimulator:
    def __init__(self):
        self.char_gen = CharacterGenerator()
        self.player_name = "Player"
        self.player_affection = 0
        self.player_wealth = 100
        self.player_charm = 50
        self.player_intelligence = 50
        self.player_humor = 50
        self.player_relationship = {}
        self.dates_completed = 0
        self.gifts_given = []
        self.game_state = "start"
        self.current_date = None
        self.current_partner = None
        self.day = 1
        self.season = "Spring"
        self.weather = "Clear"
        self.locations = self.char_gen.generate_date_locations()
        self.gifts = self.char_gen.generate_gifts()
        self.dating_scenes = []
        self.conversations = []

    def generate_player(self, name="Player"):
        self.player_name = name
        self.player_affection = 0
        self.player_wealth = 100
        self.player_charm = random.randint(30, 70)
        self.player_intelligence = random.randint(30, 70)
        self.player_humor = random.randint(30, 70)
        self.player_relationship = {}
        self.dates_completed = 0
        self.gifts_given = []
        self.game_state = "playing"
        self.day = 1
        self.season = random.choice(["Spring", "Summer", "Autumn", "Winter"])
        return {
            "name": name,
            "affection": self.player_affection,
            "wealth": self.player_wealth,
            "charm": self.player_charm,
            "intelligence": self.player_intelligence,
            "humor": self.player_humor,
            "inventory": self.gifts[:5],
            "stats": {
                "Level": random.randint(1, 20),
                "Happiness": random.randint(50, 100),
                "Mood": "Optimistic",
                "Day": self.day,
                "Season": self.season
            }
        }

    def generate_partner(self, index=0):
        partner = self.char_gen.generate_dateable_char(index)
        self.player_relationship[partner["name"]] = {
            "affection": 0,
            "dates": 0,
            "gifts_received": [],
            "status": "Stranger",
            "compatibility": partner["stats"]["Compatibility"],
            "first_meeting": self.generate_first_meeting(partner)
        }
        return partner

    def generate_first_meeting(self, partner):
        impressions = [
            "{player} and {partner} locked eyes across the crowded room.",
            "{player} bumped into {partner} on the street.",
            "{partner} appeared at {player}'s doorstep unexpectedly.",
            "{player} and {partner} were seated next to each other at a festival.",
            "{partner} saved {player} from an embarrassing situation.",
            "{player} noticed {partner} at the local tavern.",
            "{partner} and {player} crossed paths during a magical storm.",
            "{player} found {partner} reading alone in the library.",
            "{partner} waved at {player} from across the market.",
            "{player} and {partner} were both competing in the same tournament."
        ]
        return random.choice(impressions).format(player=self.player_name, partner=partner["name"])

    def generate_date(self, partner, location_idx=0):
        location = self.locations[location_idx % len(self.locations)]
        self.current_date = {
            "partner": partner["name"],
            "location": location["name"],
            "activity": location["activity"],
            "atmosphere": location["atmosphere"],
            "cost": location["cost"],
            "bonus": location["bonus"],
            "weather": self.weather,
            "season": self.season,
            "day": self.day,
            "outcomes": [],
            "dialogue": []
        }
        affection_change = self.calculate_date_outcome(partner, location)
        self.player_wealth -= location["cost"]
        self.dates_completed += 1
        self.day += 1
        if self.day > 28:
            self.day = 1
            self.season = random.choice(["Spring", "Summer", "Autumn", "Winter"])
        self.player_relationship[partner["name"]]["dates"] += 1
        self.player_relationship[partner["name"]]["affection"] += affection_change
        if affection_change > 20:
            self.player_relationship[partner["name"]]["status"] = "Dating"
        elif affection_change > 5:
            self.player_relationship[partner["name"]]["status"] = "Getting to Know"
        self.dating_scenes.append(self.current_date)
        return self.current_date, affection_change

    def calculate_date_outcome(self, partner, location):
        base_affection = random.randint(5, 30)
        location_bonus = location["cost"] * 2
        charm_modifier = self.player_charm * 0.1
        compatibility_modifier = self.player_relationship[partner["name"]]["compatibility"] * 0.05
        gift_modifier = sum(1 for g in self.gifts_given if g["name"] in partner["gifts"]) * 10
        weather_modifier = 5 if self.weather == "Clear" else -3
        total = int(base_affection + location_bonus + charm_modifier + compatibility_modifier + gift_modifier + weather_modifier)
        return max(total, 1)

    def generate_date_dialogue(self, partner):
        dialogues = [
            "{partner}: 'I love spending time with you under the {weather}. It feels like destiny.'",
            "{partner}: 'Tell me more about yourself. Your stories always captivate me.'",
            "{partner}: 'This place is beautiful, just like you.'",
            "{player}: 'I feel so happy when I'm with you.'",
            "{partner}: 'You have such a wonderful {trait} personality.'",
            "{player}: 'I never imagined I'd find someone like you.'",
            "{partner}: 'Your {trait} nature is so attractive to me.'",
            "{player}: 'Every moment with you feels like a dream.'",
            "{partner}: 'Let me share something about my {hobby}...'",
            "{player}: 'I admire your {trait} way of looking at the world.'",
            "{partner}: 'I was wondering... would you like to be with me?'",
            "{player}: 'My heart belongs to you, {partner}.' ",
            "{partner}: 'The {weather} reminds me of the day we met.'",
            "{player}: 'I want to give you this {gift} because you mean everything.'",
            "{partner}: 'You are my everything. I love you more than words can say.'"
        ]
        scene = []
        for _ in range(random.randint(5, 12)):
            dialogue = random.choice(dialogues).format(
                partner=partner["name"], player=self.player_name,
                weather=self.weather, trait=partner["personality"],
                hobby=partner["hobby"], gift=random.choice(self.gifts)["name"]
            )
            scene.append(dialogue)
        return scene

    def generate_gift_interaction(self, partner):
        gift = random.choice(self.gifts)
        self.gifts_given.append(gift)
        affection = gift["affection_bonus"]
        self.player_wealth -= gift["value"]
        self.player_relationship[partner["name"]]["gifts_received"].append(gift)
        self.player_relationship[partner["name"]]["affection"] += affection
        reactions = [
            "{partner} gasped with delight! '{gift}! This is exactly what I've always wanted!'",
            "{partner} held the {gift} close to their heart. 'You didn't have to, but I love it!'",
            "{partner} smiled warmly. 'This is the most thoughtful gift anyone has ever given me.'",
            "{partner} tears up. '{gift}... you really know me.'",
            "{partner} beamed. 'I've been wanting a {gift} for so long! Thank you!'",
            "{partner} blushed. 'This is too generous. But I love it.'",
            "{partner} clutched the {gift} tightly. 'This means the world to me.'"
        ]
        reaction = random.choice(reactions).format(partner=partner["name"], gift=gift["name"])
        return {"gift": gift, "reaction": reaction, "affection_change": affection}

    def generate_confession(self, partner):
        if self.player_relationship[partner["name"]]["affection"] < 50:
            return {"success": False, "message": f"{partner['name']} needs more affection before you can confess."}
        success = self.player_relationship[partner["name"]]["affection"] >= 80
        if success:
            messages = [
                f"{partner['name']} smiled through tears. 'I love you too. Let's be together forever.'",
                f"{partner['name']} wrapped their arms around you. 'Yes, I want to spend the rest of my life with you.'",
                f"{partner['name']} kissed you softly. 'I've been waiting for you to say that.'",
                f"{partner['name']} held your hands. 'I love you more than all the stars in the sky.'",
                f"{partner['name']} whispered. 'You found my heart. Keep it safe, my love.'"
            ]
            self.player_relationship[partner["name"]]["status"] = "In Love"
        else:
            messages = [
                f"{partner['name']} blushed. 'I appreciate your honesty, but I'm not ready yet.'",
                f"{partner['name']} smiled gently. 'Your feelings mean so much to me. Let's take it slow.'",
                f"{partner['name']} looked down. 'I care about you, but I need more time.'"
            ]
        return {"success": success, "message": random.choice(messages), "status": "In Love" if success else "Getting Closer"}

    def generate_breakup(self, partner):
        messages = [
            f"{partner['name']} looked at you sadly. 'I think we should see other people.'",
            f"{partner['name']} sighed. 'I've fallen out of love. Please be happy without me.'",
            f"{partner['name']} walked away. 'This isn't working anymore. I'm sorry.'",
            f"{partner['name']} cried. 'I can't keep pretending everything is fine.'",
            f"{partner['name']} whispered. 'Goodbye. I wish you the best.'"
        ]
        self.player_relationship[partner["name"]]["status"] = "Broken"
        self.player_relationship[partner["name"]]["affection"] = 0
        return random.choice(messages)

    def generate_compatibility_report(self, partner):
        love_lang = partner["love_language"]
        return {
            "partner": partner["name"],
            "compatibility": self.player_relationship[partner["name"]]["compatibility"],
            "affection": self.player_relationship[partner["name"]]["affection"],
            "dates": self.player_relationship[partner["name"]]["dates"],
            "status": self.player_relationship[partner["name"]]["status"],
            "love_language": love_lang,
            "favorite": partner["favorite"],
            "dislike": partner["dislike"],
            "fear": partner["fear"],
            "dream": partner["dream"],
            "favorite_date": partner["favorite_date"],
            "report": self.generate_compatibility_text(partner)
        }

    def generate_compatibility_text(self, partner):
        texts = [
            f"{partner['name']} and {self.player_name} share a {self.player_relationship[partner['name']]['compatibility']}% compatibility.",
            f"The {partner['love_language']} love language of {partner['name']} means they need {partner['favorite']} to feel loved.",
            f"Despite {partner['fear']}, {partner['name']} dreams of {partner['dream']} alongside you.",
            f"Your shared dates have created {self.player_relationship[partner['name']]['dates']} beautiful memories together."
        ]
        return random.choice(texts)

    def generate_narrative_summary(self):
        total_affection = sum(r["affection"] for r in self.player_relationship.values())
        total_dates = sum(r["dates"] for r in self.player_relationship.values())
        in_love = [name for name, r in self.player_relationship.items() if r["status"] == "In Love"]
        return {
            "player": self.player_name,
            "day": self.day,
            "season": self.season,
            "dates_completed": self.dates_completed,
            "total_affection": total_affection,
            "total_dates": total_dates,
            "in_love": in_love,
            "wealth": self.player_wealth,
            "partner_count": len(self.player_relationship),
            "story": self.generate_full_story(),
            "partners": [{
                "name": name,
                "affection": r["affection"],
                "status": r["status"],
                "dates": r["dates"],
                "first_meeting": r["first_meeting"]
            } for name, r in self.player_relationship.items()]
        }

    def generate_full_story(self):
        chapters = []
        for i in range(min(len(self.dating_scenes), 20)):
            scene = self.dating_scenes[i] if i < len(self.dating_scenes) else self.generate_date(self.generate_partner())
            chapters.append(f"Chapter {i+1}: {scene['partner']} at {scene['location']}")
        return chapters

    def save_game(self):
        return {
            "player_name": self.player_name,
            "player_affection": self.player_affection,
            "player_wealth": self.player_wealth,
            "player_charm": self.player_charm,
            "player_intelligence": self.player_intelligence,
            "player_humor": self.player_humor,
            "relationships": self.player_relationship,
            "dates_completed": self.dates_completed,
            "gifts_given": self.gifts_given,
            "day": self.day,
            "season": self.season,
            "dating_scenes": self.dating_scenes,
            "game_state": self.game_state
        }
