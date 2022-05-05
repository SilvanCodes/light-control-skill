from mycroft import MycroftSkill, intent_handler
import urllib.request

ESP_HOST = 'http://esp32.local'

POWER_ROUTE = '/power'
COLOR_ROUTE = '/color'
COLOR_ROUTE = '/party'

POWER_REQUEST = urllib.request.Request(url=f'{ESP_HOST}{POWER_ROUTE}', method='POST')
COLOR_REQUEST = urllib.request.Request(url=f'{ESP_HOST}{COLOR_ROUTE}', method='POST')
PARTY_REQUEST = urllib.request.Request(url=f'{ESP_HOST}{PARTY_ROUTE}', method='POST')

def toggle_power():
    urllib.request.urlopen(POWER_REQUEST)

def toggle_color():
    urllib.request.urlopen(COLOR_REQUEST)

def toggle_party():
    urllib.request.urlopen(PARTY_REQUEST)


class LightControl(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('control.light.on.intent')
    def handle_light_on(self, message):
        self.speak_dialog('control.light.on')
        toggle_power()

    @intent_handler('control.light.off.intent')
    def handle_light_off(self, message):
        self.speak_dialog('control.light.off')
        toggle_power()

    @intent_handler('control.light.color.intent')
    def handle_light_color(self, message):
        self.speak_dialog('control.light.color')
        toggle_color()

    @intent_handler('control.light.party.intent')
    def handle_light_color(self, message):
        self.speak_dialog('control.light.party')
        toggle_party()

def create_skill():
    return LightControl()
