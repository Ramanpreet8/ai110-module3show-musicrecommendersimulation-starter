"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import argparse

from .recommender import load_songs, recommend_songs


def main() -> None:
    """Run recommendations for the available profiles and scoring modes."""
    parser = argparse.ArgumentParser(description="Run the music recommender simulation.")
    parser.add_argument(
        "--mode",
        choices=["all", "genre_first", "mood_first", "energy_focused"],
        default="all",
        help="Scoring strategy to use (default: compare all strategies).",
    )
    args = parser.parse_args()

    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = [
        ("High-Energy Pop", {
            "genre": "pop", "mood": "happy", "energy": 0.95,
            "target_popularity": 85, "preferred_decade": 2020,
            "preferred_mood_tags": ["euphoric", "uplifting"], "target_instrumentalness": 0.10,
        }),
        ("Chill Lofi", {
            "genre": "lofi", "mood": "chill", "energy": 0.40,
            "target_popularity": 60, "preferred_decade": 2020,
            "preferred_mood_tags": ["dreamy", "calm", "focused"], "target_instrumentalness": 0.80,
        }),
        ("Deep Intense Rock", {
            "genre": "rock", "mood": "intense", "energy": 0.90,
            "target_popularity": 75, "preferred_decade": 2010,
            "preferred_mood_tags": ["aggressive", "intense", "driving"], "target_instrumentalness": 0.05,
        }),
        ("Sad High-Energy Pop", {
            "genre": "pop", "mood": "sad", "energy": 0.90,
            "target_popularity": 80, "preferred_decade": 2020,
            "preferred_mood_tags": ["wistful", "melancholic"], "target_instrumentalness": 0.10,
        }),
        ("Low-Energy Intense Rock", {
            "genre": "rock", "mood": "intense", "energy": 0.10,
            "target_popularity": 45, "preferred_decade": 2010,
            "preferred_mood_tags": ["reflective", "dark"], "target_instrumentalness": 0.65,
        }),
    ]

    modes = (
        ["genre_first", "mood_first", "energy_focused"]
        if args.mode == "all"
        else [args.mode]
    )
    for profile_name, user_prefs in profiles:
        for mode in modes:
            recommendations = recommend_songs(user_prefs, songs, k=5, mode=mode)

            heading = f"{profile_name} - Mode: {mode}"
            print(f"\n{heading}")
            print("-" * len(heading))
            for rank, (song, score, reasons) in enumerate(recommendations, start=1):
                print(f"{rank}. {song['title']} - Score: {score:.2f}")
                print(f"   Reasons: {', '.join(reasons)}")


if __name__ == "__main__":
    main()
