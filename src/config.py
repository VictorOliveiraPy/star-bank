import os


class Config:
    CRON_JOB_INTERVAL = os.getenv("CRON_JOB_INTERVAL", 3)


settings = Config()
