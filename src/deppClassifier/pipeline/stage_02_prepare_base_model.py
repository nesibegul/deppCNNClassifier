from deppClassifier.config import ConfigurationManager
from deppClassifier.components import PrepareBaseModel
from deppClassifier import logger

STAGE_NAME = "Prepare Base Model stage"


def main():

    config = ConfigurationManager()
    prepare_base_model_config = config.get_prepare_base_model_config()
    prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
    prepare_base_model.get_base_model()
    prepare_base_model.update_base_model()



if __name__ == '__main__':
    try:
        logger.info(f"x************************************x")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
