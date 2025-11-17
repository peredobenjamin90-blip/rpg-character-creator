full_dot = '●'
empty_dot = '○'
def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    stats = {"STR":strength, "INT":intelligence, "CHA":charisma}
    for stat in stats.values():
        if not isinstance(stat, int):
            return "All stats should be integers"
    for stat in stats.values():
        if stat < 1:
            return "All stats should be no less than 1"
    for stat in stats.values():
        if stat > 4:
            return "All stats should be no more than 4"
    for stat in stats.values():
        if sum(stats.values()) != 7:
            return "The character should start with 7 points"
    line_str = "STR " + (full_dot * strength) + (empty_dot * (10 - strength))
    line_int = "INT " + (full_dot * intelligence) + (empty_dot * (10 - intelligence))
    line_cha = "CHA " + (full_dot * charisma) + (empty_dot * (10 - charisma))

    return f"{name}\n{line_str}\n{line_int}\n{line_cha}"

if __name__ == "__main__":
    name = input("Enter character name: ")
    strength = int(input("Enter Strength (1–4): "))
    intelligence = int(input("Enter Intelligence (1–4): "))
    charisma = int(input("Enter Charisma (1–4): "))

    result = create_character(name, strength, intelligence, charisma)
    print("\n" + result)

#hello world
