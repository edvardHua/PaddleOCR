# -*- coding: utf-8 -*-
# @Time : 2023/7/13 15:17
# @Author : zihua.zeng
# @File : res_to_md.py

import os

import cv2
from test_translation import en_to_cn


def res2md(res, md_path, translate=False):
    f = open(md_path, "w")

    for i in range(len(res)):
        print(i, len(res))
        cur = res[i]

        if cur['type'] == "title":
            text_content = ""
            for row in cur['res']:
                text_content += row['text']

            f.write("# " + text_content)

            if translate:
                cn_text_content = en_to_cn(text_content)

                f.write("\n")
                f.write("# " + cn_text_content)

        if cur['type'] == "text":
            text_content = ""
            for row in cur['res']:
                text_content += row['text']

            f.write(text_content)

            if translate:
                cn_text_content = en_to_cn(text_content)
                f.write("\n")
                f.write(cn_text_content)

        if cur['type'] == "figure":
            basepath = os.path.split(md_path)[0]
            img_path = os.path.join(basepath, "%d.jpg" % i)
            cv2.imwrite(img_path, cur['img'])
            f.write("\n")
            f.write("![](%s)" % ("%d.jpg" % i))
            f.write("\n")

        if cur['type'] == "table":
            basepath = os.path.split(md_path)[0]
            img_path = os.path.join(basepath, "%d.jpg" % i)
            cv2.imwrite(img_path, cur['img'])
            f.write("\n")
            f.write("![](%s)" % ("%d.jpg" % i))
            f.write("\n")

        # 每写完一段，换行
        f.write("\n")

    # 最后关闭
    f.close()


if __name__ == '__main__':
    pass
