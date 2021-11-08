class CSVHelper:
    @classmethod
    def build_headers_list(cls, model):
        # return headers array
        return list(model.to_dict().keys())
