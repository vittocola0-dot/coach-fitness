"""
Database degli Esercizi - Coach Fitness Dinamico
================================================
Contiene ~50 esercizi categorizzati per tipo, gruppo muscolare e attrezzatura.
Ogni esercizio è un dizionario con i seguenti campi:
- nome: Nome dell'esercizio (italiano)
- categoria: "hiit" | "forza" | "stretching"
- gruppo: "gambe" | "petto" | "schiena" | "core" | "fullbody" | "spalle" | "braccia"
- attrezzatura: "nessuna" | "manubri" | "elastici" | "tappetino" | "sbarra"
- serie_default: Numero di serie (int)
- reps_default: Numero di ripetizioni (int) - oppure None se a tempo
- durata_default: Durata in secondi (int) - oppure None se a ripetizioni
"""

ESERCIZI = [
    # ===================================================================
    # CATEGORIA: HIIT / ALTA INTENSITÀ
    # ===================================================================

    # -- Fullbody --
    {"nome": "Burpees", "categoria": "hiit", "gruppo": "fullbody",
     "attrezzatura": "nessuna", "serie_default": 3, "reps_default": 10, "durata_default": None},
    {"nome": "Jumping Jacks", "categoria": "hiit", "gruppo": "fullbody",
     "attrezzatura": "nessuna", "serie_default": 3, "reps_default": None, "durata_default": 40},
    {"nome": "Mountain Climbers", "categoria": "hiit", "gruppo": "fullbody",
     "attrezzatura": "nessuna", "serie_default": 3, "reps_default": None, "durata_default": 30},
    {"nome": "Skip sul Posto", "categoria": "hiit", "gruppo": "fullbody",
     "attrezzatura": "nessuna", "serie_default": 3, "reps_default": None, "durata_default": 30},
    {"nome": "Squat Jump", "categoria": "hiit", "gruppo": "gambe",
     "attrezzatura": "nessuna", "serie_default": 3, "reps_default": 12, "durata_default": None},
    {"nome": "High Knees", "categoria": "hiit", "gruppo": "fullbody",
     "attrezzatura": "nessuna", "serie_default": 3, "reps_default": None, "durata_default": 30},
    {"nome": "Tuck Jump", "categoria": "hiit", "gruppo": "gambe",
     "attrezzatura": "nessuna", "serie_default": 3, "reps_default": 8, "durata_default": None},
    {"nome": "Lateral Shuffle", "categoria": "hiit", "gruppo": "gambe",
     "attrezzatura": "nessuna", "serie_default": 3, "reps_default": None, "durata_default": 30},
    {"nome": "Plank to Push-up", "categoria": "hiit", "gruppo": "fullbody",
     "attrezzatura": "tappetino", "serie_default": 3, "reps_default": 8, "durata_default": None},
    {"nome": "Speed Skaters", "categoria": "hiit", "gruppo": "gambe",
     "attrezzatura": "nessuna", "serie_default": 3, "reps_default": 12, "durata_default": None},
    {"nome": "Bicycle Crunch Veloci", "categoria": "hiit", "gruppo": "core",
     "attrezzatura": "tappetino", "serie_default": 3, "reps_default": None, "durata_default": 30},
    {"nome": "Swing con Manubrio", "categoria": "hiit", "gruppo": "fullbody",
     "attrezzatura": "manubri", "serie_default": 3, "reps_default": 15, "durata_default": None},
    {"nome": "Thrusters con Manubri", "categoria": "hiit", "gruppo": "fullbody",
     "attrezzatura": "manubri", "serie_default": 3, "reps_default": 10, "durata_default": None},
    {"nome": "Battle Rope Simulation", "categoria": "hiit", "gruppo": "fullbody",
     "attrezzatura": "nessuna", "serie_default": 3, "reps_default": None, "durata_default": 30},
    {"nome": "Box Step-up Veloce", "categoria": "hiit", "gruppo": "gambe",
     "attrezzatura": "nessuna", "serie_default": 3, "reps_default": 10, "durata_default": None},
    {"nome": "Sprawl", "categoria": "hiit", "gruppo": "fullbody",
     "attrezzatura": "nessuna", "serie_default": 3, "reps_default": 8, "durata_default": None},

    # ===================================================================
    # CATEGORIA: FORZA / POSTURA
    # ===================================================================

    # -- Gambe --
    {"nome": "Squat", "categoria": "forza", "gruppo": "gambe",
     "attrezzatura": "nessuna", "serie_default": 3, "reps_default": 12, "durata_default": None},
    {"nome": "Squat con Manubri", "categoria": "forza", "gruppo": "gambe",
     "attrezzatura": "manubri", "serie_default": 3, "reps_default": 10, "durata_default": None},
    {"nome": "Affondi Alternati", "categoria": "forza", "gruppo": "gambe",
     "attrezzatura": "nessuna", "serie_default": 3, "reps_default": 10, "durata_default": None},
    {"nome": "Affondi con Manubri", "categoria": "forza", "gruppo": "gambe",
     "attrezzatura": "manubri", "serie_default": 3, "reps_default": 10, "durata_default": None},
    {"nome": "Sumo Squat", "categoria": "forza", "gruppo": "gambe",
     "attrezzatura": "nessuna", "serie_default": 3, "reps_default": 12, "durata_default": None},
    {"nome": "Glute Bridge", "categoria": "forza", "gruppo": "gambe",
     "attrezzatura": "tappetino", "serie_default": 3, "reps_default": 15, "durata_default": None},
    {"nome": "Step-up Controllato", "categoria": "forza", "gruppo": "gambe",
     "attrezzatura": "nessuna", "serie_default": 3, "reps_default": 10, "durata_default": None},

    # -- Petto --
    {"nome": "Piegamenti sulle Braccia", "categoria": "forza", "gruppo": "petto",
     "attrezzatura": "nessuna", "serie_default": 3, "reps_default": 10, "durata_default": None},
    {"nome": "Piegamenti Diamante", "categoria": "forza", "gruppo": "petto",
     "attrezzatura": "nessuna", "serie_default": 3, "reps_default": 8, "durata_default": None},
    {"nome": "Floor Press con Manubri", "categoria": "forza", "gruppo": "petto",
     "attrezzatura": "manubri", "serie_default": 3, "reps_default": 10, "durata_default": None},

    # -- Schiena --
    {"nome": "Rematore con Manubrio", "categoria": "forza", "gruppo": "schiena",
     "attrezzatura": "manubri", "serie_default": 3, "reps_default": 10, "durata_default": None},
    {"nome": "Trazioni alla Sbarra", "categoria": "forza", "gruppo": "schiena",
     "attrezzatura": "sbarra", "serie_default": 3, "reps_default": 6, "durata_default": None},
    {"nome": "Rematore con Elastico", "categoria": "forza", "gruppo": "schiena",
     "attrezzatura": "elastici", "serie_default": 3, "reps_default": 12, "durata_default": None},
    {"nome": "Superman", "categoria": "forza", "gruppo": "schiena",
     "attrezzatura": "tappetino", "serie_default": 3, "reps_default": 12, "durata_default": None},

    # -- Core --
    {"nome": "Plank", "categoria": "forza", "gruppo": "core",
     "attrezzatura": "tappetino", "serie_default": 3, "reps_default": None, "durata_default": 30},
    {"nome": "Plank Laterale", "categoria": "forza", "gruppo": "core",
     "attrezzatura": "tappetino", "serie_default": 3, "reps_default": None, "durata_default": 25},
    {"nome": "Crunch", "categoria": "forza", "gruppo": "core",
     "attrezzatura": "tappetino", "serie_default": 3, "reps_default": 15, "durata_default": None},
    {"nome": "Russian Twist", "categoria": "forza", "gruppo": "core",
     "attrezzatura": "tappetino", "serie_default": 3, "reps_default": 12, "durata_default": None},
    {"nome": "Dead Bug", "categoria": "forza", "gruppo": "core",
     "attrezzatura": "tappetino", "serie_default": 3, "reps_default": 10, "durata_default": None},

    # -- Spalle / Braccia --
    {"nome": "Military Press con Manubri", "categoria": "forza", "gruppo": "spalle",
     "attrezzatura": "manubri", "serie_default": 3, "reps_default": 10, "durata_default": None},
    {"nome": "Alzate Laterali", "categoria": "forza", "gruppo": "spalle",
     "attrezzatura": "manubri", "serie_default": 3, "reps_default": 12, "durata_default": None},
    {"nome": "Curl con Manubri", "categoria": "forza", "gruppo": "braccia",
     "attrezzatura": "manubri", "serie_default": 3, "reps_default": 10, "durata_default": None},
    {"nome": "Dips su Sedia", "categoria": "forza", "gruppo": "braccia",
     "attrezzatura": "nessuna", "serie_default": 3, "reps_default": 10, "durata_default": None},
    {"nome": "Curl con Elastico", "categoria": "forza", "gruppo": "braccia",
     "attrezzatura": "elastici", "serie_default": 3, "reps_default": 12, "durata_default": None},

    # ===================================================================
    # CATEGORIA: STRETCHING / MOBILITÀ
    # ===================================================================
    {"nome": "Stretching Quadricipiti", "categoria": "stretching", "gruppo": "gambe",
     "attrezzatura": "tappetino", "serie_default": 2, "reps_default": None, "durata_default": 30},
    {"nome": "Stretching Hamstring", "categoria": "stretching", "gruppo": "gambe",
     "attrezzatura": "tappetino", "serie_default": 2, "reps_default": None, "durata_default": 30},
    {"nome": "Posizione del Bambino", "categoria": "stretching", "gruppo": "schiena",
     "attrezzatura": "tappetino", "serie_default": 2, "reps_default": None, "durata_default": 40},
    {"nome": "Cat-Cow", "categoria": "stretching", "gruppo": "schiena",
     "attrezzatura": "tappetino", "serie_default": 2, "reps_default": 10, "durata_default": None},
    {"nome": "Cobra Stretch", "categoria": "stretching", "gruppo": "core",
     "attrezzatura": "tappetino", "serie_default": 2, "reps_default": None, "durata_default": 30},
    {"nome": "Pigeon Pose", "categoria": "stretching", "gruppo": "gambe",
     "attrezzatura": "tappetino", "serie_default": 2, "reps_default": None, "durata_default": 30},
    {"nome": "Rotazione Toracica", "categoria": "stretching", "gruppo": "schiena",
     "attrezzatura": "tappetino", "serie_default": 2, "reps_default": 8, "durata_default": None},
    {"nome": "Stretching Pettorali al Muro", "categoria": "stretching", "gruppo": "petto",
     "attrezzatura": "nessuna", "serie_default": 2, "reps_default": None, "durata_default": 30},
    {"nome": "Stretching Spalle con Elastico", "categoria": "stretching", "gruppo": "spalle",
     "attrezzatura": "elastici", "serie_default": 2, "reps_default": None, "durata_default": 30},
    {"nome": "Forward Fold", "categoria": "stretching", "gruppo": "gambe",
     "attrezzatura": "nessuna", "serie_default": 2, "reps_default": None, "durata_default": 30},
    {"nome": "Neck Stretch", "categoria": "stretching", "gruppo": "spalle",
     "attrezzatura": "nessuna", "serie_default": 2, "reps_default": None, "durata_default": 20},
    {"nome": "Hip Circles", "categoria": "stretching", "gruppo": "gambe",
     "attrezzatura": "nessuna", "serie_default": 2, "reps_default": 10, "durata_default": None},
    {"nome": "Respirazione Diaframmatica", "categoria": "stretching", "gruppo": "core",
     "attrezzatura": "tappetino", "serie_default": 1, "reps_default": None, "durata_default": 60},
    {"nome": "Shoulder Dislocates con Elastico", "categoria": "stretching", "gruppo": "spalle",
     "attrezzatura": "elastici", "serie_default": 2, "reps_default": 10, "durata_default": None},
]


def get_esercizi_per_categoria(categoria: str) -> list:
    """Restituisce tutti gli esercizi di una determinata categoria.

    Args:
        categoria: "hiit", "forza" o "stretching"

    Returns:
        Lista di dizionari degli esercizi filtrati.
    """
    return [e for e in ESERCIZI if e["categoria"] == categoria]


def get_esercizi_per_attrezzatura(esercizi: list, attrezzatura_disponibile: list) -> list:
    """Filtra gli esercizi in base all'attrezzatura disponibile all'utente.

    Args:
        esercizi: Lista di esercizi da filtrare.
        attrezzatura_disponibile: Lista di stringhe con l'attrezzatura posseduta
                                  (es. ["nessuna", "manubri", "tappetino"]).

    Returns:
        Lista filtrata di esercizi utilizzabili.
    """
    # "nessuna" è sempre disponibile (esercizi a corpo libero)
    attr_set = set(attrezzatura_disponibile)
    attr_set.add("nessuna")
    return [e for e in esercizi if e["attrezzatura"] in attr_set]


def get_gruppi_muscolari(esercizi: list) -> list:
    """Restituisce la lista unica dei gruppi muscolari presenti negli esercizi.

    Args:
        esercizi: Lista di esercizi.

    Returns:
        Lista di stringhe con i gruppi muscolari unici.
    """
    return list(set(e["gruppo"] for e in esercizi))
