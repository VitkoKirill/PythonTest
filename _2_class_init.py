# задани
# Скопируйте код из предыдущего урока.
# Имплементируйте следующий функционал:
# 1. После убийства персонажа, уровень того, кто убил, повышается на 1.
# 2. Максимальный уровень персонажа - 3.
# 3. При повышении уровня персонажа, происходит отхил, и персонажу прибавляется половина от максимального количества хп.
# 4. Уровень должен повышаться в функции fight
# После имплементации, и запуска функции fight, при вызове должно вывестись:
# Ork is alive Ork (level: 2, hp: 140)
# Elf is dead Elf (level: 1, hp: -4)

# решение (классы очень вариативны, ваше решение может отличаться))

class Character:

    max_level = 3

    def __init__(self, *, level: int) -> None:
        self.level = level
        self.health_points = self.base_health_points * level
        self.attack_power = self.base_attack_power * level

    @property
    def max_health_points(self) -> int:
        return self.level * self.health_points

    def heal(self) -> None:
        self.health_points += self.max_health_points/2

    def attack(self, *, target: "Character") -> None:
        print(
            f"{self.character_name} attacks {target.character_name} ({target.health_points} health_points)"
            f"with {self.attack_power} power"
        )
        target.health_points -= self.attack_power
        print(f"After attack {target.character_name} hp has {target.health_points}")

    def is_alive(self) -> bool:
        return self.health_points > 0

    def __str__(self) -> str:
        if self.is_alive():
            return f"{self.character_name} is alive {self.character_name} (level: {self.level}, hp: {self.health_points})"
        else:
            return f"{self.character_name} is dead {self.character_name} (level: {self.level}, hp: {self.health_points})"

    def level_up(self) -> None:
        if self.level <= self.max_level:
            self.level += 1


class Ork(Character):
    base_health_points = 100
    base_attack_power = 10
    character_name = "Ork"


class Elf(Character):
    base_health_points = 50
    base_attack_power = 15
    character_name = "Elf"

def fight(*, character_1: Character, character_2: Character) -> None:
    while character_1.is_alive() and character_2.is_alive():
        character_1.attack(target=character_2)
        if character_2.is_alive():
            character_2.attack(target=character_1)

    print(character_1)
    print(character_2)

    if character_1.is_alive():
        character_1.level_up()
        character_1.heal()
    else:
        character_2.level_up()
        character_2.heal()

    print(character_1)
    print(character_2)

ork = Ork(level=1)
elf = Elf(level=2)

fight(character_1=ork, character_2=elf)