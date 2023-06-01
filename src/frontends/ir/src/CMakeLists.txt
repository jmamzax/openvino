# Copyright (C) 2018-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
#

ov_add_frontend(NAME ir
                FILEDESCRIPTION "FrontEnd to load OpenVINO IR file format"
                LINK_LIBRARIES openvino::pugixml
                               # TODO: remove dependency below in CVS-69781
                               openvino::runtime::dev)

if(WIN32)
    target_link_options(openvino_ir_frontend PRIVATE /PDBALTPATH:$<TARGET_PDB_FILE_NAME:openvino_ir_frontend>)
endif()