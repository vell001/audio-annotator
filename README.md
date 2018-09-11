# 音频分片打标签工具

代码在：[https://github.com/vell001/audio-annotator](https://github.com/vell001/audio-annotator)

> web端代码基于：[https://github.com/CrowdCurio/audio-annotator](https://github.com/CrowdCurio/audio-annotator)，进行汉化、按VAD需求调整标注方式以及根据server调整了一些逻辑
> server端基于tornado实现

# 原理

采用B/S(Browser/Server)架构，所有音频标注操作都是基于web端的wavesurfer框架，web端通过RESTful API从server端获取标注任务以及提交标注结果

# 使用方式

## 一、开启标注服务【Server】

### 通过打包好的可执行文件部署

可执行文件见：[github release文件夹](https://github.com/vell001/audio-annotator/releases)

解压对应操作系统的可执行文件，然后在文件夹内找到 `run` 的可执行文件，可执行文件后可带参数：

```
optional arguments:
  -h, --help            show this help message and exit
  --host HOST           host, 0.0.0.0 代表外网可以访问
  -p PORT, --port PORT  port
  -d DEBUG, --debug DEBUG
                        debug
  -l LOG_CONFIG_FILE, --log_config_file LOG_CONFIG_FILE
                        log config file, json
  --wav_dir WAV_DIR, -w WAV_DIR
                        待标注的wav文件夹
```

主要注意，`-w` 这个参数可以指定你要标注的wav文件所在的文件夹，如果不指定，默认是在 `run` 的同级目录下的 `wavs` 文件夹

![](https://ask.qcloudimg.com/draft/1420883/dynuke9yy5.png)

### 源码部署

直接执行 `run.py` 文件，参数也和可执行文件部署一样

## 二、在浏览器里进行标注【Browser】

没有指定 `--host` 的话，默认地址就是：[http://127.0.0.1:8282](http://127.0.0.1:8282)，在任意浏览器打开这个链接，尽量使用chrome  
v1.1版本增加了review功能，默认地址是：[http://127.0.0.1:8282/?review=true](http://127.0.0.1:8282/?review=true)  
v1.2版本增加了指定wav_name功能，样例地址：[http://127.0.0.1:8282/?review=true&wav_name=82c75.wav](http://127.0.0.1:8282/?review=true&wav_name=82c75.wav)  
标注界面如下：

![](https://ask.qcloudimg.com/draft/1420883/nh7nnrmkly.png)

## 三、标注结果

标注结果保存在 `wavs`里，以`[wav_name].json`命名，json格式

![](https://ask.qcloudimg.com/draft/1420883/lwrd861ue2.png)

需要关注的字段如下：

![](https://ask.qcloudimg.com/draft/1420883/xk2s6nih6l.png)