# esse modelo de detecção de spam usa Naive Bayes e TF-IDF para classificar mensagens como spam ou não spam
# é um projeto simples para tentar entender como construir um classificador de texto e criar uma interface gráfica 
# com tkinter. 
# apenas para fins educacionais.


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib
import tkinter as tk
from tkinter import messagebox


# treinar modelo

def treinar_modelo():
    url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
    df = pd.read_csv(url, sep='\t', header=None, names=['label', 'message'])

    X_train, X_test, y_train, y_test = train_test_split(
        df["message"], df["label"], test_size=0.2, random_state=42
    )

    vectorizer = TfidfVectorizer(stop_words="english")  # remove stopwords
    x_train_tfidf = vectorizer.fit_transform(X_train)

    model = MultinomialNB()
    model.fit(x_train_tfidf, y_train)

    # avaliação
    x_test_tfidf = vectorizer.transform(X_test)
    y_pred = model.predict(x_test_tfidf)
    print("Acurácia:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    # salvar modelo e vetor
    joblib.dump(model, "spam_model.pkl")
    joblib.dump(vectorizer, "vectorizer.pkl")

    return model, vectorizer

# tenta carregar modelo salvo
try:
    model = joblib.load("spam_model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
except Exception as e:
    print(f"Erro ao carregar modelo salvo: {e}")
    model, vectorizer = treinar_modelo()


# interface gráfica

def verificar_spam():
    texto = entrada.get("1.0", tk.END).strip()

    if not texto:
        messagebox.showwarning("Atenção", "Digite uma mensagem!")
        return

    entrada_tfidf = vectorizer.transform([texto])
    pred = model.predict(entrada_tfidf)[0]
    prob = model.predict_proba(entrada_tfidf)[0]

    if pred == "spam":
        resultado["text"] = f"🚨 SPAM DETECTADO! (confiança: {prob[1]*100:.2f}%)"
        resultado["fg"] = "red"
        janela.configure(bg="#ffcccc")
    else:
        resultado["text"] = f"✔️ Mensagem segura (confiança: {prob[0]*100:.2f}%)"
        resultado["fg"] = "green"
        janela.configure(bg="#ccffcc")

def limpar_texto():
    entrada.delete("1.0", tk.END)
    resultado["text"] = ""
    janela.configure(bg="SystemButtonFace")

# criar janela
janela = tk.Tk()
janela.title("Detector de Spam")
janela.geometry("450x350")

# título
titulo = tk.Label(janela, text="Detector de Spam", font=("Arial", 16))
titulo.pack(pady=10)

# caixa de texto
entrada = tk.Text(janela, height=6, width=50, font=("Arial", 12))
entrada.pack(pady=10)

# botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=5)

botao_verificar = tk.Button(frame_botoes, text="Verificar", command=verificar_spam, font=("Arial", 12))
botao_verificar.pack(side="left", padx=5)

botao_limpar = tk.Button(frame_botoes, text="Limpar", command=limpar_texto, font=("Arial", 12))
botao_limpar.pack(side="left", padx=5)

# resultado
resultado = tk.Label(janela, text="", font=("Arial", 14))
resultado.pack(pady=10)

# iniciar interface
janela.mainloop()
