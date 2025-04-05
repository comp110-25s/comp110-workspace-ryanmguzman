"""File to define River class."""

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    day: int
    bears: list[Bear] = []
    fish: list[Fish] = []

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        new_fish = []
        i = 0
        while i < len(self.fish):
            if self.fish[i].age <= 3:
                new_fish.append(self.fish[i])
            i += 1
        self.fish = new_fish

        new_bears = []
        j = 0
        while j < len(self.bears):
            if self.bears[j].age <= 5:
                new_bears.append(self.bears[j])
            j += 1
        self.bears = new_bears

    def bears_eating(self):
        i = 0
        while i < len(self.bears):
            if len(self.bears) >= 5:
                self.bears[i].eat(3)
                self.remove_fish(3)
            i += 1

    def check_hunger(self):
        surviving_bears = []
        i = 0
        while i < len(self.bears):
            if self.bears[i].hunger_score >= 0:
                surviving_bears.append(self.bears[i])
            i += 1
        self.bears = surviving_bears

    def repopulate_fish(self):
        fish_pairs = len(self.fish) // 2
        fish_total = fish_pairs * 4
        while fish_total > 0:
            self.fish.append(Fish())
            fish_total -= 1

    def repopulate_bears(self):
        bear_pairs = len(self.bears) // 2
        while bear_pairs > 0:
            self.bears.append(Bear())
            bear_pairs -= 1

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish Population: {len(self.fish)}")
        print(f"Bear Population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        i = 0
        while i < 7:
            self.one_river_day()
            i += 1

    def remove_fish(self, amount: int):
        i = 0
        while i < amount and len(self.fish) > 0:
            self.fish.pop(0)
        i += 1
