from ui.components.base_search_bar import BaseSearchBar

class BrowseSearchBar(BaseSearchBar):
    def __init__(self):
        super().__init__(
            placeholder="Search within books..."
        )
        self.value = ""

    def on_change(self, value: str):
        self.value = value
