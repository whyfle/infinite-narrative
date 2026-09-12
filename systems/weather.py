import random
from generators.names import NameGenerator
from generators.descriptions import DescriptionGenerator

class WeatherSystem:
    def __init__(self):
        self.name_gen = NameGenerator()
        self.desc_gen = DescriptionGenerator()
        self.weather_types = ["Clear Skies", "Overcast", "Rain", "Thunderstorm", "Blizzard",
            "Sandstorm", "Fog", "Hail", "Drizzle", "Typhoon", "Tornado", "Hurricane",
            "Meteor Shower", "Aurora Borealis", "Void Storm", "Ember Rain", "Frostfire",
            "Shadow Mist", "Lightning Storm", "Acid Rain", "Crystal Fog", "Dream Mist",
            "Eclipse", "Solar Flare", "Magnetic Storm", "Gravity Anomaly", "Time Distortion"]
        self.severities = ["Mild", "Moderate", "Severe", "Extreme", "Catastrophic", "Apocalyptic"]
        self.effects = [
            "reduces visibility to {distance} feet",
            "deals {damage} damage per round to all exposed creatures",
            "grants {bonus} to all {stat} checks",
            "imposes {penalty} to all {stat} checks",
            "causes {effect} to all {object}",
            "creates {hazard} that {effect}",
            "heals {amount} HP per round to all creatures in the area",
            "damages all equipment, reducing durability by {amount}%",
            "summons {creature} that {effect} for {duration} rounds",
            "alters {property} in the area, causing {effect}"
        ]
        self.Locations = ["the Plains", "the Forest", "the Mountains", "the Ocean", "the Desert",
            "the Sky", "the Abyss", "the Void", "the Crystal Caves", "the Ember Fields"]
        self.narratives = [
            "The sky turned {color} as {event} began, casting an eerie glow over the {location}.",
            "A {severity} {weather} swept through the {location}, {effect} everything in its path.",
            "The air grew {adj} as {weather} descended upon the {location} with {severity} intensity.",
            "From the {location}, a {weather} of {severity} proportions emerged, {effect} all who witnessed it.",
            "The {weather} brought {event} to the {location}, {effect} the {creature} and all living things."
        ]

    def generate_full_weather(self, index):
        weather = random.choice(self.weather_types)
        severity = random.choice(self.severities)
        location = random.choice(self.Locations)
        duration = random.randint(1, 1000)
        hazard = random.choice(["falling debris", "lightning strikes", "toxic spores", "raging flames",
            "crushing ice", "void rifts", "shadow tendrils", "electrical arcs"])
        lines = [
            f"\n{'='*60}",
            f"WEATHER PHENOMENA #{index}",
            f"{'='*60}",
            f"Weather: {weather}",
            f"Severity: {severity}",
            f"Location: {location}",
            f"Duration: {duration} rounds",
            f"\nNARRATIVE:",
        ]
        narrative = random.choice(self.narratives).format(
            color=random.choice(["crimson", "golden", "violet", "black", "silver", "green"]),
            event=random.choice(["a great upheaval", "the return of the old gods", "the breaking of the seal"]),
            location=location,
            weather=weather,
            severity=severity,
            effect=random.choice(["devastating", "transformative", "beneficial", "catastrophic", "mysterious"]),
            adj=random.choice(["oppressive", "electric", "suffocating", "beautiful", "terrifying"]),
            creature=random.choice(["the Dragon", "the Leviathan", "the Spirit", "the Ancient"]),
            hazard=hazard
        )
        lines.append(f"  {narrative}")
        lines.append(f"\nEFFECTS:")
        for _ in range(random.randint(2, 5)):
            effect = random.choice(self.effects).format(
                distance=random.randint(10, 1000),
                damage=random.randint(1, 500),
                bonus=random.choice(["+50", "+100", "+200"]),
                penalty=random.choice(["-25", "-50", "-75"]),
                amount=random.randint(10, 500),
                stat=random.choice(["Strength", "Dexterity", "Intelligence", "Wisdom"]),
                effect=random.choice(["disintegration", "petrification", "erasure", "corruption"]),
                object=random.choice(["structures", "creatures", "artifacts", "the landscape"]),
                hazard=hazard,
                creature=random.choice(["Elemental", "Spirit", "Dragon", "Beast"]),
                duration=random.randint(1, 100),
                property=random.choice("Time Space Reality Existence".split()),
                duration2=random.randint(1, 100)
            )
            lines.append(f"  - {effect}")
        lines.append(f"\n{'='*60}\n")
        return lines
