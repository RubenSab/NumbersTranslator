from functions import import_rules, digits_to_words

if __name__=='__main__':
    n = int(input('insert a number: '))

    eng_rules = import_rules("languages/eng.txt")
    ita_rules = import_rules("languages/ita.txt")
    esp_rules = import_rules("languages/esp.txt")
    ron_rules = import_rules("languages/ron.txt")

    print(f"in english, {n} is {digits_to_words(n, eng_rules)}")
    print(f"in italiano, {n} è {digits_to_words(n, ita_rules)}")
    print(f"en español, {n} es {digits_to_words(n, esp_rules)}")
    print(f"în limba română, {n} este {digits_to_words(n, ron_rules)}")
