from ctypes import cast, POINTER

from comtypes import CLSCTX_ALL

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


class VolumeController:

    def __init__(self):

        devices = AudioUtilities.GetSpeakers()

        interface = devices.Activate(
            IAudioEndpointVolume._iid_,
            CLSCTX_ALL,
            None
        )

        self.volume = cast(
            interface,
            POINTER(IAudioEndpointVolume)
        )

        self.min_volume, self.max_volume, _ = self.volume.GetVolumeRange()

    def set_volume(self, distance):

        # Clamp distance
        distance = max(50, min(distance, 150))

        # Convert distance to volume level
        volume_level = self.min_volume + (
            (distance - 50) / (150 - 50)
        ) * (self.max_volume - self.min_volume)

        self.volume.SetMasterVolumeLevel(volume_level, None)

        # Return percentage
        percentage = int(((distance - 50) / (150 - 50)) * 100)

        percentage = max(0, min(percentage, 100))

        return percentage