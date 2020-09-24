from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.app import StringProperty


class DynamicLabels(App):
    message = StringProperty

    def __init__(self):
        super().__init__()
        self.names = ["asdf", "ff", "wer", "erryhj"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.names:
            temp_label = Label(text=name)
            print(name)
            self.root.ids.name_area.add_widget(temp_label)




DynamicLabels().run()
