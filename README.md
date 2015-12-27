# hkbici_crawler

A simple web crawler designed to search topics on [hkbici forum](http://hk-bici.com/forum.php?gid=1), which function is not provided to novice users.<br>
<br>
Multiple keywords as inputs in searching are acceptable.<br>
<br>
Specify searching depth by changing the number of pages to be searched.<br>
<br>
Measures such as introducing multiple threads, DB and asyncio will be taken in the future for optimal performance.<br>
<br>

## Usage

    hkbici-crawler [-h] [-d DEPTH] [-k KEYWORD] [-i]<br>
    optional arguments:
    -h, --help          show this help message and exit
    -d DEPTH, --depth DEPTH
                        Expect numeral input for searching depth
    -k KEYWORD, --keyword KEYWORD
                        Keywords for searching
    -i, --initiation    Use this optional argument if this is your first use
    default arguments:
    DEPTH: 20 KEYWORD:'' initiation=false
    
 ---------------------
香港比思论坛是本魔法师经常光顾的一个坛子，论坛搜索功能只对一定级别的用户组开放，
遂根据自己需求写了个简单的多关键字检索的脚本。

使用请翻墙，第一次使用请加上-i选项。

有空我加个多线程或者异步IO，不知道是HTML解析还是HTTP请求导致的瓶颈，20页100多秒....快的时候30秒
