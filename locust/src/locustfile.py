from locust import HttpUser, task


class PocustfileDemo(HttpUser):
    # i = 0
    # mutex = threading.Lock();

    @task(1)
    def test1(self):
        resp = self.client.get(f"/test/test1?uid={self.uid}");
        print("test1", str(resp))

    @task(5)
    def test2(self):
        body = {"uid": self.uid, "name": "locust"}
        resp = self.client.post("/test/test2", json=body)
        print("test2", str(resp))

    def on_start(self):
        self.uid = 1