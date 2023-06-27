class Database:
    __instance = None

    def __new__(cls):
        if Database.__instance is None:
            Database.__instance = super().__new__(cls)
        return Database.__instance

    def __del__(self):
        Database.__instance = None


if __name__ == '__main__':
    database1 = Database()
    database2 = Database()
    print(database2 is database1)
