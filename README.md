# 🔐 Decriptador Híbrido de Cifra de César

Este projeto combina **abordagens formais (GLC + Autômatos) e modernas (BERT)** para criar um sistema avançado de descriptografia, atendendo tanto aos requisitos acadêmicos quanto às melhores práticas de PLN.


## 🌟 Destaques da Versão
- ✅ **Validação formal** com Gramática Livre de Contexto (GLC) e Autômatos
- 🤖 **Validação semântica** com modelo BERT multilingual
- ⚖️ **Sistema híbrido** de pontuação ponderada
- 🖥️ **Interface intuitiva** com Gradio
- ⚡ **Processamento otimizado** com PyTorch

## 📁 Estrutura do Projeto
```
Descriptografia-Python
├──Caesar/ 
    ├── app.py # Script principal com interface Gradio 
    ├── portuguese_words.txt # Lista de palavras válidas em português
    └──requirements.txt # Dependências do projeto
```

## 🛠️ Tecnologias Utilizadas
| Tecnologia | Finalidade |
|------------|------------|
| Python 3.11+ | Linguagem principal |
| Lark | Implementação de GLC e autômatos |
| Transformers | Modelo BERT multilingual |
| PyTorch | Inferência do modelo |
| Gradio | Interface web interativa |

## ⚙️ Como Funciona
1. Testa todos os 25 shifts possíveis
2. Para cada versão decriptada:
   - ✅ Valida estrutura com GLC
   - 🧠 Calcula probabilidade com BERT
   - 📖 Verifica palavras no dicionário
3. Combina os scores com pesos:
   - 40% GLC (estrutura)
   - 30% BERT (semântica)
   - 30% Dicionário (léxico)
4. Retorna a versão com maior pontuação

## 🚀 Instalação

1. Clone o repositório:
```
git clone https://github.com/JVLT0/Descriptografia-Python.git
```

2. Entre na pasta principal:
```
cd Caesar
```

3. Crie um ambiente virtual (opcional, mas recomendado):
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
```

4. Instale as dependências:
```
pip install -r requirements.txt
```
5. Execute a aplicação:
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
A ligeira raposa marrom saltou sobre o cachorro cansado

Shift: 3
Score: 0.92
```

## 📊 Comparativo de Versões
| Features | V1.0 | V2 |
|------------|------------|------------|
|Validação GLC|✓|✓|
|Modelo BERT|-|✓|
|Sistema Híbrido|-|✓|
|Peso Ajustável|-|✓|
|Requisitos RAM|~500MB|~2GB|

## 📝 Observações Técnicas
- Primeira execução baixa o modelo BERT (~700MB)
- Gramática customizável no arquivo principal
- Pesos ajustáveis no código-fonte
- Compatível com CPU (GPU recomendada)
- Esta é apenas a versão 2.0. Cifras adicionais serão adicionadas futuramente.

## 📄 Licença
- Este projeto está licenciado sob a MIT License
```
Nota Pedagógica: Esta versão mantém todos os componentes acadêmicos exigidos
(GLC e autômatos) enquanto incorpora técnicas modernas de PLN, servindo como 
ponte entre teoria formal e aplicações práticas.
```