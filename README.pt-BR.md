# 🔐 Decriptador Híbrido de Cifra de César - Versão 2.3

Este projeto implementa um **decriptador inteligente** para cifras de César, combinando **validação formal com Gramática Livre de Contexto (GLC)**, **validação lexical com dicionário** e **validação semântica com o modelo BERT multilingual**. A nova versão 2.3 traz **otimizações significativas de desempenho**, mantendo a robustez do processo de validação híbrida.

> ⚠️ ** Nota: ** A versão atual deste descriptor suporta apenas textos em ** português (PT-BR) **, pois o GLC e o dicionário são específicos do idioma.

> 🇺🇸 [Versão em inglês disponível aqui](./README.md)

---

## 🚀 Novidades na Versão 2.3

- ⚡ Processamento paralelo com `ThreadPoolExecutor` para gerar os 25 shifts de forma mais rápida.
- 🎯 Pré-seleção dos 3 melhores candidatos usando apenas GLC e Dicionário antes de aplicar o BERT.
- 🧠 Validação BERT otimizada:
  - Limite de 5 palavras mais longas por frase.
  - Frases grandes são divididas em pedaços para avaliação incremental.
- 🪶 Novos pesos na pontuação:
  - 30% GLC, 50% Dicionário, 20% BERT.

---

## 📊 Comparativo de Versões

| Recurso                      | V2.2   | V2.3         |
|-----------------------------|--------|--------------|
| Processamento paralelo      | ❌     | ✅            |
| Pré-filtragem com GLC+Dict  | ❌     | ✅            |
| Palavras limitadas no BERT  | ❌     | ✅ (5)        |
| BERT para frases grandes    | ❌     | ✅ (com divisão) |
| Pesos refinados             | 30/30/30 | 30/50/20     |
| Desempenho                  | Baixo  | Alto         |
| Memória                     | Alto   | Otimizado    |

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia      | Finalidade                                  |
|------------------|----------------------------------------------|
| Python 3.11+     | Linguagem principal                         |
| Lark             | Implementação de GLC                        |
| Transformers     | Modelo BERT multilingual                   |
| PyTorch          | Inferência do modelo                       |
| Gradio           | Interface gráfica web                      |

---

## 📁 Estrutura do Projeto

```
Descriptografia-Python/
├── Caesar/
│   │
│   ├── config/                  # Configurações e definições gerais
│   │   ├── __init__.py
│   │   ├── grammar.py           # Definição da GLC
│   │   └── settings.py          # Configurações de pesos e parâmetros
│   │
│   ├── core/                    # Núcleo da lógica de descriptografia
│   │   ├── __init__.py
│   │   ├── cipher.py            # Geração dos shifts da cifra de César
│   │   ├── validator.py         # Validações com GLC, dicionário e BERT
│   │   └── decoder.py           # Lógica principal do decriptador
│   │
│   ├── utils/                   # Funções utilitárias
│   │   ├── __init__.py
│   │   └── text_utils.py        # Limpeza e manipulação de texto
│   │
│   ├── interface/               # Interface gráfica
│   │   ├── __init__.py
│   │   └── app.py               # Aplicação com Gradio
│   │
│   ├── assets/                  # Recursos auxiliares
│   │   └── portuguese_words.txt # Lista de palavras em português
│   │
│   └── main.py                  # Ponto de entrada do programa
│
└── README.md
```

## ⚙️ Como Funciona
1. Geração paralela dos 25 possíveis shifts.
2. Avaliação preliminar (GLC + Dicionário).
3. Seleção dos 3 melhores resultados preliminares.
4. Avaliação final com BERT apenas nesses 3 candidatos.
   - Se o texto for muito longo, ele é dividido em frases e processado parcialmente.
5. Resultado exibido com explicação e gráfico dos scores.

---

## 🧪 Exemplo de Saída

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

## 🚀 Instalação

1. Clone o repositório:
```
git clone https://github.com/JVLT0/Descriptografia-Python.git
```

2. Acesse a pasta:
```
cd Descriptografia-Python/Caesar
```

3. (Opcional) Crie um ambiente virtual:
```
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

4. Instale as dependências:
```
pip install -r requirements.txt
```

5. Execute o programa:
```
python main.py
```

---

## 📝 Observações Técnicas
- O modelo BERT (~700MB) será baixado automaticamente na primeira execução.
- A gramática pode ser personalizada diretamente no código.
- Pesos de score estão definidos no próprio app.py.
- Compatível com CPU (uso de GPU recomendado, se disponível).
- Textos longos são avaliados em partes com amostragem aleatória para melhorar a performance do BERT.