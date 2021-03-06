from haystack import indexes
from discovery.models import Foo, Bar


class FooIndex(indexes.RealTimeSearchIndex):
    text = indexes.CharField(document=True, model_attr='body')
    
    def get_model(self):
        return Foo


class BarIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True)
    
    def get_model(self):
        return Bar
