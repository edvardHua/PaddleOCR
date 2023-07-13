# -*- coding: utf-8 -*-
# @Time : 2023/7/13 14:37
# @Author : zihua.zeng
# @File : layout_detect.py

import os
import sys
import argparse

__dir__ = os.path.dirname(os.path.abspath(__file__))
sys.path.append(__dir__)
sys.path.insert(0, os.path.abspath(os.path.join(__dir__, '../')))

from ppstructure.layout.predict_layout import LayoutPredictor
from pprint import pprint

if __name__ == '__main__':
    args_dict = {
        'layout_dict_path': '../ppocr/utils/dict/layout_dict/layout_publaynet_dict.txt',
        'layout_score_threshold': 0.5,
        'layout_nms_threshold': 0.5,
        'layout_model_dir': 'pretrained_models/picodet_lcnet_x1_0_fgd_layout_infer',
        'use_onnx': False,
        'use_gpu': False,
        'use_npu': False,
        'use_xpu': False,
        'enable_mkldnn': False
    }
    args = argparse.Namespace(**args_dict)
    pprint(args)
    layout_predictor = LayoutPredictor(args)
