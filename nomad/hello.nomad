job "hello-devops" {
  datacenters = ["dc1"]

  type = "service"

  group "hello-group" {
    count = 1

    task "hello" {
      driver = "docker"

      config {
        image = "hello-app:latest"
      }

      resources {
        cpu    = 200
        memory = 128
      }
    }
  }
}