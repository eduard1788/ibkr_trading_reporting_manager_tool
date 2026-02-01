import customtkinter


class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master, columns=1, callbacks=None):
        super().__init__(master)
        self.columns = columns
        self.callbacks = callbacks or {}

        self.pack(pady=20, padx=60, fill="both", expand=True)

        self.accounts = ["U3297495", "U4572134", "U7514316", "DU1717711", "DU2883726"]

        # ---- widget containers ----
        self.symbol_name_entries = {}
        self.risk_usd_entries = {}
        self.position_entries = {}
        self.entry_price_entries = {}
        self.stop_price_entries = {}
        self.limit_price_entries = {}
        self.order_id_entry_entries = {}

        self.checkbox_r_vars = {}
        self.checkbox_s_vars = {}
        self.checkbox_sh_vars = {}

        self.stp_buttons = {}
        self.lmt_buttons = {}
        self.mod_buttons = {}
        self.cancel_buttons = {}
        self.mkt_buttons = {}

        # ---- per-column UI ----
        for col in range(columns):
            customtkinter.CTkLabel(self, text=f"Symbol #{col+1}")\
                .grid(row=0, column=col, padx=5, pady=5, sticky="w")

            self.checkbox_r_vars[col] = customtkinter.BooleanVar()
            customtkinter.CTkCheckBox(
                self, text="Position-based",
                variable=self.checkbox_r_vars[col], width=1, height=1
            ).grid(row=1, column=col, padx=5, pady=5, sticky="w")

            self.checkbox_s_vars[col] = customtkinter.BooleanVar()
            customtkinter.CTkCheckBox(
                self, text="Not include STP loss",
                variable=self.checkbox_s_vars[col], width=1, height=1
            ).grid(row=2, column=col, padx=5, pady=5, sticky="w")

            self.checkbox_sh_vars[col] = customtkinter.BooleanVar()
            customtkinter.CTkCheckBox(
                self, text="Sell position",
                variable=self.checkbox_sh_vars[col], width=1, height=1
            ).grid(row=3, column=col, padx=5, pady=5, sticky="w")

            customtkinter.CTkLabel(self, text="")\
                .grid(row=4, column=col, padx=5, pady=5, sticky="w")

            self.symbol_name_entries[col] = customtkinter.CTkEntry(self, placeholder_text="Name")
            self.symbol_name_entries[col].grid(row=5, column=col, padx=5, pady=5, sticky="w")

            self.risk_usd_entries[col] = customtkinter.CTkEntry(self, placeholder_text="Risk USD")
            self.risk_usd_entries[col].grid(row=6, column=col, padx=5, pady=5, sticky="w")

            self.position_entries[col] = customtkinter.CTkEntry(self, placeholder_text="Position")
            self.position_entries[col].grid(row=7, column=col, padx=5, pady=5, sticky="w")

            self.entry_price_entries[col] = customtkinter.CTkEntry(self, placeholder_text="Entry")
            self.entry_price_entries[col].grid(row=8, column=col, padx=5, pady=5, sticky="w")

            self.stop_price_entries[col] = customtkinter.CTkEntry(self, placeholder_text="Stop")
            self.stop_price_entries[col].grid(row=9, column=col, padx=5, pady=5, sticky="w")

            self.stp_buttons[col] = customtkinter.CTkButton(
                self,
                text="Submit Stop Order",
                command=lambda c=col: self._emit("stop", c)
            )
            self.stp_buttons[col].grid(row=11, column=col, padx=5, pady=5, sticky="w")

            customtkinter.CTkLabel(self, text="")\
                .grid(row=13, column=col, padx=5, pady=5, sticky="w")

            self.limit_price_entries[col] = customtkinter.CTkEntry(self, placeholder_text="Limit")
            self.limit_price_entries[col].grid(row=14, column=col, padx=5, pady=5, sticky="w")

            self.lmt_buttons[col] = customtkinter.CTkButton(
                self,
                text="Submit Limit Order",
                command=lambda c=col: self._emit("limit", c)
            )
            self.lmt_buttons[col].grid(row=16, column=col, padx=5, pady=5, sticky="w")

            customtkinter.CTkLabel(self, text="")\
                .grid(row=18, column=col, padx=5, pady=5, sticky="w")

            self.order_id_entry_entries[col] = customtkinter.CTkEntry(self, placeholder_text="Order ID")
            self.order_id_entry_entries[col].grid(row=19, column=col, padx=5, pady=5, sticky="w")

            self.mod_buttons[col] = customtkinter.CTkButton(
                self,
                text="Modify Order",
                command=lambda c=col: self._emit("modify", c)
            )
            self.mod_buttons[col].grid(row=21, column=col, padx=5, pady=5, sticky="w")

            self.cancel_buttons[col] = customtkinter.CTkButton(
                self,
                text="Cancel Order",
                command=lambda c=col: self._emit("cancel", c)
            )
            self.cancel_buttons[col].grid(row=22, column=col, padx=5, pady=5, sticky="w")

            self.mkt_buttons[col] = customtkinter.CTkButton(
                self,
                text="Market Order",
                command=lambda c=col: self._emit("market", c)
            )
            self.mkt_buttons[col].grid(row=23, column=col, padx=5, pady=5, sticky="w")

        # ---- shared controls ----
        customtkinter.CTkLabel(self, text="") \
            .grid(row=24, column=0, padx=5, pady=5, sticky="w")

        self.dropdown_var = customtkinter.StringVar(value="Select account")
        customtkinter.CTkOptionMenu(
            self, variable=self.dropdown_var, values=self.accounts
        ).grid(row=25, column=0, padx=5, pady=5, sticky="w")

    def _emit(self, action: str, col: int):
        """UI → logic dispatcher"""
        if action in self.callbacks:
            self.callbacks[action](col)