from mycroft import MycroftSkill, intent_file_handler


class LightControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.light.intent')
    def handle_control_light(self, message):
        self.speak_dialog('control.light')


def create_skill():
    return LightControl()

