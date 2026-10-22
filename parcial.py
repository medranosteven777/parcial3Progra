import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

print("INSPECCIÓN DE DATOS")
df = pd.read_csv('inventario.csv')

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())

print("\nPRODUCTOS EN SAN SALVADOR CON PRECIO MAYOR A 100")
print(df[(df['Sucursal'] == 'San Salvador') & (df['Precio'] >= 100.0)])


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ventana de PyQt y Matplotlib')
        self.resize(700, 500)

        df_csv = pd.read_csv('inventario.csv')
        df_agrupado = df_csv.groupby("Sucursal")["Stock"].sum()

        self.figura = Figure(figsize=(6, 4))
        self.canvas = FigureCanvas(self.figura)

        ax = self.figura.add_subplot(111)
        ax.bar(df_agrupado.index, df_agrupado.values, color='blue')
        ax.set_title("Stock por sucursal")
        ax.set_xlabel("Sucursal")
        ax.set_ylabel("Stock")

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        central = QWidget()
        central.setLayout(layout)
        self.setCentralWidget(central)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())