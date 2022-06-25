import os
from dataclasses import dataclass
from typing import List
from random import uniform
import marshmallow_dataclass
import marshmallow
import json
EQUIPMENT_PATH = os.path.join(os.path.join(os.getcwd(), 'data'), 'equipment.json')

@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: 0


@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    @property
    def damage(self):
        return round(uniform(self.min_damage, self.max_damage), 1)


@dataclass
class EquipmentData:
    weapons: List[Weapon]
    armors: List[Armor]


class Equipment(EquipmentData):

    def __init__(self):
        self.equipment = self._get_equipment_data()

    def get_weapon(self, weapon_name) -> Weapon:
        for weapon in EquipmentData.weapons:
            if weapon.name == weapon_name:
                return weapon
        raise RuntimeError("Такое оружие не найдено")

    def get_armor(self, armor_name) -> Armor:
        for armor in EquipmentData.armors:
            if armor.name == armor_name:
                return armor
        raise RuntimeError("Такая броня не найдена")

    @property
    def get_weapons_names(self) -> list:
        return [item.name for item in self.weapons]

    @property
    def get_armors_names(self) -> list:
        return [item.name for item in EquipmentData.armors]

    @staticmethod
    def _get_equipment_data() -> EquipmentData:

        equipment_file = open(EQUIPMENT_PATH)
        data = json.load(equipment_file)
        equipment_schema = marshmallow_dataclass.class_schema(EquipmentData)
        try:
            return equipment_schema().load(data)
        except marshmallow.exceptions.ValidationError:
            raise ValueError


e=Equipment()

print(e.get_weapons_names)