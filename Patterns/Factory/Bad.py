"""Basic video exporting example
    """

import pathlib
from abc import ABC, abstractmethod


class VideoExporter(ABC):
    """Basic representation of video exporting codec."""

    @abstractmethod
    def prepare_export(self, video_data):
        """Prepares video data for exporting"""
        ...

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the video data to a folder."""
        ...


class LossLessVideoExporter(VideoExporter):
    """Lossless video exporting codec."""

    def prepare_export(self, video_data):
        """Prepares video data for exporting"""
        print("Preparing video data for lossless export.")
        ...

    def do_export(self, folder: pathlib.Path):
        """Exports the video data to a folder."""
        print(f"Exporting video data in lossless format to {folder}.")
        ...


class H264BPVideoExporter(VideoExporter):
    """H.264 video exporting codec with Baseline profile."""

    def prepare_export(self, video_data):
        """Prepares video data for exporting"""
        print("Preparing video data for H.264 (Baseline) export.")
        ...

    def do_export(self, folder: pathlib.Path):
        """Exports the video data to a folder."""
        print(f"Exporting video data in H.264 (Baseline) format to {folder}.")
        ...


class H264Hi422PVideoExporter(VideoExporter):
    """H.264 video exporting codec with Hi422P profile (10-bit, 4:2:2 chroma sampling)."""

    def prepare_export(self, video_data):
        """Prepares video data for exporting"""
        print("Preparing video data for H.264 (Hi422P) export.")
        ...

    def do_export(self, folder: pathlib.Path):
        """Exports the video data to a folder."""
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}.")
        ...


class AudioExporter(ABC):
    """Basic representation of audio exporting codec."""

    @abstractmethod
    def prepare_export(self, audio_data):
        """Prepares audio data for exporting"""
        ...

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the audio data to a folder."""
        ...


class AACAudioExporter(ABC):
    """AAC audio exporting codec."""

    def prepare_export(self, audio_data):
        """Prepares audio data for exporting"""
        print("Preparing audio data for AAC export.")
        ...

    def do_export(self, folder: pathlib.Path):
        """Exports the audio data to a folder."""
        print(f"Exporting audio data in AAC format to {folder}.")
        ...


class WAVAudioExporter(ABC):
    """WAV (lossless) audio exporting codec."""

    def prepare_export(self, audio_data):
        """Prepares audio data for exporting"""
        print("Preparing audio data for WAV export.")
        ...

    def do_export(self, folder: pathlib.Path):
        """Exports the audio data to a folder."""
        print(f"Exporting audio data in WAV format to {folder}.")
        ...


def main() -> None:
    """Main function."""

    # Main has too much responsibility which means that
    # it has low cohesion and tight coupling

    # read the desired export quality
    export_quality: str
    while True:
        export_quality = input(
            "Entre desired output quality (low, high, master): ")
        if export_quality in {"low", "high", "master"}:
            break
        print(f"Unknown output quality options: {export_quality}.")

    # create the video and audio exporters
    video_exporter: VideoExporter
    audio_exporter: AudioExporter
    if export_quality == "low":
        video_exporter = H264BPVideoExporter()
        audio_exporter = AACAudioExporter()
    elif export_quality == "high":
        video_exporter = H264Hi422PVideoExporter()
        audio_exporter = AACAudioExporter()
    else:
        # default master quality
        video_exporter = LossLessVideoExporter()
        audio_exporter = WAVAudioExporter()

    # prepare the export
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    # do the export
    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    main()
