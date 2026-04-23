import pandas as pd
import numpy as np
import os
import codecs
import matplotlib.pyplot as plt
from datetime import datetime

class PortfolioAnalyzer:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.positions = None
        self.closed_trades = None

    def detect_utf8_bom(self):
        with open(self.csv_file, 'rb') as f:
            raw_data = f.read(4)
        return raw_data[:3] == b'\xef\xbb\xbf'  # UTF-8 BOM

    def read_csv(self):
        if self.detect_utf8_bom():
            with codecs.open(self.csv_file, 'r', encoding='utf-8-sig') as f:
                return pd.read_csv(f)
        else:
            return pd.read_csv(self.csv_file)

    def parse_positions(self):
        data = self.read_csv()
        self.positions = data[data['Type'] == 'Position']

    def parse_closed_trades(self):
        data = self.read_csv()
        self.closed_trades = data[data['Type'] == 'Closed']

    def analyze_portfolio(self):
        self.parse_positions()
        self.parse_closed_trades()

        total_value = self.positions['Value'].sum()
        total_closed = self.closed_trades['Value'].sum()
        print(f'Total Portfolio Value: ${total_value:.2f}')
        print(f'Total Closed Trades Value: ${total_closed:.2f}')

        # Additional analysis can be added here, such as visualizations.

    def daily_import_workflow(self):
        current_date = datetime.now().strftime('%Y-%m-%d')
        import_file = f'data/fidelity_data_{current_date}.csv'
        if os.path.exists(import_file):
            self.csv_file = import_file
            self.analyze_portfolio()
        else:
            print(f'No data file for {current_date}.')

if __name__ == '__main__':
    analyzer = PortfolioAnalyzer('data/fidelity_data.csv')
    analyzer.daily_import_workflow()