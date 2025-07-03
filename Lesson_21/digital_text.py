class Document:

    def __init__(self, text: str) -> None:

        self.text = text
    
    def set_text(self, text: str) -> None:

        self.text = text
    
    def get_text(self) -> str:

        return self.text
    
    def is_in_text(self, word: str) -> bool:

        return word in self.text


class Email(Document):

    def __init__(self, text: str, sender: str, receiver: str, title_text: str) -> None:
        super().__init__(text)
    
        self.sender = sender
        self.receiver = receiver
        self.title_text = title_text.title()

    def set_sender(self, sender: str) -> None:

        self.sender = sender
    
    def set_receiver(self, receiver: str) -> None:

        self.receiver = receiver
    
    def set_title_text(self, title_text: str) -> None:

        self.title_text = title_text

    def get_sender(self) -> str:

        return self.sender
    
    def get_receiver(self) -> str:

        return self.receiver

    def get_title_text(self) -> str:

        return self.title_text
    
    def get_text(self) -> str:

        return f"From: {self.get_sender()} To: {self.get_receiver()}\nTitle: {self.get_title_text()}\n{super().get_text()}"

    def write_to_file(self, file_name="email.txt") -> None:

        with open(file_name, "w") as file:

            file.write(self.get_text())


class File(Document):

    def __init__(self, path_name: str) -> None:

        self.path_name = path_name

        super().__init__("")

    def read_text_from_file(self) -> None:

        with open(self.path_name, "r") as file:

            content = file.read()
            self.set_text(content)


email = Email(
    text="Ciao Bob, possiamo incontrarci domani?",
    sender="alice@example.com",
    receiver="bob@example.com",
    title_text="Incontro"
)

# Creazione dell'oggetto File con il percorso di un file di testo esistente
file = File("", path_name="file_di_testo.txt")
file.read_text_from_file()  # Legge il contenuto del file e lo memorizza

# Stampa del testo completo dell'email usando il metodo getText()
print("Testo Email:")
print(email.get_text())
print()

# Stampa del contenuto del file usando il metodo getText()
print("Testo File:")
print(file.get_text())
print()

# Scrittura del contenuto dell'email su un file chiamato 'email1.txt'
email.write_to_file("email1.txt")

# Verifica se la parola 'incontrarci' è presente nel testo dell'email (dovrebbe essere True)
print("Parola 'incontrarci' presente nell'email?", email.is_in_text("incontrarci"))

# Verifica se la parola 'percorso' è presente nel testo del file (supponiamo che non ci sia, quindi False)
print("Parola 'percorso' presente nel file?", file.is_in_text("percorso"))
