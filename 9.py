num_students = int(input())

all_languages = set()
at_least_one_language = set()

for _ in range(num_students):
    num_languages = int(input())
    student_languages = set()

    for _ in range(num_languages):
        language = input()
        student_languages.add(language)

  
    if not all_languages:
        all_languages = student_languages
    else:
  
        all_languages &= student_languages

   
    at_least_one_language |= student_languages


print(len(all_languages))
for language in sorted(all_languages):
    print(language)

print(len(at_least_one_language))
for language in sorted(at_least_one_language):
    print(language)
