import random

class DescriptionGenerator:
    def __init__(self):
        self.adjectives = ["ancient", "forgotten", "eternal", "mythic", "divine", "shadowy", "void", "crystalline", "radiant", "dark",
            "luminescent", "ethereal", "abyssal", "primordial", "catastrophic", "boundless", "transcendent", "supreme", "infinite", "celestial",
            "frozen", "burning", "toxic", "sacred", "profane", "eldritch", "arcane", "runic", "sigil", "enchanted",
            "cursed", "blessed", "haunted", "desolate", "barren", "fertile", "verdant", "withered", "blighted", "corrupted",
            "glorious", "magnificent", "terrible", "horrible", "beautiful", "hideous", "wonderful", "dreadful", "awe-inspiring", "horrifying",
            "tremendous", "colossal", "tiny", "massive", "gigantic", "diminutive", "vast", "narrow", "wide", "deep",
            "shallow", "tall", "short", "long", "wide", "endless", "finite", "limitless", "unbounded", "constrained"]
        self.nouns = ["realm", "dimension", "plane", "world", "kingdom", "empire", "nation", "territory", "domain", "province",
            "city", "town", "village", "hamlet", "settlement", "outpost", "fortress", "castle", "citadel", "sanctum",
            "tower", "spire", "temple", "shrine", "altar", "monastery", "abbey", "cathedral", "basilica", "chapel",
            "cave", "grotto", "cavern", "tunnel", "passage", "corridor", "hallway", "chamber", "room", "cell",
            "forest", "jungle", "desert", "tundra", "swamp", "marsh", "meadow", "prairie", "savanna", "rainforest",
            "mountain", "hill", "valley", "plain", "plateau", "mesa", "canyon", "ridge", "peak", "summit",
            "river", "lake", "ocean", "sea", "pond", "stream", "waterfall", "spring", "fount", "well",
            "dragon", "griffin", "phoenix", "titan", "golem", "wraith", "demon", "angel", "beast", "hydra",
            "sword", "shield", "crown", "throne", "relic", "artifact", "tome", "scroll", "grail", "chalice"]
        self.verbs = ["shatters", "consumes", "devours", "transforms", "creates", "destroys", "builds", "erodes", "illuminates", "darkens",
            "elevates", "descends", "ascends", "collapses", "expands", "contracts", "breathes", "pulses", "throbs", "roars",
            "whispers", "screams", "singes", "freezes", "burns", "drowns", "crushes", "lifts", "drops", "splits",
            "merges", "divides", "spins", "twists", "bends", "breaks", "mends", "heals", "poisons", "purifies",
            "summons", "banishes", "traps", "frees", "captures", "releases", "conjures", "evaporates", "materializes", "dissolves"]
        self.properties = ["Time", "Space", "Reality", "Existence", "Consciousness", "Memory", "Dreams", "Nightmares", "Hope", "Despair",
            "Life", "Death", "Light", "Darkness", "Order", "Chaos", "Creation", "Destruction", "Power", "Knowledge"]
        self.materials = ["dragonbone", "starsteel", "voidite", "crysthalis", "obsidian", "mithral", "divine gold", "shadow iron",
            "celestial silver", "abyssal bronze", "dragon scales", "phoenix feathers", "griffin quills", "titanium",
            "moonstone", "sunstone", "star crystal", "void essence", "shadow essence", "light essence"]
        self.creatures = ["dragon", "griffin", "phoenix", "leviathan", "titan", "golem", "wraith", "demon", "angel", "beast",
            "hydra", "chimera", "cerberus", "minotaur", "centaur", "manticore", "sphinx", "basilisk", "wyvern", "pegasus",
            "troll", "ogre", "giant", "elemental", "spirit", "phantom", "specter", "revenant", "lich", "vampire"]
        self.sentences_a = [
            "The air grew thick with the scent of ancient power, as if the very atmosphere remembered the glory of ages past.",
            "A low rumble echoed through the chambers, shaking dust from the ceiling and stirring memories long forgotten.",
            "The ground trembled beneath their feet, and for a moment, all of existence seemed to hold its breath.",
            "Light cascaded from above, painting the world in hues of gold and silver that defied description.",
            "Shadows danced along the walls, twisting and coiling like living things, whispering secrets of the void.",
            "The temperature shifted dramatically, from scorching heat to bone-chilling cold, without any warning.",
            "A sudden silence fell, so complete that the sound of their own heartbeats became thunderous.",
            "The horizon split open, revealing a vista beyond comprehension, a place where reality itself seemed to fracture.",
            "Time appeared to slow, then reverse, then accelerate beyond all reason, confounding every sense of measurement.",
            "The ground beneath them transformed, stone becoming glass, glass becoming liquid, liquid becoming sky."
        ]
        self.sentences_b = [
            "From the depths of the abyss, a voice rose, speaking words in a language that predated civilization itself.",
            "The stars aligned in a pattern that had not been seen in ten thousand years, heralding an era of unprecedented change.",
            "A wave of energy pulsed outward from the epicenter, flattening forests, reshaping mountains, and rewriting the laws of physics.",
            "The collective consciousness of every living thing in the realm surged forth, forming a single unified thought.",
            "Reality folded upon itself, creating paradoxes and contradictions that defied all logical understanding.",
            "An ancient prophecy came to pass, its words manifesting in the physical world with terrible and beautiful precision.",
            "The boundary between the mortal realm and the divine plane thinned to nothing, allowing the impossible to become tangible.",
            "A convergence of magical forces created a storm of pure creation, birthing new worlds from the fabric of the old.",
            "The memory of the universe itself seemed to rewrite, altering history, present, and future in a single instant.",
            "Every soul in existence felt a profound connection, as if the invisible threads that bound them all had been pulled taut."
        ]
        self.sentences_c = [
            "The air shimmered with latent magical energy, each particle carrying the weight of a thousand spells.",
            "Beneath the surface, an ancient civilization stirred from its eternal slumber, its cities of crystal and shadow rising anew.",
            "The fabric of space tore, revealing vistas of impossible geometry and colors that had no names.",
            "A chorus of voices, some familiar and some utterly alien, sang a hymn that resonated through every dimension.",
            "The wind carried whispers of forgotten names, each one a key to a door that should never have been opened.",
            "Light and darkness battled for supremacy across the sky, casting the world in alternating cycles of blinding brilliance and absolute black.",
            "The earth cracked open, revealing layers of history stacked upon history, each stratum a chapter in the story of everything.",
            "From the northernmost peak to the southernmost shore, every living creature felt the same profound, inexplicable urge.",
            "The oceans rose to meet the skies, creating a world without boundaries, where sea and cloud became one.",
            "A singular point of infinite density appeared in the center of the realm, drawing everything toward it with irresistible force."
        ]
        self.abilities = [
            "Channel the primordial energies of creation to reshape the battlefield",
            "Summon forth an army of spectral warriors from the void itself",
            "Manipulate time to slow enemies and accelerate allies",
            "Absorb the life force of fallen foes to restore vitality",
            "Project beams of pure destructive energy across any distance",
            "Create impenetrable barriers of woven light and shadow",
            "Teleport across any distance through the fold of space",
            "Control the minds of lesser beings through sheer willpower",
            "Call forth storms of elemental fury from the heavens above",
            "Seal away even the most powerful of enemies in eternal stasis",
            "See through all illusions and deceptions with omniscient clarity",
            "Walk between the planes of existence without limitation",
            "Bend the laws of gravity to defy the natural order",
            "Communicate with the spirits of the dead to gain ancient wisdom",
            "Unleash a burst of pure destruction that annihilates everything within range",
            "Heal even the most grievous wounds with the power of divine grace",
            "Summon a dragon from the depths of the elemental planes",
            "Create pocket dimensions within the fold of reality",
            "Turn invisible and move through shadows like liquid darkness",
            "Forge weapons of pure starlight that cut through any armor"
        ]
        self.curses_text = [
            "For every life you save, ten shall be lost in exchange",
            "Your power grows, but your humanity diminishes with each passing day",
            "You shall never know peace, for the artifact hungers for your soul",
            "Each use of the artifact ages you tenfold, robbing you of your mortal years",
            "The artifact speaks to you in whispers that drive you to madness",
            "Those you love will suffer unspeakable fates as a consequence of your bond",
            "You can never willingly part with the artifact, for it is now a part of your flesh",
            "The curse will only be lifted when the last star in the sky burns out",
            "Every step you take leaves a trail of corruption that cannot be cleansed",
            "You have become the servant of an ancient evil older than the universe itself"
        ]
        self.blessings_text = [
            "Grants the wielder immunity to all forms of damage and corruption",
            "Bestows eternal youth and vigor upon the bearer",
            "Allows the bearer to communicate with all living and unliving things",
            "Grants the power to see all possible futures and choose the best path",
            "Makes the bearer invisible to all malevolent forces and entities",
            "Grants the ability to breathe and thrive in any environment",
            "Bestows the knowledge of every language ever spoken in any realm",
            "Allows the bearer to create anything they envision with a mere thought",
            "Grants the power to resurrect the dead with a single touch",
            "Bestows upon the bearer the loyalty and devotion of every creature in existence"
        ]
        self.origins_text = [
            "Forged in the heart of a dying star during the first moments of creation",
            "Crafted by the hands of the first civilization to ever exist, before the concept of time",
            "Born from the collision of two parallel universes, merging their essence into one",
            "Created during the war between the gods, as a weapon of ultimate destruction",
            "Discovered in the deepest abyss, where the foundations of reality are weakest",
            "Planted by a forgotten god in the center of the world, waiting for the right champion",
            "Born from the collective dreams of every sentient being across all dimensions",
            "Forged in the depths of the underworld by the original blacksmith of the gods",
            "Created as a gift from the primordial entity that exists beyond all comprehension",
            "Manifested from the tears of the first being to ever experience loss"
        ]
        self.history_templates = [
            "This artifact was created during the {adj} age of {kingdom}, when the laws of magic were still being written into existence itself. It was wielded by the legendary {character}, who used its power to {action}. For centuries it lay hidden, until {event} brought it once more into the light of day.",
            "The origins of this relic trace back to the {adj} civilization of {city}, whose masters mastered the art of {property} manipulation. They crafted this item as a {purpose}, but their hubris led to their downfall, and the artifact was lost to the ages. It was rediscovered by {character} during {event}.",
            "Forged in the {adj} fires of {mountain}, this artifact has changed hands through a bloody history of {number} owners, each meeting a tragic fate. The {creature} that guards its resting place has consumed many who sought its power, but the artifact's call is irresistible to those with the {property} bloodline.",
            "This relic emerged from the {adj} depths of {river}, where the waters have whispered its secrets to anyone willing to listen. The {kingdom} used it to {action}, but the consequences were catastrophic, leading to the {event} that reshaped the known world.",
            "Born from the union of {property} and {property}, this artifact was the centerpiece of the {adj} war between {kingdom} and {kingdom}. Its power was so great that it {action}, leaving scars on the fabric of reality that persist to this day."
        ]

    def generate_epic_phrase(self):
        return f"The {random.choice(self.adjectives)} {random.choice(self.nouns)} of {random.choice(self.adjectives)} {random.choice(self.nouns)}"

    def generate_adjective(self):
        return random.choice(self.adjectives)

    def generate_noun(self):
        return random.choice(self.nouns)

    def generate_verb(self):
        return random.choice(self.verbs)

    def generate_property(self):
        return random.choice(self.properties)

    def generate_material(self):
        return random.choice(self.materials)

    def generate_creature(self):
        return random.choice(self.creatures)

    def generate_sentence(self):
        templates = [self.sentences_a, self.sentences_b, self.sentences_c]
        return random.choice(random.choice(templates))

    def generate_another_tale(self):
        return f"Another {random.choice(self.adjectives)} tale begins in the {random.choice(self.nouns)} of {random.choice(self.adjectives)} {random.choice(self.nouns)}."

    def generate_detailed_description(self):
        parts = [
            f"This {random.choice(self.nouns)} radiates with an {random.choice(self.adjectives)} aura that {random.choice(self.verbs)} everything within its {random.choice(self.adjectives)} perimeter.",
            f"Forged from {self.generate_material()}, it hums with the {random.choice(self.adjectives)} energy of {random.choice(self.properties)}, {random.choice(self.verbs)} those who dare to approach.",
            f"The surface is covered in {random.choice(self.adjectives)} runes that {random.choice(self.verbs)} in patterns that defy all understanding and {random.choice(self.verbs)} the minds of observers.",
            f"It {random.choice(self.verbs)} with a {random.choice(self.adjectives)} light that {random.choice(self.verbs)} through {random.choice(self.adjectives)} darkness, revealing truths hidden from mortal comprehension.",
            f"Touching it {random.choice(self.verbs)} a sensation of {random.choice(self.adjectives)} power that {random.choice(self.verbs)} the wielder with the {random.choice(self.properties)} of ages past."
        ]
        return " ".join(random.sample(parts, random.randint(2, 4)))

    def generate_ability(self):
        return random.choice(self.abilities)

    def generate_curse(self):
        return random.choice(self.curses_text)

    def generate_blessing(self):
        return random.choice(self.blessings_text)

    def generate_origin(self):
        return random.choice(self.origins_text)

    def generate_history(self):
        template = random.choice(self.history_templates)
        return template.format(
            adj=random.choice(self.adjectives),
            kingdom=random.choice(["Verdania", "Thalmora", "Drakhaven", "Solmist"]),
            city=random.choice(["Ashport", "Brimwick", "Cinderfall", "Duskhollow"]),
            character=random.choice(["Aethon Stormweaver", "Zyrion Shadowborn", "Xanaris Starfall"]),
            action=random.choice(["conquered nations", "brought peace", "unleashed destruction", "ascended to godhood"]),
            event=random.choice(["the Great Convergence", "the Shattering", "the Eternal Dawn"]),
            mountain=random.choice(["Mount Aether", "Shadowspire", "Voidpeak"]),
            river=random.choice(["River of Whispers", "Silverthread", "Voidflow"]),
            property=random.choice(["Time", "Space", "Reality", "Existence"]),
            creature=random.choice(["dragon", "griffin", "phoenix"]),
            purpose=random.choice(["weapon of last resort", "seed of creation", "bridge between worlds"]),
            number=random.randint(1, 100)
        )
