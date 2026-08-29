from src.utils.helpers import calculate_average

numbers = [10, 20, 30, 40, 50]

average = calculate_average(numbers)

print(average)







def calculate_accuracy(
    correct_predictions: int,
    total_predictions: int
) -> float:

    return correct_predictions / total_predictions
accuracy = calculate_accuracy(
    correct_predictions=90,
    total_predictions=100
)

print(accuracy) 










#import pandas as pd
#from src.data.processor import process_data
#processed_data = process_data('data')









import pandas as pd


def load_data(
    file_path: str
) -> pd.DataFrame:

    try:
        data = pd.read_csv(file_path)
        return data

    except FileNotFoundError:
        print(
            f"Файл {file_path} не найден!"
        )

        return pd.DataFrame()












    
from src.models.model import SimpleModel


model = SimpleModel(
    model_name="My First Model"
)

model.train()

model.predict()













from src.models.model import ModelTrainer 

trainer = ModelTrainer(
    model_name="Customer Churn Model",
    version="v1"
)

trainer.train()

print(
    trainer.get_info()

)










from src.utils.logger import setup_logger


logger = setup_logger()

logger.info("Приложение запущено")
logger.warning("Внимание!")
logger.error("Произошла ошибка")












from src.models.model import SimpleModel
from src.utils.logger import setup_logger


def main():

    logger = setup_logger()

    logger.info(
        "ML Engineering application started"
    )

    model = SimpleModel(
        model_name="Customer Churn Model"
    )

    model.train()

    model.predict()

    logger.info(
        "Application finished successfully"
    )


if __name__ == "__main__":
    main()