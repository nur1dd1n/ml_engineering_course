class SimpleModel:

    def __init__(
        self,
        model_name: str
    ):
        self.model_name = model_name

    def train(self):
        print(
            f"{self.model_name}: обучение началось"
        )

    def predict(self):
        print(
            f"{self.model_name}: прогнозирование"
        )















class ModelTrainer:

    def __init__(
        self,
        model_name: str,
        version: str
    ):
        self.model_name = model_name
        self.version = version
        self.is_trained = False

    def train(self):
        print(
            f"Training {self.model_name}"
        )

        self.is_trained = True

    def get_info(self):
        return {
            "model_name": self.model_name,
            "version": self.version,
            "is_trained": self.is_trained
        }
    
trainer = ModelTrainer(
    model_name="Customer Churn Model",
    version="v1"
)

trainer.train()

print(
    trainer.get_info()
)