# 🔐 Descriptografia de Cifras Clássicas com IA
Este projeto é uma ferramenta de descriptografia de textos cifrados, suportando múltiplas cifras clássicas: César, Atbash e Vigenère. Utiliza técnicas de Gramática Livre de Contexto (GLC) e Processamento de Linguagem Natural (NLP) para validar e identificar automaticamente textos plausíveis em português. A interface gráfica é construída com Gradio, permitindo uma interação simples e intuitiva.

## 📁 Estrutura do Projeto

```
Crypto/
├── core/
│   ├── __init__.py
│   ├── parser.py       # GLC e validação com spaCy
│   └── utils.py        # Pré-processamento de texto
├── ciphers/
│   ├── __init__.py
│   ├── caesar.py       # Cifra de César
│   ├── atbash.py       # Cifra de Atbash
│   └── vigenere.py     # Cifra de Vigenère
├── interface/
│   ├── __init__.py
│   └── gradio_ui.py    # Interface Gradio
├── requirements.txt
└── README.md
```

---

## 🧠 Funcionalidades
Descriptografia automática para as cifras de César, Atbash e Vigenère.

- Validação de texto utilizando:
- GLC com a biblioteca Lark para verificar a estrutura gramatical.
- NLP com spaCy para identificar palavras válidas em português.
- Interface gráfica interativa com Gradio.
- Modularização do código para facilitar manutenção e expansão.

## 🚀 Tecnologias Utilizadas
1. Python 3.11
2. Lark – Parsing de gramáticas.
3. spaCy – Processamento de linguagem natural.
4. Gradio – Interface gráfica para aplicações de ML.

## ⚙️ Instalação
Clone o repositório:

```
git clone https://github.com/JVLT0/Descriptografia-Python.git
cd Descriptografia-Python
```

- Crie um ambiente virtual (opcional, mas recomendado):

```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### Instale as dependências:

```
pip install -r requirements.txt
python -m spacy download pt_core_news_sm
```

### Execute a aplicação:

```
python app.py
```

## 📝 Exemplo de Uso
- Abra a interface gráfica que será lançada automaticamente no navegador.
- Insira o texto cifrado.
- Selecione o método de criptografia utilizado (César, Atbash ou Vigenère).
- Para Vigenère, forneça a chave utilizada na cifragem.
- Clique em "Submit" para ver o texto descriptografado.

# 📄 Licença
Este projeto está licenciado sob a MIT License.