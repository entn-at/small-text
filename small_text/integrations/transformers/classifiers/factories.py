from small_text.classifiers.factories import AbstractClassifierFactory
from small_text.integrations.transformers.classifiers.classification import \
    TransformerBasedClassification
from small_text.integrations.transformers.classifiers.setfit import SetFitClassification


class TransformerBasedClassificationFactory(AbstractClassifierFactory):

    def __init__(self, transformer_model_args, num_classes, kwargs={}):
        """
        Parameters
        ----------
        transformer_model_args : TransformerModelArguments
            Name of the sentence transformer model.
        num_classes : int
            Number of classes.
        kwargs : dict
            Keyword arguments which will be passed to `TransformerBasedClassification`.
        """
        self.transformer_model_args = transformer_model_args
        self.num_classes = num_classes
        self.kwargs = kwargs

    def new(self):
        return TransformerBasedClassification(self.transformer_model_args,
                                              self.num_classes,
                                              **self.kwargs)


class SetFitClassificationFactory(AbstractClassifierFactory):

    def __init__(self, setfit_model_args, num_classes, classification_kwargs={}):
        """
        Parameters
        ----------
        setfit_model_args : SetFitModelArguments
            Name of the sentence transformer model.
        num_classes : int
            Number of classes.
        classification_kwargs : dict
            Keyword arguments which will be passed to `SetFitClassification`.
        """
        self.setfit_model_args = setfit_model_args
        self.num_classes = num_classes
        self.classification_kwargs = classification_kwargs

    def new(self):
        return SetFitClassification(self.setfit_model_args,
                                    self.num_classes,
                                    **self.classification_kwargs)
