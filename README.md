# SampleMind AI

SampleMind AI is a next-gen sample organizer, analyzer, and smart assistant built for producers using FL Studio on macOS. Designed with quality over quantity in mind, it helps you keep your sounds, samples, and projects in perfect structure with AI-enhanced features for importing, exporting, tagging, and smart browsing.

---

## 🔧 Features (v0.1)

- 🎛️ **Sample Organizer**: Folder structure and file renaming based on BPM, key, mood, instrument.
- 🧠 **AI Analyzer**: Uses librosa to detect tempo, key, and mood for WAV files.
- 📂 **Smart Import/Export**: Add and export samples with metadata like genre, energy, mood.
- 📦 **Sample Collections**: Group samples into themed packs or project folders.
- 🗂️ **Project Snapshot**: Save a session state with all used files, version, and notes.
- 🔍 **Instant Search**: Type-based and filterable interface to quickly find any sample.
- 🚀 **CLI Tooling**: Run SampleMind from the terminal with powerful batch commands.
- 📡 **Local Web UI** *(Coming soon)*: Interface with drag-n-drop and waveform preview.
- 🔐 **Offline First**: Fully local app—no cloud required unless enabled by user.
- 🎯 **Extensible Plugin API** *(Planned)*: Hook into FL Studio or 3rd party apps.

---

## 📁 Folder Structure
```
SampleMind/
├── src/
│   ├── analyzer/
│   ├── cli/
│   ├── core/
│   ├── data/
│   ├── utils/
│   └── main.py
├── tests/
├── docs/
│   └── ROADMAP.md
├── .github/
│   └── workflows/
│       └── python-lint.yml
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── CONTRIBUTING.md
└── start.sh
```

---

## 🚀 Getting Started

### 1. Clone repository:
```bash
git clone https://github.com/your-user/samplemind.git
cd samplemind
```

### 2. Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Run main script:
```bash
python src/main.py
```

---

## 🤝 Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md)

## 📜 License
MIT License — see [LICENSE](LICENSE)
