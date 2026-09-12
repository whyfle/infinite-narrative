import random
from generators.names import NameGenerator
from generators.descriptions import DescriptionGenerator

class DialogueGenerator:
    def __init__(self):
        self.name_gen = NameGenerator()
        self.desc_gen = DescriptionGenerator()
        self.dialogue_types = ["Negotiation", "Warning", "Prophecy", "Confession", "Challenge",
            "Alliance", "Betrayal", "Revelation", "Plea", "Command", "Question", "Answer",
            "Lament", "Celebration", "Warning", "Curse", "Blessing", "Oath", "Vow", "Threat"]
        self.speakers = [
            "The Ancient Dragon", "The Oracle of Shadows", "The King of Eldoria", "The Wandering Sage",
            "The Cursed Princess", "The Betrayed General", "The Forgotten God", "The Last Witch",
            "The Young Hero", "The Ancient Demon", "The Celestial Being", "The Shadow Lord",
            "The Dream Weaver", "The Storm Caller", "The Earth Mother", "The Void Walker",
            "The Time Keeper", "The Memory Merchant", "The Truth Seeker", "The Lie Collector",
            "The Star Harvester", "The Moon Singer", "The Sun Forger", "The Dark Emperor",
            "The Light Bearer", "The Chaos Bringer", "The Order Keeper", "The Wild Card",
            "The Silent Watcher", "The Whispering Wind", "The Hollow Knight", "The Crimson Queen",
            "The Iron Smith", "The Silver Tongue", "The Golden Heart", "The Black Cloud"
        ]
        self.responses = [
            "I have waited {number} years for this moment, and it has finally arrived.",
            "You cannot possibly understand what it costs to wield such power.",
            "The prophecy spoke of this day, but never did it mention {character}.",
            "Take this {artifact} and use it wisely, for there will be no second chance.",
            "I will not hesitate this time. The {faction} has suffered long enough.",
            "You ask the wrong question. The real question is: are you prepared for the answer?",
            "Every choice has a consequence, and you have chosen {consequence}.",
            "The {location} is not what it appears. Look deeper, beyond the {adj} surface.",
            "I speak not for myself, but for all those who cannot speak at all.",
            "The {creature} will come for you. You must be ready when it arrives.",
            "Power is not given. It is taken, with blood and sacrifice.",
            "The {property} of this world depends on your decision. Choose wisely.",
            "I have seen {number} possible futures, and in none of them do you survive.",
            "You remind me of myself, before the {event} changed everything.",
            "The {faction} taught me that {lesson}. I was wrong about that.",
            "This {artifact} was not meant for you, but you were meant for it.",
            "The {location} remembers everything. Even what you have tried to forget.",
            "Fear is the {adj} enemy, for it {verb} even the strongest of us.",
            "I am not what I appear. I am {adj}, {adj}, and {adj} all at once.",
            "The {creature} was {adj} before I met it, but now... it is worse.",
            "You carry the {property} of {character} within you, though you know it not.",
            "There are {number} truths in this world, and only {number} of them are comfortable.",
            "The {faction} and the {faction} have been at war for {number} centuries.",
            "I will tell you the truth, but you may not like what you hear.",
            "The {location} was once {adj}. Now it is {adj}. And soon, it will be {adj}.",
            "You must {action} before the {time} passes, or all will be lost.",
            "The {artifact} chose you, not the other way around.",
            "Every {creature} has a {adj} story, even the ones that {verb} you.",
            "The {property} runs through my veins. It {verb} my every thought.",
            "I offer you {choice}. Do not take it lightly, for there is no {alternative}."
        ]
        self.contexts = [
            "in the throne room of {location}",
            "at the edge of the {location}",
            "within the {location} itself",
            "beneath the {location}",
            "above the {location}",
            "in the shadows of {location}",
            "before the {location}",
            "after the {location}",
            "throughout the {location}",
            "across the {location}"
        ]
        self.emotions = ["fear", "anger", "sadness", "joy", "determination", "despair", "hope",
            "rage", "calm", "confusion", "wonder", "dread", "pride", "shame", "guilt"]
        self.tone_modifiers = ["softly", "coldly", "passionately", "quietly", "fiercely",
            "regretfully", "joyfully", "darkly", "mysteriously", "urgently", "bitterly"]

    def generate_dialogue_line(self, speaker=None, context_idx=0):
        speaker = speaker or random.choice(self.speakers)
        response = random.choice(self.responses).format(
            number=random.randint(1, 10000),
            character=random.choice(self.speakers),
            artifact=random.choice(["Crown of Shadows", "Sword of Light", "Tome of Knowledge"]),
            faction=random.choice(["Order of Light", "Shadow Covenant", "Void Collective"]),
            consequence=random.choice(["everything", "nothing", "the destruction of the realm"]),
            location=random.choice(["Crystal Spire", "Abyssal Chasm", "Ember Court"]),
            adj=random.choice(["ancient", "forgotten", "eternal", "mythic", "shadowy"]),
            creature=random.choice(["Dragon", "Golem", "Wraith", "Hydra"]),
            property=random.choice(["Time", "Space", "Reality", "Consciousness"]),
            event=random.choice(["the Shattering", "the Great War", "the Age of Ruin"]),
            lesson=random.choice(["power corrupts", "hope endures", "truth is elusive"]),
            time=random.choice(["the hour", "the eve", "the dawn"]),
            alternative=random.choice(["other path", "second choice", "remaining option"]),
            verb=random.choice(["consumes", "destroys", "shatters", "twists", "corrupts"]),
            action=random.choice(["defeat the enemy", "cast the spell", "find the truth", "seal the gate", "light the flame"]),
            choice=random.choice(["path A", "path B", "path C"])
        )
        context = random.choice(self.contexts).format(
            location=random.choice(["the Citadel", "the Forest", "the Mountain", "the Ocean"])
        )
        tone = random.choice(self.tone_modifiers)
        emotion = random.choice(self.emotions)
        return f"{speaker} ({emotion}, {tone}), {context}: \"{response}\""

    def generate_scene(self, scene_idx):
        num_speakers = random.randint(2, 5)
        speakers = random.sample(self.speakers, num_speakers)
        lines = [
            f"\n{'='*60}",
            f"SCENE {scene_idx}: {random.choice(self.dialogue_types)}",
            f"Setting: {random.choice(self.desc_gen.sentences_a)}",
            f"{'='*60}",
            f"Participants: {', '.join(speakers)}"
        ]
        for i in range(random.randint(8, 20)):
            speaker = random.choice(speakers)
            lines.append(self.generate_dialogue_line(speaker))
        lines.append(f"\n{'='*60}\n")
        return lines

    def generate_full_scene(self, scene_idx):
        scene = self.generate_scene(scene_idx)
        return scene

    def generate_dialogue_tree(self, depth=3):
        tree = []
        root_speaker = random.choice(self.speakers)
        root_line = self.generate_dialogue_line(root_speaker)
        tree.append(root_line)
        for i in range(depth):
            branch = f"  Branch {i+1}: "
            for j in range(random.randint(2, 4)):
                branch += f"[{self.generate_dialogue_line()} | "
            branch = branch.rstrip(" | ") + "] "
            tree.append(branch)
        return tree
