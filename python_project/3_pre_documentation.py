class DataProcessor:
    def __init__(self, config):
        self.config = config
        self.cache = {}
        
    def transform_batch(self, batch, normalize=True):
        batch_id = hash(str(batch))
        
        if batch_id in self.cache:
            return self.cache[batch_id]
            
        result = []
        for item in batch:
            transformed = self._apply_transforms(item)
            if normalize:
                transformed = self._normalize(transformed)
            result.append(transformed)
            
        self.cache[batch_id] = result
        return result
        
    def _apply_transforms(self, item):
        for transform in self.config['transforms']:
            item = transform(item)
        return item
        
    def _normalize(self, item):
        if 'normalization' not in self.config:
            return item
            
        norm_type = self.config['normalization']
        if norm_type == 'minmax':
            return (item - item.min()) / (item.max() - item.min())
        elif norm_type == 'zscore':
            return (item - item.mean()) / item.std()
        return item
