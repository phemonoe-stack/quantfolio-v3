import pandas as pd
import numpy as np
import chardet

class FidelityDataHandler:
    def __init__(self, positions_file, closed_trades_file):
        self.positions_file = positions_file
        self.closed_trades_file = closed_trades_file

    def detect_encoding(self, file_path):
        with open(file_path, 'rb') as f:
            rawdata = f.read()
            result = chardet.detect(rawdata)
            encoding = result['encoding']
        return encoding

    def load_positions(self):
        encoding = self.detect_encoding(self.positions_file)
        try:
            df_positions = pd.read_csv(self.positions_file, encoding=encoding)
            return df_positions
        except Exception as e:
            print(f"Error loading positions: {e}")
            return None

    def load_closed_trades(self):
        encoding = self.detect_encoding(self.closed_trades_file)
        try:
            df_closed_trades = pd.read_csv(self.closed_trades_file, encoding=encoding)
            return df_closed_trades
        except Exception as e:
            print(f"Error loading closed trades: {e}")
            return None

    def convert_currency(self, amount, from_currency, to_currency, conversion_rate):
        if from_currency == to_currency:
            return amount
        return amount * conversion_rate

    def handle_data(self):
        positions = self.load_positions()
        closed_trades = self.load_closed_trades()
        
        if positions is not None:
            # Process positions data
            print(positions.head())
        if closed_trades is not None:
            # Process closed trades data
            print(closed_trades.head())
