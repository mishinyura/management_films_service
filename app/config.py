from dynaconf import Dynaconf
from pydantic import BaseModel, HttpUrl


class DBConfig(BaseModel):
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: str

    @property
    def db_url(self):
        data = "postgresql+asyncpg://{0}:{1}@{2}:{3}/{4}".format(
            self.db_user, self.db_password, self.db_host, self.db_port, self.db_name
        )
        return data


class APPConfig(BaseModel):
    app_port: int
    app_version: str
    app_name: str
    app_host: str
    app_mount: str


class KinopoiskConfig(BaseModel):
    kinopoinsk_api_key: str
    kinopoinsk_base_url: HttpUrl


class Settings(BaseModel):
    app: APPConfig
    db: DBConfig
    kinopoisk: KinopoiskConfig



dyna_settings = Dynaconf(settings_files=["settings.toml"])

settings = Settings(app=dyna_settings["app_settings"], db=dyna_settings["db_settings"], kinopoisk=dyna_settings["kinopoisk_settings"])
