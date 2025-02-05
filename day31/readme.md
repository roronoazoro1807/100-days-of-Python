# Day 31 - Flash Card App (Learn French Vocabulary)

## What I Learned:

- **Working with CSV Files:** Read and modified CSV files using the `pandas` library for storing and tracking vocabulary words.

- **Tkinter UI Development:** Created an interactive flash card application with images, buttons, and timed events.

- **Data Persistence:** Implemented a system to track learned words by updating `words_to_learn.csv`, ensuring progress is saved even after closing the application.

- **Randomized Flash Cards:** Used Python’s `random.choice()` to shuffle and present new words dynamically.

- **Using Timers in Tkinter:** Implemented `after()` to automatically flip the flash card after a short delay.

## Additional Features Added

### 🃏 Flash Card System:
- Displays a French word on the front of a flash card.
- Automatically flips after 2.5 seconds to reveal the English translation.

### 🔀 Random Word Selection:
- Each session presents vocabulary randomly from `french_words.csv`.

### 📂 Progress Tracking:
- If a word is marked as **known**, it is removed from the learning list.
- The modified word list is saved in `words_to_learn.csv`, ensuring progress is retained.

### 🖼️ Visual Enhancements:
- Uses images for the flash card background (`card_front.png` and `card_back.png`).
- Buttons (`right.png` and `wrong.png`) allow users to indicate whether they have learned a word.

### ⏳ Auto Flip Mechanism:
- A timer flips the card after 2.5 seconds to reveal the English translation.

## How It Works:

1. **Start Learning:**
   - The app picks a random French word and displays it on a flash card.
   
2. **View Translation:**
   - After 2.5 seconds, the card flips to show the English meaning.

3. **Mark Words as Known or Unknown:**
   - ✅ Click the **right button** (✔️) to mark the word as **known** (it will be removed from future practice).
   - ❌ Click the **wrong button** (❌) to keep the word for future learning.

4. **Continue Learning:**
   - The app automatically loads the next word after marking one as known or unknown.



## Code Structure

- **next_card:** Displays a new French word and starts a flip timer.
- **flip_card:** Flips the flash card to show the English translation after 2.5 seconds.
- **is_known:** Removes a learned word from the list and updates `words_to_learn.csv`.
- **Data Handling:** If `words_to_learn.csv` does not exist, the app loads from `french_words.csv`.


