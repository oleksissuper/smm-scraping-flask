from db.core import Db


class Records(Db):
    def __init__(self):
        super().__init__()

    def get(self, request_data: dict) -> dict:
        network = request_data.get("network", "All services")
        filters = request_data.get("filters", None)
        page = int(request_data.get("page", 1))
        limit = int(request_data.get("limit", 20))
        rate_range = request_data.get("rate_range")
        offset = (page - 1) * limit
        query = f"SELECT * FROM {self.table_services} WHERE 1=1"
        params = []
        if network != "All services":
            query += " AND category_service LIKE %s"
            params.append(f"%{network}%")
        if filters:
            for filter_item in filters:
                query += " AND category_service LIKE %s"
                params.append(f"%{filter_item}%")
        if rate_range and len(rate_range) > 0:
            if len(rate_range) == 2 and rate_range[0] is not None and rate_range[1] is not None:
                query += " AND rate_per_thousand BETWEEN %s AND %s"
                params.extend(rate_range)
            elif rate_range[0] is not None:
                query += " AND rate_per_thousand >= %s"
                params.append(rate_range[0])
            elif len(rate_range) > 1 and rate_range[1] is not None:
                query += " AND rate_per_thousand <= %s"
                params.append(rate_range[1])

        query += " LIMIT %s OFFSET %s"
        params.extend([limit, offset])
        self.cursor.execute(query, params)
        records = self.cursor.fetchall()
        return records
       