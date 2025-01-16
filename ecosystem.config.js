module.exports = {
  apps: [{
    name: "django_app",
    script: "gunicorn",
    args: "your_project.wsgi:application",
    interpreter: "python",
    instances: "max",  // or a number like 4
    exec_mode: "cluster",
    watch: false,
    env: {
      "DJANGO_SETTINGS_MODULE": "your_project.settings",
      "BIND": "0.0.0.0:8082"
    }
  }]
}
