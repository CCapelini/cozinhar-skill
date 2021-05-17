from mycroft import MycroftSkill, intent_file_handler


class Cozinhar(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('cozinhar.intent')
    def handle_cozinhar(self, message):
        self.speak_dialog('cozinhar')


def create_skill():
    return Cozinhar()

