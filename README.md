# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Real music platforms often combine collaborative filtering, which learns from listening patterns, likes, skips, and playlists from similar users, with content-based filtering, which compares a listener's preferences with song attributes. This project prioritizes a simple, explainable content-based approach: each `Song` also records popularity, release decade, detailed mood tags, explicit status, and instrumentalness, while each `UserProfile` can set targets for these features. The recommender scores genre, mood, energy, and these added attributes, then ranks songs by total score.

### Algorithm Recipe

Choose `genre_first`, `mood_first`, or `energy_focused` with `python -m src.main --mode <mode>`; the default `all` compares each mode. The modes weight genre, mood, and energy similarity as `(3, 1, 1)`, `(1, 3, 1)`, and `(0.5, 0.5, 3)`. Add up to 0.5 popularity points using `0.5 * (1 - abs(song.popularity - target_popularity) / 100)`, 0.5 for an exact release-decade match, 0.5 per overlapping mood tag up to 1.0, and up to 0.3 for instrumentalness closeness using `0.3 * (1 - abs(song.instrumentalness - target_instrumentalness))`. Rank songs from highest total score to lowest. These weights can favor particular features, while the small catalog and manually assigned labels limit variety and accuracy.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

```text
Loaded songs: 18

High-Energy Pop - Mode: genre_first
-----------------------------------
1. Sunrise City - Score: 7.13
   Reasons: genre match (+3.0), mood match (+1.0), energy similarity (+0.87), popularity close (+0.48), release decade match (+0.50), mood tags overlap (+1.00), instrumentalness close (+0.28)
2. Gym Hero - Score: 5.23
   Reasons: genre match (+3.0), energy similarity (+0.98), popularity close (+0.48), release decade match (+0.50), mood tags overlap (+0.00), instrumentalness close (+0.27)
3. Rooftop Lights - Score: 3.56
   Reasons: mood match (+1.0), energy similarity (+0.81), popularity close (+0.46), release decade match (+0.50), mood tags overlap (+0.50), instrumentalness close (+0.28)
4. Neon Parade - Score: 2.57
   Reasons: energy similarity (+0.86), popularity close (+0.43), release decade match (+0.50), mood tags overlap (+0.50), instrumentalness close (+0.28)
5. Iron Horizon - Score: 2.18
   Reasons: energy similarity (+0.99), popularity close (+0.42), release decade match (+0.50), mood tags overlap (+0.00), instrumentalness close (+0.27)

High-Energy Pop - Mode: mood_first
----------------------------------
1. Sunrise City - Score: 7.13
   Reasons: genre match (+1.0), mood match (+3.0), energy similarity (+0.87), popularity close (+0.48), release decade match (+0.50), mood tags overlap (+1.00), instrumentalness close (+0.28)
2. Rooftop Lights - Score: 5.56
   Reasons: mood match (+3.0), energy similarity (+0.81), popularity close (+0.46), release decade match (+0.50), mood tags overlap (+0.50), instrumentalness close (+0.28)
3. Gym Hero - Score: 3.23
   Reasons: genre match (+1.0), energy similarity (+0.98), popularity close (+0.48), release decade match (+0.50), mood tags overlap (+0.00), instrumentalness close (+0.27)
4. Neon Parade - Score: 2.57
   Reasons: energy similarity (+0.86), popularity close (+0.43), release decade match (+0.50), mood tags overlap (+0.50), instrumentalness close (+0.28)
5. Iron Horizon - Score: 2.18
   Reasons: energy similarity (+0.99), popularity close (+0.42), release decade match (+0.50), mood tags overlap (+0.00), instrumentalness close (+0.27)

High-Energy Pop - Mode: energy_focused
--------------------------------------
1. Sunrise City - Score: 5.87
   Reasons: genre match (+0.5), mood match (+0.5), energy similarity (+2.61), popularity close (+0.48), release decade match (+0.50), mood tags overlap (+1.00), instrumentalness close (+0.28)
2. Gym Hero - Score: 4.70
   Reasons: genre match (+0.5), energy similarity (+2.94), popularity close (+0.48), release decade match (+0.50), mood tags overlap (+0.00), instrumentalness close (+0.27)
3. Rooftop Lights - Score: 4.68
   Reasons: mood match (+0.5), energy similarity (+2.43), popularity close (+0.46), release decade match (+0.50), mood tags overlap (+0.50), instrumentalness close (+0.28)
4. Neon Parade - Score: 4.29
   Reasons: energy similarity (+2.58), popularity close (+0.43), release decade match (+0.50), mood tags overlap (+0.50), instrumentalness close (+0.28)
5. Iron Horizon - Score: 4.16
   Reasons: energy similarity (+2.97), popularity close (+0.42), release decade match (+0.50), mood tags overlap (+0.00), instrumentalness close (+0.27)

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this
