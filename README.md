# 🔐 Decriptador Híbrido de Cifra de César - Versão 2.1

Este projeto implementa um **decriptador inteligente** para cifras de César, combinando **validação formal com Gramática Livre de Contexto (GLC)** e **validação semântica com o modelo BERT multilingual**. A versão 2.1 traz melhorias de desempenho, estruturação interna e estabilidade, mantendo a simplicidade em um único arquivo principal.

---

## 🌟 Novidades na Versão 2.1

- ✅ **Melhor estrutura interna** do código (divisão em funções bem definidas)
- 🔄 **Validação híbrida**: GLC + Dicionário + Modelo BERT
- ⚖️ **Sistema de pontuação ponderada** com pesos personalizáveis
- 🖥️ **Interface gráfica com Gradio** mais amigável

---

## 📁 Estrutura do Projeto

```
Descriptografia-Python
├──Caesar/ 
    ├── app.py # Script principal com interface Gradio 
    ├── portuguese_words.txt # Lista de palavras válidas em português
    └──requirements.txt # Dependências do projeto
```


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

## ⚙️ Como Funciona

1. Gera os 25 possíveis deslocamentos da cifra de César.
2. Para cada tentativa:
   - ✅ **Valida com GLC**
   - 📖 **Verifica palavras no dicionário**
   - 🧠 **Calcula coerência com BERT**
3. Aplica pesos na pontuação:
   - 40% Estrutura (GLC)
   - 30% Léxico (Dicionário)
   - 30% Semântica (BERT)
4. Retorna a versão mais provável com seu shift e score.

---

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
python app.py
```

## 🧪 Exemplo de Uso
- Entrada:
```
D oljhlud udsrvd pduurp vdowrx vreuh r fdfkruur fdqvdgr
```
- Saída esperada:
```
A ligeira raposa marrom saltou sobre o cachorro cansado

Shift: 3
```

## 📊 Comparativo de Versões
| Recurso               | V2.0   | V2.1     |
| --------------------- | ------ | -------- |
| GLC (estrutura)       | ✅      | ✅        |
| Dicionário (léxico)   | ✅      | ✅        |
| BERT (semântica)      | ✅      | ✅        |
| Funções bem definidas | ⚠️     | ✅        |
| Interface Gradio      | ✅      | ✅        |
| Requisitos de RAM     | \~2 GB | \~2 GB |


## 📝 Observações Técnicas
- O modelo BERT (~700MB) será baixado automaticamente na primeira execução.
- A gramática pode ser personalizada diretamente no código.
- Pesos de score estão definidos no próprio app.py.
- Compatível com CPU (uso de GPU recomendado, se disponível).

## 📄 Licença
Projeto licenciado sob a [MIT Licens](https://opensource.org/licenses/MIT).

💡 Nota pedagógica: Este projeto une fundamentos acadêmicos (GLC, autômatos) com técnicas modernas de PLN (BERT), proporcionando uma ponte sólida entre teoria e aplicação prática em segurança da informação.