import autofl
import fl.backends.tensorflow.tff as tensorflow

tensor_model = tensorflow.TensorFlowFederated(clients = 10)

import fl
import fl.backends.pytorch.pytorchfed as pytorch

torch_model = pytorch.PytorchFederated(clients = 10)