import os
import ember
import joblib
import numpy as np

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
from tensorflow.keras.models import load_model
from tensorflow.keras.metrics import Metric, Precision, Recall
from tensorflow.keras.optimizers import Adam


class F1Score(Metric):
    def __init__(self, name="f1_score", **kwargs):
        super(F1Score, self).__init__(name=name, **kwargs)
        self.precision = Precision()
        self.recall = Recall()

    def update_state(self, y_true, y_pred, sample_weight=None):
        self.precision.update_state(y_true, y_pred, sample_weight)
        self.recall.update_state(y_true, y_pred, sample_weight)

    def result(self):
        precision = self.precision.result()
        recall = self.recall.result()
        return 2 * ((precision * recall) / (precision + recall + 1e-7))

    def reset_states(self):
        self.precision.reset_state()
        self.recall.reset_state()


def predict(sample_data, model_path=None, scaler_path=None):

    if model_path == None:
        model_path = "../model/model.h5"

    if scaler_path == None:
        scaler_path = "../model/scaler.pkl"

    # reconstruct model
    optimizer = Adam(
        learning_rate=0.0006716158100899978,
        beta_1=0.04493023214809211,
        beta_2=0.9674842399450305,
    )

    model = load_model(model_path, compile=False)

    model.compile(
        loss="binary_crossentropy",
        optimizer=optimizer,
        metrics=[
            "accuracy",
            Precision(),
            Recall(),
            F1Score(),
        ],
    )

    extractor = ember.PEFeatureExtractor(2)

    sample_data = np.array(
        extractor.feature_vector(sample_data),
        dtype=np.float32,
    ).reshape(1, -1)

    # load scaler
    scaler = joblib.load(scaler_path)
    sample_data = scaler.transform(sample_data)

    return (model.predict(sample_data, verbose=0)[0])[0]
