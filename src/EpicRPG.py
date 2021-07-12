class EpicRpg:
    def __init__(self, config, browser):
        self._config = config
        self._browser = browser
        self._login()

    def _login(self):
        self._browser.login()
        self._browser.go_to_channel()

    # Xp farm
    def adventure(self):
        self._browser("rpg adventure")

    def hunt(self):
        self._browser("rpg hunt")

    def heal(self):
        self._browser("rpg heal")

    # Resources farm
    def chop(self):
        self._browser("rpg chop")

    def fish(self):
        self._browser("rpg fish")

    # Recorrency
    def daily(self):
        self._browser("rpg daily")

    def weekly(self):
        self._browser("rpg weekly")
    
    def vote(self):
        self._browser.go_to_vote()
        self._browser.vote()
        self._browser.go_to_channel()
        pass