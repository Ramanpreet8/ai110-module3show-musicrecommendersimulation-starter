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

For each song, add 1 point when its genre matches the user's favorite genre and 1 point when its mood matches the user's favorite mood. Add energy-similarity points using `2 * (1 - abs(song.energy - user.target_energy))`; with both energy values on a 0-to-1 scale, this adds up to 2 points for an exact match and decreases as the difference grows. Rank songs from highest total score to lowest, and recommend the top results. Energy now has more influence than either categorical match, so the system may over-prioritize similar energy levels; the small catalog and manually assigned mood labels can also limit variety and accuracy.

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
```text
Loaded songs: 18

High-Energy Pop
---------------
1. Sunrise City - Score: 3.74
   Reasons: genre match (+1.0), mood match (+1.0), energy similarity (+1.74)
2. Gym Hero - Score: 2.96
   Reasons: genre match (+1.0), energy similarity (+1.96)
3. Rooftop Lights - Score: 2.62
   Reasons: mood match (+1.0), energy similarity (+1.62)
4. Iron Horizon - Score: 1.98
   Reasons: energy similarity (+1.98)
5. Storm Runner - Score: 1.92
   Reasons: energy similarity (+1.92)
```
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
