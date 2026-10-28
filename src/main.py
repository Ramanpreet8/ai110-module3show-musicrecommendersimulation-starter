"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    profiles = [
        ("High-Energy Pop", {"genre": "pop", "mood": "happy", "energy": 0.95}),
        ("Chill Lofi", {"genre": "lofi", "mood": "chill", "energy": 0.40}),
        ("Deep Intense Rock", {"genre": "rock", "mood": "intense", "energy": 0.90}),
        ("Sad High-Energy Pop", {"genre": "pop", "mood": "sad", "energy": 0.90}),
        ("Low-Energy Intense Rock", {"genre": "rock", "mood": "intense", "energy": 0.10}),
    ]

    for profile_name, user_prefs in profiles:
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n{profile_name}")
        print("-" * len(profile_name))
        for rank, (song, score, reasons) in enumerate(recommendations, start=1):
            print(f"{rank}. {song['title']} - Score: {score:.2f}")
            print(f"   Reasons: {', '.join(reasons)}")


if __name__ == "__main__":
    main()
