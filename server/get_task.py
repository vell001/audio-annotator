#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/4 5:16 PM
# @Author  : vell
# @Email   : vellhe@tencent.com
import json
import logging
import os

from server.base import BaseReqHandler
from server.file_utils import list_files, get_relative_path

logger = logging.getLogger(__name__)


class GetTask(BaseReqHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self.wav_dir = application.settings["settings"]["wav_dir"]
        print(application.settings)
        self.wavs = None

    def _get_task(self):
        if not self.wavs:
            self.wavs = list_files(self.wav_dir, ".wav")

        for wav_path in self.wavs[:]:
            wav_json_path = wav_path + ".json"
            if os.path.exists(wav_json_path) and os.path.getsize(wav_json_path) > 0:
                self.wavs.remove(wav_path)
            else:
                return wav_path
        return None

    def get(self):
        wav_path = self._get_task()
        resp = dict()
        if not wav_path:
            # 没有wav了
            resp["ret"] = "no_tasks"
        else:
            resp["ret"] = "ok"

            rel_wav_path = get_relative_path(self.wav_dir, wav_path)
            url = os.path.join("/wavs", rel_wav_path)
            resp["task"] = {
                "feedback": "none",
                "visualization": "waveform",
                "proximityTag": [],
                "annotationTag": [
                    "人说话声",
                    "突发噪音"
                ],
                "url": url,
                "tutorialVideoURL": "",
                "alwaysShowTags": True
            }
        self.write(json.dumps(resp))
