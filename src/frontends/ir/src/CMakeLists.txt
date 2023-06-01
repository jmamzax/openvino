# Copyright (C) 2018-2024 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
#

ov_add_frontend(NAME ir
                FILEDESCRIPTION "FrontEnd to load OpenVINO IR file format"
                LINK_LIBRARIES openvino::pugixml
                               openvino::core::dev)
if(WIN32)
    target_link_options(openvino_ir_frontend PRIVATE /PDBALTPATH:$<TARGET_PDB_FILE_NAME:openvino_ir_frontend>)
endif()
