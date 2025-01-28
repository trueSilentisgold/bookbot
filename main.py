def sort_on(dict):
    return dict["num"]
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.lower()
        loweredletters = list(words)
        words = file_contents.split()
        wordscounter = len(words)
        letterscounter = {}
        sortedletters = []
        for letter in loweredletters:
            if letter in letterscounter:
                letterscounter[letter] += 1
            elif letter.isalpha():
                letterscounter[letter] = 1
        for key, value in letterscounter.items():
            sortedletters.append({"char": key,"num": value})
        sortedletters.sort(reverse=True, key=sort_on)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{wordscounter} words found in the document")
        print()

        for i in range (0, len(sortedletters)):
            print(f"The '{sortedletters[i]["char"]}' character was found {sortedletters[i]["num"]} times")
main()
