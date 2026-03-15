# FraudX

A browser extension powered by a Python FastAPI backend that detects and flags fraudulent or suspicious activity in real time while you browse.

---

## Overview

FraudX is a fraud detection tool built in two parts:

- **`extension/`** — A browser extension (HTML, CSS, JavaScript) that integrates directly into your browsing experience and surfaces fraud alerts.
- **`backend/`** — A Python FastAPI server that processes requests from the extension, runs fraud detection logic, and returns results.

Together they provide real-time fraud analysis without leaving your browser.

---

## Project Structure

```
fraudx/
├── extension/           # Browser extension (HTML, CSS, JavaScript)
│   ├── manifest.json    # Extension configuration & permissions
│   ├── popup.html       # Extension UI
│   ├── popup.js         # UI logic
│   └── styles.css       # Styling
├── backend/             # Python FastAPI backend
│   ├── app.py           # Main server entry point
│   ├── model/           # Fraud detection model/logic
│   └── requirements.txt
├── .gitignore
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.9+
- Google Chrome or any Chromium-based browser
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/anikchand461/fraudx.git
cd fraudx
```

### 2. Set Up the Backend

```bash
cd backend

# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the FastAPI server
uvicorn app:app --reload
```

The backend will start on `http://localhost:8000` by default.

### 3. Load the Browser Extension

1. Open Chrome and navigate to `chrome://extensions/`
2. Enable **Developer Mode** (toggle in the top-right corner)
3. Click **Load unpacked**
4. Select the `extension/` folder from this repository

The FraudX icon will appear in your browser toolbar.

---

## Usage

1. Make sure the **backend server is running** (`uvicorn app:app --reload`)
2. Click the **FraudX extension icon** in your browser toolbar
3. The extension will analyze the current page and display a fraud risk assessment

---

## Tech Stack

| Layer | Technology |
|---|---|
| Browser Extension | HTML, CSS, JavaScript |
| Backend Server | Python, FastAPI |

---

## License

This project is licensed under the [MIT License](LICENSE).