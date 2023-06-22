class Pizza:
    def __init__(self, type, price):
        self.type = type
        self.price = price
        self.extras = []

    def get_description(self):
        description = self.type
        extras_description = ""
        for extra in self.extras:
            if extras_description == "":
                extras_description += f" with extra {extra}"
            else:
                extras_description += f", {extra}"
        description += extras_description
        return description

    def add_extra(self, extra, extra_price):
        if extra not in self.extras:
            self.extras.append(extra)
            self.price += extra_price
