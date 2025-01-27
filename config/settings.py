from environs import Env
from dataclasses import dataclass

@dataclass
class Db:
    db_user: str
    db_password: str
    db_database: str
    db_host: str
    db_port: int
@dataclass
class Logs:
    level: str
    dir: str
    format: str
    separate_log_without_rollover: bool
@dataclass
class ApiKeys:
    postlikes: str
    bulkfollows: str
    followiz: str
@dataclass
class ServicesFilters:
    networks: list
    filters: list
@dataclass
class Settings:
    db: Db
    logs: Logs
    api_keys: ApiKeys
    services: ServicesFilters

def get_settings(path: str):
    env = Env()
    env.read_env(path, override=True)

    return Settings(
        db=Db(
            db_user=env.str('DB_USER'),
            db_password=env.str('DB_PASSWORD'),
            db_database=env.str('DB_DATABASE'),
            db_host=env.str('DB_HOST'),
            db_port=env.int('DB_PORT'),
        ),
        logs=Logs(
            level=env.str('LOGS_LEVEL'),
            dir=env.str('LOGS_DIR'),
            format=env.str('LOGS_FORMAT'),
            separate_log_without_rollover=env.str('LOGS_ROLLOVER')
        ),
        api_keys=ApiKeys(
            postlikes=env.str('POSTLIKES_API_KEY'),
            bulkfollows=env.str('BULKFOLLOWS_API_KEY'),
            followiz=env.str('FOLLOWIZ_API_KEY'),
        ),
        services=ServicesFilters(
            networks = [
                "All services",
                "Instagram",
                "TikTok",
                "YouTube",
                "Facebook",
                "Twitter",
                "LinkedIn",
                "Snapchat",
                "Shopee",
                "Amazon",
            ],
            filters = [
                "Followers",
                "Likes",
                "Comments",
                "Shares",
                "Subscribers",
                "Video Views",
                "Live Stream Views",
                "Clicks",
            ]
        )
    )

settings = get_settings('.env')
