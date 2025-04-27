# 🔐Decriptador de Cifra de César com GLC e Automato
Este projeto é um decriptador de texto utilizando a Cifra de César combinado com técnicas de Gramática Livre de Contexto (GLC) e um Autômato para validação de frases em português. O objetivo principal é descriptografar mensagens cifradas por meio de um deslocamento (shift) e verificar se o texto gerado faz sentido em português, utilizando um dicionário e a estrutura de uma gramática simples.

O decriptador tenta todos os deslocamentos possíveis (de 1 a 25) para verificar qual shift resulta em um texto válido. Para garantir que o texto final seja uma frase coerente em português, ele valida tanto a estrutura da frase usando a GLC quanto a validade das palavras com um dicionário.

## 🚀 Tecnologias Utilizadas
- **Python 3.11**: Linguagem principal utilizada para desenvolver o sistema.
- **Lark**: Biblioteca para parsing de linguagens, utilizada para criar e gerenciar a Gramática Livre de Contexto (GLC) e o autômato de validação de frases.
- **Gradio**: Utilizado para criar uma interface gráfica simples onde o usuário pode inserir o texto criptografado e obter a resposta decriptografada.
- **Dicionário de Palavras em Português**: Arquivo de texto contendo palavras em português para validar a correção das palavras no texto descriptografado.

## 🧠 Como Funciona
1. **Pré-processamento do Texto**
O texto criptografado passa por um pré-processamento para remover acentos, símbolos estranhos e converte todas as letras para minúsculas.

2. **Tentativa de Descriptografar**
Em seguida, o sistema tenta todas as possíveis chaves de deslocamento (de 1 a 25) para descriptografar o texto utilizando a Cifra de César.

3. **Validação de Texto**
Após cada tentativa de decriptação:  
O texto é verificado quanto à sua estrutura (usando uma Gramática Livre de Contexto - GLC).  
O texto também é validado em relação ao dicionário de palavras em português.  
Se o texto passá-las, é considerado uma possível decriptação correta.  

4. **Resultado**
O decriptador retorna a mensagem descriptografada com o shift utilizado, caso seja válida. Caso contrário, informa que não conseguiu encontrar uma solução.

## ⚙️ Instalação
- Para rodar o projeto, siga os seguintes passos:

1. Clone o repositório:

```
git clone https://github.com/JVLT0/Descriptografia-Cesar-Python.git
```

2. Crie e ative um ambiente virtual:
```
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

3. Instale as dependências:
```
pip install -r requirements.txt
```

4. Execute o script:

```
python main.py
```

- Isso abrirá a interface gráfica, onde você pode inserir o texto criptografado e visualizar o resultado decriptografado.  
- Se a interface gráfica não abrir automaticamente, será exibido o endereço no terminal. Basta copiar e colar esse link no seu navegador para acessar a aplicação.

## 🧑‍💻 Como Usar
1. Digite um texto criptografado utilizando a Cifra de César no campo de entrada.
2. Clique em "Submit" para tentar descriptografar o texto.
3. O sistema tentará todos os possíveis deslocamentos e verificará a validade do texto gerado.
4. Se encontrar uma solução válida, será exibido o texto descriptografado com o shift utilizado.

## 🔧 Funcionalidades
- Decriptação Automática: Testa todos os deslocamentos possíveis da Cifra de César para encontrar o texto original.
- Validação Gramatical: Utiliza uma Gramática Livre de Contexto para garantir que o texto gerado é uma frase coerente em português.
- Verificação Semântica: Compara as palavras do texto descriptografado com um dicionário de palavras para garantir que elas existem em português.

# 📚 Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.