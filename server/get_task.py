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

    def _get_task(self, review=False):
        if "wavs" not in self.application.settings:
            self.application.settings["wavs"] = list_files(self.wav_dir, ".wav")
        elif not self.application.settings["wavs"]:
            del self.application.settings["wavs"]
            return None

        for wav_path in self.application.settings["wavs"][:]:
            if review:
                # 如果需要从新review，就不管json 是否存在
                self.application.settings["wavs"].remove(wav_path)
                return wav_path
            else:
                wav_json_path = wav_path + ".json"
                if os.path.exists(wav_json_path) and os.path.getsize(wav_json_path) > 0:
                    self.application.settings["wavs"].remove(wav_path)
                else:
                    return wav_path
        return None

    def get(self):
        review = self.get_argument('review', default="false")
        wav_path = self._get_task(review == "true")
        resp = dict()
        if not wav_path:
            # 没有wav了
            resp["ret"] = "no_tasks"
        else:
            resp["ret"] = "ok"

            annotations = []
            wav_json_path = wav_path + ".json"
            if os.path.exists(wav_json_path) and os.path.getsize(wav_json_path) > 0:
                with open(wav_json_path, encoding="utf-8") as f:
                    task_ret = json.load(f)
                    annotations = task_ret["annotations"]

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
                "alwaysShowTags": True,
                "annotations": annotations
            }
        self.write(json.dumps(resp))
