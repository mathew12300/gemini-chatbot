# Gemini-Chatbot


# 💬 Gemini Chatbot (Flask + Google GenAI)

A professional chatbot interface powered by **Gemini Pro (Google Generative AI)** and built using **Flask**. This project supports:
- 🌗 Dark/Light mode toggle with theme memory
- 🎙 Voice input via Web Speech API
- 🧠 Gemini AI model integration (text generation)
- 🎨 Stylish, responsive UI using HTML, CSS, and JavaScript

---

## 📸 Preview


![image](https://github.com/user-attachments/assets/9b55fa81-db44-4165-8218-2816c5135fd1)


---

## 🔧 Features

✅ Dark and Light Mode toggle  
✅ ChatGPT-like typing and response UI  
✅ Voice input for hands-free prompts  
✅ Responsive layout  
✅ Gemini Pro integration using `google.generativeai`

---

## 🛠️ Tech Stack

- 🐍 Python (Flask)
- 🌐 HTML, CSS, JavaScript
- 🔮 Google Generative AI (Gemini Pro)
- 🎤 Web Speech API (for voice input)

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/mathew12300/gemini-chatbot.git
cd gemini-chatbot
````

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On Linux/macOS
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Google API Key

1. Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)# your own api key
2. Open `app.py`
3. Replace:

```python
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

---

### 5. Run the App

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000)

---

## 🗂 Project Structure

```
gemini-chatbot/
├── app.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── style-light.css
├── requirements.txt
└── README.md
```

---



## 🛡 License

This project is open-source and free to use under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

Developed by **Mathew Rayan**
[GitHub](https://github.com/mathew12300)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

