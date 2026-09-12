import random
from generators.names import NameGenerator
from generators.descriptions import DescriptionGenerator
from generators.loot import LootGenerator

class InventorySystem:
    def __init__(self):
        self.name_gen = NameGenerator()
        self.desc_gen = DescriptionGenerator()
        self.loot_gen = LootGenerator()
        self.slot_types = ["Head", "Chest", "Legs", "Feet", "Hands", "Finger", "Neck", "Back",
            "Main Hand", "Off Hand", "Waist", "Wrist", "Eye", "Ear", "Soul"]
        self.inventory_categories = ["Weapons", "Armor", "Accessories", "Consumables", "Materials",
            "Quest Items", "Miscellaneous", "Magical Items", "Rare Finds", "Unknown"]

    def generate_inventory_report(self):
        lines = []
        total_items = random.randint(50, 500)
        lines.append(f"\n{'='*60}")
        lines.append(f"INVENTORY REPORT - {total_items} ITEMS")
        lines.append(f"{'='*60}")
        for cat in self.inventory_categories:
            items_in_cat = random.randint(0, 50)
            if items_in_cat > 0:
                lines.append(f"\n{cat.upper()} ({items_in_cat} items):")
                for i in range(items_in_cat):
                    item = self.loot_gen.generate_item(random.randint(1, 99999))
                    lines.append(f"  [{item['color']}] {item['name']} (Level {item['level']}, {item['rarity']})")
                    lines.append(f"    Value: {item['value']} gold | Weight: {item['weight']} lbs")
                    lines.append(f"    {item['description'][:100]}...")
        lines.append(f"\n{'='*60}")
        lines.append(f"Total Gold: {random.randint(0, 1000000)} | Total Weight: {random.uniform(50, 5000):.1f} lbs")
        lines.append(f"{'='*60}\n")
        return lines
