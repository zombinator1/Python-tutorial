from typing import Protocol


class FilmPlayer(Protocol):
    # Protocol members
    name: str
    audio: str
    video: str

    def play_audio(self) -> str: ...

    def play_video(self) -> str: ...


class MP4:
    def __init__(self, name: str, audio: str, video: str) -> None:
        self.name = name
        self.audio = audio
        self.video = video

    def play_audio(self) -> str:
        return self.audio

    def play_video(self) -> str:
        return self.video

    def play_video2(self) -> str:
        return self.video


def play_film(film: FilmPlayer):
    print("START film: " + film.name)
    print("Audio: " + film.play_audio())
    print("Video: " + film.play_video())
    print("END")


fightClub = MP4("Fight Club", "uuuuu uuu u", "90minutes video")

play_film(fightClub)


class MP3:
    def __init__(self, name: str, audio: str) -> None:
        self.name = name
        self.audio = audio

    def play_audio(self) -> str:
        return self.audio


whereIsMyMind = MP3("Pixies where is my mind", "uuuu uuuu u")


class AudioPlayer(Protocol):
    # Protocol members
    name: str
    audio: str

    def play_audio(self) -> str:
        ...


def play_music(content: AudioPlayer):
    print("START music from: " + content.name)
    print("Audio: " + content.play_audio())
    print("END")


play_music(whereIsMyMind)
play_music(fightClub)
