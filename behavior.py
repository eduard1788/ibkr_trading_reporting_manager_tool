from widgets import MainFrame


results = {}
class IBKROrders:
    def __init__(self, frame: MainFrame):
        self.frame = frame

    def _get_values(self, col: int):
        return {
            "symbol": self.frame.symbol_name_entries[col].get(),
            "entry": self.frame.entry_price_entries[col].get(),
            "stop": self.frame.stop_price_entries[col].get(),
            "risk_USD": self.frame.risk_usd_entries[col].get(),
            "position": self.frame.position_entries[col].get(),
            "position_based": self.frame.checkbox_r_vars[col].get(),
            "not_stp_loss": self.frame.checkbox_s_vars[col].get(),
            "short_pos": self.frame.checkbox_sh_vars[col].get(),
            "limit": self.frame.limit_price_entries[col].get(),
            "account": self.frame.dropdown_var.get(),
            "order_id": self.frame.order_id_entry_entries[col].get(),
        }

    def stop(self, col: int):
        print("STOP ORDER")
        #data = self._get_values(col)
        #self._validate_stop(data)
        #order = self._build_stop_order(data)
        #self._send_order(order)
        #self._print(col)

    def limit(self, col: int):
        print("LIMIT ORDER")
        self._print(col)

    def market(self, col: int):
        print("MARKET ORDER")
        self._print(col)

    def modify(self, col: int):
        print("MODIFY ORDER")
        self._print(col)

    def cancel(self, col: int):
        print("CANCEL ORDER")
        self._print(col)

    def _validate_stop(self, data: dict):
        pass
        #    if not data["symbol"]:
        #        raise ValueError("Symbol is required")
        #    if float(data["stop"]) <= 0:
        #        raise ValueError("Invalid stop price")

    def _build_stop_order(self, data: dict):
        pass
        #    return {
        #        "type": "STOP",
        #        "symbol": data["symbol"],
        #        "price": float(data["stop"]),
        #        "account": data["account"],
        #    }

    def _validate_limit(self, data: dict):
        pass
        #    if not data["symbol"]:
        #        raise ValueError("Symbol is required")
        #    if float(data["stop"]) <= 0:
        #        raise ValueError("Invalid stop price")

    def _build_limit_order(self, data: dict):
        pass
        #    return {
        #        "type": "LIMIT",
        #        "symbol": data["symbol"],
        #        "price": float(data["stop"]),
        #        "account": data["account"],
        #    }

    def _validate_market(self, data: dict):
        pass
        #    if not data["symbol"]:
        #        raise ValueError("Symbol is required")
        #    if float(data["stop"]) <= 0:
        #        raise ValueError("Invalid stop price")

    def _build_market_order(self, data: dict):
        pass
        #    return {
        #        "type": "MARKET",
        #        "symbol": data["symbol"],
        #        "price": float(data["stop"]),
        #        "account": data["account"],
        #    }

    def _validate_modify(self, data: dict):
        pass
        #    if not data["symbol"]:
        #        raise ValueError("Symbol is required")
        #    if float(data["stop"]) <= 0:
        #        raise ValueError("Invalid stop price")

    def _build_modify_order(self, data: dict):
        pass
        #    return {
        #        "type": "MODIFY",
        #        "symbol": data["symbol"],
        #        "price": float(data["stop"]),
        #        "account": data["account"],
        #    }

    def _validate_cancel(self, data: dict):
        pass
        #    if not data["symbol"]:
        #        raise ValueError("Symbol is required")
        #    if float(data["stop"]) <= 0:
        #        raise ValueError("Invalid stop price")

    def _build_cancel_order(self, data: dict):
        pass
        #    return {
        #        "type": "CANCEL",
        #        "symbol": data["symbol"],
        #        "price": float(data["stop"]),
        #        "account": data["account"],
        #    }

    def _send_order(self, order: dict):
        pass
        #    print("Sending order:", order)
        #    # IBKR API call here
        #

    def _print(self, col):
        values = self._get_values(col)
        for k, v in values.items():
            results[k] = v
        print(results)
    #       print(f"{k}: {v}")