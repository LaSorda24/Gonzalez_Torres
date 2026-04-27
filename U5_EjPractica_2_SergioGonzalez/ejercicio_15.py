import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential


def main() -> None:
    ventas: np.ndarray = np.array(
        [12000, 13500, 14200, 15000, 14800, 15500, 16000, 15800, 16200, 17000, 17500, 19000],
        dtype=float,
    )
    escala: float = 20000.0

    tf.random.set_seed(7)
    entradas: np.ndarray = ventas[:-1] / escala
    salidas: np.ndarray = ventas[1:] / escala

    modelo: Sequential = Sequential(
        [
            Dense(8, activation="relu", input_shape=(1,)),
            Dense(1),
        ]
    )
    modelo.compile(optimizer="adam", loss="mse")
    modelo.fit(entradas, salidas, epochs=300, verbose=0)

    ultima_venta_normalizada: np.ndarray = np.array([[ventas[-1] / escala]])
    prediccion_normalizada: float = float(
        modelo.predict(ultima_venta_normalizada, verbose=0)[0][0]
    )
    prediccion: float = prediccion_normalizada * escala

    print(f"Predicción de ventas para el próximo mes: {prediccion:.0f} €")


if __name__ == "__main__":
    main()
