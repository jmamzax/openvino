# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

#! [dataset]
import nncf
import tensorflow_datasets as tfds

calibration_loader = tfds.load(...)

def transform_fn(data_item):
    images, _ = data_item
    return images

calibration_dataset = nncf.Dataset(calibration_loader, transform_fn)
#! [dataset]

#! [quantization]
import tensorflow as tf
model = tf.saved_model.load("model_path")

quantized_model = nncf.quantize(model, calibration_dataset)
#! [quantization]

#! [inference]
import openvino.runtime as ov
from openvino.tools.mo import convert_model

# convert TensorFlow model to OpenVINO model
ov_quantized_model = convert_model(quantized_model)

# compile the model to transform quantized operations to int8
model_int8 = ov.compile_model(ov_quantized_model)

input_fp32 = ... # FP32 model input
res = model_int8(input_fp32)

# save the model
ov.serialize(ov_quantized_model, "quantized_model.xml")
#! [inference]
