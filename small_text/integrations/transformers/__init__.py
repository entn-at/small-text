from small_text.integrations.pytorch.exceptions import PytorchNotFoundError

try:
    from small_text.integrations.transformers.classifiers.classification import (
        transformers_collate_fn,
        FineTuningArguments,
        TransformerModelArguments,
        TransformerBasedClassification,
        TransformerBasedEmbeddingMixin
    )
    from small_text.integrations.transformers.classifiers.setfit import SetFitClassification
    from small_text.integrations.transformers.classifiers.factories import (
        SetFitClassificationFactory,
        TransformerBasedClassificationFactory
    )
    from small_text.integrations.transformers.datasets import (
        TransformersDataset,
        TransformersDatasetView
    )
    __all__ = [
        'transformers_collate_fn',
        'FineTuningArguments',
        'TransformerModelArguments',
        'TransformerBasedClassification',
        'TransformerBasedEmbeddingMixin',
        'SetFitClassification',
        'TransformerBasedClassificationFactory',
        'SetFitClassificationFactory',
        'TransformersDataset',
        'TransformersDatasetView'
    ]
except PytorchNotFoundError:
    __all__ = []
