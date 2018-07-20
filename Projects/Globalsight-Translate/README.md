# 项目介绍

**项目名称：** globalsight本地化

**项目功能：** 用正则表达式匹配，调用有道翻译API将globalsight网站的资源文件LocaleResource_en_US.properties翻译为中文，并写入LocaleResource_zh_CN.properties中。

**项目成员：** 杨若瑶

**文件构成：**

| 文件名                          | 说明                                                         |
| ------------------------------- | ------------------------------------------------------------ |
| globalsight_translate.py        | 项目主程序文件。用正则表达式匹配资源文件内容，调用有道API翻译为中文。 |
| youdao_translate.py             | 有道翻译API调用类文件                                        |
| LocaleResource_en_US.properties | 网站的英文资源文件                                           |
| LocaleResource_zh_CN.properties | 翻译后的中文资源文件                                         |

