# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0

import itertools

from models_hub_common.constants import test_device


def get_models_list(file_name: str):
    models = []
    with open(file_name) as f:
        for model_info in f:
            model_name, model_link = model_info.split(',')
            models.append((model_name, model_link))
    return models


def get_params(ie_device=None):
    ie_device_params = ie_device if ie_device else test_device

    test_args = []
    for element in itertools.product(ie_device_params):
        test_args.append(element)
    return test_args
