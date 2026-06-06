def format_medie(medie: dict, conteggio: dict, quadrimestre: int) -> str:
    if not medie:
        return f"⚠️  Nessun voto trovato per il {quadrimestre}° quadrimestre."

    label_q = "1° QUADRIMESTRE" if quadrimestre == 1 else "2° QUADRIMESTRE"
    righe = [f"📊 Medie — {label_q}", "", f"{'MATERIA':<38} {'VOTI':>5}  {'MEDIA':>6}", "─" * 55]

    for materia in sorted(medie.keys()):
        media = medie[materia]
        n = conteggio.get(materia, 0)

        if media >= 8:
            stato = "🟢"
        elif media >= 6:
            stato = "🟡"
        else:
            stato = "🔴"

        righe.append(f"{materia:<38} {n:>5}  {media:>6.2f}  {stato}")

    media_generale = round(sum(medie.values()) / len(medie.values()), 2)
    tot_voti = sum(conteggio.values())
    stato_gen = "🟢" if media_generale >= 8 else ("🟡" if media_generale >= 6 else "🔴")
    righe.append("─" * 55)
    righe.append(f"{'MEDIA GENERALE':<38} {tot_voti:>5}  {media_generale:>6.2f}  {stato_gen}")
    return "\n".join(righe)


def stampa_medie(medie: dict, conteggio: dict, quadrimestre: int):
    print(format_medie(medie, conteggio, quadrimestre))
