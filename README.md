# 📧 Detector de Spam em Python

Este projeto implementa um classificador de mensagens de texto para identificar se uma mensagem é spam ou não spam, utilizando Naive Bayes e TF-IDF. 
Além disso, possui uma interface gráfica simples construída com Tkinter, permitindo que o usuário insira mensagens e veja o resultado da classificação em tempo real.


## 🚀 Tecnologias utilizadas

- **Python 3**
- **Pandas** – manipulação de dados  
- **Scikit-learn** – ML clássico (Naive Bayes + TF-IDF)  
- **Tkinter** – interface gráfica nativa do Python  
- **Joblib** - serializar/deserializar (salvar/carregar) objetos Python (modelo + vetor).

## 📂 Estrutura do Projeto
```markdown
detector-spam/
 ├── spam_model.pkl # Modelo treinado salvo
 ├── vectorizer.pkl # Vetorizador TF-IDF salvo
 ├── main.py # Código principal com treino e interface gráfica
 └── README.md # Documentação do projeto
```

## 🧠 Como o modelo funciona

O texto da mensagem é transformado em números pelo TF-IDF, que mede a importância das palavras. 
Em seguida, o algoritmo Naive Bayes calcula a probabilidade de a mensagem ser spam ou não spam, escolhendo a classe mais provável.
Esse modelo é simples, leve e ideal para aprendizado de conceitos básicos de Machine Learning.

## Desenvolvedor 👩‍💻

**Sarah Santos**  
- [LinkedIn](https://www.linkedin.com/in/sarah-santos-1977b5279/) 🌐
