import logging
import onnxmltools
from keras.models import load_model
from coremltools.utils import load_spec
from sklearn.externals.joblib import load as load_sklearn
from lightgbm import Booster as LightGBMModel
from xgboost import Booster as XGBoostModel


logger = logging.getLogger("onnx")


def external_framework_factory(framework):
    """
    """
    framework_lkp = {
        "keras": KerasFramework,
        "coreml": ,
        "keras": ,
        "lightgbm": ,
        "sklearn": ,
        "sparkml": ,
        "tensorflow": ,
        "xgboost": 
    }
    return framework_lkp.get(framework)


class BaseFramework():

    @staticmethod
    def load_external_model():
        raise NotImplementedError("Method should be called from subclass")

    @staticmethod
    def convert_external_model():
        raise NotImplementedError("Method should be called from subclass")

    @staticmethod
    def save_model(model, path):
        onnxmltools.utils.save_model(model, path)


class KerasFramework(BaseFramework):

    @staticmethod
    def load_external_model(path):
        model = load_model(path)
        return model

    @classmethod
    def convert_external_model(cls, input_path, output_path):
        external_model = cls.load_external_model(input_path)
        model = onnxmltools.convert_keras(external_model)
        cls.save_model(model, output_path)


class CoreMLFramework(BaseFramework):

    @staticmethod
    def load_external_model(path):
        model = load_spec(path)
        return model

    @classmethod
    def convert_external_model(cls, input_path, output_path):
        external_model = cls.load_external_model(input_path)
        model = onnxmltools.convert_coreml(external_model)
        cls.save_model(model, output_path)


class SklearnFramework(BaseFramework):

    @staticmethod
    def load_external_model(path):
        model = load_sklearn(path)
        return model

    @classmethod
    def convert_external_model(cls, input_path, output_path):
        external_model = cls.load_external_model(input_path)
        model = onnxmltools.convert_sklearn(external_model)
        cls.save_model(model, output_path)


class LightGBMFramework(BaseFramework):

    @staticmethod
    def load_external_model(path):
        model = LightGBMModel(model_file=path)
        return model

    @classmethod
    def convert_external_model(cls, input_path, output_path):
        external_model = cls.load_external_model(input_path)
        model = onnxmltools.convert_lightgbm(external_model)
        cls.save_model(model, output_path)


class XGBoostFramework(BaseFramework):

    @staticmethod
    def load_external_model(path):
        model = XGBoostModel(path)
        return model

    @classmethod
    def convert_external_model(cls, input_path, output_path):
        external_model = cls.load_external_model(input_path)
        model = onnxmltools.convert_xgboost(external_model)
        cls.save_model(model, output_path)

"""
class SparkMLFramework(BaseFramework):

    @staticmethod
    def load_external_model():
        pass

    @classmethod
    def convert_external_model(cls, input_path, output_path):
        external_model = cls.load_external_model(input_path)
        model = onnxmltools.convert_sparkml(external_model)
        cls.save_model(model, output_path)


class TensorflowFramework(BaseFramework):

    @staticmethod
    def load_external_model():
        pass

    @classmethod
    def convert_external_model(cls, input_path, output_path):
        external_model = cls.load_external_model(input_path)
        model = onnxmltools.convert_tensorflow(external_model)
        cls.save_model(model, output_path)
"""
