import onnx
from onnxmltools.convert import convert_coreml
from onnxmltools.convert import convert_keras
from onnxmltools.convert import convert_lightgbm
from onnxmltools.convert import convert_sklearn
from onnxmltools.convert import convert_sparkml
from onnxmltools.convert import convert_tensorflow
from onnxmltools.convert import convert_xgboost


class FrameworkMixin():

    def __init__(self):
        raise(TypeError("Cannot instantiate abstract class"))

    def load(self, path):
        return self.loader(path)

    def convert(self, model):
        return self.converter(model)


class CoreML(FrameworkMixin):

    def __init__(self):
        pass

    def load(self, path):
        raise(NotImplementedError)

    def convert(self, model):
        raise(NotImplementedError)


class Keras(FrameworkMixin):

    def __init__(self):
        """Attempt to load the Keras framework and set variables for parent
           class methods
        """
        try:
            import keras
        except ImportError:
            raise RuntimeError("keras is not installed. Please install keras to use this feature")

        self.loader = keras.models.load_model
        self.converter = convert_keras


class LightGBM(FrameworkMixin):

    def __init__(self):
        pass

    def load(self, path):
        raise(NotImplementedError)

    def convert(self, model):
        raise(NotImplementedError)


class SKLearn(FrameworkMixin):

    def __init__(self):
        pass

    def load(self, path):
        raise(NotImplementedError)

    def convert(self, model):
        raise(NotImplementedError)


class SparkML(FrameworkMixin):

    def __init__(self):
        pass

    def load(self, path):
        raise(NotImplementedError)

    def convert(self, model):
        raise(NotImplementedError)


class Tensorflow(FrameworkMixin):

    def __init__(self):
        pass

    def load(self, path):
        raise(NotImplementedError)

    def convert(self, model):
        raise(NotImplementedError)


class XGBoost(FrameworkMixin):

    def __init__(self):
        """Attempt to load the XGBoost framework and set variables for parent
           class methods
        """
        try:
            import xgboost
        except ImportError:
            raise RuntimeError("xgboost is not installed. Please install"
                               "xgboost to use this feature")
        #TODO: Test this class
        bst = xgboost.Booster({'nthread':4})
        self.loader = bst.load_model
        self.converter = convert_xgboost


framework_lkp = {
    "coreml": CoreML,
    "keras": Keras,
    "lightgbm": LightGBM,
    "sklearn": SKLearn,
    "sparkml": SparkML,
    "tensorflow": Tensorflow,
    "xgboost": XGBoost
}


def handler(args):
    Framework = framework_lkp[args.framework]
    framework = Framework()
    input_model = framework.load(args.path)
    onnx_model = framework.convert(input_model)
    onnx.save_model(onnx_model, "model.onnx")
