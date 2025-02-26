from typing import Union

class BIGSDbDatabaseAPIException(Exception):
    pass


class NoBIGSdbMatchesException(BIGSDbDatabaseAPIException):
    def __init__(self, database_name: str, database_scheme_id: int, query_name: Union[None, str], *args):
        self._query_name = query_name
        super().__init__(f"No matches found with scheme with ID {database_scheme_id}  in the database \"{database_name}\".", *args)
    
    def get_causal_query_name(self) -> Union[str, None]:
        return self._query_name

class NoBIGSdbExactMatchesException(NoBIGSdbMatchesException):
    def __init__(self, database_name: str, database_scheme_id: int, *args):
        super().__init__(f"No exact match found with scheme with ID {database_scheme_id}  in the database \"{database_name}\".", *args)

class NoSuchBIGSdbDatabaseException(BIGSDbDatabaseAPIException):
    def __init__(self, database_name: str, *args):
        super().__init__(f"No database \"{database_name}\" found.", *args)

class NoSuchBigSdbschemeException(BIGSDbDatabaseAPIException):
    def __init__(self, database_name: str, database_scheme_id: int, *args):
        super().__init__(f"No scheme with ID {database_scheme_id}  in \"{database_name}\" found.", *args)
