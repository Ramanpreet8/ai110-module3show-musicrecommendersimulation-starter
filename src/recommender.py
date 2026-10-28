import csv
from dataclasses import dataclass, field
from typing import Dict, List, Tuple

@dataclass
class Song:
    """Represent a song and its musical attributes."""
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float
    popularity: int = 50
    release_decade: int = 2020
    mood_tags: List[str] = field(default_factory=list)
    explicit: int = 0
    instrumentalness: float = 0.5

@dataclass
class UserProfile:
    """Represent a user's music preferences."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool
    target_popularity: int = 50
    preferred_decade: int = 2020
    preferred_mood_tags: List[str] = field(default_factory=list)
    target_instrumentalness: float = 0.5

class Recommender:
    """Recommend songs using a user's genre, mood, and energy preferences."""

    def __init__(self, songs: List[Song]):
        """Create a recommender for the supplied song catalog."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k songs ranked by preference match."""
        if k < 0:
            raise ValueError("k must be non-negative")

        preferences = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "target_popularity": user.target_popularity,
            "preferred_decade": user.preferred_decade,
            "preferred_mood_tags": user.preferred_mood_tags,
            "target_instrumentalness": user.target_instrumentalness,
        }
        ranked_songs = sorted(
            self.songs,
            key=lambda song: score_song(preferences, song.__dict__)[0],
            reverse=True,
        )
        return ranked_songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain how a song matches the user's preferences."""
        preferences = {
            "genre": user.favorite_genre,
            "mood": user.favorite_mood,
            "energy": user.target_energy,
            "target_popularity": user.target_popularity,
            "preferred_decade": user.preferred_decade,
            "preferred_mood_tags": user.preferred_mood_tags,
            "target_instrumentalness": user.target_instrumentalness,
        }
        _, reasons = score_song(preferences, song.__dict__)
        return ", ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """Load song records from CSV and convert numeric fields."""
    integer_fields = {"id", "popularity", "release_decade", "explicit"}
    float_fields = {
        "energy",
        "tempo_bpm",
        "valence",
        "danceability",
        "acousticness",
        "instrumentalness",
    }
    list_fields = {"mood_tags"}
    songs = []

    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        for row in csv.DictReader(csv_file):
            for field in integer_fields:
                row[field] = int(row[field])
            for field in float_fields:
                row[field] = float(row[field])
            for field in list_fields:
                row[field] = [tag.strip() for tag in row[field].split("|") if tag.strip()]
            songs.append(row)

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against genre, mood, and target-energy preferences."""
    favorite_genre = user_prefs["genre"] if "genre" in user_prefs else user_prefs["favorite_genre"]
    favorite_mood = user_prefs["mood"] if "mood" in user_prefs else user_prefs["favorite_mood"]
    target_energy = user_prefs["energy"] if "energy" in user_prefs else user_prefs["target_energy"]

    score = 0.0
    reasons = []

    if song["genre"] == favorite_genre:
        score += 1.0
        reasons.append("genre match (+1.0)")
    if song["mood"] == favorite_mood:
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_similarity = 1.0 - abs(float(song["energy"]) - float(target_energy))
    energy_points = 2.0 * energy_similarity
    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    popularity_points = 0.5 * (
        1.0 - abs(song["popularity"] - user_prefs["target_popularity"]) / 100.0
    )
    score += popularity_points
    reasons.append(f"popularity close (+{popularity_points:.2f})")

    decade_points = 0.5 if song["release_decade"] == user_prefs["preferred_decade"] else 0.0
    score += decade_points
    reasons.append(f"release decade match (+{decade_points:.2f})")

    matching_tags = set(song["mood_tags"]) & set(user_prefs["preferred_mood_tags"])
    mood_tag_points = min(0.5 * len(matching_tags), 1.0)
    score += mood_tag_points
    reasons.append(f"mood tags overlap (+{mood_tag_points:.2f})")

    instrumentalness_points = 0.3 * (
        1.0 - abs(song["instrumentalness"] - user_prefs["target_instrumentalness"])
    )
    score += instrumentalness_points
    reasons.append(f"instrumentalness close (+{instrumentalness_points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, List[str]]]:
    """Return the top k songs with scores and human-readable reasons."""
    if k < 0:
        raise ValueError("k must be non-negative")

    scored_songs = [
        (song, *score_song(user_prefs, song))
        for song in songs
    ]
    return sorted(scored_songs, key=lambda recommendation: recommendation[1], reverse=True)[:k]
