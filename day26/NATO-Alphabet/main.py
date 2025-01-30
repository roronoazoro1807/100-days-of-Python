import pandas

# Load the NATO phonetic alphabet data
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary {Letter: Code}
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Get user input and convert it to phonetic code
word = input("Enter a Word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]

print(output_list)
