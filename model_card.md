# Model Card: Vibe Finder

## 1. Goal and Task

Vibe Finder recommends songs from a small catalog. It ranks songs using a user's favorite genre, favorite mood, and target energy. This is a classroom simulation, not a production music service.

## 2. Data Used

The catalog contains 18 songs, including pop, lofi, rock, jazz, ambient, synthwave, country, metal, classical, hip-hop, reggae, blues, folk, and funk. Each row has a genre, mood, energy, tempo, valence, danceability, and acousticness, along with song and artist names. The current score uses only genre, mood, and energy. These sample records do not represent the full range of music or listeners.

## 3. Algorithm Summary

An exact genre match adds 1 point, and an exact mood match adds 1 point. Energy similarity adds up to 2 points: `2 * (1 - abs(song energy - target energy))`. The program adds these points, sorts songs from highest score to lowest, and returns the top five with reasons.

## 4. Observed Behavior and Biases

Changing the weights changed the rankings, but there are no listener ratings to show that the new rankings are more accurate. Energy now has twice the maximum influence of a genre or mood match, so songs with similar energy can outrank songs that better match a user's style. Exact labels do not recognize related genres or moods, and the catalog has only a few examples for most labels. If a requested mood or genre is missing, recommendations rely more heavily on energy. The system also ignores tempo, valence, danceability, acousticness, listening history, and context.

## 5. Evaluation Process

I ran the CLI for three ordinary profiles and two conflicting profiles. I checked the top-five rankings, score explanations, and edge cases. For Deep Intense Rock, Storm Runner ranks first with 3.98 points: 1 point for rock, 1 for intense, and 1.98 for energy similarity (`2 * (1 - abs(0.91 - 0.90))`). Low-Energy Intense Rock still puts Storm Runner first because its genre and mood bonuses outweigh its low energy similarity. Sad High-Energy Pop has no matching sad song, so the results favor pop songs and similar energy instead.

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

Chill Lofi
----------
1. Midnight Coding - Score: 3.96
   Reasons: genre match (+1.0), mood match (+1.0), energy similarity (+1.96)
2. Library Rain - Score: 3.90
   Reasons: genre match (+1.0), mood match (+1.0), energy similarity (+1.90)
3. Focus Flow - Score: 3.00
   Reasons: genre match (+1.0), energy similarity (+2.00)
4. Spacewalk Thoughts - Score: 2.76
   Reasons: mood match (+1.0), energy similarity (+1.76)
5. Coffee Shop Stories - Score: 1.94
   Reasons: energy similarity (+1.94)

Deep Intense Rock
-----------------
1. Storm Runner - Score: 3.98
   Reasons: genre match (+1.0), mood match (+1.0), energy similarity (+1.98)
2. Gym Hero - Score: 2.94
   Reasons: mood match (+1.0), energy similarity (+1.94)
3. Iron Horizon - Score: 1.88
   Reasons: energy similarity (+1.88)
4. Sunrise City - Score: 1.84
   Reasons: energy similarity (+1.84)
5. Neon Parade - Score: 1.82
   Reasons: energy similarity (+1.82)

Sad High-Energy Pop
-------------------
1. Gym Hero - Score: 2.94
   Reasons: genre match (+1.0), energy similarity (+1.94)
2. Sunrise City - Score: 2.84
   Reasons: genre match (+1.0), energy similarity (+1.84)
3. Storm Runner - Score: 1.98
   Reasons: energy similarity (+1.98)
4. Iron Horizon - Score: 1.88
   Reasons: energy similarity (+1.88)
5. Neon Parade - Score: 1.82
   Reasons: energy similarity (+1.82)

Low-Energy Intense Rock
-----------------------
1. Storm Runner - Score: 2.38
   Reasons: genre match (+1.0), mood match (+1.0), energy similarity (+0.38)
2. Quiet Constellations - Score: 1.76
   Reasons: energy similarity (+1.76)
3. Spacewalk Thoughts - Score: 1.64
   Reasons: energy similarity (+1.64)
4. Paper Kites - Score: 1.54
   Reasons: energy similarity (+1.54)
5. Library Rain - Score: 1.50
   Reasons: energy similarity (+1.50)
```

### Profile comparisons

- **High-Energy Pop vs. Chill Lofi:** Pop and happy songs lead in the first profile; lofi and chill songs lead in the second because genre, mood, and target energy differ.
- **High-Energy Pop vs. Deep Intense Rock:** Storm Runner leads for rock and intense matches, despite both profiles preferring high energy.
- **High-Energy Pop vs. Sad High-Energy Pop:** Removing the happy mood match changes the leader to Gym Hero, which matches pop and energy.
- **High-Energy Pop vs. Low-Energy Intense Rock:** Lower target energy brings quieter tracks into the results, though Storm Runner remains first because of its genre and mood matches.
- **Chill Lofi vs. Deep Intense Rock:** Lofi/chill matches are replaced by Storm Runner's rock/intense matches.
- **Chill Lofi vs. Sad High-Energy Pop:** Changing genre, mood, and energy shifts the list from mellow lofi to energetic pop.
- **Chill Lofi vs. Low-Energy Intense Rock:** Both target low energy, but Storm Runner leads for the rock/intense profile because of its category bonuses.
- **Deep Intense Rock vs. Sad High-Energy Pop:** The matching genres and moods change, making Gym Hero lead for pop while Storm Runner leads for rock.
- **Deep Intense Rock vs. Low-Energy Intense Rock:** The category preferences stay the same, but the low target reduces Storm Runner's energy points; its genre and mood points keep it first.
- **Sad High-Energy Pop vs. Low-Energy Intense Rock:** Different category matches and target energy produce different results; Storm Runner's two category matches outweigh its energy mismatch.

## 6. Intended and Non-Intended Use

This tool is for learning how simple scoring and ranking work. It can demonstrate how changing preferences or weights changes a ranked list. It should not be used to make claims about a person's full taste, replace a real recommendation service, or make decisions about people.

## 7. Ideas for Improvement

Add more songs and more balanced examples for each genre and mood. Use tempo, valence, danceability, and acousticness in the score. Support multiple preferences and related mood or genre matches. Test recommendations against listener feedback and add a way to increase variety.

## 8. Personal Reflection

My biggest learning moment was seeing that the weights directly shape the recommendations: doubling energy similarity changed the ranking, but did not prove the results were better. I had to double-check the AI's suggested score by calculating the genre, mood, and energy points for Storm Runner by hand. I was surprised that Storm Runner still ranked first for a low-energy rock user because its genre and mood bonuses outweighed its energy mismatch. Next, I would add more songs, use more of their attributes, and test the results with real listener feedback.
