import screen_brightness_control as sbc


class BrightnessController:

    def set_brightness(self, distance):

        # Limit distance
        distance = max(50, min(distance, 150))

        # Convert distance → brightness %
        brightness = int((distance - 50) / (150 - 50) * 100)

        brightness = max(0, min(brightness, 100))

        sbc.set_brightness(brightness)

        return brightness