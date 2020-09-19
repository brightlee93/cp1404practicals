from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

CONVERT_RATE = 1.60934


class ConvertMilesKiloMetres(App):
    message = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def get_value(self, value):
        miles = self.error_checking(value)
        self.convert(miles)

    def convert(self, miles):
        self.message = str(miles * CONVERT_RATE)

    def change_value(self, value, change_value):
        miles = self.error_checking(value) + change_value
        self.root.ids.input_miles.text = str(miles)
        self.convert(miles)

    def error_checking(self, value):
        try:
            if value == "":
                return 0.0
            else:
                return float(value)
        except ValueError:
            return 0.0


ConvertMilesKiloMetres().run()
