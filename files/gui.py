import tkinter as tk
from tkinter import messagebox, ttk

from auth import login
from voti import calcola_medie


class ClasseVivaApp(tk.Tk):
    BG = "#f4f6fb"
    CARD = "#ffffff"
    HEADER = "#1f2937"
    ACCENT = "#2563eb"
    ACCENT_HOVER = "#1d4ed8"
    TEXT = "#111827"
    MUTED = "#6b7280"
    BORDER = "#dbe2ef"
    SUCCESS = "#15803d"
    WARNING = "#b45309"
    DANGER = "#b91c1c"

    def __init__(self):
        super().__init__()
        self.title("ClasseViva — Medie")
        self.geometry("920x680")
        self.minsize(860, 620)
        self.configure(bg=self.BG)

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.show_password_var = tk.BooleanVar(value=False)
        self.quadrimestre_var = tk.IntVar(value=1)
        self.status_var = tk.StringVar(value="Pronto.")
        self.summary_media_var = tk.StringVar(value="—")
        self.summary_voti_var = tk.StringVar(value="—")
        self.summary_materie_var = tk.StringVar(value="—")

        self._build_styles()
        self._build_ui()

    def _build_styles(self):
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure("App.TFrame", background=self.BG)
        style.configure("Card.TFrame", background=self.CARD, borderwidth=1, relief="solid")
        style.configure("Header.TFrame", background=self.HEADER)

        style.configure("Title.TLabel", background=self.HEADER, foreground="white", font=("Segoe UI", 20, "bold"))
        style.configure("Subtitle.TLabel", background=self.HEADER, foreground="#d1d5db", font=("Segoe UI", 10))
        style.configure("Section.TLabel", background=self.BG, foreground=self.TEXT, font=("Segoe UI", 11, "bold"))
        style.configure("CardTitle.TLabel", background=self.CARD, foreground=self.TEXT, font=("Segoe UI", 11, "bold"))
        style.configure("CardText.TLabel", background=self.CARD, foreground=self.MUTED, font=("Segoe UI", 9))
        style.configure("Form.TLabel", background=self.CARD, foreground=self.TEXT, font=("Segoe UI", 10))
        style.configure("SummaryLabel.TLabel", background=self.CARD, foreground=self.MUTED, font=("Segoe UI", 9))
        style.configure("SummaryValue.TLabel", background=self.CARD, foreground=self.TEXT, font=("Segoe UI", 16, "bold"))
        style.configure("Status.TLabel", background=self.BG, foreground=self.MUTED, font=("Segoe UI", 9))
        style.configure("Accent.TButton", font=("Segoe UI", 10, "bold"), padding=(14, 10))
        style.map("Accent.TButton", background=[("active", self.ACCENT_HOVER), ("!active", self.ACCENT)])

        style.configure("Modern.TRadiobutton", background=self.CARD, foreground=self.TEXT, font=("Segoe UI", 10))
        style.configure("Treeview", rowheight=28, font=("Segoe UI", 10), background="white", fieldbackground="white")
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

    def _build_ui(self):
        root = ttk.Frame(self, style="App.TFrame", padding=18)
        root.pack(fill="both", expand=True)

        self._build_header(root)
        self._build_stats(root)
        self._build_form(root)
        self._build_results(root)
        self._build_footer(root)

    def _build_header(self, parent):
        header = ttk.Frame(parent, style="Header.TFrame", padding=20)
        header.pack(fill="x")

        title_row = ttk.Frame(header, style="Header.TFrame")
        title_row.pack(fill="x")

        icon = tk.Label(
            title_row,
            text="📊",
            bg=self.HEADER,
            fg="white",
            font=("Segoe UI Emoji", 24),
        )
        icon.pack(side="left", padx=(0, 14))

        text_box = ttk.Frame(title_row, style="Header.TFrame")
        text_box.pack(side="left", fill="x", expand=True)

        ttk.Label(text_box, text="ClasseViva — Medie", style="Title.TLabel").pack(anchor="w")
        ttk.Label(
            text_box,
            text="Accedi con le tue credenziali, scegli il quadrimestre e visualizza le medie in una tabella ordinata.",
            style="Subtitle.TLabel",
            wraplength=760,
        ).pack(anchor="w", pady=(6, 0))

    def _build_stats(self, parent):
        stats_wrap = ttk.Frame(parent, style="App.TFrame")
        stats_wrap.pack(fill="x", pady=(16, 0))

        cards = ttk.Frame(stats_wrap, style="App.TFrame")
        cards.pack(fill="x")

        self._make_stat_card(cards, "MEDIA GENERALE", self.summary_media_var, 0)
        self._make_stat_card(cards, "VOTI TOTALE", self.summary_voti_var, 1)
        self._make_stat_card(cards, "MATERIE", self.summary_materie_var, 2)

        cards.columnconfigure(0, weight=1)
        cards.columnconfigure(1, weight=1)
        cards.columnconfigure(2, weight=1)

    def _make_stat_card(self, parent, label, variable, column):
        card = ttk.Frame(parent, style="Card.TFrame", padding=16)
        card.grid(row=0, column=column, sticky="nsew", padx=(0 if column == 0 else 12, 0))
        ttk.Label(card, text=label, style="SummaryLabel.TLabel").pack(anchor="w")
        ttk.Label(card, textvariable=variable, style="SummaryValue.TLabel").pack(anchor="w", pady=(6, 0))

    def _build_form(self, parent):
        form = ttk.Frame(parent, style="Card.TFrame", padding=18)
        form.pack(fill="x", pady=(16, 0))

        header_row = ttk.Frame(form, style="Card.TFrame")
        header_row.pack(fill="x", pady=(0, 10))
        ttk.Label(header_row, text="Accesso", style="CardTitle.TLabel").pack(side="left")
        ttk.Label(header_row, text="Inserisci le credenziali ClasseViva.", style="CardText.TLabel").pack(side="left", padx=(10, 0))

        grid = ttk.Frame(form, style="Card.TFrame")
        grid.pack(fill="x")
        grid.columnconfigure(1, weight=1)

        ttk.Label(grid, text="Username", style="Form.TLabel").grid(row=0, column=0, sticky="w", pady=8, padx=(0, 14))
        ttk.Entry(grid, textvariable=self.username_var, width=34).grid(row=0, column=1, sticky="we", pady=8)

        ttk.Label(grid, text="Password", style="Form.TLabel").grid(row=1, column=0, sticky="w", pady=8, padx=(0, 14))
        password_entry = ttk.Entry(grid, textvariable=self.password_var, width=34, show="*")
        password_entry.grid(row=1, column=1, sticky="we", pady=8)

        ttk.Checkbutton(
            grid,
            text="Mostra password",
            variable=self.show_password_var,
            command=lambda: self._toggle_password(password_entry),
            style="Modern.TRadiobutton",
        ).grid(row=2, column=1, sticky="w", pady=(0, 8))

        ttk.Label(grid, text="Quadrimestre", style="Form.TLabel").grid(row=3, column=0, sticky="w", pady=8, padx=(0, 14))
        q_frame = ttk.Frame(grid, style="Card.TFrame")
        q_frame.grid(row=3, column=1, sticky="w", pady=8)
        ttk.Radiobutton(q_frame, text="Primo", variable=self.quadrimestre_var, value=1, style="Modern.TRadiobutton").pack(side="left")
        ttk.Radiobutton(q_frame, text="Secondo", variable=self.quadrimestre_var, value=2, style="Modern.TRadiobutton").pack(side="left", padx=(14, 0))

        actions = ttk.Frame(form, style="Card.TFrame")
        actions.pack(fill="x", pady=(14, 0))

        self.login_button = ttk.Button(actions, text="Accedi e carica voti", command=self._on_login, style="Accent.TButton")
        self.login_button.pack(side="left")

        ttk.Label(actions, text="La tabella si aggiorna dopo il login.", style="CardText.TLabel").pack(side="left", padx=14)

    def _build_results(self, parent):
        results = ttk.Frame(parent, style="Card.TFrame", padding=18)
        results.pack(fill="both", expand=True, pady=(16, 0))

        header = ttk.Frame(results, style="Card.TFrame")
        header.pack(fill="x")
        ttk.Label(header, text="Risultati", style="CardTitle.TLabel").pack(side="left")
        ttk.Label(header, text="Medie per materia e riepilogo generale.", style="CardText.TLabel").pack(side="left", padx=(10, 0))

        columns = ("materia", "voti", "media", "stato")
        self.tree = ttk.Treeview(results, columns=columns, show="headings", height=14)
        self.tree.heading("materia", text="Materia")
        self.tree.heading("voti", text="Voti")
        self.tree.heading("media", text="Media")
        self.tree.heading("stato", text="Stato")
        self.tree.column("materia", width=400, anchor="w")
        self.tree.column("voti", width=90, anchor="center")
        self.tree.column("media", width=100, anchor="center")
        self.tree.column("stato", width=90, anchor="center")
        self.tree.pack(fill="both", expand=True, pady=(14, 0))

        self.tree.tag_configure("high", foreground=self.SUCCESS)
        self.tree.tag_configure("medium", foreground=self.WARNING)
        self.tree.tag_configure("low", foreground=self.DANGER)

        scrollbar = ttk.Scrollbar(results, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(relx=1.0, rely=0.17, relheight=0.79, anchor="ne")

    def _build_footer(self, parent):
        footer = ttk.Frame(parent, style="App.TFrame")
        footer.pack(fill="x", pady=(10, 0))
        ttk.Label(footer, textvariable=self.status_var, style="Status.TLabel").pack(anchor="w")

    def _toggle_password(self, entry):
        entry.configure(show="" if self.show_password_var.get() else "*")

    def _set_status(self, text: str):
        self.status_var.set(text)
        self.update_idletasks()

    def _clear_results(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.summary_media_var.set("—")
        self.summary_voti_var.set("—")
        self.summary_materie_var.set("—")

    def _fill_results(self, medie: dict, conteggio: dict):
        self._clear_results()

        if not medie:
            self._set_status("Nessun voto trovato per il periodo selezionato.")
            return

        tot_voti = sum(conteggio.values())
        media_generale = round(sum(medie.values()) / len(medie), 2)

        self.summary_media_var.set(f"{media_generale:.2f}")
        self.summary_voti_var.set(str(tot_voti))
        self.summary_materie_var.set(str(len(medie)))

        for materia in sorted(medie.keys()):
            media = medie[materia]
            voti = conteggio.get(materia, 0)
            if media >= 8:
                stato = "OK"
                tag = "high"
            elif media >= 6:
                stato = "ATT"
                tag = "medium"
            else:
                stato = "RISK"
                tag = "low"

            self.tree.insert("", "end", values=(materia, voti, f"{media:.2f}", stato), tags=(tag,))

        self._set_status("Operazione completata.")

    def _on_login(self):
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()
        quadrimestre = self.quadrimestre_var.get()

        if not username:
            messagebox.showerror("Errore", "Inserisci lo username.")
            return
        if not password:
            messagebox.showerror("Errore", "Inserisci la password.")
            return

        self.login_button.configure(state="disabled")
        self._clear_results()
        self._set_status("Accesso in corso...")

        try:
            utente = login(username, password)
            self._set_status("Login riuscito. Recupero voti...")
            medie, conteggio = calcola_medie(utente, quadrimestre)
            self._fill_results(medie, conteggio)
        except Exception as exc:
            self._clear_results()
            self._set_status("Errore durante l'operazione.")
            messagebox.showerror("Errore", f"Impossibile completare l'operazione:\n{exc}")
        finally:
            self.login_button.configure(state="normal")


def run():
    app = ClasseVivaApp()
    app.mainloop()
