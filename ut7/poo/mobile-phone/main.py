class MobilePhone:
    def __init__(self, manufacturer: str, screen_size: float, num_cores: int,
                 status=True):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.status = status
        self.apps: list[str] = []

    def power_on(self):
        if not self.status:
            return self.status

    def power_off(self):
        if self.status:
            self.status = False
            return self.status

    def install_app(self, apps: list[str]):
        for app in apps:
            if app not in self.apps:
                self.apps.append(app)
        return self.apps
            
    def uninstall_app(self, apps: list[str]):
        self.app = self.app.split()
        for app in self.app:
            if app in self.app:
                return self.app.pop()
            elif self.app not in app:
                return f'No existe la app'
