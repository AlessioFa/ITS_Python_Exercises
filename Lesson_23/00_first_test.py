# Importiamo Flask e url_for dal pacchetto flask
# Flask è il framework web
# url_for serve per costruire dinamicamente URL basati sul nome della funzione della route
from flask import Flask, url_for

# Creiamo un'istanza dell'app Flask
# __name__ è necessario per permettere a Flask di capire dove trovare template e risorse
app = Flask(__name__)

# Definizione delle rotte (routes)
# Ogni route associa un URL a una funzione Python che ritorna una risposta

# Rotta per la root del sito ("/")
# Quando l'utente visita http://127.0.0.1:5000/ verrà chiamata questa funzione
@app.route("/")
def home() -> str:
    # Ritorna HTML semplice come stringa
    return "<h3>Hello world!</h3>"

# Rotta dinamica con parametri: username (stringa) e age (intero)
# Flask cattura i valori direttamente dall'URL e li passa alla funzione
# Esempio URL: /user/Jogn%20Doe/age/30
@app.route("/user/<string:username>/age/<int:age>")
def show_user_profile(username: str, age: int) -> str:
    # Ritorna una stringa formattata con il nome e l'età dell'utente
    return f"Profilo di {username}, età: {age}"

# Rotta dinamica per post identificati da post_id (intero)
# Esempio URL: /post42
@app.route("/post<int:post_id>")
def show_post(post_id: int) -> str:
    # Ritorna una stringa con l'ID del post
    return f"Post {post_id}"

# Esempio di generazione URL con url_for
# Serve per ottenere l'URL di una route usando il nome della funzione
# Questo è utile se cambi l'URL della route ma vuoi mantenere i link corretti
with app.test_request_context():
    # URL della funzione home() → output: '/'
    print(url_for("home"))
    # URL della funzione show_user_profile con parametri → output: '/user/Jogn%20Doe/age/30'
    print(url_for("show_user_profile", username="Jogn Doe", age=30))
    # URL della funzione show_post con post_id → output: '/post42'
    print(url_for("show_post", post_id=42))

# Avvio del server Flask
# Questo blocco serve a far partire il server solo se esegui questo file direttamente
# debug=True → modalità debug attiva (auto-reload e debugger interattivo)
# host="127.0.0.1" → server accessibile solo da localhost
# port=5000 → porta su cui il server ascolta le richieste
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
