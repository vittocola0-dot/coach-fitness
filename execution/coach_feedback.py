"""
Coach Feedback - Coach Fitness Dinamico
=========================================
Genera feedback settimanale personalizzato basato su regole deterministiche.
Correla la variazione di peso con gli allenamenti effettivamente svolti.
"""


def genera_feedback(delta_peso: float | None,
                    num_allenamenti: int,
                    tipi_allenamento: dict,
                    settimana_num: int) -> str:
    """Genera il feedback testuale del coach per la settimana.

    Args:
        delta_peso: Variazione di peso in kg (negativo = perdita, positivo = aumento).
                   None se è la prima registrazione.
        num_allenamenti: Numero totale di allenamenti completati negli ultimi 7 giorni.
        tipi_allenamento: Dizionario con conteggio per tipo, es. {"A": 2, "B": 1, "C": 0}.
        settimana_num: Numero progressivo della settimana (1 = prima).

    Returns:
        Stringa con il feedback personalizzato del coach.
    """
    # --- Prima settimana (nessun confronto possibile) ---
    if settimana_num <= 1 or delta_peso is None:
        return (
            "🎯 **Benvenuto!** Hai registrato il tuo peso iniziale come baseline. "
            "Da questa settimana in poi potrò tracciare i tuoi progressi e darti "
            "consigli personalizzati. Inizia ad allenarti con costanza - anche "
            "2-3 sessioni a settimana fanno una grande differenza!"
        )

    # Classificazione variazione peso
    perdita_rapida = delta_peso <= -2.0
    perdita = -2.0 < delta_peso < -0.3
    stabile = -0.3 <= delta_peso <= 0.3
    aumento = 0.3 < delta_peso < 2.0
    aumento_rapido = delta_peso >= 2.0

    # Costanza allenamenti
    costante = num_allenamenti >= 3
    moderato = 1 <= num_allenamenti < 3
    inattivo = num_allenamenti == 0

    # Tipi svolti
    solo_hiit = tipi_allenamento.get("A", 0) > 0 and tipi_allenamento.get("B", 0) == 0 and tipi_allenamento.get("C", 0) == 0
    solo_stretching = tipi_allenamento.get("C", 0) > 0 and tipi_allenamento.get("A", 0) == 0 and tipi_allenamento.get("B", 0) == 0

    # Dettaglio tipi per il feedback
    dettaglio_tipi = []
    if tipi_allenamento.get("A", 0) > 0:
        dettaglio_tipi.append(f"{tipi_allenamento['A']} HIIT")
    if tipi_allenamento.get("B", 0) > 0:
        dettaglio_tipi.append(f"{tipi_allenamento['B']} Forza")
    if tipi_allenamento.get("C", 0) > 0:
        dettaglio_tipi.append(f"{tipi_allenamento['C']} Stretching")
    dettaglio_str = ", ".join(dettaglio_tipi) if dettaglio_tipi else "nessuno"

    feedback_parts = []

    # --- PERDITA RAPIDA ---
    if perdita_rapida:
        if solo_hiit:
            feedback_parts.append(
                f"⚠️ **Attenzione!** Hai perso {abs(delta_peso)} kg questa settimana, "
                f"svolgendo solo allenamenti ad alta intensità ({dettaglio_str}). "
                "Una perdita così rapida potrebbe non essere sostenibile. "
                "Se ti senti stanco o affaticato, la prossima settimana seleziona più spesso "
                "l'**Opzione B (Forza/Postura)** o **C (Stretching)** per bilanciare il recupero."
            )
        elif costante:
            feedback_parts.append(
                f"📉 Hai perso {abs(delta_peso)} kg con {num_allenamenti} allenamenti ({dettaglio_str}). "
                "La perdita è significativa - ottimo impegno! Monitora come ti senti: "
                "se hai poca energia, concediti un giorno di stretching in più."
            )
        else:
            feedback_parts.append(
                f"📉 Hai perso {abs(delta_peso)} kg ma hai fatto solo {num_allenamenti} allenamento/i. "
                "Una perdita così rapida senza allenamento regolare potrebbe dipendere "
                "da altri fattori (alimentazione, idratazione). Cerca di essere più costante!"
            )

    # --- PERDITA MODERATA ---
    elif perdita:
        if costante:
            feedback_parts.append(
                f"🎉 **Ottimo lavoro!** La bilancia segna **{delta_peso} kg** e hai completato "
                f"con costanza {num_allenamenti} allenamenti ({dettaglio_str}). "
                "Continua così, siamo sulla strada giusta!"
            )
        elif moderato:
            feedback_parts.append(
                f"👍 Bene, hai perso {abs(delta_peso)} kg! Però hai completato solo "
                f"{num_allenamenti} allenamento/i ({dettaglio_str}). "
                "Per rendere questi risultati duraturi, punta a completare almeno "
                "3 allenamenti a settimana."
            )
        else:
            feedback_parts.append(
                f"📉 Il peso è sceso di {abs(delta_peso)} kg, ma non hai completato "
                "nessun allenamento questa settimana. La perdita potrebbe non essere "
                "di grasso ma di liquidi o massa muscolare. Riprendi ad allenarti!"
            )

    # --- PESO STABILE ---
    elif stabile:
        if costante:
            feedback_parts.append(
                f"💪 Il tuo peso è rimasto stabile ({delta_peso:+.1f} kg) nonostante "
                f"{num_allenamenti} allenamenti ({dettaglio_str}). "
                "Questo potrebbe significare che il tuo corpo sta facendo "
                "**ricomposizione corporea** (più muscolo, meno grasso). Continua così!"
            )
        elif moderato:
            feedback_parts.append(
                f"⚖️ Questa settimana il tuo peso è rimasto invariato, "
                f"ma hai completato solo {num_allenamenti} allenamento/i ({dettaglio_str}). "
                "Per vedere variazioni di peso, dobbiamo cercare di essere più costanti "
                "nei prossimi giorni - punta ad almeno 3 sessioni!"
            )
        else:
            feedback_parts.append(
                "⚖️ Peso invariato e nessun allenamento completato. "
                "Per iniziare a vedere risultati, il primo passo è la costanza: "
                "prova a completare almeno 2-3 allenamenti la prossima settimana, "
                "anche solo l'Opzione C (Stretching) nei giorni più impegnativi."
            )

    # --- AUMENTO MODERATO ---
    elif aumento:
        if costante:
            feedback_parts.append(
                f"📊 Il peso è salito di {delta_peso:+.1f} kg con {num_allenamenti} "
                f"allenamenti ({dettaglio_str}). Non preoccuparti: se ti stai allenando "
                "con costanza, potrebbe essere **aumento di massa muscolare**. "
                "I muscoli pesano più del grasso! Continua così e monitora le prossime settimane."
            )
        elif moderato:
            feedback_parts.append(
                f"📊 Il peso è aumentato di {delta_peso:+.1f} kg con solo "
                f"{num_allenamenti} allenamento/i ({dettaglio_str}). "
                "Per contrastare l'aumento, cerca di aumentare la frequenza di allenamento "
                "e fai attenzione all'alimentazione."
            )
        else:
            feedback_parts.append(
                f"⚠️ Il peso è aumentato di {delta_peso:+.1f} kg e non hai completato "
                "nessun allenamento. Prova a ricominciare con sessioni brevi (15-20 min) "
                "anche a bassa intensità - l'importante è riprendere il ritmo!"
            )

    # --- AUMENTO RAPIDO ---
    elif aumento_rapido:
        feedback_parts.append(
            f"⚠️ **Attenzione:** il peso è aumentato di {delta_peso:+.1f} kg in una sola settimana. "
            "Controlla l'alimentazione e l'idratazione. Se il dato ti sembra anomalo, "
            "pesati di nuovo tra 2-3 giorni alla stessa ora e nelle stesse condizioni. "
            f"Allenamenti svolti: {num_allenamenti} ({dettaglio_str})."
        )

    # --- Suggerimento bilanciamento tipi ---
    if not (perdita_rapida and solo_hiit):  # Già gestito sopra
        if solo_hiit and num_allenamenti >= 2:
            feedback_parts.append(
                "\n💡 **Suggerimento:** Stai facendo solo sessioni HIIT. "
                "Prova ad alternare con Forza (Opzione B) per costruire muscolo "
                "e Stretching (Opzione C) per il recupero."
            )
        elif solo_stretching and num_allenamenti >= 2:
            feedback_parts.append(
                "\n💡 **Suggerimento:** Stai facendo solo stretching. È ottimo per il recupero, "
                "ma per vedere risultati sul peso prova ad aggiungere 1-2 sessioni "
                "di Forza (B) o HIIT (A) a settimana."
            )

    return "\n\n".join(feedback_parts) if feedback_parts else (
        "📋 Settimana registrata. Continua ad allenarti con costanza!"
    )
