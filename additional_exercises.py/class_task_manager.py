"""
Progetta una classe TaskManager per gestire un insieme di attività.
Attributi:
task: dict[str, dict]
"""


class TaskManager:

    # nell' init passo tasks perchè posso voler passare il dizionario in input, sennò posso mettere solo il self e a quel punto devo inizializzare self.task = {}
    def __init__(self, tasks: dict[str, dict[str, str | bool]]):

        self.tasks: dict[str, dict[str, str | bool]] = {}

    def create_task(self, task_id: str, description: str) -> dict[str, dict[str, str | bool]]:

        if task_id in self.tasks:
 
            self.tasks[task_id]["Completato"] = True

            # per costruzione si deve aggiungere task_id: poichè l esercizio vuole un nuovo dizionario
            return {task_id: self.tasks[task_id]}

        else:
            # se l esercizio avesse chiesto un eccezione: raise KeyError("Chiave non presente!")
            return "Task not found!"

    def update_description(self, task_id: str, new_description: str) -> dict[str, dict[str, str | bool]]:

        if task_id not in self.tasks:

            return "Task not found."

        else:
            self.tasks[task_id]["Description"] = new_description

            return {task_id: self.tasks[task_id]}

    def remove_task(self, task_id: str) -> dict | str:

        if task_id not in self.tasks:

            return "Task not found!"

        else:
            """
            si potrebbe usare .popitem che restituisce una tupla , la parte a sinistra della tupla
            sarebbe la chiave associata al valore nel dizionario mentre la parte di destra il valore associato alla chiave stessa
            """
            value = self.tasks.pop(task_id)

            # ritorno un dizionario che ritorna solo quella chiave e valore 
            return {task_id: value}

    def list_tasks(self) -> list[str]:

        keys: list[str] = [key for key in self.tasks.key()]

        return keys

    def get_task(self, task_id: str) -> dict | str:

        if task_id not in self.tasks:

            return "Error, task not found."

        else:
            return {task_id: self.tasks[task_id]}
