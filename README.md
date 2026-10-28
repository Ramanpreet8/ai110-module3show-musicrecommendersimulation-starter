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

Real music platforms often combine collaborative filtering, which learns from listening patterns, likes, skips, and playlists from similar users, with content-based filtering, which compares a listener's preferences with song attributes. This project prioritizes a simple, explainable content-based approach: each `Song` has a genre, mood, energy, tempo, valence, danceability, and acousticness, while a `UserProfile` stores a favorite genre and mood, a target energy, and whether the user likes acoustic music. The recommender is designed to score each song for how well it matches those preferences—including rewarding energy values close to the user's target—and then rank songs by score to choose recommendations.

### Algorithm Recipe

For each song, add 2 points when its genre matches the user's favorite genre and 1 point when its mood matches the user's favorite mood. Add up to 1 energy-similarity point using `1 - abs(song.energy - user.target_energy)`; since both energy values are on a 0-to-1 scale, this gives the full point for an exact match and fewer points as the difference grows. Rank songs from highest total score to lowest, and recommend the top results. This favors genre matches over mood matches, so it may over-prioritize a user's favorite genre and under-recommend songs from other genres; the small catalog and manually assigned mood labels can also limit variety and accuracy.

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

```
Loaded songs: 18

Top recommendations
===================
1. Sunrise City - Score: 3.98
   Reasons: genre match (+2.0), mood match (+1.0), energy similarity (+0.98)
2. Gym Hero - Score: 2.87
   Reasons: genre match (+2.0), energy similarity (+0.87)
3. Rooftop Lights - Score: 1.96
   Reasons: mood match (+1.0), energy similarity (+0.96)
4. Neon Parade - Score: 0.99
   Reasons: energy similarity (+0.99)
5. Sidewalk Cypher - Score: 0.98
   Reasons: energy similarity (+0.98)
```

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
