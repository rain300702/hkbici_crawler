# hkbici_crawler

A simple web crawler designed to search topics on [hkbici forum](http://hk-bici.com/forum.php?gid=1), which function is not provided to novice users.<br>
<br>
Multiple keywords as inputs in searching are acceptable.<br>
<br>
Specify searching depth by changing the number of pages to be searched.<br>
<br>
Crawler will use multiple threads to finish different tasks. Create 10 threads by default or change it in optional arguments.<br>
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
    -n, --threadNum     Expect numeral input for thread number     
    default arguments:
    DEPTH: 50 KEYWORD:'' initiation=false threadNum: 10
    
 ---------------------
香港比思论坛是本魔法师经常光顾的一个坛子，论坛搜索功能只对一定级别的用户组开放，
遂根据自己需求写了个简单的多关键字检索的脚本。

使用请翻墙，第一次使用请加上-i选项。

最近一次更新用Queue做了个线程池，队列中的任务轮流执行减少了一部分网络IO阻塞的时间；因为是翻墙所以网络IO的时间极其之长，谁有能最大程度优化这一问题的方案请告诉我，不用重写大部分代码、不用分布式（没资源）比较实际的那种。
