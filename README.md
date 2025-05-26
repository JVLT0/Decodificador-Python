# 🔐 Hybrid Caesar Cipher Decryptor – Version 2.3

This project implements an **intelligent Caesar cipher decryptor**, combining **formal validation using Context-Free Grammar (CFG)**, **lexical validation with a dictionary**, and **semantic validation using the multilingual BERT model**. Version 2.3 brings **significant performance optimizations** while maintaining the robustness of the hybrid validation process.

> ⚠️ **Note:** The current version of this decryptor only supports texts in **Portuguese (pt-BR)**, as the CFG and dictionary are language-specific.

> 🇧🇷 [Read in Portuguese here](./README.pt-BR.md)

---

## 🚀 What's New in Version 2.3

- ⚡ Parallel processing with `ThreadPoolExecutor` to generate all 25 Caesar shifts more efficiently.
- 🎯 Pre-selection of the top 3 candidates using only CFG and dictionary before applying BERT.
- 🧠 Optimized BERT validation:
  - Analyzes only the 5 longest words in each sentence.
- 🪶 Updated scoring weights:
  - 30% CFG, 50% Dictionary, 20% BERT.

---

## 📊 Version Comparison

| Feature                          | V2.2     | V2.3     |
|----------------------------------|----------|----------|
| Parallel processing              | ❌       | ✅        |
| Pre-filtering with CFG + Dict    | ❌       | ✅        |
| Word limit in BERT validation    | ❌       | ✅ (5)    |
| Refined scoring weights          | 30/30/30 | 30/50/20 |
| Overall performance              | Low      | High     |
| Memory usage                     | High     | Optimized|

---

## 🛠️ Technologies Used

| Technology      | Purpose                                  |
|----------------|-------------------------------------------|
| Python 3.11+    | Main programming language                |
| Lark            | CFG implementation                      |
| Transformers    | Multilingual BERT model                 |
| PyTorch         | Model inference                        |
| Gradio          | Web graphical interface                |

---

## 📁 Project Structure

```
Descriptografia-Python/
├── Caesar/
│ ├── config/ # Configurations and general definitions
│ │ ├── init.py
│ │ ├── grammar.py # CFG definition
│ │ └── settings.py # Scoring weights and parameters
│ │
│ ├── core/ # Core decryption logic
│ │ ├── init.py
│ │ ├── cipher.py # Caesar shift generation
│ │ ├── validator.py # Validation (CFG, dictionary, BERT)
│ │ └── decoder.py # Main decryptor logic
│ │
│ ├── utils/ # Utility functions
│ │ ├── init.py
│ │ └── text_utils.py # Text cleaning and formatting
│ │
│ ├── interface/ # Gradio UI
│ │ ├── init.py
│ │ └── app.py
│ │
│ ├── assets/
│ │ └── portuguese_words.txt # Portuguese word list
│ │
│ └── main.py # Program entry point
│
└── README.md
```

---

## ⚙️ How It Works

1. Generates all 25 Caesar shifts in parallel.
2. Performs preliminary evaluation using CFG and dictionary.
3. Selects the top 3 preliminary candidates.
4. Applies BERT validation only to those top 3.
5. Returns the most likely decryption with explanation and score chart.

---

## 🧪 Sample Output

```
📜 Texto decifrado:
Apesar das inúmeras tentativas de estabelecer um consenso entre os diversos setores
envolvidos no projeto de revitalização urbana — que, por sua vez, apresenta uma gama de
interesses conflitantes, desde a preservação do patrimônio histórico até a promoção do
desenvolvimento econômico sustentável —, ainda persiste uma resistência significativa
por parte de determinados grupos sociais que, legitimamente, temem a descaracterização
cultural de suas comunidades e a consequente gentrificação que, historicamente, tem
acompanhado iniciativas semelhantes em outras regiões metropolitanas.

🔁 Shift identificado: 23

🔍 Componentes do score:

Estrutura (GLC): ✅ Válido
Léxico (Dicionário): 0.92
Semântica (BERT): 0.20
⭐ Score Final: 0.80
```


---

## 🚀 Installation

1. Clone the repository:
```
git clone https://github.com/JVLT0/Descriptografia-Python.git
```

2. Navigate to the directory:
```
cd Descriptografia-Python/Caesar
```

3. (Optional) Create a virtual environment:
```
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

4. Install dependencies:
```
pip install -r requirements.txt
```

5. Run the application:
```
python main.py
```


---

## 📝 Technical Notes

- The BERT model (~700MB) is automatically downloaded on the first run.
- The grammar is customizable directly in `grammar.py`.
- Scoring weights are defined in `app.py`.
- Works on CPU (GPU recommended for better performance).

---

## 📄 License

Licensed under the [MIT License](https://opensource.org/licenses/MIT).

#### Educational Note: This project bridges academic foundations (CFGs, automata) with modern NLP techniques (BERT), creating a strong link between theory and real-world application in cybersecurity.
