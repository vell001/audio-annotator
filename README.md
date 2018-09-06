# 音频分片打标签工具
> web端代码基于：https://github.com/CrowdCurio/audio-annotator，进行汉化、按VAD需求调整标注方式以及根据server调整了一些逻辑
> server端基于tornado实现

# 原理
采用B/S(Browser/Server)架构，所有音频标注操作都是基于web端的wavesurfer框架，web端通过RESTful API从server端获取标注任务以及提交标注结果

# 使用方式
### 通过打包好的可执行文件部署
可执行文件见：[release文件夹](release)

解压对应操作系统的可执行文件，然后在文件夹内找到 `run` 的可执行文件，可执行文件后可带参数：

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
                            
主要注意，`-w` 这个参数可以指定你要标注的wav文件所在的文件夹，如果不指定，默认是在 `run` 的同级目录下的 `wavs` 文件夹
### 源码部署
直接执行 `run.py` 文件，参数也一样