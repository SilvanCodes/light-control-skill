from mycroft import MycroftSkill, intent_file_handler
import urllib.request

ESP_HOST = 'http://esp32.local'

POWER_ROUTE = '/power'
COLOR_ROUTE = '/color'

POWER_REQUEST = urllib.request.Request(url=f'{ESP_HOST}{POWER_ROUTE}', method='POST')
COLOR_REQUEST = urllib.request.Request(url=f'{ESP_HOST}{COLOR_ROUTE}', method='POST')

def toggle_power():
    urllib.request.urlopen(POWER_REQUEST)

def toggle_color():
    urllib.request.urlopen(COLOR_REQUEST)


class LightControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('control.light.on.intent')
    def handle_control_light(self, message):
        toggle_power()
        self.speak_dialog('control.light.on')

    @intent_file_handler('control.light.off.intent')
    def handle_control_light(self, message):
        toggle_power()
        self.speak_dialog('control.light.off')

    @intent_file_handler('control.light.color.intent')
    def handle_control_light(self, message):
        toggle_color()
        self.speak_dialog('control.light.color')

def create_skill():
    return LightControl()
