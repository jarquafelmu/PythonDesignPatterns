"""Factory Pattern: Separate creation from use"""

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


class ExporterFactory(ABC):
    """
    Factory that represents a combination of video and audio codecs.
    The factor is not an owner of the things it can create it keeps 
    no reference to them
    """

    @abstractmethod
    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter instance."""
        ...

    @abstractmethod
    def get_audio_exporter(self) -> AudioExporter:
        """Returns a new audio exporter instance."""
        ...


class FastExporter(ExporterFactory):
    """Factory aimed at providing high speed, lower quality export."""

    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter instance."""
        return H264BPVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        """Returns a new audio exporter instance."""
        return AACAudioExporter()


class HighQualityExporter(ExporterFactory):
    """Factory aimed at providing slower speed, high quality export."""

    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter instance."""
        return H264Hi422PVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        """Returns a new audio exporter instance."""
        return AACAudioExporter()


class MasterQualityExporter(ExporterFactory):
    """Factory aimed at providing low speed, master quality export."""

    def get_video_exporter(self) -> VideoExporter:
        """Returns a new video exporter instance."""
        return LossLessVideoExporter()

    def get_audio_exporter(self) -> AudioExporter:
        """Returns a new audio exporter instance."""
        return WAVAudioExporter()


def read_exporter() -> ExporterFactory:
    """Constructs an exporter factory based on the user's preference"""
    factories = {
        "low": FastExporter(),
        "high": HighQualityExporter(),
        "master": MasterQualityExporter()
    }
    # read the desired export quality
    while True:
        export_quality = input(
            "Entre desired output quality (low, high, master): ")
        if export_quality in factories:
            return factories[export_quality]
        print(f"Unknown output quality options: {export_quality}.")


def main() -> None:
    """Main function."""

    # increase cohesion by spinning off responsibilities to other functions or classes
    # less coupling because main no longer has to know about the various exporters

    fac = read_exporter()

    # retreive the video and audio exporters
    video_exporter = fac.get_video_exporter()
    audio_exporter = fac.get_audio_exporter()

    # prepare the export
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    # do the export
    folder = pathlib.Path("/usr/tmp/video")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    main()
