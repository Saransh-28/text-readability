# count total number of syllables in the paragraph
def count_syllables(words):
    count = 0
    for word in words:
        word_count = count_syllables_in_word(word)
        count = count + word_count
    return count
def count_syllables_in_word(word):
    count = 0
    endings = '.,;!?:'
    last_char = word[-1]
    if last_char in endings:
        new_word = word[0:-1]
    else:
        new_word = word
    if len(new_word) <= 3:
        return 1
    if new_word[-1] in 'eE':
        new_word = new_word[0:-1]
    vowels = "aeiouAEIOU"
    prev_vowel = False
    for char in new_word:
        if char in vowels:
            if not prev_vowel:
                count = count + 1
                prev_vowel = True
        else:
            prev_vowel = False
        if new_word[-1] in 'yY':
            count = count + 1
        return count

# count total numeber of sentences
def count_sentences(text):
    count = 0
    ends = '.;?!'
    for char in text:
        if char in ends:
            count = count + 1
    return count

# output the result as per the scored
def output_results(score):
    if score >= 90:
        print('Reading level - 5th Grade')
    elif score >= 80:
        print('Reading level - 6th Grade')
    elif score >= 70:
        print('Reading level - 7th Grade')
    elif score >= 60:
        print('Reading level - 8-9th Grade')
    elif score >= 50:
        print('Reading level - 10-12th Grade')
    elif score >= 30:
        print('Reading level - College Student')
    else:
        print('Reading level - College Graduate')

# computer the readability using the formula
def compute_readability(text):
    words = text.split()
    total_words = len(words)
    total_sentences = count_sentences(text)
    total_syllables = count_syllables(words)
    score = (206.835 - 1.015 * (total_words / total_sentences)- 84.6 * (total_syllables / total_words))
    output_results(score)

text = 'Generating random paragraphs can be an excellent way for writers to get their creative flow going at the beginning of the day. The writer has no idea what topic the random paragraph will be about when it appears. This forces the writer to use creativity to complete one of three common writing challenges. The writer can use the paragraph as the first one of a short story and build upon it. A second option is to use the random paragraph somewhere in a short story they create. The third option is to have the random paragraph be the ending paragraph in a short story. No matter which of these challenges is undertaken, the writer is forced to use creativity to incorporate the paragraph into their writing.'

compute_readability(text)

