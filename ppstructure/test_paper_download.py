# -*- coding: utf-8 -*-
# @Time : 2023/7/13 18:27
# @Author : zihua.zeng
# @File : test_paper_download.py
#
# 下载 arixv 的论文，转换成图片，储存下来
#

import os
import arxiv
import pandas as pd

out_path = "pdf_files"
os.makedirs(out_path, exist_ok=True)

df = pd.read_csv("arxiv_list.csv")

for i in range(len(df)):
    print(i, len(df))
    pdf_id = str(df['PDF'][i])
    paper = next(arxiv.Search(id_list=[pdf_id]).results())
    # Download the PDF to the PWD with a custom filename.
    paper.download_pdf(dirpath=out_path)
