import re


def count_words(subtitles):
    # Remove all punctuation except apostrophes
    cleaned_text = re.sub(r'[^\w\s\']', '', subtitles)

    # Split the text into words
    words = cleaned_text.split()

    # Convert words to lowercase
    words = [word.lower() for word in words]

    # Count the occurrences of each word
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


def main():
    subtitles = "That's the password: 'PASSWORD 123'!, cried the Special Agent. So I fled."
    word_count = count_words(subtitles)

    # Output the word counts
    for word, count in word_count.items():
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
