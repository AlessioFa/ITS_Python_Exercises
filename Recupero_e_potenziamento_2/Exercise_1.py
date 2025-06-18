"""In biologia molecolare, le molecole di DNA possono essere viste come stringhe sull’alfabeto dei nucleotidi
A = adenina, C = citosina, G =guanina, T = timina.

Ad esempio: DNA: CAGCTGATCGATGCTAGCCTG.

Scrivere un programma in linguaggio Python che legge dall’utente due stringhe s1 e s2 corripondenti a frammenti di
DNA e verifica se s2 puo' essere sovrapposta su s1 in modo che una parte iniziale (prefisso) di s2 coincida con
una parte finale (suffisso) di s1.
 
Il programma dovra' dare la lunghezza della massima sovrapposizione (0 se non si possono sovrapporre).
 
Ad esempio, se l’utente ha inserito:
s1= CAGCTGATCGATGCTAGCCTG
s2= AGCCTGTTGCACCTAGA

Le due stringhe si sovrappongono come segue:
CAGCTGATCGATGCTAGCCTG
                                  AGCCTGTTGCACCTAGA

Il programma dovra' quindi stampare in output:

    le stringhe sovrapposte come nell'esempio.

    La massima lunghezza di sovrapposizione e' 6.


NOTA1:
il programma dovra' anche verificare la correttezza dell’input, ovvero le stringhe inserite dall’utente devono essere effettivamente frammenti di DNA.
Suggerimento: scrivere una funzione isDNA() che, data in input una sequenza, restituisca True se la sequenza passata è una valida sequenza del DNA formata dai soli caratteri A, C, G o T, e che restituisca False altirmenti.
Può essere utile usare una regex.

Nota2: trovare una soluzione che eviti di scrivere codice replicato per inizializzare le sequenze s1 e s2.

Infine, verificare le seguenti coppie di frammenti di DNA:
- s1= TTGACCAGGTCA
- s2= AACCGGTTAA
La massima lunghezza è 1

- s1= GGTACCGTGA
- s2= CGTGAACCTT
La massima lunghezza è 5

- s1= AAGCTTACG
- s2= ACGTTCGA
La massima lunghezza è 3

- s1= TTACGAGTACGCTAGT
- s2= ACGCTAGTCCGA
La massima lunghezza è 8"""


def is_DNA(s1: str, s2: str) -> bool:
    "Function that checks if s1 and s2 are strings and "
    "if all their character are valid. "

    char_check = "ACGT"  # valid DNA characters

    # check that both input are strings
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise ValueError("s1 and s2 must be strings!")

    # create a single string and checks if all char are valid, if not return false
    for char in s1 + s2:
        if char not in char_check:
            print(f"Character '{char}' not valid.")

            return False

    return True


def string_checker(s1: str, s2: str) -> None:
    """Function that checks the maximum overlap between the end of s1
    and the beginning of s2, only if both strings are valid DNA sequences. """

    if not is_DNA(s1, s2):
        print("Error: the entered strings are not valid DNA sequence.")

        return

    max_overlap: int = 0

    #  Loop through all possible overlap lengths
    for i in range(min(len(s1), len(s2)) + 1):

        if s1[-i:] == s2[:i]:

            max_overlap = i

    print(f"Maximum overlap: {max_overlap}")


if __name__ == "__main__":
    string_checker("AGCTGA", "GAACCT")
