class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{name} 유닉이 생성 되었습니다")
        print(f"체력 {hp}, 공격력 {1}")
    
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    
    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격 함 [공격력 {self.damage}]")

dog = AttackUnit('dog', 30, 10)
print(dog.attack('1시'))