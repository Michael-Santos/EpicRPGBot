class EpicRpg:
    def __init__(self, config, browser):
        print("Starting EpicRPG")
        self._config = config
        self._browser = browser
        self._login()


    def _login(self):
        self._browser.login()
        self._browser.go_to_channel()


    # Xp farm
    def adventure(self):
        self._browser.send_chat_command("rpg adventure")


    def hunt(self):
        self._browser.send_chat_command("rpg hunt")


    def heal(self):
        self._browser.send_chat_command("rpg heal")


    # Resources farm
    def chop(self):
        self._browser.send_chat_command("rpg chop")


    def fish(self):
        self._browser.send_chat_command("rpg fish")


    # Recorrency
    def daily(self):
        self._browser.send_chat_command("rpg daily")


    def weekly(self):
        self._browser.send_chat_command("rpg weekly")
    

    def vote(self):
        self._browser.go_to_vote()
        self._browser.vote()
        self._browser.go_to_channel()


    def profile(self):
        self._browser.send_chat_command("rpg profile")

