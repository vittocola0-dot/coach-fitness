Workout Generator — Coach Fitness Dinamico
============================================
Genera 3 alternative di allenamento (A, B, C) in base a:
- Tempo disponibile (minuti)
- Livello di energia (Alta, Media, Bassa)
- Profilo utente (attrezzatura disponibile)

La generazione è deterministica: usa il database esercizi, filtra per attrezzatura,
seleziona un numero adeguato di esercizi e adatta volume/intensità.
"""

import random
from copy import deepcopy

from esercizi_db import (
    get_esercizi_per_categoria,
    get_esercizi_per_attrezzatura,
)


# Mappatura tempo → numero di esercizi per opzione
TEMPO_ESERCIZI = {
    10: 3, 15: 4, 20: 4,
    25: 5, 30: 5, 35: 6,
    40: 7, 45: 7, 50: 8,
    55: 9, 60: 10,
}

# Nomi descrittivi delle opzioni
NOMI_OPZIONI = {
    "A": "Alta Intensità (HIIT)",
    "B": "Forza / Postura",
    "C": "Stretching / Mobilità",
}

# Mappatura opzione → categoria esercizi
OPZIONE_CATEGORIA = {
    "A": "hiit",
    "B": "forza",
    "C": "stretching",
}

# Moltiplicatori di intensità in base all'energia
MOLTIPLICATORE_ENERGIA = {
    "Alta": {"serie": 1.2, "reps": 1.2, "durata": 1.2},
    "Media": {"serie": 1.0, "reps": 1.0, "durata": 1.0},
    "Bassa": {"serie": 0.8, "reps": 0.8, "durata": 0.8},
}


def _calcola_num_esercizi(tempo_minuti: int) -> int:
    """Determina il numero di esercizi in base al tempo disponibile.

    Args:
        tempo_minuti: Tempo disponibile in minuti.

    Returns:
        Numero di esercizi da includere nell'allenamento.
    """
    # Trova il valore più vicino nella mappatura
    tempi_ordinati = sorted(TEMPO_ESERCIZI.keys())
    for t in tempi_ordinati:
        if tempo_minuti <= t:
            return TEMPO_ESERCIZI[t]
    return TEMPO_ESERCIZI[tempi_ordinati[-1]]


def _seleziona_esercizi(esercizi_disponibili: list, num_esercizi: int) -> list:
    """Seleziona un mix bilanciato di esercizi da gruppi muscolari diversi.

    Cerca di coprire quanti più gruppi muscolari possibile senza ripetere
    lo stesso gruppo consecutivamente.

    Args:
        esercizi_disponibili: Lista degli esercizi filtrati.
        num_esercizi: Numero di esercizi da selezionare.

    Returns:
        Lista di esercizi selezionati.
    """
    if len(esercizi_disponibili) <= num_esercizi:
        return esercizi_disponibili[:num_esercizi]

    # Raggruppa per gruppo muscolare
    gruppi = {}
    for ex in esercizi_disponibili:
        g = ex["gruppo"]
        if g not in gruppi:
            gruppi[g] = []
        gruppi[g].append(ex)

    # Mescola dentro ogni gruppo
    for g in gruppi:
        random.shuffle(gruppi[g])

    # Seleziona alternando tra gruppi per varietà muscolare
    selezionati = []
    nomi_gruppi = list(gruppi.keys())
    random.shuffle(nomi_gruppi)
    idx = 0

    while len(selezionati) < num_esercizi:
        gruppo = nomi_gruppi[idx % len(nomi_gruppi)]
        if gruppi[gruppo]:
            ex = gruppi[gruppo].pop(0)
            # Evita duplicati
            if ex["nome"] not in [s["nome"] for s in selezionati]:
                selezionati.append(ex)
        idx += 1

        # Sicurezza: se abbiamo fatto troppe iterazioni, esci
        if idx > num_esercizi * 3 + len(esercizi_disponibili):
            break

    return selezionati


def _adatta_volume(esercizi: list, energia: str) -> list:
    """Adatta serie, ripetizioni e durata in base al livello di energia.

    Args:
        esercizi: Lista di esercizi selezionati.
        energia: "Alta", "Media" o "Bassa".

    Returns:
        Lista di esercizi con volume adattato.
    """
    molt = MOLTIPLICATORE_ENERGIA.get(energia, MOLTIPLICATORE_ENERGIA["Media"])
    risultato = []

    for ex in esercizi:
        ex_adattato = deepcopy(ex)

        # Adatta le serie
        serie_base = ex_adattato["serie_default"]
        ex_adattato["serie"] = max(1, round(serie_base * molt["serie"]))

        # Adatta ripetizioni o durata
        if ex_adattato["reps_default"] is not None:
            reps_base = ex_adattato["reps_default"]
            ex_adattato["reps"] = max(4, round(reps_base * molt["reps"]))
            ex_adattato["durata"] = None
        elif ex_adattato["durata_default"] is not None:
            durata_base = ex_adattato["durata_default"]
            ex_adattato["durata"] = max(10, round(durata_base * molt["durata"] / 5) * 5)
            ex_adattato["reps"] = None
        else:
            ex_adattato["reps"] = ex_adattato.get("reps_default")
            ex_adattato["durata"] = ex_adattato.get("durata_default")

        risultato.append(ex_adattato)

    return risultato


def formatta_esercizio(ex: dict) -> str:
    """Formatta un esercizio in stringa leggibile.

    Args:
        ex: Dizionario dell'esercizio con campi adattati.

    Returns:
        Stringa formattata, es. "Squat — 3×12" o "Plank — 3×30s".
    """
    nome = ex["nome"]
    serie = ex.get("serie", ex["serie_default"])

    if ex.get("reps") is not None:
        return f"{nome} — {serie}×{ex['reps']}"
    elif ex.get("durata") is not None:
        return f"{nome} — {serie}×{ex['durata']}s"
    else:
        return nome


def genera_opzioni(tempo_minuti: int, energia: str, profilo: dict) -> dict:
    """Genera le 3 opzioni di allenamento (A, B, C).

    Args:
        tempo_minuti: Tempo disponibile in minuti (10-60).
        energia: Livello di energia ("Alta", "Media", "Bassa").
        profilo: Dizionario del profilo utente (serve per attrezzatura).

    Returns:
        Dizionario con chiavi "A", "B", "C", ciascuna contenente:
        - "nome": nome descrittivo dell'opzione
        - "esercizi": lista di esercizi adattati
        - "esercizi_formattati": lista di stringhe formattate
    """
    # Recupera attrezzatura disponibile dal profilo
    attrezzatura = profilo.get("attrezzatura", [])
    if not attrezzatura:
        attrezzatura = ["nessuna"]

    num_esercizi = _calcola_num_esercizi(tempo_minuti)
    opzioni = {}

    for lettera, categoria in OPZIONE_CATEGORIA.items():
        # 1. Prendi tutti gli esercizi della categoria
        tutti = get_esercizi_per_categoria(categoria)

        # 2. Filtra per attrezzatura disponibile
        disponibili = get_esercizi_per_attrezzatura(tutti, attrezzatura)

        # 3. Seleziona il numero giusto di esercizi
        selezionati = _seleziona_esercizi(disponibili, num_esercizi)

        # 4. Adatta volume in base all'energia
        adattati = _adatta_volume(selezionati, energia)

        # 5. Formatta per la visualizzazione
        formattati = [formatta_esercizio(ex) for ex in adattati]

        opzioni[lettera] = {
            "nome": NOMI_OPZIONI[lettera],
            "esercizi": adattati,
            "esercizi_formattati": formattati,
        }

    return opzioni
