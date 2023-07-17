# -*- coding: utf-8 -*-
# @Time : 2023/7/13 15:17
# @Author : zihua.zeng
# @File : res_to_md.py

import os
import re
import cv2
from test_translation import en_to_cn


def get_title_level(title):
    # 识别1, 1.1, 1.1.1
    patterns = ["^\d+", "^\d+\.\d+\s+", "^\d+\.\d+\.\d+\s+"]
    title_level = -1
    for i, pattern in enumerate(patterns):
        res = re.match(pattern, title)
        if res:
            title_level = (i + 1)
    return title_level


def res2md(res, md_path, translate=False):
    f = open(md_path, "w")
    bn = (os.path.basename(md_path)).replace(".md", "")
    jump_flag = False
    for i in range(len(res)):
        if jump_flag:
            jump_flag = False
            continue

        cur = res[i]

        if cur['type'] == "title":
            text_content = ""
            for row in cur['res']:
                text_content += row['text']

            prefix = "#"
            level = get_title_level(text_content)

            if level == 1:
                prefix = "#"
            elif level == 2:
                prefix = "##"
            elif level == "3":
                prefix = "###"

            if translate:
                cn_text_content = en_to_cn(text_content)
                text_content = "%s | %s" % (text_content, cn_text_content)

            f.write("%s %s" % (prefix, text_content))
            f.write("\n")

        if cur['type'] == "text":
            text_content = ""
            for row in cur['res']:
                text_content += row['text']

            f.write(text_content)

            if translate:
                cn_text_content = en_to_cn(text_content)
                f.write("\n")
                f.write("\n")
                f.write(cn_text_content)
                f.write("\n")

        if cur['type'] == "figure":
            basepath = os.path.split(md_path)[0]
            img_path = os.path.join(basepath, "%s_figure_%d.jpg" % (bn, i))
            cv2.imwrite(img_path, cur['img'])

            text_content = ""
            # 当前为图片，一般下一个为图片说明
            if (i + 1) < len(res) and res[i + 1]['type'] == 'text':
                next = res[i + 1]
                for row in next['res']:
                    text_content += row['text']
                jump_flag = True

            f.write("\n")
            f.write("![%s](%s)" % (text_content, "%s_figure_%d.jpg" % (bn, i)))
            f.write("\n")

        if cur['type'] == "table":
            basepath = os.path.split(md_path)[0]
            img_path = os.path.join(basepath, "%s_table_%d.jpg" % (bn, i))
            cv2.imwrite(img_path, cur['img'])

            text_content = ""
            # 当前为表格，一般下一个为表格说明
            if (i + 1) < len(res) and res[i + 1]['type'] == 'text':
                next = res[i + 1]
                for row in next['res']:
                    text_content += row['text']
                jump_flag = True

            f.write("\n")
            f.write("![%s](%s)" % (text_content, "%s_table_%d.jpg" % (bn, i)))
            f.write("\n")
        # 每写完一段，换行
        f.write("\n")

    # 最后关闭
    f.close()


if __name__ == '__main__':
    pass
