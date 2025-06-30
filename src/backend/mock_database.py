"""
Mock database for testing without MongoDB
"""

class MockCollection:
    def __init__(self):
        self.data = {}
    
    def count_documents(self, query):
        return len(self.data)
    
    def find_one(self, query):
        if "_id" in query:
            return self.data.get(query["_id"])
        return None
    
    def find(self, query=None):
        result = []
        for _id, document in self.data.items():
            doc_copy = document.copy()
            doc_copy['_id'] = _id
            result.append(doc_copy)
        return result
    
    def insert_one(self, document):
        _id = document.get("_id")
        if _id:
            self.data[_id] = document
        return None
    
    def update_one(self, query, update):
        class Result:
            def __init__(self, modified):
                self.modified_count = modified
        
        if "_id" in query:
            _id = query["_id"]
            if _id in self.data:
                if "$push" in update:
                    for key, value in update["$push"].items():
                        if key in self.data[_id]:
                            self.data[_id][key].append(value)
                        else:
                            self.data[_id][key] = [value]
                if "$pull" in update:
                    for key, value in update["$pull"].items():
                        if key in self.data[_id] and value in self.data[_id][key]:
                            self.data[_id][key].remove(value)
                return Result(1)
        return Result(0)

activities_collection = MockCollection()
teachers_collection = MockCollection()