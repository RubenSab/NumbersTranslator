from language_rules import LanguageRules

def import_rules(filename: str) -> LanguageRules:
	rules = LanguageRules()
	with open(filename, "r") as f:
		lines = [line.strip().split(" ") for line in f.readlines() if line.strip()]
		for line in lines:
			for i in range(len(line)):
				line[i] = line[i].replace("*", " ")

			# merging rules
			if len(line) == 6 and \
			(line[1], line[3], line[4]) == ("and", "merge", "into"):
				rules.merge_extremities[(line[0], line[2])] = line[5]

			# plural and singular name of hundreds
			if len(line) == 5 and \
			(line[0], line[1], line[3]) == ("hundreds", "is", "singular"):
				rules.hundreds = (line[2], line[4])

			# plural and singular name of milestones
			if len(line) == 6 and \
			(line[0], line[2], line[4]) == ("milestone", "is", "singular"):
				rules.milestones[line[1]] = (line[3], line[5])

			# name of individual numbers
			if len(line) == 3 and line[1] == "is":
				rules.numbers[line[0]] = line[2]

	return rules


def digits_to_words(number: int, rules: LanguageRules):
    triples = [""]
    for digit in str(number)[::-1]:
        if len(triples[-1]) < 3:
            triples[-1] = digit + triples[-1]
        else:
            triples.append(digit)

    translation = ""
    pos = 1
    for t in triples:
        if int(t) != 0:
            if len(t) == 1 and t[0] == "1":
                name_of_triple = f" {rules.milestones[str(pos)][1]} "
            else:
                name_of_triple = triple_to_words(t, rules)
                if pos > 1:
                    name_of_triple += f" {rules.milestones[str(pos)][0]} "
            translation = name_of_triple + translation
        pos += 3

    return translation.replace("  ", " ")


def triple_to_words(triple: str, rules: LanguageRules):
	if int(triple) == 0:
		return ""

	# only hundreds
	if len(triple) == 1:
		return rules.numbers[triple]

	# only tens and units
	if len(triple) == 2:
		if triple in rules.numbers:
			return rules.numbers[triple]
		if triple[1] != '0':
			return merge_tens_and_units(
				rules.numbers[triple[0] + '0'],
				rules.numbers[triple[1]],
				rules
			)
		else:
			return rules.numbers[triple[0] + '0']

	# hundreds, tens and units
	translation = ""
	# hundreds
	if triple[0] == '1':
		translation += rules.hundreds[1]
	elif triple[0] != '0':
		count = rules.numbers[triple[0]]
		translation += count + rules.hundreds[0]
	# tens
	if triple[1:] in rules.numbers:
		return translation + rules.numbers[triple[1:]]
	if triple[1] != '0':
		return translation + \
		merge_tens_and_units(
		    rules.numbers[triple[1] + '0'], rules.numbers[triple[2]], rules
        )
	else:
		if triple[2] != '0':
			return translation + rules.numbers[triple[2]]
		else:
			return translation



def merge_tens_and_units(word1: str, word2: str, rules: LanguageRules):
    if len(word1) == 0:
        return word2
    if len(word2) == 0:
        return word1
    if ('.', '.') in rules.merge_extremities:
        return word1 + rules.merge_extremities[('.', '.')] + word2
    extremities = (word1[-1], word2[0])
    if extremities in rules.merge_extremities:
        return word1[:-1] + rules.merge_extremities[extremities] + word2[1:]
    else:
        return word1 + word2
