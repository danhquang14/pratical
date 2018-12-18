from kivy.app import App
from kivy.lang import Builder

class BoxLayout(App):
    def build(self):
        self.root = Builder.load_file("box_layout.kv")
        return self.root
    def clear(self):
        if self.root.ids.text_input.text =="":
            self.root.ids.label_display.text = "Enter Your Name"

        else:
            self.root.ids.text_input.text = ""
            self.root.ids.label_display.text = "Enter Your Name"

    def pressed(self):
        message = self.root.ids.text_input.text
        self.root.ids.label_display.text = "Hello {:10}".format(message)

    def text_input(self):
        print(self.root.ids.text_input.text)
BoxLayout().run()