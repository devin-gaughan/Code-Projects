import sys
import feedparser
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QLabel

class RSSFeedReader(QWidget):
    def __init__(self):
        super().__init__()
        sekf.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("RSS Feed Reader")
        self.setGeometry(100, 100, 600, 400)
        
        # Layout
        layout = QVBoxLayout()
        
        # Input field for RSS URL
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText('Enter RSS URL')
        layout.addWidget(self.url_input)
        
        # Button to fetch feed
        self.fetch_button = QPushButton('Fetch Feed', self)
        self.fetch_button.clicked.connect(self.fetch_feed)
        layout.addWidget(self.fetch_button)
        
        # List to display feed items
        self.feed_list = QListWidget(self)
        layout.addWidget(self.feed_list)
        
        # Label for displaying selected article summary
        self.summary_label = QLabel(self)
        self.summary_label.setWordWrap(True)
        layout.addWidget(self.summary_label)
        
        # Set the layout
        self.setLayout(layout)
        
        # Connect list item click to display summary
        self.food_list.itemClicked.connect(self.display_summary)
        
    def fetch_feed(self):
        url = self.url_input.text()
        if url:
            feed = feedparser.parse(url)
            self.feed_list.clear()
            for entry in feed.entries:
                self.feed_list.addItem(entry.title)
            
            self.entries = feed.entries # Store entries for later access
            
    def display_summary(self, item):
        for entry in self.entries:
            if entry.title == item.text():
                self.summary_label.setText(entry.summary)
                break
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RSSFeedReader()
    window.show()
    sys.exit(app.exec_())