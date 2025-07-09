import file_operations
import os
from faker import Faker
import random
import shutil


LETTERS_MAPPING = {
        'а': 'а͠',
        'б': 'б̋',
        'в': 'в͒͠',
        'г': 'г͒͠',
        'д': 'д̋',
        'е': 'е͠',
        'ё': 'ё͒͠',
        'ж': 'ж͒',
        'з': 'з̋̋͠',
        'и': 'и',
        'й': 'й͒͠',
        'к': 'к̋̋',
        'л': 'л̋͠',
        'м': 'м͒͠',
        'н': 'н͒',
        'о': 'о̋',
        'п': 'п̋͠',
        'р': 'р̋͠',
        'с': 'с͒',
        'т': 'т͒',
        'у': 'у͒͠',
        'ф': 'ф̋̋͠',
        'х': 'х͒͠',
        'ц': 'ц̋',
        'ч': 'ч̋͠',
        'ш': 'ш͒͠',
        'щ': 'щ̋',
        'ъ': 'ъ̋͠',
        'ы': 'ы̋͠',
        'ь': 'ь̋',
        'э': 'э͒͠͠',
        'ю': 'ю̋͠',
        'я': 'я̋',
        'А': 'А͠',
        'Б': 'Б̋',
        'В': 'В͒͠',
        'Г': 'Г͒͠',
        'Д': 'Д̋',
        'Е': 'Е',
        'Ё': 'Ё͒͠',
        'Ж': 'Ж͒',
        'З': 'З̋̋͠',
        'И': 'И',
        'Й': 'Й͒͠',
        'К': 'К̋̋',
        'Л': 'Л̋͠',
        'М': 'М͒͠',
        'Н': 'Н͒',
        'О': 'О̋',
        'П': 'П̋͠',
        'Р': 'Р̋͠',
        'С': 'С͒',
        'Т': 'Т͒',
        'У': 'У͒͠',
        'Ф': 'Ф̋̋͠',
        'Х': 'Х͒͠',
        'Ц': 'Ц̋',
        'Ч': 'Ч̋͠',
        'Ш': 'Ш͒͠',
        'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠',
        'Ы': 'Ы̋͠',
        'Ь': 'Ь̋',
        'Э': 'Э͒͠͠',
        'Ю': 'Ю̋͠',
        'Я': 'Я̋',
        ' ': ' '}
NUMBER_PEOPLE = int(input("сколько надо карточек "))

def create_character():
    fake = Faker("ru_RU")
    skills = ["удар кувалдой",
              "раскалённый метал"
              "выквока мечей",
              "Стремительный прыжок",
              "Электрический выстрел",
              "Ледяной удар",
              "Стремительный удар",
              "Кислотный взгляд",
              "Тайный побег",
              "Огненный заряд",
              "Ледяной выстрел", ]
    if not os.path.exists("characters"):
        pass
    else:
        shutil.rmtree("characters")
    os.mkdir("characters")
    for skill_number in range(len(skills)):
        skills[skill_number] = "".join(LETTERS_MAPPING.get(letter) for letter in skills[skill_number])
    for i in range(NUMBER_PEOPLE):
        skills_three = random.sample(skills, 3)
        context = {
            "first_name": (fake.first_name()),
            "last_name": (fake.last_name()),
            "job": (fake.job()),
            "town": (fake.city()),
            "strength": (random.randint(3, 18)),
            "agility": (random.randint(3, 18)),
            "endurance": (random.randint(3, 18)),
            "intelligence": (random.randint(3, 18)),
            "luck": (random.randint(3, 18)),
            "skill_1": skills_three[0],
            "skill_2": skills_three[1],
            "skill_3": skills_three[2]
        }
        file_operations.render_template("charsheet.svg", f"characters/result{i + 1}.svg", context)


def main():
    create_character()


if __name__ == "__main__":
    main()
