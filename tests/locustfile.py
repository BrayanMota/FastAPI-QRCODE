from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.post("/v1/qrcode?text=Teste")
