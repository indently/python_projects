from dataclasses import dataclass


@dataclass
class Prediction:
    value: float
    r2_score: float
    slope: float
    intercept: float
    mean_absolute_error: float

    def __str__(self):
        return f'Prediction: {self.value:.2f} ({self.r2_score:.2%})'
