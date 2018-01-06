# scrapy-jdxl
[00](http://uegeek.com) 的第一个爬虫项目：用 scrapy 抓取简单心理网站上心理咨询师的资料。

## 如何运行

```
git clone git@github.com:kidult00/scrapy-jdxl.git
```
然后安装 Python 依赖：

```
(sudo) pip install -r requirements.txt
```

进入内层 ``jdxl`` 目录：

```
scrapy crawl counselor
```

## 数据分析

用 Pandas 对爬取的咨询师资料做了简单的数据处理和分析。详情请查看 [jdxl\_experts\_analysis.ipynb](https://github.com/kidult00/scrapy-jdxl/blob/master/jdxl/ouput/jdxl_experts_analysis.ipynb)。

![wordcloud.png](https://github.com/kidult00/scrapy-jdxl/blob/master/jdxl/ouput/wordcloud.png)