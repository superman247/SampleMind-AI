import librosa
from typing import Tuple


def analyze_bpm(file_path: str) -> float:
    y, sr = librosa.load(file_path)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    return round(tempo, 2)


def analyze_key(file_path: str) -> str:
    y, sr = librosa.load(file_path)
    chroma = librosa.feature.chroma_cens(y=y, sr=sr)
    chroma_mean = chroma.mean(axis=1)
    key_index = chroma_mean.argmax()
    keys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    return keys[key_index]


def analyze_file(file_path: str) -> Tuple[float, str]:
    return analyze_bpm(file_path), analyze_key(file_path)
