#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# @Time    : 2021/7/20 10:00

python3.9 predict_system.py \
--image_dir \
/Users/zihua.zeng/Workspace/EnglishPaperTranslation/assets/page0.pdf \
--recovery \
True \
--use_pdf2docx_api \
False \
--output \
output \
--layout_model_dir \
pretrained_models/picodet_lcnet_x1_0_fgd_layout_infer \
--det_model_dir \
pretrained_models/en_PP-OCRv3_det_slim_infer \
--rec_model_dir \
pretrained_models/en_PP-OCRv3_rec_slim_infer \
--table_model_dir \
pretrained_models/en_ppocr_mobile_v2.0_table_structure_infer