# 🔐 Decriptador Híbrido de Cifra de César

Este projeto combina **abordagens formais (GLC + Autômatos) e modernas (BERT + Correções inteligentes),** para criar um sistema avançado de descriptografia, atendendo tanto a requisitos acadêmicos quanto às melhores práticas de PLN.

## 🌟 Destaques da Versão 2.1
- ✅ Validação formal com Gramática Livre de Contexto (GLC).
- 🤖 Validação semântica com modelo BERT multilingual.
- 📖 Validação lexical com dicionário em português.
- ⚖️ Sistema híbrido de pontuação ponderada.
- 🧠 Sugestão de correções inteligentes com BERT + dicionário.
- 📊 Dashboard interativo com gráficos Plotly.
- 🧾 Histórico de tentativas com média de score.
- 🖥️ Interface intuitiva com Gradio.


## 📁 Estrutura do Projeto
```
Crypto/
│
├── main.py                  # Ponto de entrada principal
├── requirements.txt         # Dependências atualizadas
│
├── core/
│   ├── _init_.py
│   ├── encryption/          # Nova pasta para algoritmos de criptografia
│   │   ├── _init_.py
│   │   ├── base.py          # Classe base abstrata
│   │   ├── caesar.py        # Implementação Caesar
│   │   └──  vigenere.py     # Nova implementação
│   │
│   ├── decryption.py        # Modificado para multi-algoritmos
│   ├── validation.py      
│   └── correction.py      
│
├── utils/
│   ├── _init_.py
│   ├── text_processing.py 
│   └── visualization.py   
│
├── data/
│   ├── portuguese_words.txt
│   └── english_words.txt    # Novo dicionário
│
└── interface/
    ├── _init_.py
    └── gradio_ui.py         # Interface atualizada
```
## 🛠️ Tecnologias Utilizadas
| Tecnologia | Finalidade |
|------------|------------|
|**Python 3.11+**|Linguagem principal.|
|**Lark**|Implementação de GLC e autômatos.|
|**Transformers**|Modelo BERT multilingual.|
|**PyTorch**|Inferência do modelo.|
|**Gradio**|Interface web interativa.|
|**Plotly**|Visualizações interativas de dados.|

## ⚙️ Como Funciona

1. Testa todos os 25 shifts possíveis da Cifra de César.

2. Para cada versão decriptada:

- ✅ Valida estrutura com GLC.
- 🧠 Calcula probabilidade semântica com BERT.
- 📖 Verifica palavras válidas no dicionário.
---
3. Aplica validação híbrida com pesos:

- *40% GLC.*
- *30% BERT.*
- *30% Dicionário.*
---
4. Exibe o resultado com:

- 🔓 Texto decriptado.
- 🔧 Sugestão corrigida com IA.
- 📈 Score, shift e média de tentativas.
- 📊 Gráficos de pontuação e confiança.
- 📊 Visualizações.
---

5. Linha: Pontuação de cada shift (Plotly).

6. Pizza: Peso de cada componente de validação.

7. Histórico: Número total de tentativas e média de score.

- 🧠 Correções Inteligentes.
---

8. Sugere palavras alternativas com base no:
- 🔍 Dicionário.
- 🧠 Preenchimento de máscara com BERT ([MASK]).
---

9. Substitui palavras inválidas por sugestões mais prováveis.
- 🚀 Instalação
---

## 1. Clone o repositório
```
git clone https://github.com/JVLT0/Descriptografia-Python.git
```
## 2. Acesse a pasta
```
cd Descriptografia-Python/Caesar
```

## 3. (Opcional) Crie um ambiente virtual
```
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

## 4. Instale as dependências
```
pip install -r requirements.txt
```

## 5. Execute a aplicação
```
python app.py
```
## 🧪 Exemplo Prático
- Entrada:
```
D oljhlud udsrvd pduurp vdowrx vreuh r fdfkruur fdqvdgr
```

- Saída:
```
🔓 Decodificado: A ligeira raposa marrom saltou sobre o cachorro cansado
🔧 Sugestão: A ligeira raposa marrom saltou sobre o cachorro cansado

🔐 Shift: 3
📈 Score: 0.92

📊 Tentativas: 4
📉 Média Score: 0.89
```
## 📄 Comparativo de Versões

|Feature|V1.0|V2.0|V2.1|
|-------|----|----|----|
|Validação GLC|	✓|	✓|	✓|
|Modelo BERT|	-|	✓|	✓|
|Validação com dicionário|	-|	✓|	✓|
|Correções automáticas|	-|	-|	✓|
|Gráficos Plotly|	-|	-|	✓|
|Histórico de tentativas|	-|	-|	✓|
|requisitos RAM| ~500MB| ~2GB| ~2GB|

## 📝 Observações Técnicas
- O modelo BERT (~700MB) é baixado na primeira execução.
- A gramática pode ser adaptada diretamente no código-fonte.
- O sistema funciona com CPU, mas o uso de GPU acelera o BERT.
- Suporta acentuação e pontuação (removida apenas internamente para validação).

## 📄 Licença
- MIT License
```
Nota pedagógica: Este projeto combina teoria formal,
(gramáticas e autômatos) com práticas modernas de PLN.
Sendo ideal para fins educacionais e demonstrações técnicas.
```