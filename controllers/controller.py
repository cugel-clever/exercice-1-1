from services.store_service import StoreService

class Controller:
    def __init__(self, store_service: StoreService):
        self.store_service = store_service