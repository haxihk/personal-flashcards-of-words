# Personal Flashcards of Words

![License](https://img.shields.io/github/license/haxihk/personal-flashcards-of-words)
![Last Commit](https://img.shields.io/github/last-commit/haxihk/personal-flashcards-of-words)
![Issues](https://img.shields.io/github/issues/haxihk/personal-flashcards-of-words)

A customizable, web-based flashcard application to help you efficiently learn and review vocabulary. Built with Python (Flask), HTML, CSS, and JavaScript.

---

## 🚀 Demo

![Demo Screenshot](demo_screenshot.png)

<!-- Uncomment and add your live demo link if available
[Live Demo](https://your-demo-link.com)
-->

---

## ✨ Features

- ✏️ **Create Flashcards**: Add your own words, definitions, examples, or translations.
- 🗂️ **Categorization**: Organize flashcards into decks for focused study.
- 🔄 **Interactive Learning**: Flip cards, mark as known/unknown, and track progress.
- 📱 **Responsive Design**: Works on desktops, tablets, and phones.
- 💾 **Persistent Storage**: Flashcards and progress are saved locally.

---

## 🛠️ Getting Started

### Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/haxihk/personal-flashcards-of-words.git
    cd personal-flashcards-of-words
    ```

2. **(Optional) Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```bash
    python app.py
    ```
    The app will be accessible at [http://localhost:5000](http://localhost:5000).

#### 🐛 Troubleshooting

- If you encounter issues with pip, ensure pip is updated: `pip install --upgrade pip`
- On Windows, if virtual environment activation fails, try:  
  `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`

---


---

## ⚙️ Technologies Used

- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS, JavaScript
- **Storage:** Local file system or browser local storage

---

## 🚦 Quick Start

1. Launch the application (`python app.py`).
2. Open [http://localhost:5000](http://localhost:5000) in your browser.
3. Add new flashcards or import a set.
4. Review flashcards using the interactive interface.
5. Organize words into thematic decks as desired.
6. Track your progress and revisit challenging cards.

---

## 🎨 Customization

You can modify the CSS and HTML in the `static/` and `templates/` folders to personalize the look and feel. The Python backend can be extended to support additional features such as spaced repetition, export/import, or user authentication.

---

## 🤝 Contributing

Contributions are welcome! To get started:

1. **Fork** the repository.
2. **Clone** your fork:
    ```bash
    git clone https://github.com/your-username/personal-flashcards-of-words.git
    ```
3. **Create a new branch** for your feature or fix:
    ```bash
    git checkout -b feature-name
    ```
4. **Commit** your changes:
    ```bash
    git commit -m "Describe your changes"
    ```
5. **Push** to your fork and open a Pull Request.

Please open an issue first for major changes.

---

## ❓ FAQ

**Q: Can I import/export flashcards?**  
A: Not yet, but this is a planned feature!

**Q: Where is my data stored?**  
A: Flashcards and progress are saved locally on your device (either in the file system or browser local storage).

**Q: Can I use this app without Python knowledge?**  
A: Yes! Follow the "Getting Started" instructions above.

**Q: How do I customize the appearance?**  
A: Edit the files in `static/` for CSS and JS, and `templates/` for HTML.

---

## 📝 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more information.

---

## 🙏 Acknowledgements

- Inspired by classic flashcard learning techniques.
- Thanks to the open-source community for libraries and tools.

---

*Happy Learning!*


