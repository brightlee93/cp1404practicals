from prac_06.programming_language import ProgrammingLanguage

language_list = []

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print(python)

language_list.append(ruby)
language_list.append(python)
language_list.append(visual_basic)


print("The dynamically typed languages are:")
for entry in language_list:
    if entry.is_dynamic():
        print(entry.name)

