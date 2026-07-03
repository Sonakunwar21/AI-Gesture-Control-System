import screen_brightness_control as sbc


class BrightnessController:

    def set_brightness(self, distance):

        # Limit distance
        distance = max(30, min(distance, 250))

        # Convert distance → brightness %
        brightness = int((distance - 30) / (250 - 30) * 100)

        brightness = max(0, min(brightness, 100))

        sbc.set_brightness(brightness)

        return brightness