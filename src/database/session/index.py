from src.export.json.export import ExportJSON


class SessionDB:
    __db = dict()
    file_path: str = None

    @staticmethod
    def contains(key: str) -> bool:
        return SessionDB.__db.get(key, None) is not None

    @staticmethod
    def get(key: str) -> any:
        return SessionDB.__db.get(key, None)

    @staticmethod
    def save(key: str, value: any) -> None:
        SessionDB.__db[key] = value

    @staticmethod
    def delete(key: str) -> any:
        return SessionDB.__db.pop(key)

    @staticmethod
    def sync():
        if SessionDB.file_path is None or "airports" not in SessionDB.__db or "connections" not in SessionDB.__db:
            return

        ExportJSON.export(SessionDB.file_path, SessionDB.get("airports"), SessionDB.get("connections"))