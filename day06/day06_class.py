class Pokemon:
    def __init__(self, name, owner, skills):  # 객체 생성 시 동작
        self.name = name
        self.owner = owner
        self.skills = skills.split('/')
        print(f"포켓몬 {name} 생성됨")
    def info(self):
        print(f'{self.owner}의 포켓몬은 {self.name}입니다.')
        for skill in self.skills:
            print(skill)
class Pikachu(Pokemon):  # inheritance
    pass

pi1 = Pikachu('피카츄', '덴트', '번개')
pi1.info()

# p1 = Pokemon('피카츄', '한지우', '50만 볼트/100만 볼트/번개')
# p2 = Pokemon('꼬부기', '오바람', '고속 스핀/거품/몸통 박치기/하이드로펌프')
# print(p1.name)
# print(p2.name)
# print(p1, p2)
# print(f'{p1.owner}의 포켓몬은 {p1.name}입니다.')
# print(f'{p2.owner}의 포켓몬은 {p2.name}입니다.')
# p1.info()
# p2.info()
# print(p2.skills)
