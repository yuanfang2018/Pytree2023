import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
import openai

openai.api_key = "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"

class ChatGPTWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChatGPT Demo")
        self.layout = QVBoxLayout()
        self.input_box = QLineEdit()
        self.output_box = QLabel()
        self.button = QPushButton("Ask")

        self.layout.addWidget(self.input_box)
        self.layout.addWidget(self.output_box)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.on_click)

    def on_click(self):
        input_text = self.input_box.text()
        print("input_text:"+input_text)
        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            prompt = input_text,
            temperature=0,
            max_tokens=2048
        )
        print(response)
        output_text = response.choices[0].text
        #output_text = output_text.encode('utf-8')
        self.output_box.setText(output_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = ChatGPTWidget()
    widget.show()
    sys.exit(app.exec_())
