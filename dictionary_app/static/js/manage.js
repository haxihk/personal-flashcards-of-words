document.addEventListener("DOMContentLoaded", () => {
    const wordList = [];

    const form = document.getElementById("manage-form");
    const wordInput = document.getElementById("word");
    const definitionInput = document.getElementById("definition");
    const wordListElement = document.getElementById("wordList");

    // بارگذاری کلمات ذخیره‌شده از Local Storage
    function loadFromLocalStorage() {
        const storedWords = JSON.parse(localStorage.getItem("wordList")) || [];
        wordList.push(...storedWords);
        displayWords();
    }

    // ذخیره‌سازی کلمات در Local Storage
    function saveToLocalStorage() {
        localStorage.setItem("wordList", JSON.stringify(wordList));
    }

    form.addEventListener("submit", (e) => {
        e.preventDefault();
        const word = wordInput.value.trim();
        const definition = definitionInput.value.trim();

        if (!word || !definition) {
            alert("لطفاً تمامی فیلدها را پر کنید.");
            return;
        }

        const existingWordIndex = wordList.findIndex((item) => item.word === word);

        if (existingWordIndex !== -1) {
            // ویرایش کلمه موجود
            wordList[existingWordIndex].definition = definition;
            alert(`معنی "${word}" به‌روزرسانی شد.`);
        } else {
            // افزودن کلمه جدید
            wordList.push({ word, definition });
            alert(`کلمه "${word}" اضافه شد.`);
        }

        saveToLocalStorage();
        displayWords();
        form.reset();
    });

    function displayWords() {
        wordListElement.innerHTML = "";

        wordList.forEach((item, index) => {
            const li = document.createElement("li");
            li.innerHTML = `
                <div>
                    <strong>${item.word}:</strong> ${item.definition}
                </div>
                <button onclick="deleteWord(${index})" class="btn btn-danger">حذف</button>
            `;
            wordListElement.appendChild(li);
        });
    }

    window.deleteWord = (index) => {
        const deletedWord = wordList[index].word;
        wordList.splice(index, 1);
        alert(`کلمه "${deletedWord}" حذف شد.`);
        saveToLocalStorage();
        displayWords();
    };

    // بارگذاری کلمات هنگام بارگذاری صفحه
    loadFromLocalStorage();
});