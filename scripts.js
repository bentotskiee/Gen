// Toggle Dark Mode
document.getElementById('darkModeToggle').addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    const container = document.querySelector('.container');
    if (container) {
        container.classList.toggle('dark-mode');
    }
    const isDarkMode = document.body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDarkMode ? 'enabled' : 'disabled');
});

// Apply Dark Mode from Local Storage
if (localStorage.getItem('darkMode') === 'enabled') {
    document.body.classList.add('dark-mode');
    const container = document.querySelector('.container');
    if (container) {
        container.classList.add('dark-mode');
    }
}

// Translate Gen Z Word
async function translateWord() {
    const wordInput = document.getElementById('wordInput')?.value.trim();
    const language = document.getElementById('languageSelect')?.value;
    const output = document.getElementById('translationOutput');
    const spinner = document.getElementById('loadingSpinner');
    const audioBtn = document.getElementById('playAudio');
    const suggestionContainer = document.getElementById('suggestionContainer');
    const suggestedWord = document.getElementById('suggestedWord');

    // Ensure elements exist before proceeding
    if (!output || !spinner || !audioBtn || !suggestionContainer || !suggestedWord) {
        console.error("Some DOM elements are missing. Check your HTML structure.");
        return;
    }

    output.style.display = "none";
    audioBtn.style.display = "none";

    if (!wordInput) {
        output.textContent = "Please enter a Gen Z word.";
        output.style.display = "block";
        return;
    }

    spinner.style.display = "block";

    try {
        const response = await fetch('/translate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ word: wordInput, language }),
        });

        const data = await response.json();
        spinner.style.display = "none";

        if (response.ok) {
            output.textContent = `Translation: ${data.translation}`;
            output.style.display = "block";

            // Save to History
            saveToHistory(wordInput, data.translation, language);

            // Display suggestion if available
            if (data.suggestion) {
                suggestionContainer.style.display = "block";
                suggestedWord.textContent = data.suggestion;
                suggestedWord.onclick = () => {
                    document.getElementById("wordInput").value = data.suggestion;
                };
            } else {
                suggestionContainer.style.display = "none";
            }

            if (data.audio_url) {
                audioBtn.style.display = "block";
                audioBtn.setAttribute('data-audio-url', data.audio_url);
            }
        } else {
            output.textContent = "Translation not found.";
            output.style.display = "block";
        }
    } catch (error) {
        spinner.style.display = "none";
        console.error("Error during translation:", error);
        output.textContent = "An error occurred. Please try again.";
        output.style.display = "block";
    }
}

// Play Audio
document.getElementById('playAudio').addEventListener('click', (e) => {
    const audioUrl = e.target.getAttribute('data-audio-url');
    if (audioUrl) {
        const audio = new Audio(audioUrl);
        audio.playbackRate = 1.7; // Set playback speed to 1.7x (adjust as needed)
        audio.play().catch(err => console.error("Audio playback error:", err));
    }
});

// Save Translation to History
function saveToHistory(word, translation, language) {
    const historyList = document.getElementById('translationHistory');
    if (!historyList) {
        console.error("Translation history container is missing.");
        return;
    }

    const historyItem = document.createElement('li');
    historyItem.className = 'list-group-item';
    historyItem.innerHTML = `<strong>${word}</strong> ➡️ ${translation} <span class="text-muted">[${language === 'en' ? 'English' : 'Tagalog'}]</span>`;
    historyList.prepend(historyItem);

    // Save to LocalStorage
    const history = JSON.parse(localStorage.getItem('translationHistory')) || [];
    history.unshift({ word, translation, language });
    localStorage.setItem('translationHistory', JSON.stringify(history));
}

// Load Translation History
function loadHistory() {
    const historyList = document.getElementById('translationHistory');
    if (!historyList) {
        console.error("Translation history container is missing.");
        return;
    }

    const history = JSON.parse(localStorage.getItem('translationHistory')) || [];
    history.forEach(({ word, translation, language }) => {
        const historyItem = document.createElement('li');
        historyItem.className = 'list-group-item';
        historyItem.innerHTML = `<strong>${word}</strong> ➡️ ${translation} <span class="text-muted">[${language === 'en' ? 'English' : 'Tagalog'}]</span>`;
        historyList.appendChild(historyItem);
    });
}

// Clear Button
document.getElementById('clearBtn').addEventListener('click', () => {
    const wordInput = document.getElementById('wordInput');
    const translationOutput = document.getElementById('translationOutput');
    const playAudio = document.getElementById('playAudio');
    const suggestionContainer = document.getElementById('suggestionContainer');
    const historyList = document.getElementById('translationHistory');

    if (wordInput) wordInput.value = '';
    if (translationOutput) translationOutput.style.display = "none";
    if (playAudio) playAudio.style.display = "none";
    if (suggestionContainer) suggestionContainer.style.display = "none";

    if (historyList) {
        while (historyList.firstChild) {
            historyList.removeChild(historyList.firstChild);
        }
    }

    localStorage.removeItem('translationHistory');
});

// Event Listeners
document.getElementById('translateBtn')?.addEventListener('click', translateWord);
document.addEventListener('DOMContentLoaded', loadHistory);
