# -*- coding: UTF-8 –*-

from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def screen_v1(self):
        self.client.post("/poi/advanced/screen/v1", {
            "city": "city",
            "level1": "level1",
            "level2": "level2",
            "level3": "level3"
        })

    @task
    def screen_v2(self):
        self.client.post("/poi/advanced/screen/v2", {
            "city": "city",
            "level1": "level1",
            "level2": "level2",
            "level3": "level3"
        })

    @task
    def merge_v1(self):
        self.client.post("/fetch/all/merge/v1", {
            "city": "",
            "source": "",
            "intervalStar": "",
            "intervalEnd": "",
        })

    @task
    def merge_v2(self):
        self.client.post("/fetch/all/merge/v2", {
            "city": "",
            "source": "",
            "intervalStar": "",
            "intervalEnd": "",
        })

