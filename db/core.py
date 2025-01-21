from mysql.connector import connect, Error
import time
import json
from config.settings import settings
from utils.logger import Logger


class Db():
    def __init__(self):
        self.logger = Logger().get_logger(__name__)
        self.connecting()
        self.table_services = "services"

    def connecting(self, max_retries=10, delay=5) -> None:    
        for attempt in range(max_retries):
            try:
                self.connection = connect(
                    host=settings.db.db_host,
                    port=settings.db.db_port,
                    user=settings.db.db_user,
                    password=settings.db.db_password,
                    database=settings.db.db_database
                )
                self.cursor = self.connection.cursor()
                return 
            except Error as e:
                self.logger.error(f"Connection failed: {e}")
                time.sleep(delay)
        raise Exception("Could not connect to the database after multiple attempts")

    def __del__(self):
        self.close_connection()

    def insert(self, sql: str, params: tuple = None) -> None:
        if not params:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql, params)
        self.connection.commit()

    def select(self, sql: str) -> list:
        self.cursor.execute(sql)
        rows = self.cursor.fetchall() 
        return rows
        
    def close_connection(self) -> None:
        if hasattr(self, "cursor"):
            self.cursor.close()
        if hasattr(self, "connection"):
            self.connection.close()

    def bulk_insert_or_update(self, data_list: list[dict]) -> None:
        if not data_list:
            return
        values = [
            (
                row["service_id"],
                row["service_name"],
                row["rate_per_thousand"],
                row["minimum_quantity"],
                row["maximum_quantity"],
                row["average_time"],
                json.dumps(row["category_service"]) if isinstance(row["category_service"], list) else row["category_service"],
                row["description"],
                row["source"]
            )
            for row in data_list
        ]
        fields = [
            "service_id", "service_name", "rate_per_thousand", "minimum_quantity",
            "maximum_quantity", "average_time", "category_service", "description", "source"
        ]
        update_fields = ", ".join([f"{field} = VALUES({field})" for field in fields if field not in ["service_id", "source"]])
        query = f"""
            INSERT INTO `{self.table_services}` ({', '.join(fields)})
            VALUES ({', '.join(['%s'] * len(fields))})
            ON DUPLICATE KEY UPDATE {update_fields};
        """
        self.cursor.executemany(query, values)
        self.connection.commit()


class IsDbCreated():
    def check(self) -> None:
        for attempt in range(5):
            try:
                connection = connect(host=settings.db.db_host, 
                                     port=settings.db.db_port, 
                                     user=settings.db.db_user, 
                                     password=settings.db.db_password)
                cursor = connection.cursor()
                cursor.execute("SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode, 'ONLY_FULL_GROUP_BY', ''))")
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {settings.db.db_database}")
                connection.close()
                IsDbTable().check()
                return
            except Error as e:
                print(f"Connection failed: {e}")
                time.sleep(5)
        raise Exception("Could not connect to MySQL for database creation after multiple attempts.")


class IsDbTable(Db):
    def __init__(self):
        super().__init__()

    def check(self) -> None:
        if self.check_tables(self.table_services):
            self.create_services()

    def create_services(self) -> None:
        self.insert(f"""
                CREATE TABLE IF NOT EXISTS `{self.table_services}` (
                `id` BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                `service_id` BIGINT NOT NULL,
                `service_name` VARCHAR(255),
                `rate_per_thousand` FLOAT,
                `minimum_quantity` BIGINT,
                `maximum_quantity` BIGINT,
                `average_time` VARCHAR(255),
                `category_service` JSON,
                `description` TEXT,
                `source` VARCHAR(255) NOT NULL,
                `add_to_db` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE KEY `unique_service_source` (`service_id`, `source`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
        """)
    
    def check_tables(self, table_name: str) -> bool:
        sql = f"SHOW TABLES FROM {settings.db.db_database} LIKE '{table_name}'"
        rows = self.select(sql)
        if len(rows) == 0:
            return True
        return False