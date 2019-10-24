#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : packet.py
# Author            : INMAK <jchrys@me.com>
# Date              : 24.10.2019
# Last Modified Date: 24.10.2019
# Last Modified By  : INMAK <jchrys@me.com>

import uuid

class PacketManager():
    STATUS_TLE = "TLE"
    STATUS_WA = "WA"
    STATUS_OK = "OK"

    def __init__(self, host, port, judge):
        self.judge = judge

    def send_packet(self, packet):
        print(packet)

    def recieve_packet(self, packet):
        name = packet["name"]
        if name == "submission-request":
            self.submission_handshake_packet()
            judge.begin_grading(packet["problem-id"], packet["language"], packet["source"])
        elif name =="get-current-submission":
            self.current_submission_packet()
        else:
            print("ERROR AT RECEIVE PACKET ELSE")
    
    def submission_handshake_packet(self):
        self.judge.current_submission = uuid.uuid1().hex
        self.send_packet({ "name": "handshake",
                           "submission-id": self.judge.current_submission})


        def test_case_status_packet(self, status, time, memory, output):
            self.send_packet({"name": "test-case-status",
                              "submission-id": self.judge.current_submission,
                              "status": status,
                              "time": time,
                              "memory": memory,
                              "output": output})

        def compile_error_packet(self, log):
            self.send_packet({
                "name": "compile-error",
                "submission-id": self.judge.current_submission,
                "log": log
                })

        def begin_grading_packet(self):
            self.send_packet({
                "name": "grading-begin",
                "submission-id": self.judge.current_submission
                })

        def grading_end_packet(self):
            self.send_packet({
                "name": "grading-end",
                "submission-id": self.judge.current_submission
                })
            judge.current_submission = None

        def current_submission_packet(self):
            self.send_packet({
                "name": "current-submission-id",
                "submission-id": self.judge.current_submission
                })
